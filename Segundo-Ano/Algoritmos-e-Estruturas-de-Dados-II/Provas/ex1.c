#include <stdio.h>

void trocaValor(int *n1, int *n2)
{
    int aux = 0;

    aux = *n1;

    *n1 = *n2;

    *n2 = aux;

    printf("Valores trocados: %d %d\n", *n1, *n2);
}

int main()
{
    int valor1;
    int valor2;

    printf("Informe o valor 1: ");
    scanf("%d", &valor1);

    printf("Informe o valor 2: ");
    scanf("%d", &valor2);

    printf("Valores originais: %d %d\n", valor1, valor2);
    trocaValor(&valor1, &valor2);

    return 0;
}
