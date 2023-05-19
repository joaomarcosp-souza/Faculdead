#include <stdio.h>

double potencia(int num, double x)
{
    if (num == 0)
    {
        return 1;
    }
    else if (num > 0)
    {
        return x * potencia(num - 1, x);
    }
    else
    {
        return (1 / x) * potencia(num + 1, x);
    }
}

int main()
{
    int n;
    double x;

    printf("Informe a potencia a ser calculada: ");
    scanf("%d", &n);

    printf("Informe um numero inteiro: ");
    scanf("%lf", &x);

    printf("O resultado de %.2lf elevado a %d e: %.2lf\n", x, n, potencia(n, x));
}
