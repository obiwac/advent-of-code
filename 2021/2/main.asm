; assembler: nasm -felf64 main.asm -o main.o
; compiler un stub C (fichier vide): cc -c stub.c -o stub.o
; link: cc main.o stub.o -o main

global main
default rel

extern fopen ; oue bon faut pas exagérer non plus, j'allais pas faire tout avec des syscalls
extern fclose
extern feof
extern fscanf
extern printf

section .data

	path: db "input", 0
	mode: db "rb", 0
	fmt: db "%s %d", 0
	part1: db "part 1 %d", 0xA, 0

section .bss

	fp: resq 1 ; qword pcq on met 'rax' dedans
	a: resb 32 ; assez
	n: resd 1
	x: resd 1
	y: resd 1

section .text

main:
	; fopen(path, mode)

	push rbp

	mov dword [x], 0
	mov dword [y], 0

	lea rdi, [path]
	lea rsi, [mode]

	call fopen
	mov [fp], rax

read_line:
	mov byte [a], 0
	mov dword [n], 0

	; fscanf(fp, "%s %d", &a[c], &n[c])

	mov rdi, [fp]
	lea rsi, [fmt]
	lea rdx, [a]
	lea rcx, [n]

	call fscanf

	; x

	mov ecx, 0

	mov ebx, 1
	cmp byte [a], 0x66 ; 'f'
	cmove ecx, ebx
	
	mov ebx, -1
	cmp byte [a], 0x62 ; 'b'
	cmove ecx, ebx

	mov eax, [n]
	imul eax, ecx
	
	add [x], eax

	; y

	mov ecx, 0

	mov ebx, 1
	cmp byte [a], 0x64 ; 'd'
	cmove ecx, ebx

	mov ebx, -1
	cmp byte [a], 0x75 ; 'u'
	cmove ecx, ebx

	mov eax, [n]
	imul eax, ecx
	add [y], eax

	; feof(fp)

	mov rdi, [fp]
	call feof

	cmp rax, 0
	jz read_line

	; fclose(fp)

	mov rdi, [fp]
	call fclose

	; printf("part 1 %d\n", x * y)

	lea rdi, [part1]
	mov rsi, [x]
	imul rsi, [y]

	call printf

	; return

	xor rax, rax
	pop rbp
	ret