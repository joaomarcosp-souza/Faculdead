#include <stdio.h>

void vereficar(int num)
{
    if (num % 2 == 0)
    {
        printf("O numero %d e par", num);
    }
    else
    {
        printf("O numero %d e impar", num);
    }
}

int main()
{

    int num;

    printf("Numero: ");
    scanf("%d", &num);

    vereficar(num);

    return 0;
}
