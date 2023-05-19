#include <stdio.h>

void calcularMedia(int num1, int num2, int num3)
{
    int media;

    media = (num1 + num2 + num3) / 3;

    printf("Media das notas ficou: %d", media);
}

int main()
{
    int notas[3];

    for (int i = 0; i < 3; i++)
    {
        printf("Informe o valor da %i prova: ", i + 1);
        scanf("%d", &notas[i]);
    }

    calcularMedia(notas[0], notas[1], notas[2]);

    return 0;
}
