#include <stdio.h>
#include <stdlib.h>
int main(){
	FILE *fptr1, *fptr2, *fptr3;
	char filename[100], c;
	printf("Enter the filename to open for reading: \n");
	scanf("%s", filename);
	fptr1 = fopen(filename, "r");
	if (fptr1 == NULL){
		printf("Cannot open file %s \n", filename);
		exit(0);
	}
	scanf("%s", filename);
	fptr2 = fopen(filename, "r");
	if (fptr2 == NULL){
		printf("Cannot open file %s \n", filename);
		exit(0);
	}
	printf("Enter the filename to open for writing: \n");
	scanf("%s", filename);
	fptr3 = fopen(filename, "w+"); // Open another file for writing
	int f1_done = 0, f2_done = 0;
	while (!f1_done || !f2_done) {
	    // Process one line from File 1
	    if (!f1_done) {
		while (1) {
		    c = fgetc(fptr1);
		    if (c == EOF) {
		        f1_done = 1;
		        break;
		    }
		    fputc(c, fptr3);
		    if (c == '\n') break; // End of line reached
		}
	    }
	    // Process one line from File 2
	    if (!f2_done) {
		while (1) {
		    c = fgetc(fptr2);
		    if (c == EOF) {
		        f2_done = 1;
		        break;
		    }
		    fputc(c, fptr3);
		    if (c == '\n') break; // End of line reached
		}
	    }
	}
	printf("\nContents merged to %s \n", filename);
	fclose(fptr1);
	fclose(fptr2);
	fclose(fptr3);
	return 0;
}
