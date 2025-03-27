
```asm
; hello.asm
;

global _start

section .text:

_start:
        mov eax, 0x4            ;use the write syscall
        mov ebx, 1              ;use stdout as the fd, file descriptor
        mov ecx, message        ;use the message  as  the buffer
        mov edx, message_length ;use message_length as the length
        int 0x80                ;running the syscall

        mov eax, 0x1            ;exit the program
        mov ebx, 0              ;return code
        int 0x80                ;run the syscall


section .data:
        message: db "Hello  World!", 0xA
        message_length: equ $-message
```
