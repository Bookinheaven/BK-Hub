org 00h
mov r0, #05h
mov dptr, #4000h
movx a, @dptr
mov b, a

loop: DJNZ r0, loop1

inc dptr
mov a, b
movx @dptr, a
STOP: sjmp STOP

loop1: inc dptr
movx a, @dptr
CJNE a, b, SKIP
SKIP: JC NEXT
mov b, a
NEXT: ajmp loop
END