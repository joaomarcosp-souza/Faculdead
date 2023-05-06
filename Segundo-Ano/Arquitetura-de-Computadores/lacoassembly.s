
/*  
r0 = 0
r1 = 5
r2 = 5

while(r0 < r1){
 	r2 = r2 +1
	r0 = r0 +1
}

*/

	mov r0, 0
	mov r1, 5
	mov r2, 5
	mov r3, 1

laco:
	cmp_gt_eq r4, r0, r1
	jump_cond r4, fim
	add r2, r2, r3
	jump laco

laco2:
	add r2, r2, r3
	add r0, r0, r3
	cmp_less r4, r0, r1
	jump_cond laco2

fim:

