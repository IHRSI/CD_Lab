#include <stdio.h> 
#include <stdlib.h> 
int main() { 
  FILE *fp1, *fp2; long size; char filename[100],ch; 
  printf("Enter the filename to open for reading: \n"); 
  scanf("%s", filename); 
  fp1 = fopen(filename, "r");  
  printf("Enter the filename to open for writing: \n"); 
  scanf("%s", filename); 
  fp2 = fopen(filename, "w+"); 
  fseek(fp1, 0, SEEK_END); 
  size = ftell(fp1); 
  printf("Size of the file: %ld bytes\n", size); 
  for (long i = 1; i <= size; i++) { 
    fseek(fp1, -i, SEEK_END); 
    ch = fgetc(fp1); 
    fputc(ch, fp2); 
  } 
  fclose(fp1); 
  fclose(fp2); 
  printf("File contents reversed successfully.\n"); 
  return 0; 
}
