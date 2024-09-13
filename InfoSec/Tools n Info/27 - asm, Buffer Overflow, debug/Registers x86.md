
### Registers

#### General registers

##### Data registers

| 64-bit | 32-bit | 16-bit | 8-bit | Description                                                                                                 | Functions for functions | Calling  <br>a function | In a function      |
| ------ | ------ | ------ | ----- | ----------------------------------------------------------------------------------------------------------- | ----------------------- | ----------------------- | ------------------ |
| rax    | eax    | ax     | ah,al | Accumulator is used in input/output and for arithmetic operations                                           | Return Value            | Might be changed        | Use freely         |
| rbx    | ebx    | bx     | bh,bl | Base is used in indexed addressing                                                                          |                         | Will not be changed     | Save before using! |
| rcx    | ecx    | cx     | ch,cl | Counter is used to rotate instructions and count loops                                                      | 4th integer argument    | Might be changed        | Use freely         |
| rdx    | edx    | dx     | dh,dl | Data is used for I/O and in arithmetic operations for multiply and divide operations involving large values | 3rd integer argument    | Might be changed        | Use freely         |
| r8     | r8d    | r8w    | r8b   |                                                                                                             | 5th integer argument    | Might be changed        | Use freely         |
| r9     | r9d    | r9w    | r9b   |                                                                                                             | 6th integer argument    | Might be changed        | Use freely         |
| r10    | r10d   | r10w   | r10b  |                                                                                                             |                         | Might be changed        | Use freely         |
| r11    | r11d   | r11w   | r11b  |                                                                                                             |                         | Might be changed        | Use freely         |
| r12    | r12d   | r12w   | r12b  |                                                                                                             |                         | Will not be changed     | Save before using! |
| r13    | r13d   | r13w   | r13b  |                                                                                                             |                         | Will not be changed     | Save before using! |
| r14    | r14d   | r14w   | r14b  |                                                                                                             |                         | Will not be changed     | Save before using! |
| r15    | r15d   | r15w   | r15b  |                                                                                                             |                         | Will not be changed     | Save before using! |
<font size=2>"Might be changed" = "Caller saved";  "Will not be changed" = "Callee saved".<br>(from https://math.hws.edu/eck/cs220/f22/registers.html?ref=hailstormsec.com, https://academy.hackthebox.com/module/31/section/396)</font>

Integer registers R8 - R15
The first 8 floating point arguments are passed in registers xmm0 to xmm7

##### Pointer registers

| 64-bit | 32-bit | 16-bit | 8-bit | Description                                                                                                 | Functions for functions | Calling  <br>a function | In a function    |
| ------ | ------ | ------ | ----- | ----------------------------------------------------------------------------------------------------------- | ----------------------- | ----------------------- | ---------------- |
| rip    | eip    |        |       | Instruction Pointer stores the offset address of the next instruction to be executed                        |                         |                         |                  |
| rsp    | esp    | sp     | spl   | Stack Pointer points to the top of the stack                                                                | Stack Pointer           | Be Very Careful!        | Be Very Careful! |
| rbp    | ebp    | bp     | bpl   | Base Pointer is also known as `Stack Base Pointer` or `Frame Pointer` thats points to the base of the stack | Frame Pointer           | Maybe Be Careful        | Maybe Be Careful |
##### Index registers

| 64-bit | 32-bit | 16-bit | 8-bit | Description                                                             | Functions for functions | Calling  <br>a function | In a function |
| ------ | ------ | ------ | ----- | ----------------------------------------------------------------------- | ----------------------- | ----------------------- | ------------- |
| rdi    | edi    | di     | sil   | Destination is used as a pointer to a destination for string operations | 1st integer argument    | Might be changed        | Use freely    |
| rsi    | esi    |        |       | Source Index is used as a pointer from a source for string operations   |                         |                         |               |

