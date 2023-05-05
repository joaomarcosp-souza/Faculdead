#include <stdio.h>

struct dadosAluno
{
    char nome_aluno[50];
    int idade_aluno;
};

int main()
{
    struct dadosAluno alunos_dados[10];

    int count_aluno = 10;

    for (int i = 0; i < count_aluno; i++)
    {
        printf("Nome do %i Aluno: ", i + 1);
        scanf("%s", alunos_dados[i].nome_aluno);

        printf("Idade do %i Aluno: ", i + 1);
        scanf("%i", &alunos_dados[i].idade_aluno);

        printf("\nAluno %s, cadastrado com sucesso.", alunos_dados[i].nome_aluno);
        printf("\n");
    }

    for (int i = 0; i < count_aluno; i++)
    {
        printf("Dados do Aluno %i: \n", i+1);
        printf("Nome: %s, Idade:%i \n", alunos_dados[i].nome_aluno, alunos_dados[i].idade_aluno);
    }

    return 0;
}
