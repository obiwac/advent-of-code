; assemble: nasm -felf64 main.asm -o main.o
; link: ld main.o

global _start
default rel

section .data

	path: db "input", 0
	prefix: db "part 1 "
	nl: db 0xA

section .bss

	fd: resq 1 ; qword bc we're putting 'rax' inside
	buf: resb 1
	act: resb 1
	num: resd 1
	unit: resq 1 ; qword bc we're using a special trick for dividing by 10
	x: resd 1
	y: resd 1

section .text

read_byte:
	; read(fd, &a, 1)

	mov rdi, [fd]
	lea rsi, [buf]
	mov rdx, 1 ; only read one buffer

	mov rax, 0 ; read
	syscall

	ret

_start:
	; open(path, O_RDONLY)

	lea rdi, [path]
	mov rsi, 0 ; O_RDONLY

	mov rax, 2 ; open
	syscall
	mov [fd], rax

iter:
	call read_byte

	; read action

	mov al, [buf]
	mov [act], al

until_space:
	call read_byte

	cmp byte [buf], 0x0A ; unexpected newline
	je finish

	cmp byte [buf], 0x20 ; space character
	jne until_space ; continuously read bytes until we arrive at a space character

	; read number

	call read_byte

	xor eax, eax
	mov al, [buf] ; low byte of eax
	sub al, 0x30 ; convert to number
	mov [num], eax

	; process data

	mov eax, 0
	cmp byte [act], 0x66 ; 'f'
	cmove eax, [num]
	add [x], eax

	mov ecx, 0

	mov ebx, 1
	cmp byte [act], 0x64 ; 'd'
	cmove ecx, ebx

	mov ebx, -1
	cmp byte [act], 0x75 ; 'u'
	cmove ecx, ebx

	mov eax, [num]
	imul eax, ecx
	add [y], eax

	; eat newline

	call read_byte
	jmp iter

finish:

	; close(fd)

	lea rdi, [fd]

	mov rax, 3 ; close
	syscall

	; write(stdout, "part 1 ", 7 /* exclude NULL */)

	mov rdi, 1 ; stdout
	lea rsi, [prefix]
	mov rdx, 7

	mov rax, 1 ; write
	syscall

	; print number

	mov eax, [x]
	imul eax, [y]
	mov [num], eax

	mov dword [unit], 100000000
	mov bl, 0 ; not reduce?

digit:
	xor edx, edx
	mov eax, [num]
	div dword [unit]

	; mod 10

	xor edx, edx
	mov ecx, 10
	div ecx

	; reduce

	mov al, bl
	or al, dl

	cmp al, 0
	je reduce

	mov bl, 1

	add edx, 0x30
	mov byte [buf], dl

	; write(stdout, buf, 1)

	mov rdi, 1 ; stdout
	lea rsi, [buf]
	mov rdx, 1

	mov rax, 1 ; write
	syscall

reduce:

	; little trick to divide unit by 10

	mov eax, 3435973837
	imul rax, qword [unit]
	shr rax, 35	
	mov [unit], eax

	cmp dword [unit], 0
	jne digit

	; write(stdout, "\n", 1)

	lea rsi, [nl]

	mov rax, 1 ; write
	syscall

	; exit(0)

	mov rdi, 0

	mov rax, 60 ; exit
	syscall
