#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

typedef struct no
{
    int valor;
    struct no *proximo;
} No;

typedef struct pilha
{
    struct no *topo;
    int menor;
    int maior;
} Pilha;

void inicializarPilha(Pilha *p)
{
    p->topo = NULL;
    p->menor = INT_MAX;
    p->maior = INT_MIN;
}

bool verificarPilhaVazia(Pilha *p)
{
    return (p->topo == NULL);
}

void push(Pilha *p, int valor)
{
    No *novo = (No *)malloc(sizeof(No));
    if (novo)
    {
        novo->valor = valor;
        novo->proximo = p->topo;
        p->topo = novo;

        if (valor < p->menor)
        {
            p->menor = valor;
        }
        if (valor > p->maior)
        {
            p->maior = valor;
        }
    }
}

int pop(Pilha *p)
{
    if (!verificarPilhaVazia(p))
    {
        int retorno = 0;
        No *aux = p->topo;
        retorno = p->topo->valor;
        p->topo = aux->proximo;

        if (retorno == p->menor)
        {
            p->menor = INT_MAX;
            No *temp = p->topo;
            while (temp)
            {
                if (temp->valor < p->menor)
                {
                    p->menor = temp->valor;
                }
                temp = temp->proximo;
            }
        }

        if (retorno == p->maior)
        {
            p->maior = INT_MIN;
            No *temp = p->topo;
            while (temp)
            {
                if (temp->valor > p->maior)
                {
                    p->maior = temp->valor;
                }
                temp = temp->proximo;
            }
        }

        free(aux);
        return retorno;
    }
    else
    {
        printf("Pilha sem elementos\n");
        return -1;
    }
}

int getMin(Pilha *p)
{
    if (!verificarPilhaVazia(p))
    {
        return p->menor;
    }
    else
    {
        printf("Pilha sem elementos\n");
        return -1;
    }
}

int getMax(Pilha *p)
{
    if (!verificarPilhaVazia(p))
    {
        return p->maior;
    }
    else
    {
        printf("Pilha sem elementos\n");
        return -1;
    }
}

void imprimir(Pilha *p)
{
    No *aux = p->topo;
    while (aux)
    {
        printf("[%d]\n", aux->valor);
        aux = aux->proximo;
    }
}

int main()
{
    Pilha pilha;
    int valor, opcao;

    inicializarPilha(&pilha);

    do
    {
        printf("  ---MENU---  \n");
        printf(" 1 - Push \n");
        printf(" 2 - Pop \n");
        printf(" 3 - Get Min \n");
        printf(" 4 - Get Max \n");
        printf(" 5 - Imprimir \n");
        printf(" 6 - Sair \n");
        printf("Informe a opcao: ");
        scanf("%d", &opcao);

        if (opcao == 1)
        {
            printf("Digite o valor a ser inserido na pilha: ");
            scanf("%d", &valor);
            push(&pilha, valor);
        }
        else if (opcao == 2)
        {
            valor = pop(&pilha);
            if (valor != -1)
            {
                printf("O valor %d foi removido da pilha.\n", valor);
            }
        }
        else if (opcao == 3)
        {
            valor = getMin(&pilha);
            if (valor != -1)
            {
                printf("Menor valor na pilha: %d\n", valor);
            }
        }
        else if (opcao == 4)
        {
            valor = getMax(&pilha);
            if (valor != -1)
            {
                printf("Menor valor na pilha: %d\n", valor);
            }
        }
        else if (opcao == 5)
        {
            imprimir(&pilha);
        }
        else if (opcao == 6)
        {
            printf("Encerrando o programa...\n");
        }
        else
        {
            printf("Opcao Invalida.\n");
        }

    } while (opcao != 6);

    return 0;
}
