#include <stdio.h>

void ordenar(int num1, int num2)
{
    int temp;
    if (num1 > num2)
    {
        temp = num1;
        num1 = num2;
        num2 = temp;
    }
    
    printf("Valores ordenados: num1 = %d, num2 = %d", num1, num2);
}

int main()
{
    int n1, n2;

    printf("Informe um numero inteiro: ");
    scanf("%d", &n1);

    printf("Informe um numero inteiro: ");
    scanf("%d", &n2);

    ordenar(n1, n2);
    return 0;
}