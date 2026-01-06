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
	c = fgetc(fptr1); // Read contents from file
	int ct_line=0;
	int eof_ct=0;
	while (c != EOF){
		fputc(c, fptr3);
		if(c=='\n') ++ct_line;
		if(ct_line&1) c=fgetc(fptr2);
		else c=fgetc(fptr1);
		if(c==EOF && eof_ct==0){
			++eof_ct;
			c=fgetc(fptr2);
		}
	}
	printf("\nContents merged to %s \n", filename);
	fclose(fptr1);
	fclose(fptr2);
	fclose(fptr3);
	return 0;
}
