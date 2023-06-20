#Fazer um c�digo assembly que escreva na mem�ria prim�ria um vetor contendo a sequ�ncia dos quadrados perfeitos de 1 at� n, sendo n uma vari�vel na mem�ria. O valor do quadrado perfeito dever� ser calculado pelo c�digo em execu��o. Dever� tamb�m escrever uma sa�da no terminal contendo:
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
