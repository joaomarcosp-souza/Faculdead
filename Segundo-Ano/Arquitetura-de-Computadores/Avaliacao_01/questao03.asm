#Deverá escrever um código assembly que implemente o algoritmo selection sort.
.data
    vetor: .word 7, 2, 6, 4, 8, 2,3
    tamanho_Vetor: .word 8
    pula_Linha: .asciiz "\n"
    ordenado: .asciiz "Vetor ordenado:\n"

.text
    la $t0, vetor 
    lw $t2, ($t0)
    li $t3, 0
    lw $t5, tamanho_Vetor

loop: #vetor[i]
    bge $t3, $t5, fimLoop
    add $t4, $t3, $zero
    la $t1, ($t0)
    lw $t2, ($t0)

loopInterno: #vetor[j], j = i, j < tamanhoVetor, j++

    bge $t4, $t5, troca
    lw $t6, ($t1)
    add $t4, $t4, 1
    blt $t6, $t2, menor

    add $t1, $t1, 4
    b loopInterno 

menor: #muda o valor registrado em t2 para o menor valor encontrado

    add $t2, $t6, $zero
    la $t7, ($t1)
    add $t1, $t1, 4
    b loopInterno
    
troca: #troca o valor de vetor[i] com o menor valor encontrado, i++
    la $s0, ($t0)
    lw $s1, ($s0)

    beq $s1, $t2, igual

    sw $t2, ($t0)
    sw $s1, ($t7)

igual: #qunado o valor de vetor[i] for igual ao menor valor encontrado, i++
   
    add $t3, $t3, 1
    add $t0, $t0, 4
    b loop
    
fimLoop:
    la $t0, vetor
    li $t1, 1
    lw $t2, tamanho_Vetor

    add $v0, $zero, 4
	la $a0, ordenado
	syscall
   
vetorOrdenado: #imprime o vetor ordenado
    bge $t1, $t2, exit
    lw $t3, ($t0)

    add $v0, $zero, 1
    move $a0, $t3
    syscall

    add $v0, $zero, 4
    la $a0, pula_Linha
    syscall

    add $t0, $t0, 4
    add $t1, $t1, 1
    b vetorOrdenado
   
exit: #termina o programa
    li $v0, 10  
    syscall