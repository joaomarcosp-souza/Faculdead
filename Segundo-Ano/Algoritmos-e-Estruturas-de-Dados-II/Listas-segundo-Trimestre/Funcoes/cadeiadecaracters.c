#include <stdio.h>

int cadeiacaracters(char caract[], char one)
{
    int cont = 0;
    for (int i = 0; i < 20; i++)
    {
        if (caract[i] == one)
        {
            cont++;
        }
    }
    return cont;
}

int main()
{

    char cadeia[20], one;

    printf("Informe uma cadeia de  caracters ate o maximo de 20: ");
    fgets(cadeia, 20, stdin);

    printf("Informe um caractere para a contagem deles na cadeia: ");
    scanf(" %c", &one);

    int iguais = cadeiacaracters(cadeia, one);

    printf("O caractere '%c' aparece %d vezes na cadeia.\n", one, iguais);

    return 0;
}
