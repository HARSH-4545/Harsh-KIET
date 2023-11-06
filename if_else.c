#include <stdio.h>
int main()
{
    int age;
    printf("Enter your age = ");
    scanf("%d", &age);
    if (age<17)
    {
      printf("You are not eligible for driving\n");
}

else
{
     printf("HURRAH! You are eligible for driving");
} 
if(age<=17)
{
    printf("Bro you can not drive, Keep Growing Up");

}
return 0;
}