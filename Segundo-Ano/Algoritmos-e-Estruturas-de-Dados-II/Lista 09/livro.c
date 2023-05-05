#include <stdio.h>
#include <time.h>

struct livro
{
    char nome_livro[50];
    char editora_livro[50];
    char isbn[14];
    int numero_paginas;
    float preco;
};

int main()
{

    struct livro livros[2];
    struct tm data[2];

    int count_livro = 2;

    for (int i = 0; i < count_livro; i++)
    {
        printf("Nome do Livro %i: ", i + 1);
        fgets(livros[i].nome_livro, 50, stdin);
        livros[i].nome_livro[strcspn(livros[i].nome_livro, "\n")] = '\0';

        // Lê uma linha extra para consumir o caractere de nova linha no buffer de entrada
        char extra[2];
        fgets(extra, 2, stdin);

        printf("Editora do Livro %i: ", i + 1);
        fgets(livros[i].editora_livro, 50, stdin);
        livros[i].editora_livro[strcspn(livros[i].editora_livro, "\n")] = '\0'; // encontrando a posição do caractere de nova linha na string e, em seguida, substituí-lo por um caractere nulo (\0).

        printf("ISBN do Livro %i: ", i + 1);
        fgets(livros[i].isbn, 50, stdin);

        printf("Data de Publicacao Livro %i: \n", i + 1);
        printf("Dia: ");
        scanf("%d/", &data[i].tm_mday);
        printf("Mes: ");
        scanf("%d/", &data[i].tm_mon);
        printf("Ano: ");
        scanf("%d/", &data[i].tm_year);
        data[i].tm_mon--;        // Ajuste para o formato esperado pela estrutura
        data[i].tm_year -= 1900; // Ajuste para o formato esperado pela estrutura

        printf("Quantidade de Paginas %i: ", i + 1);
        scanf("%i", &livros[i].numero_paginas);

        printf("Preco Livro %i: ", i + 1);
        scanf("%f", &livros[i].preco);

        printf("Livro %i, Cadastrado com sucesso. \n", i + 1);
    }

    for (int i = 0; i < count_livro; i++)
    {
        printf("Informacoes Livro %i: \n", i + 1);
        printf("Nome: %s\nEditora: %s\nISBN: %s\nData Publicacao:%02d/%02d/%04d\nPaginas: %i\nPreco: R$%0.2f\n",
               livros[i].nome_livro, livros[i].editora_livro, livros[i].isbn, data[i].tm_mday, data[i].tm_mon + 1,
               data[i].tm_year + 1900, livros[i].numero_paginas, livros[i].preco);
        printf(" \n ");
    }

    return 0;
}
