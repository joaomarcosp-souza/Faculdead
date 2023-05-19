#include <stdio.h>

int fib(int num)
{
    if (num == 0)
    {
        return 0;
    }
    else
    {
        if (num == 1)
        {
            return 1;
        }
        else
        {
            return (fib(num - 1) + fib(num - 2));
        }
    }
}

int main()
{
    int n;

    printf("Informe um valor inteiro: ");
    scanf("%d", &n);

    printf("Resultado: %d", fib(n));
}