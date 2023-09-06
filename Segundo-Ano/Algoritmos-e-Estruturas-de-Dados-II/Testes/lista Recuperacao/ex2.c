#include <stdio.h>

int media(int medias[2][2])
{
    int somaTotal = 0;
    int media = 0;

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            somaTotal += medias[i][j];
        }
    }
    media = somaTotal / 4;
    return media;
}

int maior(int maior[2][2])
{
    int maiorNumero = 0;
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            if (maior[i][j] > maiorNumero)
            {
                maiorNumero = maior[i][j];
            }
        }
    }
    return maiorNumero;
}

int main()
{
    int matriz[2][2];
    int mediaValor;
    int maiorValor;

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            printf("Informe o valor da matriz [%d][%d]: ", (j + 1), (i + 1));
            scanf("%d", &matriz[i][j]);
        }
    }

    mediaValor = media(matriz);
    maiorValor = maior(matriz);

    printf("Valor Medio: %d \n", mediaValor);
    printf("Maior Numero: %d", maiorValor);

    return 0;
}