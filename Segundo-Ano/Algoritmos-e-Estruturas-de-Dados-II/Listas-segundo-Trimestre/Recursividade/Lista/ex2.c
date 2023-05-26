#include <stdio.h>

int razao_pro(int razao, int posicao)
{
    if (posicao == 1)
    {
        return razao;
    }
    else
    {
        return razao + razao_pro(razao, posicao - 1);
    }
}

int main()
{
    int razao, posicao;

    printf("Informe a razao: ");
    scanf("%d", &razao);

    printf("Informe a posicao: ");
    scanf("%d", &posicao);

    printf("Resultado: %d", razao_pro(razao, posicao));
}