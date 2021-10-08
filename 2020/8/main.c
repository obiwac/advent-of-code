#include <stdio.h>
#include <stdlib.h>

typedef enum {
	OPCODE_NOP = 'n',
	OPCODE_ACC = 'a',
	OPCODE_JMP = 'j',
} opcode_t;

typedef struct {
	char opcode[4];
	int argument;
	int has_been_executed;
} instruction_t;

int simulate(instruction_t* instructions, int instruction_count, int* acc_pointer) {
	int ip = 0;
	*acc_pointer = 0;

	for (; ip < instruction_count; ip++) instructions[ip].has_been_executed = 0;
	ip = 0;

	for (; ip < instruction_count; ip++) {
		instruction_t* instruction = &instructions[ip];
		
		if (instruction->has_been_executed) return 1; // error in code
		instruction->has_been_executed = 1;

		// *(*instruction->opcode == OPCODE_ACC ? &acc : &ip) += instruction->argument;

		switch (*instruction->opcode) {
			case OPCODE_ACC: *acc_pointer += instruction->argument; break;
			case OPCODE_JMP: ip += instruction->argument - 1; break;
			
			case OPCODE_NOP:
			default: break;
		}
	}

	return 0;
}

void main(void) {
	FILE* fp = fopen("input", "r");
	
	instruction_t* instructions = (instruction_t*) 0;
	int instruction_count = 0;

	while (1) {
		instructions = (instruction_t*) realloc(instructions, ++instruction_count * sizeof(*instructions));
		instruction_t* instruction = &instructions[instruction_count - 1];

		// memset(instruction, 0, sizeof(*instruction));
		fscanf(fp, "%s %d", instruction->opcode, &instruction->argument);

		if (fgetc(fp) != '\n') {
			break;
		}
	}

	int acc = 0;
	simulate(instructions, instruction_count, &acc);
	printf("part 1: %d\n", acc);

	int switch_ip = 0;
	
	for (; switch_ip < instruction_count; switch_ip++) {
		instruction_t* instruction = &instructions[switch_ip];
		
		if (*instruction->opcode == OPCODE_JMP) *instruction->opcode = OPCODE_NOP;
		else if (*instruction->opcode == OPCODE_NOP) *instruction->opcode = OPCODE_JMP;
		else continue;

		if (!simulate(instructions, instruction_count, &acc)) {
			break; // found solution
		}

		if (*instruction->opcode == OPCODE_JMP) *instruction->opcode = OPCODE_NOP;
		else if (*instruction->opcode == OPCODE_NOP) *instruction->opcode = OPCODE_JMP;
	}

	printf("part 2: %d\n", acc);
}