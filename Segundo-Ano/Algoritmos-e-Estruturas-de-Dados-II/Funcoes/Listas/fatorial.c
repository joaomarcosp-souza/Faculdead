#include <stdio.h>

int calculaFatoria(int num)
{
    int fat;
    for (fat = 1; num > 1; num = num - 1)
    {
        fat = fat * num;
    }
    return fat;
}

int main()
{
    int num, fat;

    printf("Informe um valor para fazer o fatorial: ");
    scanf("%d", &num);

    fat = calculaFatoria(num);
    printf("Fatorial de '%d' e '%d' ", num, fat);

    return 0;
}