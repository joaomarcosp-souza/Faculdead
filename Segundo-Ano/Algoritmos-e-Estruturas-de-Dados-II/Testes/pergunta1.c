#include <stdio.h>
#include <stdlib.h>

/*int main()
{
    int arr = {10, 20, 30, 40, 50};
    int *ptr = arr;
    printf("%i", *(ptr++));
    printf("%i", *ptr);

    return 0;
};*/

int main()
{
    int x = 5;
    int y = 10;

    int *ptr1 = &x;
    int *ptr2 = &y;

    ptr1 = ptr2;
    *ptr1 = 20;
    
    printf("%d", y);

    return 0;
}
