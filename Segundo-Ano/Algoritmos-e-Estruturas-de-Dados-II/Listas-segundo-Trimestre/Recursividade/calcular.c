#include <stdio.h>

int calcula(int num)
{
    if (num == 0)
    {
        return 0;
    }
    else
    {
        return num + calcula(num - 1);
    }
}

int main()
{
    int n;

    printf("Informe um numero inteiro: ");
    scanf("%d", &n);

    printf("O somatorio de 1 a %d e: %d\n", n, calcula(n));
}
