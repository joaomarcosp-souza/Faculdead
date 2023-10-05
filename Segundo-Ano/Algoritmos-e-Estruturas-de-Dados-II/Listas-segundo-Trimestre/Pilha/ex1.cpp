#include <stdio.h>
#include <stdlib.h>

typedef struct no
{
	int valor;
	struct no *proximo;
} No;

typedef struct pilha
{
	struct no *topo;
} Pilha;

void inicializarPilha(Pilha *p)
{
	p->topo = NULL;
}

bool verificarPilhaVazia(Pilha *p)
{
	return (p->topo != NULL);
}

void push(Pilha *p, int valor)
{
	No *novo = (No *)malloc(sizeof(No));
	if (novo)
	{
		novo->valor = valor;
		novo->proximo = p->topo;
		p->topo = novo;
	}
}

int pop(Pilha *p)
{
	if (verificarPilhaVazia(p))
	{
		int retorno = 0;
		No *aux = p->topo;
		retorno = p->topo->valor;
		p->topo = aux->proximo;
		free(aux);
		return retorno;
	}
	else
	{
		printf("Pilha sem elementos\n");
	}
	return NULL;
}

void imprimir(Pilha *p)
{
	No *aux = p->topo;
	while (aux)
	{
		printf("[");
		printf("%d", aux->valor);
		printf("]\n");
		aux = aux->proximo;
	}
}
int main()
{
	Pilha pilha;
	int valor, opcao;

	do
	{
		printf("  ---MENU---  \n");
		printf(" 1 - Push \n");
		printf(" 2 - Pop \n");
		printf(" 3 - Imprimir \n");
		printf(" 4 - Sair \n");
		printf("Informe a opcao: ");
		scanf("%d", &opcao);

		if (opcao = 1)
		{
			printf("Digite o valor a ser inserido na pilha: ");
			scanf("%d", &valor);
			push(&pilha, valor);
		}
		else if (opcao = 2)
		{
			valor = pop(&pilha);
			if (valor != -1)
			{
				printf("O valor removido %d sera removido da pilha; ", valor);
			}
		}
		else if (opcao = 3)
		{
			imprimir(&pilha);
		}
		else if (opcao = 4)
		{
			printf("Encerrando o programa...");
		}
		else
		{
			printf("Opcao Invalida.");
		}

	} while (opcao != 4);

	return 0;
}
