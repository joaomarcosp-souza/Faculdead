section .data
    ; Definir o vetor na memória
    vetor: times 100 db 0 ; tamanho máximo do vetor é 100

section .text
    global _start

start:
    ; Definir variáveis na memória
    mov eax, 10 ; definir n como 10
    mov ebx, 1 ; inicializar o registrador com o valor 1
    mov ecx, vetor ; definir o ponteiro do vetor

    ; Iniciar o loop que se repete n vezes
    loop_start:
        ; Calcular o quadrado perfeito
        mul ebx ; multiplicar o registrador por ele mesmo
        mov [ecx], eax ; armazenar o resultado no vetor

        ; Avançar para o próximo valor
        inc ebx

        ; Verificar se ainda há valores para calcular
        cmp ebx, eax
        jle loop_start

    ; Escrever a saída no terminal
    mov ebx, 1 ; inicializar o contador para imprimir os valores
    mov ecx, vetor ; definir o ponteiro do vetor

    ; Loop para escrever a saída
    output_loop:
        ; Escrever o valor do índice e do quadrado perfeito
        push ebx ; preparar argumentos para função printf
        push ecx
        push quadrado_perfeito_format ; definir o formato da saída
        call printf ; chamar a função printf

        ; Avançar para o próximo valor
        inc ebx
        add ecx, 4 ; avançar 4 bytes no ponteiro do vetor

        ; Verificar se ainda há valores para imprimir
        cmp ebx, eax
        jle output_loop

    ; Encerrar o programa
    mov eax, 1 ; definir o código de saída
    xor ebx, ebx ; definir o segundo argumento como 0
    int 0x80 ; chamar a função de saída

section .data
    quadrado_perfeito_format db "%d - %d", 10, 0 ; formato da saída do printf