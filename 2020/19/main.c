#include <stdio.h>
#include <stdint.h>
#include <string.h>

typedef struct {
	unsigned single_char : 1;
	unsigned multiple_rules : 1;

	char chr;
	uint8_t numbers[4];
} rule_t;

#define MAX_RULES 256
static rule_t rules[MAX_RULES];

void main(void) {
	//FILE* f = stdin;
	FILE* f = fopen("example-input", "rb");

	// read first part of file


	 for (; fgetc(f) != '\n';) {
	 	for (; fgetc(f) != '\n';) {
			uint32_t rule_index;
			fscanf(f, "%u:", &rule_index);
			
			rule_t* rule = rules + rule_index;
			memset(rule, 0, sizeof(*rule));

			char s[30];
			fscanf(f, "%[^ab0-9]s", s);
			rule->single_char = *s == '"';

			if (rule->single_char) {
				fscanf(f, "%c\"", &rule->chr);

			} else {
				fscanf(f, "%hhu %hhu", rule->numbers, rule->numbers + 1, s);
				rule->multiple_rules = *s == '|';

				if (!rule->multiple_rules) fscanf(f, "%hhu", rule->numbers + 2);
				else fscanf(f, "%hhu %hhu", rule->numbers + 2, rule->numbers + 3);
			}

			printf("%d %d, %c, %d %d %d %d\n", rule->single_char, rule->multiple_rules, rule->chr, rule->numbers[0], rule->numbers[1], rule->numbers[2], rule->numbers[3]);
	 	}
		
		return;
	}
}