#include <stdio.h>

void trocaTroca(int n1, int n2)
{
    int temp = n1;
    n1 = n2;
    n2 = temp;
    printf("Valores trocados: num1 = %d, num2 = %d", n1, n2);
}

int main()
{
    int num1, num2;

    printf("Valor num1: ");
    scanf("%d", &num1);

    printf("Valor num2: ");
    scanf("%d", &num2);

    printf("Valores originais: num1 = %d, num2 = %d\n", num1, num2);

    trocaTroca(num1, num2);

    return 0;
}
