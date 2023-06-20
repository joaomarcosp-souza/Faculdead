#Dado um vetor na memória com n elementos, elabore um código assembly que identifique o maior valor do vetor, onde n deverá ser especificado na memória. Imprimir o resultado usando chamadas de sistema.

.data
    vetor: .word 150 22 30 80 24 666 69 10
    n:  .word 8
    stringMaior_Numero: .asciiz "Maior numero: "
    pular_Linha: .asciiz "\n"

.text

main:
    la $t0, vetor          
    lw $t1, n               
    li $t2, 0               

    li $t4, 0              
    li $t5, 0             
    la $t7, vetor         

loop_Vetor:
    bge $t4, $t1, exit     
    lw $t3, ($t7)          

    slt $t6, $t3, $t5       
    beq $t6, $zero, Maior_Numero

    add $t4, $t4, 1         
    add $t7, $t7, 4         
    j loop_Vetor         


Maior_Numero:
    move $t5, $t3            

    add $t4, $t4, 1         
    add $t7, $t7, 4        
    j loop_Vetor         

 exit:
    li $v0, 4              
    la $a0, pular_Linha       
    syscall

    li $v0, 4              
    la $a0, stringMaior_Numero    
    syscall

    li $v0, 1             
    move $a0, $t5           
    syscall

    li $v0, 10             
    syscall