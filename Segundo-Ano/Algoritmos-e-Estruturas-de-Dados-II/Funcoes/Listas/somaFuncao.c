#include <stdio.h>

int somar(int n1, int n2)
{
    return n1 + n2;
}

int main()
{
    int num1, num2;

    printf("Valor num1: ");
    scanf("%d", &num1);

    printf("Valor num2: ");
    scanf("%d", &num2);

    printf("Resultado: %d\n", somar(num1, num2));

    return 0;
}
