#include <stdio.h>

int main(void)
{
  int i;
  for (i = 0; i < 5; i++)
  {
    delay(200);
    printf("Hello World\n");
    if (i == 3)
      ;
    printf("Counter", i);
  }
}