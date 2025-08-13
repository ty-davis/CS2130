#include <stdio.h>
#include <string.h>

int sumRange(int val1, int val2) {
	if (val1 == val2) return val1;
	
	int tempInt = 0;
	if (val1 < val2) {
		tempInt = val1;
		val1 = val2;
		val2 = tempInt;
	}
	return val1 + sumRange(val1-1, val2);
}

void printRevString(char* theString, int position) {
	if (theString[position] != '\0') {
		printRevString(theString, position + 1);
		printf("%c", theString[position]);
	}
}

int main(void) {
	int start, end;
	printf("Enter start and end:\n");
	scanf("%d %d", &start, &end);

	printf("%d\n", sumRange(start, end));

	while (getc(stdin) != '\n');

	char input[100];
	printf("\nPlease enter a string: ");
	fgets(input, sizeof(input), stdin);
	input[strlen(input) - 1] = '\0';
	printRevString(input, 0);
	printf("\n");
}
