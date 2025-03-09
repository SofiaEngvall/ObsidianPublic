(solved by 2 teams)

Our threat intelligence has found a malware sample that seems heavily targeted at our competitor, MeatCTF. We tried to analyze it, but it just does nothing when we run it in a VM, can you help us analyze this?

Download the sample [here](https://metaproblems.com/ed113c20f4da2c4b91e580ffd3ac4497/carrot.zip) and unzip with the password `infected`

---

```sh
┌──(kali㉿kali)-[~/Downloads/carrot]
└─$ unzip carrot.zip    
Archive:  carrot.zip
[carrot.zip] carrot password: 
  inflating: carrot

┌──(kali㉿kali)-[~/Downloads/carrot]
└─$ ls -la
total 120
drwxrwxr-x 2 kali kali  4096 Feb 27 23:52 .
drwxr-xr-x 7 kali kali 77824 Feb 27 23:52 ..
-rwxr-xr-x 1 kali kali 23200 Feb 27 21:17 carrot
-rw-rw-r-- 1 kali kali  8389 Feb 27 23:51 carrot.zip
```

```
┌──(kali㉿kali)-[~/Downloads/carrot]
└─$ strings carrot |grep Meta                     
```

```sh
┌──(kali㉿kali)-[~/Downloads/carrot]
└─$ r2 -A -d carrot    
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
INFO: Skipping type matching analysis in debugger mode (aaft)
INFO: Propagate noreturn information (aanr)
INFO: Use -AA or aaaa to perform additional experimental analysis
[0x7ff1ea9abb00]> afl
0x55c08601c030    1      6 sym.imp.EVP_EncryptUpdate
0x55c08601c040    1      6 sym.imp.BIO_new_mem_buf
0x55c08601c050    1      6 sym.imp.EVP_DecryptInit_ex
0x55c08601c060    1      6 sym.imp.strstr
0x55c08601c070    1      6 sym.imp.fork
0x55c08601c080    1      6 sym.imp.curl_global_init
0x55c08601c090    1      6 sym.imp.curl_slist_free_all
0x55c08601c0a0    1      6 sym.imp.mkstemp
0x55c08601c0b0    1      6 sym.imp.EVP_DecryptFinal_ex
0x55c08601c0c0    1      6 sym.imp.write
0x55c08601c0d0    1      6 sym.imp.curl_global_cleanup
0x55c08601c0e0    1      6 sym.imp.strlen
0x55c08601c0f0    1      6 sym.imp.unlink
0x55c08601c100    1      6 sym.imp.strncmp
0x55c08601c110    1      6 sym.imp.getuid
0x55c08601c120    1      6 sym.imp.difftime
0x55c08601c130    1      6 sym.imp.EVP_aes_128_cbc
0x55c08601c140    1      6 sym.imp.RSA_size
0x55c08601c150    1      6 sym.imp.EVP_EncryptInit_ex
0x55c08601c160    1      6 sym.imp.curl_easy_getinfo
0x55c08601c170    1      6 sym.imp.getnameinfo
0x55c08601c180    1      6 sym.imp.EVP_DecryptUpdate
0x55c08601c190    1      6 sym.imp.EVP_CIPHER_CTX_new
0x55c08601c1a0    1      6 sym.imp.RSA_public_encrypt
0x55c08601c1b0    1      6 sym.imp.strncat
0x55c08601c1c0    1      6 sym.imp.sleep
0x55c08601c1d0    1      6 sym.imp.perror
0x55c08601c1e0    1      6 sym.imp.ptrace
0x55c08601c1f0    1      6 sym.imp.chmod
0x55c08601c200    1      6 sym.imp.time
0x55c08601c210    1      6 sym.imp.fclose
0x55c08601c220    1      6 sym.imp.BIO_free
0x55c08601c230    1      6 sym.imp.fdopen
0x55c08601c240    1      6 sym.imp.EVP_CIPHER_CTX_free
0x55c08601c250    1      6 sym.imp.__stack_chk_fail
0x55c08601c260    1      6 sym.imp.RSA_free
0x55c08601c270    1      6 sym.imp.fputs
0x55c08601c280    1      6 sym.imp.curl_easy_setopt
0x55c08601c290    1      6 sym.imp.getpwuid
0x55c08601c2a0    1      6 sym.imp.fopen
0x55c08601c2b0    1      6 sym.imp.free
0x55c08601c2c0    1      6 sym.imp.exit
0x55c08601c2d0    1      6 sym.imp.getenv
0x55c08601c2e0    1      6 sym.imp.curl_easy_cleanup
0x55c08601c2f0    1      6 sym.imp.execl
0x55c08601c300    1      6 sym.imp.curl_slist_append
0x55c08601c310    1      6 sym.imp.curl_easy_init
0x55c08601c320    1      6 sym.imp.curl_easy_perform
0x55c08601c330    1      6 sym.imp.malloc
0x55c08601c340    1      6 sym.imp.strcmp
0x55c08601c350    1      6 sym.imp.RAND_bytes
0x55c08601c360    1      6 sym.imp.gethostname
0x55c08601c370    1      6 sym.imp.opendir
0x55c08601c380    1      6 sym.imp.readdir
0x55c08601c390    1      6 sym.imp.atoi
0x55c08601c3a0    1      6 sym.imp.strtok
0x55c08601c3b0    1      6 sym.imp.fgets
0x55c08601c3c0    1      6 sym.imp.EVP_EncryptFinal_ex
0x55c08601c3d0    1      6 sym.imp.snprintf
0x55c08601c3e0    1      6 sym.imp.closedir
0x55c08601c3f0    1      6 sym.imp.realloc
0x55c08601c400    1      6 sym.imp.freeifaddrs
0x55c08601c410    1      6 sym.imp.strdup
0x55c08601c420    1      6 sym.imp.getifaddrs
0x55c08601c430    1      6 sym.imp.close
0x55c08601c440    1      6 sym.imp.PEM_read_bio_RSA_PUBKEY
0x55c08601c640    1     37 entry0
0x55c08601ffc8   10   4166 reloc.__libc_start_main
0x55c08601c450   30    484 main
0x55c08601c730    5     60 entry.init0
0x55c08601c6e0    5     55 entry.fini0
0x55c08601ffc0    1      8 reloc.__cxa_finalize
0x55c08601c670    4     34 fcn.55c08601c670
0x7ff1ea99a120   23    409 fcn.7ff1ea99a120
0x7ff1ea9a98e0    3     45 fcn.7ff1ea9a98e0
0x7ff1ea99c8f0    3    162 fcn.7ff1ea99c8f0
0x7ff1ea99c240  111   1675 fcn.7ff1ea99c240
0x7ff1ea99cc30    3    208 fcn.7ff1ea99cc30
0x7ff1ea9a9790    5    174 fcn.7ff1ea9a9790
0x7ff1ea9b2e00    1     74 fcn.7ff1ea9b2e00
0x7ff1ea991130    3    148 fcn.7ff1ea991130
0x7ff1ea993800    8    194 fcn.7ff1ea993800
0x7ff1ea9911d0    5     96 fcn.7ff1ea9911d0
0x7ff1ea991230    7    104 fcn.7ff1ea991230
0x7ff1ea9b2db0    1     79 fcn.7ff1ea9b2db0
0x7ff1ea991430   21    340 fcn.7ff1ea991430
0x7ff1ea991600   17    254 fcn.7ff1ea991600
0x7ff1ea9a0120   58   1081 fcn.7ff1ea9a0120
0x7ff1ea9a6f00    8    152 fcn.7ff1ea9a6f00
0x7ff1ea99fe80   14    187 fcn.7ff1ea99fe80
0x7ff1ea9c49f0    1      8 fcn.7ff1ea9c49f0
0x7ff1ea9c49e8    1      8 fcn.7ff1ea9c49e8
0x7ff1ea9a0590   30    407 fcn.7ff1ea9a0590
0x7ff1ea9a6d50    5     49 fcn.7ff1ea9a6d50
0x7ff1ea9925a0    5     64 fcn.7ff1ea9925a0
0x7ff1ea992590    1      1 fcn.7ff1ea992590
0x7ff1ea9a3e20    6    117 fcn.7ff1ea9a3e20
0x7ff1ea9b24c0   18    187 fcn.7ff1ea9b24c0
0x7ff1ea991710  199   3536 fcn.7ff1ea991710
0x7ff1ea997940  124   2819 fcn.7ff1ea997940
0x7ff1ea9b36e0   27    459 fcn.7ff1ea9b36e0
0x7ff1ea9b58a0   13    380 fcn.7ff1ea9b58a0
0x7ff1ea995350   24    359 fcn.7ff1ea995350
0x7ff1ea9952a0   10    162 fcn.7ff1ea9952a0
0x7ff1ea9b4040   10    526 fcn.7ff1ea9b4040
0x7ff1ea994440   11    200 fcn.7ff1ea994440
0x7ff1ea9b5a40   27    438 fcn.7ff1ea9b5a40
0x7ff1ea99c080   19    403 fcn.7ff1ea99c080
0x7ff1ea9b36d0    1      8 fcn.7ff1ea9b36d0
0x7ff1ea9b2a50   14    160 fcn.7ff1ea9b2a50
0x7ff1ea993d50    1     31 fcn.7ff1ea993d50
0x7ff1ea9b38c0   18    187 fcn.7ff1ea9b38c0
0x7ff1ea9937c0    3     51 fcn.7ff1ea9937c0
0x7ff1ea9b2ba0    3     32 fcn.7ff1ea9b2ba0
0x7ff1ea9b2c60    7     73 fcn.7ff1ea9b2c60
0x7ff1ea9b2d10    1     21 fcn.7ff1ea9b2d10
0x7ff1ea991080    9    152 fcn.7ff1ea991080
0x7ff1ea9941d0   20    302 fcn.7ff1ea9941d0
0x7ff1ea9b3400   40    681 fcn.7ff1ea9b3400
0x7ff1ea9b2970    6    100 fcn.7ff1ea9b2970
0x7ff1ea9b2a10    3     29 fcn.7ff1ea9b2a10
0x7ff1ea9b2880    3     30 fcn.7ff1ea9b2880
0x7ff1ea9b29e0    3     35 fcn.7ff1ea9b29e0
0x7ff1ea9a6d90   10    166 fcn.7ff1ea9a6d90
0x7ff1ea994700   51    867 fcn.7ff1ea994700
0x7ff1ea9b2760    3     30 fcn.7ff1ea9b2760
0x7ff1ea9b2860    1     18 fcn.7ff1ea9b2860
0x7ff1ea99c9a0    3    162 fcn.7ff1ea99c9a0
0x7ff1ea9b4260   17    337 fcn.7ff1ea9b4260
0x7ff1ea9b3990   27    790 fcn.7ff1ea9b3990
0x7ff1ea994520   40    410 fcn.7ff1ea994520
0x7ff1ea9a9bf0   13    112 fcn.7ff1ea9a9bf0
0x7ff1ea9b2630    1      7 fcn.7ff1ea9b2630
0x7ff1ea9b2b00   10    141 fcn.7ff1ea9b2b00
0x7ff1ea9b2bc0    3     32 fcn.7ff1ea9b2bc0
0x7ff1ea99cb90    3    158 fcn.7ff1ea99cb90
0x7ff1ea9c49f8    1     16 fcn.7ff1ea9c49f8
0x7ff1ea9b2690    4    162 fcn.7ff1ea9b2690
0x7ff1ea9b2e50   14    424 fcn.7ff1ea9b2e50
0x7ff1ea9b76c0    3     30 fcn.7ff1ea9b76c0
0x7ff1ea9b27b0    3     32 fcn.7ff1ea9b27b0
0x7ff1ea9b2a30    3     32 fcn.7ff1ea9b2a30
0x7ff1ea9954d0   13    267 fcn.7ff1ea9954d0
0x7ff1ea9a9120   28    904 fcn.7ff1ea9a9120
0x7ff1ea9958c0   32    451 fcn.7ff1ea9958c0
0x7ff1ea9955e0   40    697 fcn.7ff1ea9955e0
0x7ff1ea99a8a0   52   1020 fcn.7ff1ea99a8a0
0x7ff1ea9951b0   11    224 fcn.7ff1ea9951b0
0x7ff1ea99a590    7     81 fcn.7ff1ea99a590
0x7ff1ea99a800    6    140 fcn.7ff1ea99a800
0x7ff1ea9c4a08    9   1834 fcn.7ff1ea9c4a08
0x7ff1ea995f20   34    462 fcn.7ff1ea995f20
0x7ff1ea99ff50   11    200 fcn.7ff1ea99ff50
0x7ff1ea9a0ae0   17    292 fcn.7ff1ea9a0ae0
0x7ff1ea9a6e40    7    183 fcn.7ff1ea9a6e40
0x7ff1ea993d70   21    338 fcn.7ff1ea993d70
0x7ff1ea996130  281   6067 fcn.7ff1ea996130
0x7ff1ea9b5840    3     61 fcn.7ff1ea9b5840
0x7ff1ea994aa0   69   1515 fcn.7ff1ea994aa0
0x7ff1ea995ab0    9     95 fcn.7ff1ea995ab0
0x7ff1ea9a37f0   39    792 fcn.7ff1ea9a37f0
0x7ff1ea9950c0   10    170 fcn.7ff1ea9950c0
0x7ff1ea998640  144   3554 fcn.7ff1ea998640
0x7ff1ea99a5f0    6     64 fcn.7ff1ea99a5f0
0x7ff1ea9938d0   69   1060 fcn.7ff1ea9938d0
0x7ff1ea9912a0    9    247 fcn.7ff1ea9912a0
0x7ff1ea99a050   10    200 fcn.7ff1ea99a050
0x7ff1ea9b2be0    6    109 fcn.7ff1ea9b2be0
0x7ff1ea9a2640    9     98 fcn.7ff1ea9a2640
0x7ff1ea9b0c20   89   1517 fcn.7ff1ea9b0c20
0x7ff1ea99af30    1     32 fcn.7ff1ea99af30
0x7ff1ea9b1700    7    109 fcn.7ff1ea9b1700
0x7ff1ea9a3b30    3     70 fcn.7ff1ea9a3b30
0x7ff1ea99b0b0   14    199 fcn.7ff1ea99b0b0
0x7ff1ea9925f0   21    332 fcn.7ff1ea9925f0
0x7ff1ea9927c0  163   3915 fcn.7ff1ea9927c0
0x7ff1ea9a26c0  123   2246 fcn.7ff1ea9a26c0
0x7ff1ea99cf90  454   8607 fcn.7ff1ea99cf90
0x7ff1ea9b1f60   85   1331 fcn.7ff1ea9b1f60
0x7ff1ea9a1610   16    315 fcn.7ff1ea9a1610
0x7ff1ea99b480   13    348 fcn.7ff1ea99b480
0x7ff1ea9a9d80   59   1831 fcn.7ff1ea9a9d80
0x7ff1ea9a12b0   50   1088 fcn.7ff1ea9a12b0
0x7ff1ea9a1760   11    283 fcn.7ff1ea9a1760
0x7ff1ea99af50   16    342 fcn.7ff1ea99af50
0x7ff1ea991000    8    118 map._usr_lib_x86_64_linux_gnu_ld_linux_x86_64.so.2.r_x
0x7ff1ea99acc0   20    581 fcn.7ff1ea99acc0
0x7ff1ea9b2d80    1      8 fcn.7ff1ea9b2d80
0x7ff1ea9b2d50    4     30 fcn.7ff1ea9b2d50
0x7ff1ea99cd00   15    264 fcn.7ff1ea99cd00
0x7ff1ea9994b0  157   2901 fcn.7ff1ea9994b0
0x7ff1ea9a71d0   25    623 fcn.7ff1ea9a71d0
0x7ff1ea99ceb0    3    212 fcn.7ff1ea99ceb0
0x7ff1ea99ce50    4     95 fcn.7ff1ea99ce50
0x7ff1ea9a3b80   37    636 fcn.7ff1ea9a3b80
0x7ff1ea99ce20    4     48 fcn.7ff1ea99ce20
0x7ff1ea9a7460   22    541 fcn.7ff1ea9a7460
0x7ff1ea9aa4d0   23    501 fcn.7ff1ea9aa4d0
0x7ff1ea9a0020   14    193 fcn.7ff1ea9a0020
0x7ff1ea9a98b0    1     48 fcn.7ff1ea9a98b0
0x7ff1ea9a0740    3     61 fcn.7ff1ea9a0740
0x7ff1ea9a09a0    7    171 fcn.7ff1ea9a09a0
0x7ff1ea9c49e0    1      8 fcn.7ff1ea9c49e0
0x7ff1ea9a0e70    5    200 fcn.7ff1ea9a0e70
0x7ff1ea99fb30   36    813 fcn.7ff1ea99fb30
0x7ff1ea9a7680    9    320 fcn.7ff1ea9a7680
0x7ff1ea99f870   35    680 fcn.7ff1ea99f870
0x7ff1ea9a1e20   30    288 fcn.7ff1ea9a1e20
0x7ff1ea99a640   36    397 fcn.7ff1ea99a640
0x7ff1ea9a1f70    6    123 fcn.7ff1ea9a1f70
0x7ff1ea99caf0    3    158 fcn.7ff1ea99caf0
0x7ff1ea9a3080   17    237 fcn.7ff1ea9a3080
0x7ff1ea9a9910   13    259 fcn.7ff1ea9a9910
0x7ff1ea9a7020   15    392 fcn.7ff1ea9a7020
0x7ff1ea9a3170   75   1615 fcn.7ff1ea9a3170
0x7ff1ea99a500    7    131 fcn.7ff1ea99a500
0x7ff1ea9a14e0    8     84 fcn.7ff1ea9a14e0
0x7ff1ea9a1890    5     58 fcn.7ff1ea9a1890
0x7ff1ea9a4d80   53    658 fcn.7ff1ea9a4d80
0x7ff1ea9a4710   14    394 fcn.7ff1ea9a4710
0x7ff1ea9a5110   62   1689 fcn.7ff1ea9a5110
0x7ff1ea9a2020    1     28 fcn.7ff1ea9a2020
0x7ff1ea9a2000    1     25 fcn.7ff1ea9a2000
0x7ff1ea9a5020   11    225 fcn.7ff1ea9a5020
0x7ff1ea9a48b0   89   1150 fcn.7ff1ea9a48b0
0x7ff1ea9a41c0   19    294 fcn.7ff1ea9a41c0
0x7ff1ea9a4300   24    311 fcn.7ff1ea9a4300
0x7ff1ea9a57d0  134   4693 fcn.7ff1ea9a57d0
0x7ff1ea9a3070    1      8 fcn.7ff1ea9a3070
0x7ff1ea9a77c0    6    152 fcn.7ff1ea9a77c0
0x7ff1ea9a7860    6    126 fcn.7ff1ea9a7860
0x7ff1ea9a78e0    1     64 fcn.7ff1ea9a78e0
0x7ff1ea9a94c0   15    175 fcn.7ff1ea9a94c0
0x7ff1ea9a8eb0   11    394 fcn.7ff1ea9a8eb0
0x7ff1ea9a8730   52   2871 fcn.7ff1ea9a8730
0x7ff1ea9a7d40   26    396 fcn.7ff1ea9a7d40
0x7ff1ea9a7ef0   26    353 fcn.7ff1ea9a7ef0
0x7ff1ea9a8060   13    486 fcn.7ff1ea9a8060
0x7ff1ea9a7920    1     20 fcn.7ff1ea9a7920
0x7ff1ea9b2d90    3     32 fcn.7ff1ea9b2d90
0x7ff1ea9a96d0    5     64 fcn.7ff1ea9a96d0
0x7ff1ea9a9580    9    149 fcn.7ff1ea9a9580
0x7ff1ea9a9080    4    156 fcn.7ff1ea9a9080
0x7ff1ea9a9620   13    159 fcn.7ff1ea9a9620
0x7ff1ea9aa700   11    418 fcn.7ff1ea9aa700
0x7ff1ea9a2040   84   1108 fcn.7ff1ea9a2040
0x7ff1ea9a00f0    1     42 fcn.7ff1ea9a00f0
0x7ff1ea9b0bf0    3     38 fcn.7ff1ea9b0bf0
0x7ff1ea9a6ca0    3     16 fcn.7ff1ea9a6ca0
0x7ff1ea9b13e0   12    120 fcn.7ff1ea9b13e0
0x7ff1ea9b1510   13    200 fcn.7ff1ea9b1510
0x7ff1ea9ab6f0    8    152 fcn.7ff1ea9ab6f0
0x7ff1ea995b20   36   1018 fcn.7ff1ea995b20
0x7ff1ea9ac780  107   1902 fcn.7ff1ea9ac780
0x7ff1ea994310   17    285 fcn.7ff1ea994310
0x7ff1ea99b180   33    741 fcn.7ff1ea99b180
0x7ff1ea9abc30   25    537 fcn.7ff1ea9abc30
0x7ff1ea9915b0    1     65 fcn.7ff1ea9915b0
0x7ff1ea9b56c0   15    371 fcn.7ff1ea9b56c0
0x7ff1ea9b74b0   10    510 fcn.7ff1ea9b74b0
0x7ff1ea9b30d0   53    743 fcn.7ff1ea9b30d0
0x7ff1ea992520    5    109 fcn.7ff1ea992520
0x7ff1ea9a2ff0    7     99 fcn.7ff1ea9a2ff0
0x7ff1ea9b7290   19    494 fcn.7ff1ea9b7290
0x7ff1ea9a0a50    3    144 fcn.7ff1ea9a0a50
0x7ff1ea9a0c90   17    462 fcn.7ff1ea9a0c90
0x7ff1ea9a15c0    6     62 fcn.7ff1ea9a15c0
0x7ff1ea9a1940    6    308 fcn.7ff1ea9a1940
0x7ff1ea9a9740    1     57 fcn.7ff1ea9a9740
0x7ff1ea9ab440    7    177 fcn.7ff1ea9ab440
0x7ff1ea9abe70   27    519 fcn.7ff1ea9abe70
0x7ff1ea9ac110    3    142 fcn.7ff1ea9ac110
0x7ff1ea9a18e0    1     85 fcn.7ff1ea9a18e0
0x7ff1ea9a8f80    8     55 fcn.7ff1ea9a8f80
0x7ff1ea9ab510   22    472 fcn.7ff1ea9ab510
0x7ff1ea9a0c10   10    113 fcn.7ff1ea9a0c10
0x7ff1ea9a6cd0    6    127 fcn.7ff1ea9a6cd0
0x7ff1ea9b2740    3     30 fcn.7ff1ea9b2740
0x7ff1ea9913a0    6    132 fcn.7ff1ea9913a0
0x7ff1ea9a0f40   31    671 fcn.7ff1ea9a0f40
0x7ff1ea9ab500    1      1 fcn.7ff1ea9ab500
0x7ff1ea9ac1a0   19    337 fcn.7ff1ea9ac1a0
0x7ff1ea9ac5e0   18    408 fcn.7ff1ea9ac5e0
0x7ff1ea9ac310    8    175 fcn.7ff1ea9ac310
0x7ff1ea9ab790    4     75 fcn.7ff1ea9ab790
0x7ff1ea9ab800   31    707 fcn.7ff1ea9ab800
0x7ff1ea9b1db0   26    587 fcn.7ff1ea9b1db0
0x7ff1ea9a9a20    3    270 fcn.7ff1ea9a9a20
0x7ff1ea9a9c70   12    262 fcn.7ff1ea9a9c70
0x7ff1ea9ac3d0   26    492 fcn.7ff1ea9ac3d0
0x7ff1ea9b5890    6     50 fcn.7ff1ea9b5890
0x7ff1ea9b3040   11    128 fcn.7ff1ea9b3040
0x7ff1ea9a8fe0   16    141 fcn.7ff1ea9a8fe0
0x7ff1ea9acf30   14    235 fcn.7ff1ea9acf30
0x7ff1ea9a24d0   13    253 fcn.7ff1ea9a24d0
0x7ff1ea9ab7e0    1     32 fcn.7ff1ea9ab7e0
0x7ff1ea9a7940   27   1003 fcn.7ff1ea9a7940
0x7ff1ea9b27d0    1     21 fcn.7ff1ea9b27d0
0x7ff1ea9b27f0    6     89 fcn.7ff1ea9b27f0
0x7ff1ea9b1550    3     38 fcn.7ff1ea9b1550
0x7ff1ea9b1580   11    147 fcn.7ff1ea9b1580
0x7ff1ea9b28a0    7    106 fcn.7ff1ea9b28a0
0x7ff1ea9b1280    8    182 fcn.7ff1ea9b1280
0x7ff1ea9b1620    9    113 fcn.7ff1ea9b1620
0x7ff1ea9b2780    3     34 fcn.7ff1ea9b2780
0x7ff1ea9b16a0    1     40 fcn.7ff1ea9b16a0
0x7ff1ea9b16d0    3     44 fcn.7ff1ea9b16d0
0x7ff1ea9b1780    6     99 fcn.7ff1ea9b1780
0x7ff1ea9b17f0   29    407 fcn.7ff1ea9b17f0
[0x7ff1ea9abb00]> pdf @main
            ;-- section..text:
            ; DATA XREF from entry0 @ 0x55c08601c658(r)
┌ 484: int main (int argc, char **argv, char **envp);
│ afv: vars(5:sp[0x40..0x68])
│           0x55c08601c450      4157           push r15                ; [13] -r-x section size 5592 named .text
│           0x55c08601c452      4156           push r14
│           0x55c08601c454      4155           push r13
│           0x55c08601c456      4154           push r12
│           0x55c08601c458      55             push rbp
│           0x55c08601c459      53             push rbx
│           0x55c08601c45a      4883ec38       sub rsp, 0x38
│           0x55c08601c45e      64488b0425..   mov rax, qword fs:[0x28]
│           0x55c08601c467      4889442428     mov qword [var_28h], rax
│           0x55c08601c46c      31c0           xor eax, eax
│           0x55c08601c46e      e8be100000     call 0x55c08601d531
│           0x55c08601c473      85c0           test eax, eax
│       ┌─< 0x55c08601c475      740c           je 0x55c08601c483
│ ┌┌┌┌┌┌──> 0x55c08601c477      31c0           xor eax, eax
│ ╎╎╎╎╎╎│   0x55c08601c479      e87e140000     call 0x55c08601d8fc
│ ────────< 0x55c08601c47e      e996000000     jmp 0x55c08601c519
│ ╎╎╎╎╎╎└─> 0x55c08601c483      31c0           xor eax, eax
│ ╎╎╎╎╎╎    0x55c08601c485      e890120000     call 0x55c08601d71a
│ ╎╎╎╎╎╎    0x55c08601c48a      85c0           test eax, eax
│ ────────< 0x55c08601c48c      75e9           jne 0x55c08601c477
│ ╎╎╎╎╎╎    0x55c08601c48e      e8e0120000     call 0x55c08601d773
│ ╎╎╎╎╎╎    0x55c08601c493      85c0           test eax, eax
│ ────────< 0x55c08601c495      75e0           jne 0x55c08601c477
│ ╎╎╎╎╎╎    0x55c08601c497      e8d3100000     call 0x55c08601d56f
│ ╎╎╎╎╎╎    0x55c08601c49c      85c0           test eax, eax
│ ────────< 0x55c08601c49e      75d7           jne 0x55c08601c477
│ ╎╎╎╎╎╎    0x55c08601c4a0      e87d110000     call 0x55c08601d622
│ ╎╎╎╎╎╎    0x55c08601c4a5      85c0           test eax, eax
│ ────────< 0x55c08601c4a7      75ce           jne 0x55c08601c477
│ ╎╎╎╎╎╎    0x55c08601c4a9      e82c130000     call 0x55c08601d7da
│ ╎╎╎╎╎╎    0x55c08601c4ae      85c0           test eax, eax
│ └───────< 0x55c08601c4b0      74c5           je 0x55c08601c477
│  ╎╎╎╎╎    0x55c08601c4b2      31c0           xor eax, eax
│  ╎╎╎╎╎    0x55c08601c4b4      e8fd0d0000     call 0x55c08601d2b6
│  ╎╎╎╎╎    0x55c08601c4b9      85c0           test eax, eax
│  └──────< 0x55c08601c4bb      74ba           je 0x55c08601c477
│   ╎╎╎╎    0x55c08601c4bd      31c0           xor eax, eax
│   ╎╎╎╎    0x55c08601c4bf      e8b40e0000     call 0x55c08601d378
│   ╎╎╎╎    0x55c08601c4c4      85c0           test eax, eax
│   └─────< 0x55c08601c4c6      75af           jne 0x55c08601c477
│    ╎╎╎    0x55c08601c4c8      e836100000     call 0x55c08601d503
│    ╎╎╎    0x55c08601c4cd      85c0           test eax, eax
│    └────< 0x55c08601c4cf      74a6           je 0x55c08601c477
│     ╎╎    0x55c08601c4d1      31c0           xor eax, eax
│     ╎╎    0x55c08601c4d3      e8af070000     call 0x55c08601cc87
│     ╎╎    0x55c08601c4d8      85c0           test eax, eax
│     └───< 0x55c08601c4da      759b           jne 0x55c08601c477
│      ╎    0x55c08601c4dc      e879070000     call 0x55c08601cc5a
│      ╎    0x55c08601c4e1      ffc8           dec eax
│      └──< 0x55c08601c4e3      7e92           jle 0x55c08601c477
│           0x55c08601c4e5      31c0           xor eax, eax
│           0x55c08601c4e7      e8a7020000     call 0x55c08601c793
│           0x55c08601c4ec      4889c3         mov rbx, rax
│           0x55c08601c4ef      4885c0         test rax, rax
│       ┌─< 0x55c08601c4f2      7416           je 0x55c08601c50a
│       │   0x55c08601c4f4      488d35c21d..   lea rsi, [0x55c08601e2bd] ; "www"
│       │   0x55c08601c4fb      4889c7         mov rdi, rax
│       │   0x55c08601c4fe      e83dfeffff     call sym.imp.strcmp     ; int strcmp(const char *s1, const char *s2)
│       │   0x55c08601c503      4189c5         mov r13d, eax
│       │   0x55c08601c506      85c0           test eax, eax
│      ┌──< 0x55c08601c508      741a           je 0x55c08601c524
│      │└─> 0x55c08601c50a      31c0           xor eax, eax
│      │    0x55c08601c50c      e8eb130000     call 0x55c08601d8fc
│      │    ; CODE XREF from main @ 0x55c08601c568(x)
│     ┌─┌─> 0x55c08601c511      4889df         mov rdi, rbx
│    ┌────> 0x55c08601c514      e897fdffff     call sym.imp.free       ; void free(void *ptr)
│    ╎╎│╎   ; CODE XREFS from main @ 0x55c08601c47e(x), 0x55c08601c5b3(x)
│ ─┌┌─────> 0x55c08601c519      41bd01000000   mov r13d, 1
│ ┌───────< 0x55c08601c51f      e9e9000000     jmp 0x55c08601c60d
│ │╎╎╎╎└──> 0x55c08601c524      4889df         mov rdi, rbx
│ │╎╎╎╎ ╎   0x55c08601c527      e884fdffff     call sym.imp.free       ; void free(void *ptr)
│ │╎╎╎╎ ╎   0x55c08601c52c      31c0           xor eax, eax
│ │╎╎╎╎ ╎   0x55c08601c52e      e86c070000     call 0x55c08601cc9f
│ │╎╎╎╎ ╎   0x55c08601c533      4889c3         mov rbx, rax
│ │╎╎╎╎ ╎   0x55c08601c536      4885c0         test rax, rax
│ │└──────< 0x55c08601c539      74de           je 0x55c08601c519
│ │ ╎╎╎ ╎   0x55c08601c53b      31c0           xor eax, eax
│ │ ╎╎╎ ╎   0x55c08601c53d      e857080000     call 0x55c08601cd99
│ │ ╎╎╎ ╎   0x55c08601c542      4889c5         mov rbp, rax
│ │ ╎╎╎ ╎   0x55c08601c545      4885c0         test rax, rax
│ │ ╎╎└───< 0x55c08601c548      74c7           je 0x55c08601c511
│ │ ╎╎  ╎   0x55c08601c54a      4c8d742408     lea r14, [var_8h]
│ │ ╎╎  ╎   0x55c08601c54f      be10000000     mov esi, 0x10           ; 16
│ │ ╎╎  ╎   0x55c08601c554      4c89f7         mov rdi, r14
│ │ ╎╎  ╎   0x55c08601c557      e8f4fdffff     call sym.imp.RAND_bytes
│ │ ╎╎  ╎   0x55c08601c55c      85c0           test eax, eax
│ │ ╎╎ ┌──< 0x55c08601c55e      750a           jne 0x55c08601c56a
│ │ ╎╎┌───> 0x55c08601c560      4889ef         mov rdi, rbp
│ │ ╎╎╎│╎   0x55c08601c563      e8f8fcffff     call sym.imp.RSA_free
│ │ ╎╎╎│└─< 0x55c08601c568      eba7           jmp 0x55c08601c511
│ │ ╎╎╎└──> 0x55c08601c56a      4c8d7c2418     lea r15, [var_18h]
│ │ ╎╎╎     0x55c08601c56f      be10000000     mov esi, 0x10           ; 16
│ │ ╎╎╎     0x55c08601c574      4c89ff         mov rdi, r15
│ │ ╎╎╎     0x55c08601c577      e8d4fdffff     call sym.imp.RAND_bytes
│ │ ╎╎╎     0x55c08601c57c      85c0           test eax, eax
│ │ ╎╎└───< 0x55c08601c57e      74e0           je 0x55c08601c560
│ │ ╎╎      0x55c08601c580      4889df         mov rdi, rbx
│ │ ╎╎      0x55c08601c583      e858fbffff     call sym.imp.strlen     ; size_t strlen(const char *s)
│ │ ╎╎      0x55c08601c588      4889df         mov rdi, rbx
│ │ ╎╎      0x55c08601c58b      4989e0         mov r8, rsp
│ │ ╎╎      0x55c08601c58e      4c89f9         mov rcx, r15
│ │ ╎╎      0x55c08601c591      4c89f2         mov rdx, r14
│ │ ╎╎      0x55c08601c594      89c6           mov esi, eax
│ │ ╎╎      0x55c08601c596      e83b080000     call 0x55c08601cdd6
│ │ ╎╎      0x55c08601c59b      4889df         mov rdi, rbx
│ │ ╎╎      0x55c08601c59e      4989c4         mov r12, rax
│ │ ╎╎      0x55c08601c5a1      e80afdffff     call sym.imp.free       ; void free(void *ptr)
│ │ ╎╎      0x55c08601c5a6      4d85e4         test r12, r12
│ │ ╎╎  ┌─< 0x55c08601c5a9      750d           jne 0x55c08601c5b8
│ │ ╎╎  │   0x55c08601c5ab      4889ef         mov rdi, rbp
│ │ ╎╎  │   0x55c08601c5ae      e8adfcffff     call sym.imp.RSA_free
│ │ └─────< 0x55c08601c5b3      e961ffffff     jmp 0x55c08601c519
│ │  ╎  └─> 0x55c08601c5b8      488d542404     lea rdx, [var_4h]
│ │  ╎      0x55c08601c5bd      4c89f6         mov rsi, r14
│ │  ╎      0x55c08601c5c0      4889ef         mov rdi, rbp
│ │  ╎      0x55c08601c5c3      e805090000     call 0x55c08601cecd
│ │  ╎      0x55c08601c5c8      4889ef         mov rdi, rbp
│ │  ╎      0x55c08601c5cb      4889c3         mov rbx, rax
│ │  ╎      0x55c08601c5ce      e88dfcffff     call sym.imp.RSA_free
│ │  ╎      0x55c08601c5d3      4c89e7         mov rdi, r12
│ │  ╎      0x55c08601c5d6      4885db         test rbx, rbx
│ │  └────< 0x55c08601c5d9      0f8435ffffff   je 0x55c08601c514
│ │         0x55c08601c5df      50             push rax
│ │         0x55c08601c5e0      4889da         mov rdx, rbx
│ │         0x55c08601c5e3      41b910000000   mov r9d, 0x10           ; 16
│ │         0x55c08601c5e9      4d89f8         mov r8, r15
│ │         0x55c08601c5ec      4156           push r14
│ │         0x55c08601c5ee      8b4c2414       mov ecx, dword [var_4h]
│ │         0x55c08601c5f2      8b742410       mov esi, dword [var_10h]
│ │         0x55c08601c5f6      e82e0a0000     call 0x55c08601d029
│ │         0x55c08601c5fb      4c89e7         mov rdi, r12
│ │         0x55c08601c5fe      e8adfcffff     call sym.imp.free       ; void free(void *ptr)
│ │         0x55c08601c603      4889df         mov rdi, rbx
│ │         0x55c08601c606      e8a5fcffff     call sym.imp.free       ; void free(void *ptr)
│ │         0x55c08601c60b      5a             pop rdx
│ │         0x55c08601c60c      59             pop rcx
│ │         ; CODE XREF from main @ 0x55c08601c51f(x)
│ └───────> 0x55c08601c60d      488b442428     mov rax, qword [var_28h]
│           0x55c08601c612      64482b0425..   sub rax, qword fs:[0x28]
│       ┌─< 0x55c08601c61b      7405           je 0x55c08601c622
│       │   0x55c08601c61d      e82efcffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
│       └─> 0x55c08601c622      4883c438       add rsp, 0x38
│           0x55c08601c626      4489e8         mov eax, r13d
│           0x55c08601c629      5b             pop rbx
│           0x55c08601c62a      5d             pop rbp
│           0x55c08601c62b      415c           pop r12
│           0x55c08601c62d      415d           pop r13
│           0x55c08601c62f      415e           pop r14
│           0x55c08601c631      415f           pop r15
└           0x55c08601c633      c3             ret
[0x7ff1ea9abb00]> 
```
nice that pdf @main works without a main :)

```sh
┌──(kali㉿kali)-[~/Downloads/carrot]
└─$ file carrot     
carrot: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=fd82f7845645aea67dee789f5cac0de456e83108, for GNU/Linux 4.4.0, stripped
```

```
┌──(kali㉿kali)-[~/Downloads/carrot]
└─$ strings carrot                                
/lib64/ld-linux-x86-64.so.2
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
curl_slist_append
curl_global_cleanup
curl_easy_cleanup
curl_slist_free_all
curl_easy_init
curl_global_init
curl_easy_perform
curl_easy_getinfo
curl_easy_setopt
RSA_free
EVP_DecryptUpdate
RAND_bytes
EVP_aes_128_cbc
BIO_free
EVP_CIPHER_CTX_new
EVP_CIPHER_CTX_free
PEM_read_bio_RSA_PUBKEY
EVP_EncryptUpdate
EVP_EncryptFinal_ex
RSA_size
RSA_public_encrypt
EVP_DecryptFinal_ex
BIO_new_mem_buf
EVP_EncryptInit_ex
EVP_DecryptInit_ex
fgets
gethostname
snprintf
chmod
sleep
perror
__stack_chk_fail
exit
strdup
closedir
unlink
difftime
strtok
fopen
getpwuid
fork
strlen
strstr
ptrace
mkstemp
realloc
getnameinfo
atoi
malloc
__libc_start_main
execl
strncat
fdopen
__cxa_finalize
readdir
getenv
fclose
fputs
opendir
getuid
strcmp
getifaddrs
write
freeifaddrs
strncmp
libcurl.so.4
libcrypto.so.3
libc.so.6
CURL_OPENSSL_4
GLIBC_2.3
GLIBC_2.4
GLIBC_2.34
GLIBC_2.2.5
OPENSSL_3.0.0
AWAVAUATUSH
D$(1
D$(dH+
[]A\A]A^A_
PTE1
u3UH
[]A\
AVAUATUSH
[]A\A]A^
AWAVAUATUSH
[]A\A]A^A_
AWAVL
AUATE1
[]A\A]A^A_
AVAUATUSH
[]A\A]A^A_
ATUSH
Hct$
[]A\A]A^A_
AVATI
[]A\A^
ATUSH
Hct$
[]A\A]A^A_
AVAULc
USIc
|$ H
D$(dH
D$@1
t$ Ic
T$(L
t$HH
/tmp/sysL
l$PH
temd-tmpH
D$PL
-XXXXXX
T$XH
tVHcT$4H
D$hdH+
x[]A\A]A^A_
ATUSH
[]A\
AVAUATU1
[]A\A]A^
[]A\
ATUSH
l$8H
[]A\A]
AUATUSH
/tmp/XXXL
XXXXXX.tL
[]A\A]A^
gethostname
getpwuid
malloc
getifaddrs
/proc
opendir
/proc/%s/cmdline
%s/%s
_input
/sys/class/hwmon
/sys/devices
/proc/acpi/fan
LD_PRELOAD
unknown
{"ip_addresses": "%s", "hostname": "%s", "username": "%s", "processes": "%s", "fan_count": %d, "ld_preload_set": %d}
Content-Type: application/octet-stream
https://e973351f665441a608f99ad8fa2cd797.statichosting-aws.com/register
chmod
10.13.37.
wireshark
pspy
strace
ltrace
apache2
meatctf
ptrace
/proc/cpuinfo
fopen
hypervisor
VMware
VirtualBox
QEMU
/sys/class/dmi/id/product_name
/sys/class/dmi/id/sys_vendor
/proc/scsi/scsi
/proc/ide/hd0/model
/proc/ide/hd1/model
https://metactf.com
https://e205e724dda896b5a70bb03b7aed1dba.metactf.com
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvbjqnQ9qenZQsaJZPQuj
pgwv3hHwdmi45mBS/AjnjluAW1tKFFtCJU5GSpnLs6jgRzjxT1BguUTAdkKF1Qr9
sPMj3HpKR3i2oQeh07k4bRxUdAy8O3AYzKfSWo0Qv34Y5Tp/SvTcIMT2omjnuw3I
lDdLK7aSnHU3RS2EBID/7PnZ6iPGGgxjeJkn6T+JxGbYPIJlMKkL8FAT51Xgzip5
q5iRiTbwlEmbSQ5zz2dZwZcD1iUIfYnsfdkKiuz8VtFFKeyTTOGTTaoX/nubyZUe
r3NVodJ/y6bFx6ERJevDYPc3Ck16wurGnR0GZo3RRpHexz9Jr0vhmb8PFGCzRjTf
WQIDAQAB
-----END PUBLIC KEY-----
fffff
;*3$"
GCC: (GNU) 14.2.1 20250207
.shstrtab
.note.gnu.property
.note.gnu.build-id
.interp
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.note.ABI-tag
.init_array
.fini_array
.dynamic
.got
.got.plt
.data
.bss
.comment
```

Looked at it in ghidra too, in c we see it as a big if with lots of function calls in it - I need to learn more about ghidra and re to finish this one!

