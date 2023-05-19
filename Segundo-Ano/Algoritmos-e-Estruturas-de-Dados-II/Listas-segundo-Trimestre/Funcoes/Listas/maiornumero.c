#include <stdio.h>

void maiorNumero(int n1, int n2)
{
    if (n1 > n2)
    {
        printf("%d e maior", n1);
    }
    else
    {
        printf("%d e maior", n2);
    }
}

int main()
{
    int num1, num2;

    printf("Informe o primeiro valor inteiro: ");
    scanf("%d", &num1);

    printf("Informe o primeiro valor inteiro: ");
    scanf("%d", &num2);

    while (num1 < 0 || num2 < 0)
    {
        printf("Valor invalido, por favor, informe um novo valor. \n");
        if (num1 < 0)
        {
            printf("o primeiro numero inteiro: ");
            scanf("%d", &num1);
        }
        else
        {
            printf("o segundo numero inteiro: ");
            scanf("%d", &num2);
        }
    }

    maiorNumero(num1, num2);

    return 0;
}
