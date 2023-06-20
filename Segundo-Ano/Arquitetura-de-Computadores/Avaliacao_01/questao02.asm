#Fazer um código assembly que escreva na memória primária um vetor contendo a sequência dos quadrados perfeitos de 1 até n, sendo n uma variável na memória. O valor do quadrado perfeito deverá ser calculado pelo código em execução. Deverá também escrever uma saída no terminal contendo:
.data

    vetor: .word 0 0 0 0 0 0 0 0 0
    n: .word 10
    trequinho: .asciiz "-"
    pular_Linha: .asciiz "\n"

.text
main:
    lw $t0, n
    la $t1, vetor
    li $t2, 1

loop:
    mul $t3, $t2, $t2 #Var3 = Var2 * Var2
    sw $t3, ($t1)

    move $a0, $t2
    li $v0, 1
    syscall
    
    li $v0, 4
    la $a0, trequinho
    syscall
    
    move $a0, $t3
    li $v0, 1
    syscall
    
    li $v0, 4
    la $a0, pular_Linha
    syscall

    add $t1, $t1, 4
    add $t2, $t2, 1

    bne $t2, $t0, loop

    li $v0, 10
    syscall
