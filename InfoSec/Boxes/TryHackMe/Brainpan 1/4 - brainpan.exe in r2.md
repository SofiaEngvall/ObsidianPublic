
```sh
┌──(kali㉿kali)-[~/thm/brainpan1]
└─$ r2 -A brainpan.exe 
WARN: Relocs has not been applied. Please use `-e bin.relocs.apply=true` or `-e bin.cache=true` next time
INFO: Analyze all flags starting with sym. and entry0 (aa)
INFO: Analyze imports (af@@@i)
INFO: Analyze entrypoint (af@ entry0)
INFO: Analyze symbols (af@@@s)
INFO: Analyze all functions arguments/locals (afva@@@F)
INFO: Analyze function calls (aac)
INFO: Analyze len bytes of instructions for references (aar)
INFO: Finding and parsing C++ vtables (avrr)
INFO: Analyzing methods (af @@ method.*)
INFO: Recovering local variables (afva@@@F)
INFO: Type matching analysis for all functions (aaft)
INFO: Propagate noreturn information (aanr)
INFO: Use -AA or aaaa to perform additional experimental analysis
[0x31171280]> afl
0x31171280    1     32 entry0
0x31171150    8    290 sym.___mingw_CRTStartup
0x31171000   26    322 sym.__gnu_exception_handler_4
0x311712a0    1     32 sym._WinMainCRTStartup
0x311712c0    1     12 sym._atexit
0x311712d0    1     12 sym.__onexit
0x311712e0    1      9 sym.___do_sjlj_init
0x311712f0    1      5 sym._winkwink
0x311712fc    1    103 sym._get_reply
0x31171cf8    1      6 sym._printf
0x31171cf0    1      6 sym._strcpy
0x31171ce8    1      6 sym._strlen
0x31171ce0    1      6 sym._strcmp
0x31171363   16    918 main
0x31171760    3     41 sym.___do_global_dtors
0x31171790    9     83 sym.___do_global_ctors
0x311717f0    3     27 sym.___main
0x31171810    4     34 sym.__pei386_runtime_relocator
0x31171840   23    248 sym.___cpu_features_init
0x31171940    1      7 sym._fpreset
0x31171950    1     14 sym.___w32_sharedptr_default_unexpected
0x31171960    9    160 sym.___w32_sharedptr_get
0x31171a00   15    624 sym.___w32_sharedptr_initialize
0x31171d10    1      6 sym._malloc
0x31171cd8    1      6 sym._memset
0x31171d08    1      6 sym._free
0x31171d18    1      6 sym._abort
0x31171d50    1      9 sym.___sjlj_init_ctor
0x31171ca8    1      6 sym.__cexit
0x31171cc0    1      6 sym.___p__fmode
0x31171d28    1      6 sym._SetUnhandledExceptionFilter_4
0x31171710    1      6 sym._recv_16
0x31171cb0    1      6 sym.___p__environ
0x31171730    1      6 sym._bind_12
0x31171720    1      6 sym._accept_12
0x31171740    1      6 sym._socket_12
0x31171d20    1      6 sym._ExitProcess_4
0x31171cd0    1      6 sym.___getmainargs
0x31171718    1      6 sym._send_16
0x31171750    1      6 sym._WSAStartup_8
0x31171cb8    1      6 sym._signal
0x31171748    1      6 sym._WSAGetLastError_0
0x31171728    1      6 sym._listen_8
0x31171738    1      6 sym._htons_4
0x31171cc8    1      6 sym.__setmode
0x31171708    1      6 sym._closesocket_4
0x31171d00    1      6 sym.__assert
0x31171700    1      6 sym._WSACleanup_0
0x31171c70    4     45 fcn.31171c70
```

```sh
[0x31171280]> pdf @main
            ;-- _main:
            ; CALL XREF from sym.___mingw_CRTStartup @ 0x31171246(x)
┌ 918: int main (int argc, char **argv, char **envp);
│           ; var void *var_3f8h @ ebp-0x3f8
│           ; var char *var_3fch @ ebp-0x3fc
│           ; var char *var_400h @ ebp-0x400
│           ; var char *var_404h @ ebp-0x404
│           ; var int32_t var_408h @ ebp-0x408
│           ; var int32_t var_40ch @ ebp-0x40c
│           ; var int32_t var_410h @ ebp-0x410
│           ; var int32_t var_5a8h @ ebp-0x5a8
│           ; var SOCKET s @ ebp-0x5ac
│           ; var SOCKET var_5b0h @ ebp-0x5b0
│           ; var int32_t var_5c4h @ ebp-0x5c4
│           ; var u_short var_5c6h @ ebp-0x5c6
│           ; var int32_t var_5c8h @ ebp-0x5c8
│           ; var int32_t var_5d8h @ ebp-0x5d8
│           ; var int32_t var_5dch @ ebp-0x5dc
│           ; var int32_t var_5ech @ ebp-0x5ec
│           ; var char *var_4h_8 @ esp+0x18
│           ; var size_t var_8h_6 @ esp+0x1c
│           ; var int32_t var_ch_3 @ esp+0x20
│           ; var char *var_4h_7 @ esp+0x28
│           ; var int32_t var_8h_5 @ esp+0x2c
│           ; var int32_t var_ch_2 @ esp+0x30
│           ; var char *buf @ esp+0x38
│           ; var size_t len @ esp+0x3c
│           ; var int32_t flags @ esp+0x40
│           ; var sockaddr *addr @ esp+0x44
│           ; var int32_t addrlen @ esp+0x48
│           ; var int32_t backlog @ esp+0x4c
│           ; var sockaddr *name @ esp+0x58
│           ; var int32_t namelen @ esp+0x5c
│           ; var int32_t type @ esp+0x68
│           ; var int32_t protocol @ esp+0x6c
│           ; var LPWSADATA lpWSAData @ esp+0x70
│           0x31171363      55             push ebp
│           0x31171364      89e5           mov ebp, esp
│           0x31171366      81ec08060000   sub esp, 0x608
│           0x3117136c      83e4f0         and esp, 0xfffffff0
│           0x3117136f      b800000000     mov eax, 0
│           0x31171374      83c00f         add eax, 0xf                ; 15
│           0x31171377      83c00f         add eax, 0xf                ; 15
│           0x3117137a      c1e804         shr eax, 4
│           0x3117137d      c1e004         shl eax, 4
│           0x31171380      898514faffff   mov dword [var_5ech], eax
│           0x31171386      8b8514faffff   mov eax, dword [var_5ech]
│           0x3117138c      e8df080000     call fcn.31171c70
│           0x31171391      e85a040000     call sym.___main
│           0x31171396      c78504fcff..   mov dword [var_3fch], str._______________________________________________________________________n____________________________________________________n__________________________________________________________n___________________________________________________________n_______________________________________________________n________________________________________________________________________n______________________________________________n_n__________________________WELCOME_TO_BRAINPAN____________________________n__________________________ENTER_THE_PASSWORD_______________________________n_n____________________________ ; 0x3117304c ; "_|                            _|                                        \n_|_|_|    _|  _|_|    _|_|_|      _|_|_|    _|_|_|      _|_|_|  _|_|_|  \n_|    _|  _|_|      _|    _|  _|  _|    _|  _|    _|  _|    _|  _|    _|\n_|    _|  _|        _|    _|  _|  _|    _|  _|    _|  _|    _|  _|    _|\n_|_|_|    _|          _|_|_|  _|  _|    _|  _|_|_|      _|_|_|  _|    _|\n                                            _|                          \n                                            _|\n\n[________________________ WELCOME TO BRAINPAN _________________________]\n                          ENTER THE PASSWORD                              \n\n                          >> "                      
│           0x311713a0      c78500fcff..   mov dword [var_400h], str.__________________________ACCESS_DENIED_n ; 0x311732e8 ; "                          ACCESS DENIED\n"                                                                                   
│           0x311713aa      c785fcfbff..   mov dword [var_404h], str.__________________________ACCESS_GRANTED_n ; 0x31173314 ; "                          ACCESS GRANTED\n"                                                                                 
│           0x311713b4      c785f4fbff..   mov dword [var_40ch], 0x270f ; '\x0f\''
│           0x311713be      c785f0fbff..   mov dword [var_410h], 1
│           0x311713c8      c704243e33..   mov dword [esp], str.___initializing_winsock... ; [0x3117333e:4]=0x205d2b5b ; "[+] initializing winsock..." ; const char *format                                                                                 
│           0x311713cf      e824090000     call sym._printf            ; int printf(const char *format)
│           0x311713d4      8d8558faffff   lea eax, [var_5a8h]
│           0x311713da      89442404       mov dword [lpWSAData], eax  ; LPWSADATA lpWSAData
│           0x311713de      c704240202..   mov dword [esp], 0x202      ; [0x202:4]=-1 ; 514 ; WORD wVersionRequested
│           0x311713e5      e866030000     call sym._WSAStartup_8      ; int WSAStartup(WORD wVersionRequested, LPWSADATA lpWSAData)                                                                                                                        
│           0x311713ea      83ec08         sub esp, 8
│           0x311713ed      85c0           test eax, eax
│       ┌─< 0x311713ef      7424           je 0x31171415
│       │   0x311713f1      e852030000     call sym._WSAGetLastError_0 ; int WSAGetLastError(void)
│       │   0x311713f6      89442404       mov dword [type], eax
│       │   0x311713fa      c704245a33..   mov dword [esp], str.____winsock_init_failed:__d ; [0x3117335a:4]=0x205d215b ; "[!] winsock init failed: %d" ; const char *format                                                                                
│       │   0x31171401      e8f2080000     call sym._printf            ; int printf(const char *format)
│       │   0x31171406      c78524faff..   mov dword [var_5dch], 1
│      ┌──< 0x31171410      e9dc020000     jmp 0x311716f1
│      ││   ; CODE XREF from main @ 0x311713ef(x)
│      │└─> 0x31171415      c704247633..   mov dword [esp], str.done._n ; [0x31173376:4]=0x656e6f64 ; "done.\n" ; const char *format                                                                                                                        
│      │    0x3117141c      e8d7080000     call sym._printf            ; int printf(const char *format)
│      │    0x31171421      c744240800..   mov dword [protocol], 0     ; int protocol
│      │    0x31171429      c744240401..   mov dword [type], 1         ; int type
│      │    0x31171431      c704240200..   mov dword [esp], 2          ; int af
│      │    0x31171438      e803030000     call sym._socket_12         ; SOCKET socket(int af, int type, int protocol)
│      │    0x3117143d      83ec0c         sub esp, 0xc
│      │    0x31171440      898554faffff   mov dword [s], eax
│      │    0x31171446      83bd54faff..   cmp dword [s], 0xffffffff
│      │┌─< 0x3117144d      7515           jne 0x31171464
│      ││   0x3117144f      e8f4020000     call sym._WSAGetLastError_0 ; int WSAGetLastError(void)
│      ││   0x31171454      89442404       mov dword [namelen], eax
│      ││   0x31171458      c704248033..   mov dword [esp], str.____could_not_create_socket:__d ; [0x31173380:4]=0x205d215b ; "[!] could not create socket: %d" ; const char *format                                                                        
│      ││   0x3117145f      e894080000     call sym._printf            ; int printf(const char *format)
│      ││   ; CODE XREF from main @ 0x3117144d(x)
│      │└─> 0x31171464      c70424a033..   mov dword [esp], str.___server_socket_created._n ; [0x311733a0:4]=0x205d2b5b ; "[+] server socket created.\n" ; const char *format                                                                               
│      │    0x3117146b      e888080000     call sym._printf            ; int printf(const char *format)
│      │    0x31171470      66c78538fa..   mov word [var_5c8h], 2
│      │    0x31171479      c7853cfaff..   mov dword [var_5c4h], 0
│      │    0x31171483      c704240f27..   mov dword [esp], 0x270f     ; '\x0f\''
│      │                                                               ; [0x270f:4]=-1 ; u_short hostshort                    
│      │    0x3117148a      e8a9020000     call sym._htons_4           ; u_short htons(u_short hostshort)
│      │    0x3117148f      83ec04         sub esp, 4
│      │    0x31171492      6689853afa..   mov word [var_5c6h], ax
│      │    0x31171499      c744240810..   mov dword [namelen], 0x10   ; [0x10:4]=-1 ; 16 ; int namelen
│      │    0x311714a1      8d8538faffff   lea eax, [var_5c8h]
│      │    0x311714a7      89442404       mov dword [name], eax       ; const sockaddr *name
│      │    0x311714ab      8b8554faffff   mov eax, dword [s]
│      │    0x311714b1      890424         mov dword [esp], eax        ; SOCKET s
│      │    0x311714b4      e877020000     call sym._bind_12           ; int bind(SOCKET s, const sockaddr *name, int namelen)
│      │    0x311714b9      83ec0c         sub esp, 0xc
│      │    0x311714bc      83f8ff         cmp eax, 0xffffffff
│      │┌─< 0x311714bf      7515           jne 0x311714d6
│      ││   0x311714c1      e882020000     call sym._WSAGetLastError_0 ; int WSAGetLastError(void)
│      ││   0x311714c6      89442404       mov dword [backlog], eax
│      ││   0x311714ca      c70424bc33..   mov dword [esp], str.____bind_failed:__d ; [0x311733bc:4]=0x205d215b ; "[!] bind failed: %d" ; const char *format                                                                                                
│      ││   0x311714d1      e822080000     call sym._printf            ; int printf(const char *format)
│      ││   ; CODE XREF from main @ 0x311714bf(x)
│      │└─> 0x311714d6      8b85f4fbffff   mov eax, dword [var_40ch]
│      │    0x311714dc      89442404       mov dword [backlog], eax
│      │    0x311714e0      c70424d033..   mov dword [esp], str.___bind_done_on_port__d_n ; [0x311733d0:4]=0x205d2b5b ; "[+] bind done on port %d\n" ; const char *format                                                                                   
│      │    0x311714e7      e80c080000     call sym._printf            ; int printf(const char *format)
│      │    0x311714ec      c744240403..   mov dword [backlog], 3      ; int backlog
│      │    0x311714f4      8b8554faffff   mov eax, dword [s]
│      │    0x311714fa      890424         mov dword [esp], eax        ; SOCKET s
│      │    0x311714fd      e826020000     call sym._listen_8          ; int listen(SOCKET s, int backlog)
│      │    0x31171502      83ec08         sub esp, 8
│      │    0x31171505      c70424ea33..   mov dword [esp], str.___waiting_for_connections._n ; [0x311733ea:4]=0x205d2b5b ; "[+] waiting for connections.\n" ; const char *format                                                                           
│      │    0x3117150c      e8e7070000     call sym._printf            ; int printf(const char *format)
│      │    0x31171511      c785f8fbff..   mov dword [var_408h], 0x10  ; 16
│      │    ; CODE XREF from main @ 0x31171696(x)
│      │┌─> 0x3117151b      8d85f8fbffff   lea eax, [var_408h]
│      │╎   0x31171521      89442408       mov dword [addrlen], eax    ; int *addrlen
│      │╎   0x31171525      8d8528faffff   lea eax, [var_5d8h]
│      │╎   0x3117152b      89442404       mov dword [addr], eax       ; sockaddr *addr
│      │╎   0x3117152f      8b8554faffff   mov eax, dword [s]
│      │╎   0x31171535      890424         mov dword [esp], eax        ; SOCKET s
│      │╎   0x31171538      e8e3010000     call sym._accept_12         ; SOCKET accept(SOCKET s, sockaddr *addr, int *addrlen)
│      │╎   0x3117153d      83ec0c         sub esp, 0xc
│      │╎   0x31171540      898550faffff   mov dword [var_5b0h], eax
│      │╎   0x31171546      83bd50faff..   cmp dword [var_5b0h], 0xffffffff
│     ┌───< 0x3117154d      0f8448010000   je 0x3117169b
│     ││╎   0x31171553      c704240834..   mov dword [esp], str.___received_connection._n ; [0x31173408:4]=0x205d2b5b ; "[+] received connection.\n" ; const char *format                                                                                   
│     ││╎   0x3117155a      e899070000     call sym._printf            ; int printf(const char *format)
│     ││╎   0x3117155f      c7442408e8..   mov dword [len], 0x3e8      ; [0x3e8:4]=-1 ; 1000 ; size_t n
│     ││╎   0x31171567      c744240400..   mov dword [buf], 0          ; int c
│     ││╎   0x3117156f      8d8508fcffff   lea eax, [var_3f8h]
│     ││╎   0x31171575      890424         mov dword [esp], eax        ; void *s
│     ││╎   0x31171578      e85b070000     call sym._memset            ; void *memset(void *s, int c, size_t n)
│     ││╎   0x3117157d      8b8504fcffff   mov eax, dword [var_3fch]
│     ││╎   0x31171583      890424         mov dword [esp], eax        ; const char *s
│     ││╎   0x31171586      e85d070000     call sym._strlen            ; size_t strlen(const char *s)
│     ││╎   0x3117158b      c744240c00..   mov dword [flags], 0        ; int flags
│     ││╎   0x31171593      89442408       mov dword [len], eax        ; int len
│     ││╎   0x31171597      8b8504fcffff   mov eax, dword [var_3fch]
│     ││╎   0x3117159d      89442404       mov dword [buf], eax        ; const char *buf
│     ││╎   0x311715a1      8b8550faffff   mov eax, dword [var_5b0h]
│     ││╎   0x311715a7      890424         mov dword [esp], eax        ; SOCKET s
│     ││╎   0x311715aa      e869010000     call sym._send_16           ; int send(SOCKET s, const char *buf, int len, int flags)                                                                                                                            
│     ││╎   0x311715af      83ec10         sub esp, 0x10
│     ││╎   0x311715b2      c744240c00..   mov dword [var_ch_2], 0     ; int flags
│     ││╎   0x311715ba      c7442408e8..   mov dword [var_8h_5], 0x3e8 ; [0x3e8:4]=-1 ; 1000 ; int len
│     ││╎   0x311715c2      8d8508fcffff   lea eax, [var_3f8h]
│     ││╎   0x311715c8      89442404       mov dword [var_4h_7], eax   ; char *buf
│     ││╎   0x311715cc      8b8550faffff   mov eax, dword [var_5b0h]
│     ││╎   0x311715d2      890424         mov dword [esp], eax        ; SOCKET s
│     ││╎   0x311715d5      e836010000     call sym._recv_16           ; int recv(SOCKET s, char *buf, int len, int flags)
│     ││╎   0x311715da      83ec10         sub esp, 0x10
│     ││╎   0x311715dd      8d8508fcffff   lea eax, [var_3f8h]
│     ││╎   0x311715e3      890424         mov dword [esp], eax        ; int32_t arg_8h
│     ││╎   0x311715e6      e811fdffff     call sym._get_reply
│     ││╎   0x311715eb      8985f0fbffff   mov dword [var_410h], eax
│     ││╎   0x311715f1      8b85f0fbffff   mov eax, dword [var_410h]
│     ││╎   0x311715f7      89442404       mov dword [var_4h_8], eax
│     ││╎   0x311715fb      c704242234..   mov dword [esp], str.___check_is__d_n ; [0x31173422:4]=0x205d2b5b ; "[+] check is %d\n" ; const char *format                                                                                                     
│     ││╎   0x31171602      e8f1060000     call sym._printf            ; int printf(const char *format)
│     ││╎   0x31171607      8d8508fcffff   lea eax, [var_3f8h]
│     ││╎   0x3117160d      890424         mov dword [esp], eax        ; int32_t arg_8h
│     ││╎   0x31171610      e8e7fcffff     call sym._get_reply
│     ││╎   0x31171615      85c0           test eax, eax
│    ┌────< 0x31171617      7537           jne 0x31171650
│    │││╎   0x31171619      8b8500fcffff   mov eax, dword [var_400h]
│    │││╎   0x3117161f      890424         mov dword [esp], eax        ; const char *s
│    │││╎   0x31171622      e8c1060000     call sym._strlen            ; size_t strlen(const char *s)
│    │││╎   0x31171627      c744240c00..   mov dword [var_ch_3], 0     ; int flags
│    │││╎   0x3117162f      89442408       mov dword [var_8h_6], eax   ; int len
│    │││╎   0x31171633      8b85fcfbffff   mov eax, dword [var_404h]
│    │││╎   0x31171639      89442404       mov dword [var_4h_8], eax   ; const char *buf
│    │││╎   0x3117163d      8b8550faffff   mov eax, dword [var_5b0h]
│    │││╎   0x31171643      890424         mov dword [esp], eax        ; SOCKET s
│    │││╎   0x31171646      e8cd000000     call sym._send_16           ; int send(SOCKET s, const char *buf, int len, int flags)                                                                                                                            
│    │││╎   0x3117164b      83ec10         sub esp, 0x10
│   ┌─────< 0x3117164e      eb35           jmp 0x31171685
│   ││││╎   ; CODE XREF from main @ 0x31171617(x)
│   │└────> 0x31171650      8b85fcfbffff   mov eax, dword [var_404h]
│   │ ││╎   0x31171656      890424         mov dword [esp], eax        ; const char *s
│   │ ││╎   0x31171659      e88a060000     call sym._strlen            ; size_t strlen(const char *s)
│   │ ││╎   0x3117165e      c744240c00..   mov dword [var_ch_3], 0     ; int flags
│   │ ││╎   0x31171666      89442408       mov dword [var_8h_6], eax   ; int len
│   │ ││╎   0x3117166a      8b8500fcffff   mov eax, dword [var_400h]
│   │ ││╎   0x31171670      89442404       mov dword [var_4h_8], eax   ; const char *buf
│   │ ││╎   0x31171674      8b8550faffff   mov eax, dword [var_5b0h]
│   │ ││╎   0x3117167a      890424         mov dword [esp], eax        ; SOCKET s
│   │ ││╎   0x3117167d      e896000000     call sym._send_16           ; int send(SOCKET s, const char *buf, int len, int flags)                                                                                                                            
│   │ ││╎   0x31171682      83ec10         sub esp, 0x10
│   │ ││╎   ; CODE XREF from main @ 0x3117164e(x)
│   └─────> 0x31171685      8b8550faffff   mov eax, dword [var_5b0h]
│     ││╎   0x3117168b      890424         mov dword [esp], eax        ; SOCKET s
│     ││╎   0x3117168e      e875000000     call sym._closesocket_4     ; int closesocket(SOCKET s)
│     ││╎   0x31171693      83ec04         sub esp, 4
│     ││└─< 0x31171696      e980feffff     jmp 0x3117151b
│     ││    ; CODE XREF from main @ 0x3117154d(x)
│     └───> 0x3117169b      83bd50faff..   cmp dword [var_5b0h], 0xffffffff
│      │┌─< 0x311716a2      7521           jne 0x311716c5
│      ││   0x311716a4      e89f000000     call sym._WSAGetLastError_0 ; int WSAGetLastError(void)
│      ││   0x311716a9      89442404       mov dword [buf], eax
│      ││   0x311716ad      c704243334..   mov dword [esp], str.____accept_failed:__d ; [0x31173433:4]=0x205d215b ; "[!] accept failed: %d" ; const char *format                                                                                            
│      ││   0x311716b4      e83f060000     call sym._printf            ; int printf(const char *format)
│      ││   0x311716b9      c78524faff..   mov dword [var_5dch], 1
│     ┌───< 0x311716c3      eb2c           jmp 0x311716f1
│     │││   ; CODE XREF from main @ 0x311716a2(x)
│     ││└─> 0x311716c5      c704244934..   mov dword [esp], str.___cleaning_up._n ; [0x31173449:4]=0x205d2b5b ; "[+] cleaning up.\n" ; const char *format                                                                                                   
│     ││    0x311716cc      e827060000     call sym._printf            ; int printf(const char *format)
│     ││    0x311716d1      8b8554faffff   mov eax, dword [s]
│     ││    0x311716d7      890424         mov dword [esp], eax        ; SOCKET s
│     ││    0x311716da      e829000000     call sym._closesocket_4     ; int closesocket(SOCKET s)
│     ││    0x311716df      83ec04         sub esp, 4
│     ││    0x311716e2      e819000000     call sym._WSACleanup_0      ; int WSACleanup(void)
│     ││    0x311716e7      c78524faff..   mov dword [var_5dch], 0
│     ││    ; CODE XREFS from main @ 0x31171410(x), 0x311716c3(x)
│     └└──> 0x311716f1      8b8524faffff   mov eax, dword [var_5dch]
│           0x311716f7      c9             leave
└           0x311716f8      c3             ret
[0x31171280]> 
```

var_3fch   What's the password
var_400h access denied
var_404h ACCESS_GRANTED

var_3f8h the input buffer

; var char *var_3fch @ ebp-0x3fc
; var char *var_400h @ ebp-0x400
; var char *var_404h @ ebp-0x404

```sh
[0x31171280]> pdf @sym._get_reply
            ; CALL XREFS from main @ 0x311715e6(x), 0x31171610(x)
┌ 103: sym._get_reply (void *arg_8h);
│           ; arg void *arg_8h @ ebp+0x8
│           ; var char *dest @ ebp-0x208
│           ; var char *src @ esp+0x4
│           0x311712fc      55             push ebp
│           0x311712fd      89e5           mov ebp, esp
│           0x311712ff      81ec18020000   sub esp, 0x218
│           0x31171305      8b4508         mov eax, dword [arg_8h]
│           0x31171308      89442404       mov dword [src], eax
│           0x3117130c      c704240030..   mov dword [esp], str._get_reply__s____s__n ; section..rdata
│                                                                      ; [0x31173000:4]=0x7465675b ; "[get_reply] s = [%s]\n" ; const char *format                                                                                                          
│           0x31171313      e8e0090000     call sym._printf            ; int printf(const char *format)
│           0x31171318      8b4508         mov eax, dword [arg_8h]
│           0x3117131b      89442404       mov dword [src], eax        ; const char *src
│           0x3117131f      8d85f8fdffff   lea eax, [dest]
│           0x31171325      890424         mov dword [esp], eax        ; char *dest
│           0x31171328      e8c3090000     call sym._strcpy            ; char *strcpy(char *dest, const char *src)
│           0x3117132d      8d85f8fdffff   lea eax, [dest]
│           0x31171333      890424         mov dword [esp], eax        ; const char *s
│           0x31171336      e8ad090000     call sym._strlen            ; size_t strlen(const char *s)
│           0x3117133b      89442404       mov dword [src], eax
│           0x3117133f      c704241830..   mov dword [esp], str._get_reply__copied__d_bytes_to_buffer_n ; [0x31173018:4]=0x7465675b ; "[get_reply] copied %d bytes to buffer\n" ; const char *format                                                        
│           0x31171346      e8ad090000     call sym._printf            ; int printf(const char *format)
│           0x3117134b      8d85f8fdffff   lea eax, [dest]
│           0x31171351      c74424043f..   mov dword [src], str.shitstorm_n ; [0x3117303f:4]=0x74696873 ; "shitstorm\n" ; const char *s2                                                                                                                    
│           0x31171359      890424         mov dword [esp], eax        ; const char *s1
│           0x3117135c      e87f090000     call sym._strcmp            ; int strcmp(const char *s1, const char *s2)
│           0x31171361      c9             leave
└           0x31171362      c3             ret
```

```sh
┌──(kali㉿kali)-[~]
└─$ nc 10.10.157.116 9999
_|                            _|                                        
_|_|_|    _|  _|_|    _|_|_|      _|_|_|    _|_|_|      _|_|_|  _|_|_|  
_|    _|  _|_|      _|    _|  _|  _|    _|  _|    _|  _|    _|  _|    _|
_|    _|  _|        _|    _|  _|  _|    _|  _|    _|  _|    _|  _|    _|
_|_|_|    _|          _|_|_|  _|  _|    _|  _|_|_|      _|_|_|  _|    _|
                                            _|                          
                                            _|

[________________________ WELCOME TO BRAINPAN _________________________]
                          ENTER THE PASSWORD                              

                          >> shitstorm
                          ACCESS GRANTED  
```

