#include <stdio.h>
#include <stdlib.h>
int main(){
	FILE *fptr1;
	char filename[100], c;
	printf("Enter the filename to open for reading: \n");
	scanf("%s", filename);
	fptr1 = fopen(filename, "r");
	if (fptr1 == NULL){
		printf("Cannot open file %s \n", filename);
		exit(0);
	}
	int ct_lines=0;
	int ct_chars=0;
	c = fgetc(fptr1); // Read contents from file
	while (c != EOF){
		if(c=='\n') ++ct_lines;
		else ++ct_chars;
		c = fgetc(fptr1);
	}
	printf("\n File %s has %d lines and %d characters.\n", filename,ct_lines,ct_chars);
	fclose(fptr1);
	return 0;
}
