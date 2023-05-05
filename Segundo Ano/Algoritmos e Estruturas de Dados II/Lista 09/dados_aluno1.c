#include <stdio.h>

struct dadosAluno
{
    char nome_aluno[50];
    int idade_aluno;
};

int main()
{
    struct dadosAluno alunos_dados;

    printf("Nome Aluno: ");
    scanf("%s", alunos_dados.nome_aluno);

    printf("Idade Aluno: ");
    scanf("%i", &alunos_dados.idade_aluno);

    printf("Dados Alunos: ");
    printf("Nome: %s, Idade:%i", alunos_dados.nome_aluno, alunos_dados.idade_aluno);

    return 0;
}
