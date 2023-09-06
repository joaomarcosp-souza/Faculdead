#include <stdio.h>
#include <string.h>

int maiorNota(float notas[][4], int qtdeAlunos)
{
    int alunoMaiorNota = 0;
    float maiorNota = notas[0][2];

    for (int i = 1; i < qtdeAlunos; i++)
    {
        if (notas[i][2] > maiorNota)
        {
            maiorNota = notas[i][2];
            alunoMaiorNota = i;
        }
    }

    return alunoMaiorNota;
}

int main()
{
    int qtdeAlunos = 5;
    char nomes[5][100];
    float notas[5][4];

    for (int i = 0; i < 5; i++)
    {
        printf("Informe o nome para o %d aluno: ", i + 1);
        scanf("%s", nomes[i]);

        for (int j = 0; j < 4; j++)
        {
            printf("Informe a %d nota do aluno %s no %d bimestre: ", j + 1, nomes[i], j + 1);
            scanf("%f", &notas[i][j]);
        }
    }

    int maiorNotaAluno = maiorNota(notas, qtdeAlunos);

    printf("O aluno com a maior nota no 3 bimestre é: %s\n", nomes[maiorNotaAluno]);

    return 0;
}
