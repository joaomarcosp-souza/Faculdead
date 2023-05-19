#include <stdio.h>

int somar(int n1, int n2)
{
    int resultado;
    resultado = n1 + n2;
    return resultado;
}

int main()
{

    int a, b, r;

    printf("N1: ");
    scanf("%d", &a);

    printf("N2: ");
    scanf("%d", &b);

    r = somar(a, b);
    printf("Resultado: %d", r);

    return 0;
}
