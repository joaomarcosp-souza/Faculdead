#include <stdio.h>

int somar(int num){
    if(num == 0){
        return 0;
    }else{
        return num + somar(num - 1);
    }
}

int main(){
    int n;

    printf("Informe um numero inteiro: ");
    scanf("%d", &n);

    printf("Resultado: %d", somar(n));

    return 0;
}