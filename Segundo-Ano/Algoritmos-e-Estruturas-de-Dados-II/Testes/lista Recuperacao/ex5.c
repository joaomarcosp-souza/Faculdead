#include <stdio.h>

char verificarTriangulo(int x, int y, int z)
{
    if (x == y && y == z)
        return 'E'; 
    else if (x == y || y == z || x == z)
        return 'I';
    else
        return 'S';
}

int main()
{
    int x, y, z;

    printf("Informe o valor de X: ");
    scanf("%d", &x);

    printf("Informe o valor de Y: ");
    scanf("%d", &y);

    printf("Informe o valor de Z: ");
    scanf("%d", &z);

    char tipo = verificarTriangulo(x, y, z);

    if (tipo == 'E')
        printf("O triângulo é equilátero.\n");
    else if (tipo == 'I')
        printf("O triângulo é isósceles.\n");
    else if (tipo == 'S')
        printf("O triângulo é escaleno.\n");

    return 0;
}
