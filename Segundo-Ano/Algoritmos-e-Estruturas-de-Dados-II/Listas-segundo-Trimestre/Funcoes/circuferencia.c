#include <stdio.h>
#include <math.h>

float calculaArea(float raio)
{
    float area = 3.14 * pow(raio, 2);
    return (area);
};

int main()
{
    float raio, area;

    printf("Raio: ");
    scanf("%f", &raio);

    area = calculaArea(raio);

    printf("Area: %.2f", area);

    return 0;
};