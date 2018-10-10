#include <stdio.h>

int totalThrough(int n)
{
  /* declare variables */
  int numbers[n];
  int i;
  int total;

  /* build the list */
  for (i = 0; i < n; i++) {numbers[i] = i;}

  /* add up the numbers in the list */
  total = 0;
  for (i = 0; i < n; i++)
  {
    total += numbers[i];
  }
  return total;
}

int main( int argc, const char* argv[] )
{
  printf("The total is %d\n", totalThrough(100));
}
