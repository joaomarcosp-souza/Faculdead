#include <stdio.h>

int somar_digitos(int num)
{
    if (num == 0)
        return 0;
    else
    {
        return (num % 10) + somar_digitos(num / 10);
    }
}


int main()
{
    int n;

    printf("Informe um numero para somar seus digitos: ");
    scanf("%d", &n);

    printf("O resultado alcancado da soma eh: %d", somar_digitos(n));

    return 0;
}
