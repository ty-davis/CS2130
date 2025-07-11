/* Ty Davis
 * 7/10/2025
 * CS 2130
 * Dr. Huson
 * Bit representations of values
 * filename: hw3.c
*/

// necessary import for input/output
#include <stdio.h>

// print the integer's binary representation
void printBinary(int val) {
	for (int i=sizeof(int)*8-1; i >= 0; i--) {
		if (((val >> i) & 1) > 0) {
			printf("1");
		} else {
			printf("0");
		}
		// space for readability
		if (i % 4 == 0) {
			printf(" ");
		}
	}
	printf("\n");
}

int main() {
	int val;
	printf("Welcome to the bit representer!\n");
	
	// repeat until error or user wants to be done
	while (1) {
		printf("Enter an integer to see the bit representation (0 to quit):\n>> ");
		int result = scanf("%d", &val);
		if (val == 0 || result == 0) {
			break;
		}
		// call the function
		printBinary(val);
	}
	printf("\nCome again some time!\n");
}
