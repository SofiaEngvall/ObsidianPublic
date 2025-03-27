

Running the program:
```sh
┌──(kali㉿kali)-[~/thm/valley]
└─$ ./valleyAuthenticator                         
Welcome to Valley Inc. Authenticator
What is your username: q
What is your password: q
Wrong Password or Username
```

tried Radare2 (included in kali):
```sh
┌──(kali㉿kali)-[~/thm/valley]
└─$ r2 -A valleyAuthenticator 
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Finding and parsing C++ vtables (avrr)
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information (aanr)
[x] Use -AA or aaaa to perform additional experimental analysis.
[0x0049a3e8]> 
[0x0049a3e8]> help
Usage: head 7 [file]
[0x0049a3e8]> iz
[Strings]
nth paddr vaddr len size section type string
――――――――――――――――――――――――――――――――――――――――――――

[0x0049a3e8]> exit
```

tried opening in ghidra, there are errors
![[Images/Pasted image 20240517174628.png]]

looked at the strings (search, for strings, uncheck req null term, All blocks)
![[Images/Pasted image 20240517175521.png]]
![[Images/Pasted image 20240517174809.png]]

Googling.. upx -d filename to extract
Running upx (included in kali):
```sh
┌──(kali㉿kali)-[~/thm/valley]
└─$ ls -la
total 59576
...
-rw-r--r--  1 kali kali 1972448 Mar  6  2023 siemHTTP2.pcapng
-rwxr-xr-x  1 kali kali  749128 May 17 16:21 valleyAuthenticator

┌──(kali㉿kali)-[~/thm/valley]
└─$ upx -d valleyAuthenticator 
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2024
UPX 4.2.2       Markus Oberhumer, Laszlo Molnar & John Reiser    Jan 3rd 2024

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
   2290962 <-    749128   32.70%   linux/amd64   valleyAuthenticator

Unpacked 1 file.
                                                                                                                              
┌──(kali㉿kali)-[~/thm/valley]
└─$ ls -la
total 61080
...
-rw-r--r--  1 kali kali 1972448 Mar  6  2023 siemHTTP2.pcapng
-rwxr-xr-x  1 kali kali 2285616 May 17 16:21 valleyAuthenticator
```
File has grown

Running r2 again - this time finding the strings!
```sh
┌──(kali㉿kali)-[~/thm/valley]
└─$ r2 -A valleyAuthenticator
[Cannot find basic block for switch case at 0x004e3d21 bbdelta = 26
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[Error reading vmi_base_counttables (avrr)
[x] Finding and parsing C++ vtables (avrr)
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information (aanr)
[x] Use -AA or aaaa to perform additional experimental analysis.
[0x00404460]> iz
Do you want to print 1906 lines? (y/N) y
[Strings]
nth  paddr      vaddr      len size section type    string
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
0    0x0015c008 0x0055c008 32  33   .rodata ascii   e6722920bab2326f8217e4bf6b1b58ac
1    0x0015c030 0x0055c030 32  33   .rodata ascii   dd2921cc76ee3abfd2beb60709056cfb
2    0x0015c058 0x0055c058 36  37   .rodata ascii   Welcome to Valley Inc. Authenticator
3    0x0015c07d 0x0055c07d 23  24   .rodata ascii   What is your username: 
4    0x0015c095 0x0055c095 23  24   .rodata ascii   What is your password: 
5    0x0015c0ad 0x0055c0ad 13  14   .rodata ascii   Authenticated
6    0x0015c0bb 0x0055c0bb 26  27   .rodata ascii   Wrong Password or Username
7    0x0015c0d8 0x0055c0d8 41  42   .rodata ascii   basic_string::_M_construct null not valid
8    0x0015c109 0x0055c109 4   5    .rodata ascii   %02x
9    0x0015c110 0x0055c110 41  42   .rodata ascii   basic_string::_M_construct null not valid
10   0x0015c170 0x0055c170 29  30   .rodata ascii   terminate called recursively\n
11   0x0015c191 0x0055c191 11  12   .rodata ascii     what():  
12   0x0015c1a0 0x0055c1a0 48  49   .rodata ascii   terminate called after throwing an instance of '
13   0x0015c1d8 0x0055c1d8 45  46   .rodata ascii   terminate called without an active exception\n
14   0x0015c206 0x0055c206 20  21   .rodata ascii   basic_string::append
15   0x0015c220 0x0055c220 35  36   .rodata ascii   __gnu_cxx::__concurrence_lock_error
16   0x0015c248 0x0055c248 37  38   .rodata ascii   __gnu_cxx::__concurrence_unlock_error
17   0x0015c270 0x0055c270 48  49   .rodata ascii   locale::_S_normalize_category category not found
18   0x0015c2a8 0x0055c2a8 31  32   .rodata ascii   locale::_Impl::_M_replace_facet
19   0x0015c2f0 0x0055c2f0 17  18   .rodata ascii   NSt6locale5facetE
20   0x0015c320 0x0055c320 38  39   .rodata ascii   N9__gnu_cxx24__concurrence_lock_errorE
21   0x0015c360 0x0055c360 40  41   .rodata ascii   N9__gnu_cxx26__concurrence_unlock_errorE
22   0x0015c3c0 0x0055c3c0 29  30   .rodata ascii   St18__moneypunct_cacheIcLb1EE
23   0x0015c3e0 0x0055c3e0 29  30   .rodata ascii   St18__moneypunct_cacheIcLb0EE
24   0x0015c400 0x0055c400 29  30   .rodata ascii   St18__moneypunct_cacheIwLb1EE
25   0x0015c420 0x0055c420 29  30   .rodata ascii   St18__moneypunct_cacheIwLb0EE
26   0x0015c43e 0x0055c43e 4   5    .rodata ascii   true
27   0x0015c443 0x0055c443 5   6    .rodata ascii   false
28   0x0015c44c 0x0055c44c 4   20   .rodata utf32le true
29   0x0015c460 0x0055c460 5   24   .rodata utf32le false
30   0x0015c478 0x0055c478 5   6    .rodata ascii   UTF-8
31   0x0015c486 0x0055c486 15  16   .rodata ascii   ASCII//TRANSLIT
32   0x0015c496 0x0055c496 5   6    .rodata ascii   ASCII
33   0x0015c4a0 0x0055c4a0 23  24   .rodata ascii   St16__numpunct_cacheIcE
34   0x0015c4c0 0x0055c4c0 23  24   .rodata ascii   St16__numpunct_cacheIwE
35   0x0015c4e0 0x0055c4e0 16  17   .rodata ascii   St12codecvt_base
36   0x0015c500 0x0055c500 45  46   .rodata ascii   St23__codecvt_abstract_baseIDsc11__mbstate_tE
37   0x0015c530 0x0055c530 28  29   .rodata ascii   St7codecvtIDsc11__mbstate_tE
38   0x0015c560 0x0055c560 45  46   .rodata ascii   St23__codecvt_abstract_baseIDic11__mbstate_tE
39   0x0015c590 0x0055c590 28  29   .rodata ascii   St7codecvtIDic11__mbstate_tE
40   0x0015c5c0 0x0055c5c0 46  47   .rodata ascii   St23__codecvt_abstract_baseIDsDu11__mbstate_tE
41   0x0015c5f0 0x0055c5f0 29  30   .rodata ascii   St7codecvtIDsDu11__mbstate_tE
42   0x0015c620 0x0055c620 46  47   .rodata ascii   St23__codecvt_abstract_baseIDiDu11__mbstate_tE
43   0x0015c650 0x0055c650 29  30   .rodata ascii   St7codecvtIDiDu11__mbstate_tE
44   0x0015c670 0x0055c670 27  28   .rodata ascii   St19__codecvt_utf8_baseIDsE
45   0x0015c690 0x0055c690 28  29   .rodata ascii   St20__codecvt_utf16_baseIDsE
46   0x0015c6c0 0x0055c6c0 33  34   .rodata ascii   St25__codecvt_utf8_utf16_baseIDsE
47   0x0015c6f0 0x0055c6f0 27  28   .rodata ascii   St19__codecvt_utf8_baseIDiE
48   0x0015c710 0x0055c710 28  29   .rodata ascii   St20__codecvt_utf16_baseIDiE
49   0x0015c740 0x0055c740 33  34   .rodata ascii   St25__codecvt_utf8_utf16_baseIDiE
50   0x0015c770 0x0055c770 26  27   .rodata ascii   St19__codecvt_utf8_baseIwE
51   0x0015c790 0x0055c790 27  28   .rodata ascii   St20__codecvt_utf16_baseIwE
52   0x0015c7c0 0x0055c7c0 32  33   .rodata ascii   St25__codecvt_utf8_utf16_baseIwE
53   0x0015c7e4 0x0055c7e4 26  27   .rodata ascii   uninitialized __any_string
54   0x0015c800 0x0055c800 41  42   .rodata ascii   basic_string::_S_construct null not valid
55   0x0015c8e0 0x0055c8e0 44  45   .rodata ascii   cannot create shim for unknown locale::facet
56   0x0015c920 0x0055c920 52  53   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_113numpunct_shimIcEE
57   0x0015c960 0x0055c960 51  52   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_112collate_shimIcEE
58   0x0015c9a0 0x0055c9a0 58  59   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_115moneypunct_shimIcLb1EEE
59   0x0015c9e0 0x0055c9e0 58  59   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_115moneypunct_shimIcLb0EEE
60   0x0015ca20 0x0055ca20 53  54   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_114money_get_shimIcEE
61   0x0015ca60 0x0055ca60 53  54   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_114money_put_shimIcEE
62   0x0015caa0 0x0055caa0 52  53   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_113messages_shimIcEE
63   0x0015cae0 0x0055cae0 52  53   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_113numpunct_shimIwEE
64   0x0015cb20 0x0055cb20 51  52   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_112collate_shimIwEE
65   0x0015cb60 0x0055cb60 58  59   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_115moneypunct_shimIwLb1EEE
66   0x0015cba0 0x0055cba0 58  59   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_115moneypunct_shimIwLb0EEE
67   0x0015cbe0 0x0055cbe0 53  54   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_114money_get_shimIwEE
68   0x0015cc20 0x0055cc20 53  54   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_114money_put_shimIwEE
69   0x0015cc60 0x0055cc60 52  53   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_113messages_shimIwEE
70   0x0015cca0 0x0055cca0 24  25   .rodata ascii   NSt6locale5facet6__shimE
71   0x0015ccc0 0x0055ccc0 52  53   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_113time_get_shimIcEE
72   0x0015cd00 0x0055cd00 52  53   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_113time_get_shimIwEE
73   0x0015cd38 0x0055cd38 54  55   .rodata ascii   %s: __pos (which is %zu) > this->size() (which is %zu)
74   0x0015cd70 0x0055cd70 67  68   .rodata ascii   basic_string::at: __n (which is %zu) >= this->size() (which is %zu)
75   0x0015cdb4 0x0055cdb4 18  19   .rodata ascii   basic_string::copy
76   0x0015cdc7 0x0055cdc7 21  22   .rodata ascii   basic_string::compare
77   0x0015cddd 0x0055cddd 23  24   .rodata ascii   basic_string::_S_create
78   0x0015cdf5 0x0055cdf5 19  20   .rodata ascii   basic_string::erase
79   0x0015ce09 0x0055ce09 28  29   .rodata ascii   basic_string::_M_replace_aux
80   0x0015ce26 0x0055ce26 20  21   .rodata ascii   basic_string::insert
81   0x0015ce3b 0x0055ce3b 21  22   .rodata ascii   basic_string::replace
82   0x0015ce51 0x0055ce51 20  21   .rodata ascii   basic_string::assign
83   0x0015ce66 0x0055ce66 20  21   .rodata ascii   basic_string::resize
84   0x0015ce7b 0x0055ce7b 26  27   .rodata ascii   basic_string::basic_string
85   0x0015ce96 0x0055ce96 20  21   .rodata ascii   basic_string::substr
86   0x0015ced8 0x0055ced8 5   6    .rodata ascii   POSIX
87   0x0015cee0 0x0055cee0 14  15   .rodata ascii   St10ctype_base
88   0x0015cef0 0x0055cef0 11  12   .rodata ascii   St5ctypeIcE
89   0x0015cf00 0x0055cf00 11  12   .rodata ascii   St5ctypeIwE
90   0x0015cf10 0x0055cf10 19  20   .rodata ascii   St12ctype_bynameIwE
91   0x0015cf47 0x0055cf47 6   7    .rodata ascii    print
92   0x0015cf4e 0x0055cf4e 5   6    .rodata ascii   cntrl
93   0x0015cf54 0x0055cf54 5   6    .rodata ascii   upper
94   0x0015cf5a 0x0055cf5a 5   6    .rodata ascii   lower
95   0x0015cf60 0x0055cf60 5   6    .rodata ascii   alpha
96   0x0015cf66 0x0055cf66 6   7    .rodata ascii   xdigit
97   0x0015cf6d 0x0055cf6d 5   6    .rodata ascii   alnum
98   0x0015cf73 0x0055cf73 5   6    .rodata ascii   graph
99   0x0015cf79 0x0055cf79 5   6    .rodata ascii   blank
100  0x0015cf80 0x0055cf80 19  20   .rodata ascii   St12ctype_bynameIcE
101  0x0015cf98 0x0055cf98 41  42   .rodata ascii   basic_string::_M_construct null not valid
102  0x0015d014 0x0055d014 5   6    .rodata ascii   %.*Lf
103  0x0015d01a 0x0055d01a 8   9    .rodata ascii   %m/%d/%y
104  0x0015d023 0x0055d023 5   6    .rodata ascii   %H:%M
105  0x0015d029 0x0055d029 8   9    .rodata ascii   %H:%M:%S
106  0x0015d118 0x0055d118 14  15   .rodata ascii   St10money_base
107  0x0015d130 0x0055d130 17  18   .rodata ascii   St13messages_base
108  0x0015d148 0x0055d148 12  13   .rodata ascii   St9time_base
109  0x0015d160 0x0055d160 23  24   .rodata ascii   NSt7__cxx117collateIcEE
110  0x0015d180 0x0055d180 31  32   .rodata ascii   NSt7__cxx1114collate_bynameIcEE
111  0x0015d1a0 0x0055d1a0 24  25   .rodata ascii   NSt7__cxx118numpunctIcEE
112  0x0015d1c0 0x0055d1c0 32  33   .rodata ascii   NSt7__cxx1115numpunct_bynameIcEE
113  0x0015d200 0x0055d200 31  32   .rodata ascii   NSt7__cxx1110moneypunctIcLb1EEE
114  0x0015d220 0x0055d220 31  32   .rodata ascii   NSt7__cxx1110moneypunctIcLb0EEE
115  0x0015d240 0x0055d240 24  25   .rodata ascii   NSt7__cxx118messagesIcEE
116  0x0015d260 0x0055d260 38  39   .rodata ascii   NSt7__cxx1117moneypunct_bynameIcLb0EEE
117  0x0015d2a0 0x0055d2a0 38  39   .rodata ascii   NSt7__cxx1117moneypunct_bynameIcLb1EEE
118  0x0015d2e0 0x0055d2e0 69  70   .rodata ascii   NSt7__cxx119money_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEE
119  0x0015d340 0x0055d340 69  70   .rodata ascii   NSt7__cxx119money_putIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEEE
120  0x0015d3a0 0x0055d3a0 68  69   .rodata ascii   NSt7__cxx118time_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEE
121  0x0015d400 0x0055d400 76  77   .rodata ascii   NSt7__cxx1115time_get_bynameIcSt19istreambuf_iteratorIcSt11char_traitsIcEEEE
122  0x0015d460 0x0055d460 32  33   .rodata ascii   NSt7__cxx1115messages_bynameIcEE
123  0x0015d540 0x0055d540 52  53   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_113numpunct_shimIcEE
124  0x0015d580 0x0055d580 51  52   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_112collate_shimIcEE
125  0x0015d5c0 0x0055d5c0 58  59   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_115moneypunct_shimIcLb1EEE
126  0x0015d600 0x0055d600 58  59   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_115moneypunct_shimIcLb0EEE
127  0x0015d640 0x0055d640 53  54   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_114money_get_shimIcEE
128  0x0015d680 0x0055d680 53  54   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_114money_put_shimIcEE
129  0x0015d6c0 0x0055d6c0 52  53   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_113messages_shimIcEE
130  0x0015d700 0x0055d700 52  53   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_113numpunct_shimIwEE
131  0x0015d740 0x0055d740 51  52   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_112collate_shimIwEE
132  0x0015d780 0x0055d780 58  59   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_115moneypunct_shimIwLb1EEE
133  0x0015d7c0 0x0055d7c0 58  59   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_115moneypunct_shimIwLb0EEE
134  0x0015d800 0x0055d800 53  54   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_114money_get_shimIwEE
135  0x0015d840 0x0055d840 53  54   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_114money_put_shimIwEE
136  0x0015d880 0x0055d880 52  53   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_113messages_shimIwEE
137  0x0015d8c0 0x0055d8c0 52  53   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_113time_get_shimIcEE
138  0x0015d900 0x0055d900 52  53   .rodata ascii   *NSt13__facet_shims12_GLOBAL__N_113time_get_shimIwEE
139  0x0015da70 0x0055da70 23  24   .rodata ascii   NSt7__cxx117collateIwEE
140  0x0015daa0 0x0055daa0 31  32   .rodata ascii   NSt7__cxx1114collate_bynameIwEE
141  0x0015dac0 0x0055dac0 24  25   .rodata ascii   NSt7__cxx118numpunctIwEE
142  0x0015dae0 0x0055dae0 32  33   .rodata ascii   NSt7__cxx1115numpunct_bynameIwEE
143  0x0015db20 0x0055db20 31  32   .rodata ascii   NSt7__cxx1110moneypunctIwLb1EEE
144  0x0015db40 0x0055db40 31  32   .rodata ascii   NSt7__cxx1110moneypunctIwLb0EEE
145  0x0015db60 0x0055db60 24  25   .rodata ascii   NSt7__cxx118messagesIwEE
146  0x0015db80 0x0055db80 38  39   .rodata ascii   NSt7__cxx1117moneypunct_bynameIwLb0EEE
147  0x0015dbc0 0x0055dbc0 38  39   .rodata ascii   NSt7__cxx1117moneypunct_bynameIwLb1EEE
148  0x0015dc00 0x0055dc00 69  70   .rodata ascii   NSt7__cxx119money_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEE
149  0x0015dc60 0x0055dc60 69  70   .rodata ascii   NSt7__cxx119money_putIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEEE
150  0x0015dcc0 0x0055dcc0 68  69   .rodata ascii   NSt7__cxx118time_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEE
151  0x0015dd20 0x0055dd20 76  77   .rodata ascii   NSt7__cxx1115time_get_bynameIwSt19istreambuf_iteratorIwSt11char_traitsIwEEEE
152  0x0015dd80 0x0055dd80 32  33   .rodata ascii   NSt7__cxx1115messages_bynameIwEE
153  0x0015ddc0 0x0055ddc0 53  54   .rodata ascii   N9__gnu_cxx18stdio_sync_filebufIcSt11char_traitsIcEEE
154  0x0015de00 0x0055de00 53  54   .rodata ascii   N9__gnu_cxx18stdio_sync_filebufIwSt11char_traitsIwEEE
155  0x0015de40 0x0055de40 48  49   .rodata ascii   N9__gnu_cxx13stdio_filebufIcSt11char_traitsIcEEE
156  0x0015de80 0x0055de80 48  49   .rodata ascii   N9__gnu_cxx13stdio_filebufIwSt11char_traitsIwEEE
157  0x0015deb8 0x0055deb8 59  60   .rodata ascii   basic_filebuf::underflow codecvt::max_length() is not valid
158  0x0015def8 0x0055def8 54  55   .rodata ascii   basic_filebuf::underflow invalid byte sequence in file
159  0x0015df30 0x0055df30 53  54   .rodata ascii   basic_filebuf::underflow incomplete character in file
160  0x0015df68 0x0055df68 47  48   .rodata ascii   basic_filebuf::underflow error reading the file
161  0x0015df98 0x0055df98 44  45   .rodata ascii   basic_filebuf::xsgetn error reading the file
162  0x0015dfc8 0x0055dfc8 54  55   .rodata ascii   basic_filebuf::_M_convert_to_external conversion error
163  0x0015e000 0x0055e000 38  39   .rodata ascii   St13basic_filebufIcSt11char_traitsIcEE
164  0x0015e040 0x0055e040 39  40   .rodata ascii   St14basic_ifstreamIcSt11char_traitsIcEE
165  0x0015e080 0x0055e080 39  40   .rodata ascii   St14basic_ofstreamIcSt11char_traitsIcEE
166  0x0015e0c0 0x0055e0c0 38  39   .rodata ascii   St13basic_fstreamIcSt11char_traitsIcEE
167  0x0015e100 0x0055e100 38  39   .rodata ascii   St13basic_filebufIwSt11char_traitsIwEE
168  0x0015e140 0x0055e140 39  40   .rodata ascii   St14basic_ifstreamIwSt11char_traitsIwEE
169  0x0015e180 0x0055e180 39  40   .rodata ascii   St14basic_ofstreamIwSt11char_traitsIwEE
170  0x0015e1c0 0x0055e1c0 38  39   .rodata ascii   St13basic_fstreamIwSt11char_traitsIwEE
171  0x0015e1e7 0x0055e1e7 16  17   .rodata ascii   basic_ios::clear
172  0x0015e200 0x0055e200 33  34   .rodata ascii   St9basic_iosIcSt11char_traitsIcEE
173  0x0015e240 0x0055e240 33  34   .rodata ascii   St9basic_iosIwSt11char_traitsIwEE
174  0x0015e268 0x0055e268 41  42   .rodata ascii   ios_base::_M_grow_words allocation failed
175  0x0015e298 0x0055e298 36  37   .rodata ascii   ios_base::_M_grow_words is not valid
176  0x0015e2c0 0x0055e2c0 11  12   .rodata ascii   St8ios_base
177  0x0015e360 0x0055e360 39  40   .rodata ascii   St14basic_iostreamIwSt11char_traitsIwEE
178  0x0015e3a0 0x0055e3a0 38  39   .rodata ascii   St13basic_istreamIwSt11char_traitsIwEE
179  0x0015e500 0x0055e500 13  14   .rodata ascii   St7collateIcE
180  0x0015e510 0x0055e510 21  22   .rodata ascii   St14collate_bynameIcE
181  0x0015e528 0x0055e528 14  15   .rodata ascii   St8numpunctIcE
182  0x0015e540 0x0055e540 22  23   .rodata ascii   St15numpunct_bynameIcE
183  0x0015e560 0x0055e560 57  58   .rodata ascii   St7num_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEE
184  0x0015e5a0 0x0055e5a0 57  58   .rodata ascii   St7num_putIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEE
185  0x0015e5e0 0x0055e5e0 24  25   .rodata ascii   St17__timepunct_cacheIcE
186  0x0015e600 0x0055e600 18  19   .rodata ascii   St11__timepunctIcE
187  0x0015e620 0x0055e620 21  22   .rodata ascii   St10moneypunctIcLb1EE
188  0x0015e640 0x0055e640 21  22   .rodata ascii   St10moneypunctIcLb0EE
189  0x0015e658 0x0055e658 14  15   .rodata ascii   St8messagesIcE
190  0x0015e680 0x0055e680 44  45   .rodata ascii   St23__codecvt_abstract_baseIcc11__mbstate_tE
191  0x0015e6c0 0x0055e6c0 35  36   .rodata ascii   St14codecvt_bynameIcc11__mbstate_tE
192  0x0015e6f0 0x0055e6f0 28  29   .rodata ascii   St17moneypunct_bynameIcLb0EE
193  0x0015e710 0x0055e710 28  29   .rodata ascii   St17moneypunct_bynameIcLb1EE
194  0x0015e740 0x0055e740 59  60   .rodata ascii   St9money_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEE
195  0x0015e780 0x0055e780 59  60   .rodata ascii   St9money_putIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEE
196  0x0015e7c0 0x0055e7c0 58  59   .rodata ascii   St8time_putIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEE
197  0x0015e800 0x0055e800 66  67   .rodata ascii   St15time_put_bynameIcSt19ostreambuf_iteratorIcSt11char_traitsIcEEE
198  0x0015e860 0x0055e860 58  59   .rodata ascii   St8time_getIcSt19istreambuf_iteratorIcSt11char_traitsIcEEE
199  0x0015e8a0 0x0055e8a0 66  67   .rodata ascii   St15time_get_bynameIcSt19istreambuf_iteratorIcSt11char_traitsIcEEE
200  0x0015e8f0 0x0055e8f0 22  23   .rodata ascii   St15messages_bynameIcE
201  0x0015e910 0x0055e910 28  29   .rodata ascii   St21__ctype_abstract_baseIcE
202  0x0015e940 0x0055e940 38  39   .rodata ascii   St13basic_ostreamIwSt11char_traitsIwEE
203  0x0015e967 0x0055e967 28  29   .rodata ascii   random_device: rdrand failed
204  0x0015e984 0x0055e984 28  29   .rodata ascii   random_device: rdseed failed
205  0x0015e9a1 0x0055e9a1 12  13   .rodata ascii   /dev/urandom
206  0x0015e9ae 0x0055e9ae 7   8    .rodata ascii   default
207  0x0015e9b6 0x0055e9b6 6   7    .rodata ascii   rdseed
208  0x0015e9bd 0x0055e9bd 6   7    .rodata ascii   rdrand
209  0x0015e9c4 0x0055e9c4 5   6    .rodata ascii   rdrnd
210  0x0015e9ca 0x0055e9ca 11  12   .rodata ascii   /dev/random
211  0x0015e9d8 0x0055e9d8 67  68   .rodata ascii   random_device::random_device(const std::string&): unsupported token
212  0x0015ea20 0x0055ea20 70  71   .rodata ascii   random_device::random_device(const std::string&): device not available
213  0x0015ea67 0x0055ea67 7   8    .rodata ascii   mt19937
214  0x0015ea70 0x0055ea70 31  32   .rodata ascii   random_device could not be read
215  0x0015eaa0 0x0055eaa0 136 137  .rodata ascii   not enough space for format expansion (Please submit full bug report at https://gcc.gnu.org/bugsSt15basic_streambufIcSt11char_traitsIcEE
216  0x0015eb40 0x0055eb40 40  41   .rodata ascii   St15basic_streambufIwSt11char_traitsIwEE
217  0x0015eb69 0x0055eb69 23  24   .rodata ascii   basic_string::_M_create
218  0x0015eb81 0x0055eb81 24  25   .rodata ascii   basic_string::_M_replace
219  0x0015eb9a 0x0055eb9a 14  15   .rodata ascii   string::string
220  0x0015ecf0 0x0055ecf0 13  14   .rodata ascii   St7collateIwE
221  0x0015ed00 0x0055ed00 21  22   .rodata ascii   St14collate_bynameIwE
222  0x0015ed20 0x0055ed20 28  29   .rodata ascii   St21__ctype_abstract_baseIwE
223  0x0015ed40 0x0055ed40 14  15   .rodata ascii   St8numpunctIwE
224  0x0015ed50 0x0055ed50 22  23   .rodata ascii   St15numpunct_bynameIwE
225  0x0015ed80 0x0055ed80 57  58   .rodata ascii   St7num_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEE
226  0x0015edc0 0x0055edc0 57  58   .rodata ascii   St7num_putIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEE
227  0x0015ee00 0x0055ee00 24  25   .rodata ascii   St17__timepunct_cacheIwE
228  0x0015ee20 0x0055ee20 18  19   .rodata ascii   St11__timepunctIwE
229  0x0015ee40 0x0055ee40 21  22   .rodata ascii   St10moneypunctIwLb1EE
230  0x0015ee60 0x0055ee60 21  22   .rodata ascii   St10moneypunctIwLb0EE
231  0x0015ee78 0x0055ee78 14  15   .rodata ascii   St8messagesIwE
232  0x0015eea0 0x0055eea0 44  45   .rodata ascii   St23__codecvt_abstract_baseIwc11__mbstate_tE
233  0x0015eee0 0x0055eee0 35  36   .rodata ascii   St14codecvt_bynameIwc11__mbstate_tE
234  0x0015ef10 0x0055ef10 28  29   .rodata ascii   St17moneypunct_bynameIwLb0EE
235  0x0015ef30 0x0055ef30 28  29   .rodata ascii   St17moneypunct_bynameIwLb1EE
236  0x0015ef60 0x0055ef60 59  60   .rodata ascii   St9money_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEE
237  0x0015efa0 0x0055efa0 59  60   .rodata ascii   St9money_putIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEE
238  0x0015efe0 0x0055efe0 58  59   .rodata ascii   St8time_putIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEE
239  0x0015f020 0x0055f020 66  67   .rodata ascii   St15time_put_bynameIwSt19ostreambuf_iteratorIwSt11char_traitsIwEEE
240  0x0015f080 0x0055f080 58  59   .rodata ascii   St8time_getIwSt19istreambuf_iteratorIwSt11char_traitsIwEEE
241  0x0015f0c0 0x0055f0c0 66  67   .rodata ascii   St15time_get_bynameIwSt19istreambuf_iteratorIwSt11char_traitsIwEEE
242  0x0015f110 0x0055f110 22  23   .rodata ascii   St15messages_bynameIwE
243  0x0015f138 0x0055f138 14  15   .rodata ascii   std::bad_alloc
244  0x0015f148 0x0055f148 12  13   .rodata ascii   St9bad_alloc
245  0x0015f155 0x0055f155 25  26   .rodata ascii   std::bad_array_new_length
246  0x0015f170 0x0055f170 24  25   .rodata ascii   St20bad_array_new_length
247  0x0015f189 0x0055f189 13  14   .rodata ascii   std::bad_cast
248  0x0015f198 0x0055f198 11  12   .rodata ascii   St8bad_cast
249  0x0015f1a4 0x0055f1a4 15  16   .rodata ascii   std::bad_typeid
250  0x0015f1b8 0x0055f1b8 14  15   .rodata ascii   St10bad_typeid
251  0x0015f1e0 0x0055f1e0 33  34   .rodata ascii   N10__cxxabiv117__class_type_infoE
252  0x0015f9a4 0x0055f9a4 21  22   .rodata ascii   (anonymous namespace)
253  0x0015f9ba 0x0055f9ba 4   5    .rodata ascii   auto
254  0x0015f9bf 0x0055f9bf 14  15   .rodata ascii   decltype(auto)
255  0x0015f9ce 0x0055f9ce 17  18   .rodata ascii   decltype(nullptr)
256  0x0015f9e0 0x0055f9e0 14  15   .rodata ascii   string literal
257  0x0015f9f3 0x0055f9f3 5   6    .rodata ascii   [abi:
258  0x0015f9f9 0x0055f9f9 13  14   .rodata ascii   {default arg#
259  0x0015fa0b 0x0055fa0b 5   6    .rodata ascii   auto:
260  0x0015fa11 0x0055fa11 8   9    .rodata ascii   VTT for 
261  0x0015fa1a 0x0055fa1a 24  25   .rodata ascii   construction vtable for 
262  0x0015fa33 0x0055fa33 4   5    .rodata ascii   -in-
263  0x0015fa38 0x0055fa38 13  14   .rodata ascii   typeinfo for 
264  0x0015fa46 0x0055fa46 18  19   .rodata ascii   typeinfo name for 
265  0x0015fa59 0x0055fa59 16  17   .rodata ascii   typeinfo fn for 
266  0x0015fa6a 0x0055fa6a 21  22   .rodata ascii   non-virtual thunk to 
267  0x0015fa80 0x0055fa80 26  27   .rodata ascii   covariant return thunk to 
268  0x0015fa9b 0x0055fa9b 15  16   .rodata ascii   java Class for 
269  0x0015faab 0x0055faab 19  20   .rodata ascii   guard variable for 
270  0x0015fabf 0x0055fabf 22  23   .rodata ascii   TLS init function for 
271  0x0015fad6 0x0055fad6 25  26   .rodata ascii   TLS wrapper function for 
272  0x0015faf0 0x0055faf0 21  22   .rodata ascii   reference temporary #
273  0x0015fb06 0x0055fb06 17  18   .rodata ascii   hidden alias for 
274  0x0015fb18 0x0055fb18 26  27   .rodata ascii   non-transaction clone for 
275  0x0015fb33 0x0055fb33 5   6    .rodata ascii   _Sat 
276  0x0015fb39 0x0055fb39 6   7    .rodata ascii   _Accum
277  0x0015fb40 0x0055fb40 6   7    .rodata ascii   _Fract
278  0x0015fb4a 0x0055fb4a 8   9    .rodata ascii   operator
279  0x0015fb53 0x0055fb53 9   10   .rodata ascii   operator 
280  0x0015fb6d 0x0055fb6d 4   5    .rodata ascii   new 
281  0x0015fb72 0x0055fb72 14  15   .rodata ascii   java resource 
282  0x0015fb81 0x0055fb81 10  11   .rodata ascii   decltype (
283  0x0015fb8c 0x0055fb8c 4   5    .rodata ascii   this
284  0x0015fb91 0x0055fb91 6   7    .rodata ascii   {parm#
285  0x0015fb98 0x0055fb98 29  30   .rodata ascii   global constructors keyed to 
286  0x0015fbb6 0x0055fbb6 28  29   .rodata ascii   global destructors keyed to 
287  0x0015fbd3 0x0055fbd3 8   9    .rodata ascii   {lambda(
288  0x0015fbdf 0x0055fbdf 14  15   .rodata ascii   {unnamed type#
289  0x0015fbee 0x0055fbee 8   9    .rodata ascii    [clone 
290  0x0015fbf7 0x0055fbf7 9   10   .rodata ascii    restrict
291  0x0015fc01 0x0055fc01 9   10   .rodata ascii    volatile
292  0x0015fc0b 0x0055fc0b 6   7    .rodata ascii    const
293  0x0015fc12 0x0055fc12 17  18   .rodata ascii    transaction_safe
294  0x0015fc24 0x0055fc24 9   10   .rodata ascii    noexcept
295  0x0015fc2e 0x0055fc2e 6   7    .rodata ascii    throw
296  0x0015fc38 0x0055fc38 9   10   .rodata ascii    _Complex
297  0x0015fc42 0x0055fc42 11  12   .rodata ascii    _Imaginary
298  0x0015fc52 0x0055fc52 10  11   .rodata ascii    __vector(
299  0x0015fc5d 0x0055fc5d 8   9    .rodata ascii   _GLOBAL_
300  0x0015fc66 0x0055fc66 4   5    .rodata ascii   (...
301  0x0015fc6b 0x0055fc6b 4   5    .rodata ascii   ...)
302  0x0015fc70 0x0055fc70 5   6    .rodata ascii    ... 
303  0x0015fc76 0x0055fc76 14  15   .rodata ascii   std::allocator
304  0x0015fc85 0x0055fc85 17  18   .rodata ascii   std::basic_string
305  0x0015fc97 0x0055fc97 11  12   .rodata ascii   std::string
306  0x0015fca3 0x0055fca3 12  13   .rodata ascii   std::istream
307  0x0015fcb0 0x0055fcb0 13  14   .rodata ascii   basic_istream
308  0x0015fcbe 0x0055fcbe 12  13   .rodata ascii   std::ostream
309  0x0015fccb 0x0055fccb 13  14   .rodata ascii   basic_ostream
310  0x0015fcd9 0x0055fcd9 13  14   .rodata ascii   std::iostream
311  0x0015fce7 0x0055fce7 14  15   .rodata ascii   basic_iostream
312  0x0015fd02 0x0055fd02 8   9    .rodata ascii   alignof 
313  0x0015fd0e 0x0055fd0e 9   10   .rodata ascii   co_await 
314  0x0015fd1e 0x0055fd1e 10  11   .rodata ascii   const_cast
315  0x0015fd3c 0x0055fd3c 6   7    .rodata ascii   [...]=
316  0x0015fd46 0x0055fd46 9   10   .rodata ascii   delete[] 
317  0x0015fd53 0x0055fd53 12  13   .rodata ascii   dynamic_cast
318  0x0015fd66 0x0055fd66 7   8    .rodata ascii   delete 
319  0x0015fda7 0x0055fda7 11  12   .rodata ascii   operator"" 
320  0x0015fdd4 0x0055fdd4 5   6    .rodata ascii   new[]
321  0x0015fe1b 0x0055fe1b 16  17   .rodata ascii   reinterpret_cast
322  0x0015fe37 0x0055fe37 9   10   .rodata ascii   sizeof...
323  0x0015fe47 0x0055fe47 11  12   .rodata ascii   static_cast
324  0x0015fe57 0x0055fe57 7   8    .rodata ascii   sizeof 
325  0x0015fe65 0x0055fe65 6   7    .rodata ascii   throw 
326  0x0015fe6c 0x0055fe6c 4   5    .rodata ascii   bool
327  0x0015fe71 0x0055fe71 7   8    .rodata ascii   boolean
328  0x0015fe79 0x0055fe79 4   5    .rodata ascii   byte
329  0x0015fe7e 0x0055fe7e 11  12   .rodata ascii   long double
330  0x0015fe8a 0x0055fe8a 5   6    .rodata ascii   float
331  0x0015fe90 0x0055fe90 10  11   .rodata ascii   __float128
332  0x0015fe9b 0x0055fe9b 13  14   .rodata ascii   unsigned char
333  0x0015fea9 0x0055fea9 12  13   .rodata ascii   unsigned int
334  0x0015feb6 0x0055feb6 8   9    .rodata ascii   unsigned
335  0x0015febf 0x0055febf 13  14   .rodata ascii   unsigned long
336  0x0015fecd 0x0055fecd 17  18   .rodata ascii   unsigned __int128
337  0x0015fedf 0x0055fedf 14  15   .rodata ascii   unsigned short
338  0x0015feee 0x0055feee 4   5    .rodata ascii   void
339  0x0015fef3 0x0055fef3 7   8    .rodata ascii   wchar_t
340  0x0015fefb 0x0055fefb 18  19   .rodata ascii   unsigned long long
341  0x0015ff0e 0x0055ff0e 9   10   .rodata ascii   decimal32
342  0x0015ff18 0x0055ff18 9   10   .rodata ascii   decimal64
343  0x0015ff22 0x0055ff22 10  11   .rodata ascii   decimal128
344  0x0015ff2d 0x0055ff2d 4   5    .rodata ascii   half
345  0x0015ff32 0x0055ff32 7   8    .rodata ascii   char8_t
346  0x0015ff3a 0x0055ff3a 8   9    .rodata ascii   char16_t
347  0x0015ff43 0x0055ff43 8   9    .rodata ascii   char32_t
348  0x0015ff50 0x0055ff50 30  31   .rodata ascii   template parameter object for 
349  0x0015ff70 0x0055ff70 70  71   .rodata ascii   std::basic_string<char, std::char_traits<char>, std::allocator<char> >
350  0x0015ffb8 0x0055ffb8 49  50   .rodata ascii   std::basic_istream<char, std::char_traits<char> >
351  0x0015fff0 0x0055fff0 49  50   .rodata ascii   std::basic_ostream<char, std::char_traits<char> >
352  0x00160028 0x00560028 50  51   .rodata ascii   std::basic_iostream<char, std::char_traits<char> >
353  0x0016005b 0x0056005b 14  15   .rodata ascii   std::exception
354  0x0016006a 0x0056006a 18  19   .rodata ascii   std::bad_exception
355  0x00160080 0x00560080 12  13   .rodata ascii   St9exception
356  0x00160090 0x00560090 17  18   .rodata ascii   St13bad_exception
357  0x001600c0 0x005600c0 31  32   .rodata ascii   N10__cxxabiv115__forced_unwindE
358  0x001600e0 0x005600e0 35  36   .rodata ascii   N10__cxxabiv119__foreign_exceptionE
359  0x00160120 0x00560120 34  35   .rodata ascii   N9__gnu_cxx20recursive_init_errorE
360  0x00160160 0x00560160 36  37   .rodata ascii   N10__cxxabiv120__si_class_type_infoE
361  0x00160188 0x00560188 12  13   .rodata ascii   St9type_info
362  0x001601a0 0x005601a0 37  38   .rodata ascii   N10__cxxabiv121__vmi_class_type_infoE
363  0x001602d8 0x005602d8 48  49   .rodata ascii   locale::facet::_S_create_c_locale name not valid
364  0x00160310 0x00560310 51  52   .rodata ascii   locale::facet::_S_lc_ctype_c_locale duplocale error
365  0x00160348 0x00560348 51  52   .rodata ascii   locale::facet::_S_lc_ctype_c_locale newlocale error
366  0x0016037c 0x0056037c 25  26   .rodata ascii   vector::_M_realloc_insert
367  0x00160396 0x00560396 10  11   .rodata ascii   LC_NUMERIC
368  0x001603a1 0x005603a1 7   8    .rodata ascii   LC_TIME
369  0x001603a9 0x005603a9 10  11   .rodata ascii   LC_COLLATE
370  0x001603b4 0x005603b4 11  12   .rodata ascii   LC_MONETARY
371  0x001603c0 0x005603c0 11  12   .rodata ascii   LC_MESSAGES
372  0x001603cc 0x005603cc 8   9    .rodata ascii   LC_PAPER
373  0x001603d5 0x005603d5 7   8    .rodata ascii   LC_NAME
374  0x001603dd 0x005603dd 10  11   .rodata ascii   LC_ADDRESS
375  0x001603e8 0x005603e8 12  13   .rodata ascii   LC_TELEPHONE
376  0x001603f5 0x005603f5 14  15   .rodata ascii   LC_MEASUREMENT
377  0x00160404 0x00560404 17  18   .rodata ascii   LC_IDENTIFICATION
378  0x00160460 0x00560460 27  28   .rodata ascii   St7codecvtIcc11__mbstate_tE
379  0x00160480 0x00560480 27  28   .rodata ascii   St7codecvtIwc11__mbstate_tE
380  0x001604a0 0x005604a0 36  37   .rodata ascii   -+xX0123456789abcdef0123456789ABCDEF
381  0x001604c5 0x005604c5 26  27   .rodata ascii   -+xX0123456789abcdefABCDEF
382  0x001604e0 0x005604e0 11  12   .rodata ascii   -0123456789
383  0x001604f4 0x005604f4 4   5    .rodata ascii   AKST
384  0x00160548 0x00560548 4   20   .rodata utf32le AKST
385  0x00160600 0x00560600 15  16   .rodata ascii   St11logic_error
386  0x00160610 0x00560610 16  17   .rodata ascii   St12domain_error
387  0x00160630 0x00560630 20  21   .rodata ascii   St16invalid_argument
388  0x00160650 0x00560650 16  17   .rodata ascii   St12length_error
389  0x00160670 0x00560670 16  17   .rodata ascii   St12out_of_range
390  0x00160690 0x00560690 17  18   .rodata ascii   St13runtime_error
391  0x001606b0 0x005606b0 15  16   .rodata ascii   St11range_error
392  0x001606c0 0x005606c0 18  19   .rodata ascii   St14overflow_error
393  0x001606e0 0x005606e0 19  20   .rodata ascii   St15underflow_error
394  0x001606fa 0x005606fa 6   7    .rodata ascii   Sunday
395  0x00160701 0x00560701 6   7    .rodata ascii   Monday
396  0x00160708 0x00560708 7   8    .rodata ascii   Tuesday
397  0x00160710 0x00560710 9   10   .rodata ascii   Wednesday
398  0x0016071a 0x0056071a 8   9    .rodata ascii   Thursday
399  0x00160723 0x00560723 6   7    .rodata ascii   Friday
400  0x0016072a 0x0056072a 8   9    .rodata ascii   Saturday
401  0x0016074f 0x0056074f 7   8    .rodata ascii   January
402  0x00160757 0x00560757 8   9    .rodata ascii   February
403  0x00160760 0x00560760 5   6    .rodata ascii   March
404  0x00160766 0x00560766 5   6    .rodata ascii   April
405  0x00160770 0x00560770 4   5    .rodata ascii   June
406  0x00160775 0x00560775 4   5    .rodata ascii   July
407  0x0016077a 0x0056077a 6   7    .rodata ascii   August
408  0x00160781 0x00560781 9   10   .rodata ascii   September
409  0x0016078b 0x0056078b 7   8    .rodata ascii   October
410  0x00160793 0x00560793 8   9    .rodata ascii   November
411  0x0016079c 0x0056079c 8   9    .rodata ascii   December
412  0x001607d8 0x005607d8 8   36   .rodata utf32le %m/%d/%y
413  0x00160800 0x00560800 8   36   .rodata utf32le %H:%M:%S
414  0x00160828 0x00560828 7   32   .rodata utf32le Tuesday
415  0x00160848 0x00560848 9   40   .rodata utf32le Wednesday
416  0x00160870 0x00560870 8   36   .rodata utf32le Thursday
417  0x00160898 0x00560898 8   36   .rodata utf32le Saturday
418  0x001608c0 0x005608c0 7   32   .rodata utf32le January
419  0x001608e0 0x005608e0 8   36   .rodata utf32le February
420  0x00160908 0x00560908 9   40   .rodata utf32le September
421  0x00160930 0x00560930 7   32   .rodata utf32le October
422  0x00160950 0x00560950 8   36   .rodata utf32le November
423  0x00160978 0x00560978 8   36   .rodata utf32le December
424  0x001609b4 0x005609b4 6   28   .rodata utf32le Sunday
425  0x001609d0 0x005609d0 6   28   .rodata utf32le Monday
426  0x001609ec 0x005609ec 6   28   .rodata utf32le Friday
427  0x00160a78 0x00560a78 5   24   .rodata utf32le March
428  0x00160a90 0x00560a90 5   24   .rodata utf32le April
429  0x00160ab8 0x00560ab8 4   20   .rodata utf32le June
430  0x00160acc 0x00560acc 4   20   .rodata utf32le July
431  0x00160ae0 0x00560ae0 6   28   .rodata utf32le August
432  0x00160bac 0x00560bac 14  15   .rodata ascii   iostream error
433  0x00160bbb 0x00560bbb 13  14   .rodata ascii   Unknown error
434  0x00160bd0 0x00560bd0 28  29   .rodata ascii   NSt8ios_base7failureB5cxx11E
435  0x00160c00 0x00560c00 36  37   .rodata ascii   *N12_GLOBAL__N_117io_error_categoryE
436  0x00160c30 0x00560c30 17  18   .rodata ascii   St13__ios_failure
437  0x00160c50 0x00560c50 23  24   .rodata ascii   St19__iosfail_type_info
438  0x00160c68 0x00560c68 7   8    .rodata ascii   generic
439  0x00160c70 0x00560c70 24  25   .rodata ascii   NSt3_V214error_categoryE
440  0x00160c90 0x00560c90 16  17   .rodata ascii   St12system_error
441  0x00160cc0 0x00560cc0 41  42   .rodata ascii   *N12_GLOBAL__N_122generic_error_categoryE
442  0x00160d00 0x00560d00 40  41   .rodata ascii   *N12_GLOBAL__N_121system_error_categoryE
443  0x00160d30 0x00560d30 21  22   .rodata ascii   NSt8ios_base7failureE
444  0x001614c8 0x005614c8 4   5    .rodata ascii   #\b@\t
445  0x001614d0 0x005614d0 4   5    .rodata ascii   %\b@\t
446  0x001614d8 0x005614d8 4   5    .rodata ascii   )\b@\t
447  0x00161558 0x00561558 4   5    .rodata ascii   G\b@\t
448  0x00161570 0x00561570 4   5    .rodata ascii   J\f@\t
449  0x00161580 0x00561580 4   5    .rodata ascii   L\f@\t
450  0x001616a0 0x005616a0 29  30   .rodata ascii   ../sysdeps/x86/dl-cacheinfo.h
451  0x001616be 0x005616be 11  12   .rodata ascii   offset == 2
452  0x001616ca 0x005616ca 8   9    .rodata ascii   xeon_phi
453  0x001616d3 0x005616d3 7   8    .rodata ascii   haswell
454  0x001616db 0x005616db 19  20   .rodata ascii   ../csu/libc-start.c
455  0x001616ef 0x005616ef 22  23   .rodata ascii   FATAL: kernel too old\n
456  0x00161708 0x00561708 47  48   .rodata ascii   __ehdr_start.e_phentsize == sizeof *GL(dl_phdr)
457  0x00161738 0x00561738 40  41   .rodata ascii   Unexpected reloc type in static binary.\n
458  0x00161768 0x00561768 39  40   .rodata ascii   FATAL: cannot determine kernel version\n
459  0x00161790 0x00561790 16  17   .rodata ascii   intel_check_word
460  0x001617b0 0x005617b0 17  18   .rodata ascii   __libc_start_main
461  0x001617c2 0x005617c2 9   10   .rodata ascii   /dev/full
462  0x001617cc 0x005617cc 9   10   .rodata ascii   /dev/null
463  0x001617d8 0x005617d8 52  53   .rodata ascii   cannot set %fs base address for thread-local storage
464  0x0016180d 0x0056180d 7   8    .rodata ascii   iconv.c
465  0x00161815 0x00561815 5   6    .rodata ascii   iconv
466  0x00161820 0x00561820 34  35   .rodata ascii   !"Nothing like this should happen"
467  0x00161868 0x00561868 7   8    .rodata ascii   gconv.c
468  0x00161870 0x00561870 20  21   .rodata ascii   irreversible != NULL
469  0x00161888 0x00561888 33  34   .rodata ascii   outbuf != NULL && *outbuf != NULL
470  0x001618b0 0x005618b0 7   8    .rodata ascii   __gconv
471  0x001618b8 0x005618b8 10  11   .rodata ascii   gconv_db.c
472  0x001618c3 0x005618c3 23  24   .rodata ascii   step->__end_fct == NULL
473  0x001618e0 0x005618e0 20  21   .rodata ascii   __gconv_release_step
474  0x001618f5 0x005618f5 12  13   .rodata ascii   gconv_conf.c
475  0x00161902 0x00561902 14  15   .rodata ascii   result == NULL
476  0x00161911 0x00561911 12  13   .rodata ascii   elem != NULL
477  0x0016191e 0x0056191e 11  12   .rodata ascii   cwd != NULL
478  0x0016192e 0x0056192e 5   6    .rodata ascii   alias
479  0x00161934 0x00561934 6   7    .rodata ascii   module
480  0x0016193b 0x0056193b 15  16   .rodata ascii   ISO-10646/UCS4/
481  0x0016194b 0x0056194b 15  16   .rodata ascii   =INTERNAL->ucs4
482  0x0016195b 0x0056195b 15  16   .rodata ascii   =ucs4->INTERNAL
483  0x0016196b 0x0056196b 9   10   .rodata ascii   UCS-4LE//
484  0x00161975 0x00561975 17  18   .rodata ascii   =INTERNAL->ucs4le
485  0x00161987 0x00561987 17  18   .rodata ascii   =ucs4le->INTERNAL
486  0x00161999 0x00561999 15  16   .rodata ascii   ISO-10646/UTF8/
487  0x001619a9 0x005619a9 15  16   .rodata ascii   =INTERNAL->utf8
488  0x001619b9 0x005619b9 15  16   .rodata ascii   =utf8->INTERNAL
489  0x001619c9 0x005619c9 15  16   .rodata ascii   ISO-10646/UCS2/
490  0x001619d9 0x005619d9 15  16   .rodata ascii   =ucs2->INTERNAL
491  0x001619e9 0x005619e9 15  16   .rodata ascii   =INTERNAL->ucs2
492  0x001619f9 0x005619f9 16  17   .rodata ascii   ANSI_X3.4-1968//
493  0x00161a0a 0x00561a0a 16  17   .rodata ascii   =ascii->INTERNAL
494  0x00161a1b 0x00561a1b 16  17   .rodata ascii   =INTERNAL->ascii
495  0x00161a2c 0x00561a2c 12  13   .rodata ascii   UNICODEBIG//
496  0x00161a39 0x00561a39 22  23   .rodata ascii   =ucs2reverse->INTERNAL
497  0x00161a50 0x00561a50 22  23   .rodata ascii   =INTERNAL->ucs2reverse
498  0x00161a70 0x00561a70 16  17   .rodata ascii   __gconv_get_path
499  0x00161aa0 0x00561aa0 6   7    .rodata ascii   UCS4//
500  0x00161aa7 0x00561aa7 15  16   .rodata ascii   ISO-10646/UCS4/
501  0x00161ab7 0x00561ab7 7   8    .rodata ascii   UCS-4//
502  0x00161abf 0x00561abf 15  16   .rodata ascii   ISO-10646/UCS4/
503  0x00161acf 0x00561acf 9   10   .rodata ascii   UCS-4BE//
504  0x00161ad9 0x00561ad9 15  16   .rodata ascii   ISO-10646/UCS4/
505  0x00161ae9 0x00561ae9 8   9    .rodata ascii   CSUCS4//
506  0x00161af2 0x00561af2 15  16   .rodata ascii   ISO-10646/UCS4/
507  0x00161b02 0x00561b02 11  12   .rodata ascii   ISO-10646//
508  0x00161b0e 0x00561b0e 15  16   .rodata ascii   ISO-10646/UCS4/
509  0x00161b1e 0x00561b1e 14  15   .rodata ascii   10646-1:1993//
510  0x00161b2d 0x00561b2d 15  16   .rodata ascii   ISO-10646/UCS4/
511  0x00161b3d 0x00561b3d 18  19   .rodata ascii   10646-1:1993/UCS4/
512  0x00161b50 0x00561b50 15  16   .rodata ascii   ISO-10646/UCS4/
513  0x00161b60 0x00561b60 13  14   .rodata ascii   OSF00010104//
514  0x00161b6e 0x00561b6e 15  16   .rodata ascii   ISO-10646/UCS4/
515  0x00161b7e 0x00561b7e 13  14   .rodata ascii   OSF00010105//
516  0x00161b8c 0x00561b8c 15  16   .rodata ascii   ISO-10646/UCS4/
517  0x00161b9c 0x00561b9c 13  14   .rodata ascii   OSF00010106//
518  0x00161baa 0x00561baa 15  16   .rodata ascii   ISO-10646/UCS4/
519  0x00161bba 0x00561bba 9   10   .rodata ascii   WCHAR_T//
520  0x00161bc4 0x00561bc4 8   9    .rodata ascii   INTERNAL
521  0x00161bcd 0x00561bcd 6   7    .rodata ascii   UTF8//
522  0x00161bd4 0x00561bd4 15  16   .rodata ascii   ISO-10646/UTF8/
523  0x00161be4 0x00561be4 7   8    .rodata ascii   UTF-8//
524  0x00161bec 0x00561bec 15  16   .rodata ascii   ISO-10646/UTF8/
525  0x00161bfc 0x00561bfc 12  13   .rodata ascii   ISO-IR-193//
526  0x00161c09 0x00561c09 15  16   .rodata ascii   ISO-10646/UTF8/
527  0x00161c19 0x00561c19 13  14   .rodata ascii   OSF05010001//
528  0x00161c27 0x00561c27 15  16   .rodata ascii   ISO-10646/UTF8/
529  0x00161c37 0x00561c37 16  17   .rodata ascii   ISO-10646/UTF-8/
530  0x00161c48 0x00561c48 15  16   .rodata ascii   ISO-10646/UTF8/
531  0x00161c58 0x00561c58 6   7    .rodata ascii   UCS2//
532  0x00161c5f 0x00561c5f 15  16   .rodata ascii   ISO-10646/UCS2/
533  0x00161c6f 0x00561c6f 7   8    .rodata ascii   UCS-2//
534  0x00161c77 0x00561c77 15  16   .rodata ascii   ISO-10646/UCS2/
535  0x00161c87 0x00561c87 13  14   .rodata ascii   OSF00010100//
536  0x00161c95 0x00561c95 15  16   .rodata ascii   ISO-10646/UCS2/
537  0x00161ca5 0x00561ca5 13  14   .rodata ascii   OSF00010101//
538  0x00161cb3 0x00561cb3 15  16   .rodata ascii   ISO-10646/UCS2/
539  0x00161cc3 0x00561cc3 13  14   .rodata ascii   OSF00010102//
540  0x00161cd1 0x00561cd1 15  16   .rodata ascii   ISO-10646/UCS2/
541  0x00161ce1 0x00561ce1 11  12   .rodata ascii   ANSI_X3.4//
542  0x00161ced 0x00561ced 16  17   .rodata ascii   ANSI_X3.4-1968//
543  0x00161cfe 0x00561cfe 10  11   .rodata ascii   ISO-IR-6//
544  0x00161d09 0x00561d09 16  17   .rodata ascii   ANSI_X3.4-1968//
545  0x00161d1a 0x00561d1a 16  17   .rodata ascii   ANSI_X3.4-1986//
546  0x00161d2b 0x00561d2b 16  17   .rodata ascii   ANSI_X3.4-1968//
547  0x00161d3c 0x00561d3c 18  19   .rodata ascii   ISO_646.IRV:1991//
548  0x00161d4f 0x00561d4f 16  17   .rodata ascii   ANSI_X3.4-1968//
549  0x00161d60 0x00561d60 7   8    .rodata ascii   ASCII//
550  0x00161d68 0x00561d68 16  17   .rodata ascii   ANSI_X3.4-1968//
551  0x00161d79 0x00561d79 11  12   .rodata ascii   ISO646-US//
552  0x00161d85 0x00561d85 16  17   .rodata ascii   ANSI_X3.4-1968//
553  0x00161d96 0x00561d96 10  11   .rodata ascii   US-ASCII//
554  0x00161da1 0x00561da1 16  17   .rodata ascii   ANSI_X3.4-1968//
555  0x00161db2 0x00561db2 4   5    .rodata ascii   US//
556  0x00161db7 0x00561db7 16  17   .rodata ascii   ANSI_X3.4-1968//
557  0x00161dc8 0x00561dc8 8   9    .rodata ascii   IBM367//
558  0x00161dd1 0x00561dd1 16  17   .rodata ascii   ANSI_X3.4-1968//
559  0x00161de2 0x00561de2 7   8    .rodata ascii   CP367//
560  0x00161dea 0x00561dea 16  17   .rodata ascii   ANSI_X3.4-1968//
561  0x00161dfb 0x00561dfb 9   10   .rodata ascii   CSASCII//
562  0x00161e05 0x00561e05 16  17   .rodata ascii   ANSI_X3.4-1968//
563  0x00161e16 0x00561e16 13  14   .rodata ascii   OSF00010020//
564  0x00161e24 0x00561e24 16  17   .rodata ascii   ANSI_X3.4-1968//
565  0x00161e35 0x00561e35 15  16   .rodata ascii   UNICODELITTLE//
566  0x00161e45 0x00561e45 15  16   .rodata ascii   ISO-10646/UCS2/
567  0x00161e55 0x00561e55 9   10   .rodata ascii   UCS-2LE//
568  0x00161e5f 0x00561e5f 15  16   .rodata ascii   ISO-10646/UCS2/
569  0x00161e6f 0x00561e6f 9   10   .rodata ascii   UCS-2BE//
570  0x00161e79 0x00561e79 12  13   .rodata ascii   UNICODEBIG//
571  0x00161e88 0x00561e88 13  14   .rodata ascii   gconv-modules
572  0x00161ec0 0x00561ec0 31  32   .rodata ascii   /usr/lib/x86_64-linux-gnu/gconv
573  0x00161ee0 0x00561ee0 15  16   .rodata ascii   gconv_builtin.c
574  0x00161ef0 0x00561ef0 36  37   .rodata ascii   cnt < sizeof (map) / sizeof (map[0])
575  0x00161f20 0x00561f20 25  26   .rodata ascii   __gconv_get_builtin_trans
576  0x00161f3a 0x00561f3a 19  20   .rodata ascii   ../iconv/skeleton.c
577  0x00161f4e 0x00561f4e 19  20   .rodata ascii   outbufstart == NULL
578  0x00161f62 0x00561f62 16  17   .rodata ascii   outbuf == outerr
579  0x00161f73 0x00561f73 14  15   .rodata ascii   gconv_simple.c
580  0x00161f82 0x00561f82 21  22   .rodata ascii   *outptrp + 4 > outend
581  0x00161f98 0x00561f98 15  16   .rodata ascii   ../iconv/loop.c
582  0x00161fa8 0x00561fa8 24  25   .rodata ascii   ch != 0xc0 && ch != 0xc1
583  0x00161fc8 0x00561fc8 30  31   .rodata ascii   nstatus == __GCONV_FULL_OUTPUT
584  0x00161fe8 0x00561fe8 52  53   .rodata ascii   cnt_after <= sizeof (data->__statep->__value.__wchb)
585  0x00162020 0x00562020 47  48   .rodata ascii   (state->__count & 7) <= sizeof (state->__value)
586  0x00162050 0x00562050 45  46   .rodata ascii   inlen_after <= sizeof (state->__value.__wchb)
587  0x00162080 0x00562080 38  39   .rodata ascii   inptr - bytebuf > (state->__count & 7)
588  0x001620a8 0x005620a8 35  36   .rodata ascii   inend != &bytebuf[MAX_NEEDED_INPUT]
589  0x001620d0 0x005620d0 37  38   .rodata ascii   inend - inptr > (state->__count & ~7)
590  0x001620f8 0x005620f8 47  48   .rodata ascii   inend - inptr <= sizeof (state->__value.__wchb)
591  0x00162140 0x00562140 32  33   .rodata ascii   internal_ucs2reverse_loop_single
592  0x00162180 0x00562180 38  39   .rodata ascii   __gconv_transform_internal_ucs2reverse
593  0x001621c0 0x005621c0 32  33   .rodata ascii   ucs2reverse_internal_loop_single
594  0x00162200 0x00562200 38  39   .rodata ascii   __gconv_transform_ucs2reverse_internal
595  0x00162240 0x00562240 31  32   .rodata ascii   __gconv_transform_internal_ucs2
596  0x00162260 0x00562260 31  32   .rodata ascii   __gconv_transform_ucs2_internal
597  0x00162280 0x00562280 31  32   .rodata ascii   __gconv_transform_utf8_internal
598  0x001622a0 0x005622a0 31  32   .rodata ascii   __gconv_transform_internal_utf8
599  0x001622c0 0x005622c0 32  33   .rodata ascii   __gconv_transform_internal_ascii
600  0x00162300 0x00562300 32  33   .rodata ascii   __gconv_transform_ascii_internal
601  0x00162340 0x00562340 33  34   .rodata ascii   __gconv_transform_ucs4le_internal
602  0x00162380 0x00562380 33  34   .rodata ascii   __gconv_transform_internal_ucs4le
603  0x001623c0 0x005623c0 31  32   .rodata ascii   __gconv_transform_ucs4_internal
604  0x001623e0 0x005623e0 31  32   .rodata ascii   __gconv_transform_internal_ucs4
605  0x00162400 0x00562400 25  26   .rodata ascii   internal_ucs2_loop_single
606  0x00162420 0x00562420 25  26   .rodata ascii   ucs2_internal_loop_single
607  0x00162440 0x00562440 25  26   .rodata ascii   utf8_internal_loop_single
608  0x00162460 0x00562460 25  26   .rodata ascii   internal_utf8_loop_single
609  0x00162480 0x00562480 26  27   .rodata ascii   internal_ascii_loop_single
610  0x001624a0 0x005624a0 20  21   .rodata ascii   ucs4le_internal_loop
611  0x001624b5 0x005624b5 10  11   .rodata ascii   GCONV_PATH
612  0x001624c0 0x005624c0 51  52   .rodata ascii   /usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache
613  0x001624f4 0x005624f4 10  11   .rodata ascii   gconv_dl.c
614  0x001624ff 0x005624ff 16  17   .rodata ascii   obj->counter > 0
615  0x00162510 0x00562510 21  22   .rodata ascii   found->handle == NULL
616  0x00162526 0x00562526 5   6    .rodata ascii   gconv
617  0x0016252c 0x0056252c 10  11   .rodata ascii   gconv_init
618  0x00162537 0x00562537 9   10   .rodata ascii   gconv_end
619  0x00162550 0x00562550 16  17   .rodata ascii   do_release_shlib
620  0x00162570 0x00562570 18  19   .rodata ascii   __gconv_find_shlib
621  0x00162583 0x00562583 9   10   .rodata ascii   ,TRANSLIT
622  0x0016258d 0x0056258d 7   8    .rodata ascii   /IGNORE
623  0x00162595 0x00562595 7   8    .rodata ascii   ,IGNORE
624  0x0016259d 0x0056259d 7   8    .rodata ascii   LOCPATH
625  0x001625a8 0x005625a8 6   7    .rodata ascii   \b\n\a\n\v\v
626  0x001625af 0x005625af 4   5    .rodata ascii   \b\a\n\f
627  0x001625c7 0x005625c7 6   7    .rodata ascii   ?HP[hw
628  0x001625e0 0x005625e0 10  11   .rodata ascii   LC_COLLATE
629  0x001625eb 0x005625eb 8   9    .rodata ascii   LC_CTYPE
630  0x001625f4 0x005625f4 11  12   .rodata ascii   LC_MONETARY
631  0x00162600 0x00562600 10  11   .rodata ascii   LC_NUMERIC
632  0x0016260b 0x0056260b 7   8    .rodata ascii   LC_TIME
633  0x00162613 0x00562613 11  12   .rodata ascii   LC_MESSAGES
634  0x0016261f 0x0056261f 8   9    .rodata ascii   LC_PAPER
635  0x00162628 0x00562628 7   8    .rodata ascii   LC_NAME
636  0x00162630 0x00562630 10  11   .rodata ascii   LC_ADDRESS
637  0x0016263b 0x0056263b 12  13   .rodata ascii   LC_TELEPHONE
638  0x00162648 0x00562648 14  15   .rodata ascii   LC_MEASUREMENT
639  0x00162657 0x00562657 17  18   .rodata ascii   LC_IDENTIFICATION
640  0x00162669 0x00562669 6   7    .rodata ascii   LC_ALL
641  0x00162670 0x00562670 4   5    .rodata ascii   LANG
642  0x00162675 0x00562675 12  13   .rodata ascii   findlocale.c
643  0x00162682 0x00562682 22  23   .rodata ascii   locale_codeset != NULL
644  0x00162699 0x00562699 4   5    .rodata ascii   /../
645  0x001626a0 0x005626a0 15  16   .rodata ascii   _nl_find_locale
646  0x001626b0 0x005626b0 15  16   .rodata ascii   /usr/lib/locale
647  0x001626f4 0x005626f4 12  13   .rodata ascii   loadlocale.c
648  0x00162701 0x00562701 20  21   .rodata ascii   category == LC_CTYPE
649  0x001629b0 0x005629b0 9   40   .rodata utf32le \b\b\b\b\b\b\n\b\b
650  0x00162c1c 0x00562c1c 10  44   .rodata utf32le \b\b\b\b\b\b\b\b\b\b
651  0x00162c98 0x00562c98 4   20   .rodata utf32le \b\b\b\b
652  0x00162d08 0x00562d08 4   20   .rodata utf32le \b\b\b\b
653  0x00162d24 0x00562d24 4   20   .rodata utf32le \b\b\b\b
654  0x00162d38 0x00562d38 4   20   .rodata utf32le \b\b\b\b
655  0x00162dd0 0x00562dd0 22  23   .rodata ascii   _nl_intern_locale_data
656  0x00162df0 0x00562df0 13  14   .rodata ascii   loadarchive.c
657  0x00162dfe 0x00562dfe 22  23   .rodata ascii   archmapped == &headmap
658  0x00162e18 0x00562e18 35  36   .rodata ascii   headmap.len == archive_stat.st_size
659  0x00162e40 0x00562e40 22  23   .rodata ascii   _nl_archive_subfreeres
660  0x00162e60 0x00562e60 28  29   .rodata ascii   _nl_load_locale_from_archive
661  0x00162e80 0x00562e80 30  31   .rodata ascii   /usr/lib/locale/locale-archive
662  0x00162ed8 0x00562ed8 14  15   .rodata ascii   ANSI_X3.4-1968
663  0x00162ee8 0x00562ee8 40  41   .rodata ascii   %s%s%s:%u: %s%sAssertion `%s' failed.\n%n
664  0x00162f20 0x00562f20 18  19   .rodata ascii   Unexpected error.\n
665  0x00162f60 0x00562f60 14  15   .rodata ascii   OUTPUT_CHARSET
666  0x00162f6f 0x00562f6f 8   9    .rodata ascii   charset=
667  0x00162f7c 0x00562f7c 5   6    .rodata ascii   %s/%s
668  0x00162f82 0x00562f82 8   9    .rodata ascii   LANGUAGE
669  0x00162f90 0x00562f90 17  18   .rodata ascii   /usr/share/locale
670  0x00162fa8 0x00562fa8 8   9    .rodata ascii   messages
671  0x00162fc0 0x00562fc0 17  18   .rodata ascii   /usr/share/locale
672  0x00162fd8 0x00562fd8 13  14   .rodata ascii   /locale.alias
673  0x00163244 0x00563244 9   10   .rodata ascii   \a\b\t\n\n\n\v\f\r
674  0x00163254 0x00563254 4   5    .rodata ascii   \a\b\t\n
675  0x0016325d 0x0056325d 4   5    .rodata ascii   \a\b\t\n
676  0x0016326e 0x0056326e 11  12   .rodata ascii   \a\b\t\n\a\b\t\n\b\t\n
677  0x00163280 0x00563280 5   6    .rodata ascii   \a\t\f\b\r
678  0x001633e2 0x005633e2 5   6    .rodata ascii   \a\b\t\n\v
679  0x001633fa 0x005633fa 7   8    .rodata ascii   \e\e\e\e\e\e\e
680  0x0016340c 0x0056340c 7   8    .rodata ascii   plural=
681  0x00163414 0x00563414 9   10   .rodata ascii   nplurals=
682  0x00163460 0x00563460 12  13   .rodata ascii   cxa_atexit.c
683  0x0016346d 0x0056346d 9   10   .rodata ascii   l != NULL
684  0x00163477 0x00563477 12  13   .rodata ascii   func != NULL
685  0x00163488 0x00563488 12  13   .rodata ascii   __new_exitfn
686  0x001634a0 0x005634a0 17  18   .rodata ascii   __internal_atexit
687  0x00163508 0x00563508 8   9    .rodata ascii   UUUUUUUU
688  0x00163517 0x00563517 9   10   .rodata ascii   ?33333333
689  0x00163550 0x00563550 7   8    .rodata ascii   UUUUUUU
690  0x0016358b 0x0056358b 5   6    .rodata ascii   P^Cy\r
691  0x0016359e 0x0056359e 4   7    .rodata utf8    0\f袋. blocks=Basic Latin,CJK Unified Ideographs
692  0x001635ac 0x005635ac 4   5    .rodata ascii   ,d!\v
693  0x001635b7 0x005635b7 9   12   .rodata utf8    \np=\nףp=\n؉ blocks=Basic Latin,Hebrew,Arabic
694  0x001635cc 0x005635cc 6   7    .rodata ascii   ^B{\t$I
695  0x00163607 0x00563607 9   10   .rodata ascii   \aP\auP\auP\a
696  0x00163617 0x00563617 17  18   .rodata ascii   \a*nsize < MPNSIZE
697  0x00163629 0x00563629 15  16   .rodata ascii   decimal_len > 0
698  0x0016363d 0x0056363d 5   6    .rodata ascii   inity
699  0x00163647 0x00563647 16  17   .rodata ascii   dig_no >= int_no
700  0x00163658 0x00563658 9   10   .rodata ascii   bits != 0
701  0x00163662 0x00563662 10  11   .rodata ascii   digcnt > 0
702  0x0016366d 0x0056366d 27  28   .rodata ascii   int_no > 0 && exponent == 0
703  0x00163689 0x00563689 20  21   .rodata ascii   need_frac_digits > 0
704  0x0016369e 0x0056369e 21  22   .rodata ascii   numsize == 1 && n < d
705  0x001636b4 0x005636b4 18  19   .rodata ascii   numsize == densize
706  0x001636c7 0x005636c7 7   8    .rodata ascii   cy != 0
707  0x001636d0 0x005636d0 32  33   .rodata ascii   dig_no <= (uintmax_t) INTMAX_MAX
708  0x001636f8 0x005636f8 59  60   .rodata ascii   int_no <= (uintmax_t) (INTMAX_MAX + MIN_EXP - MANT_DIG) / 4
709  0x00163738 0x00563738 54  55   .rodata ascii   lead_zero == 0 && int_no <= (uintmax_t) INTMAX_MAX / 4
710  0x00163770 0x00563770 55  56   .rodata ascii   lead_zero <= (uintmax_t) (INTMAX_MAX - MAX_EXP - 3) / 4
711  0x001637a8 0x005637a8 58  59   .rodata ascii   int_no <= (uintmax_t) (INTMAX_MAX + MIN_10_EXP - MANT_DIG)
712  0x001637e8 0x005637e8 50  51   .rodata ascii   lead_zero == 0 && int_no <= (uintmax_t) INTMAX_MAX
713  0x00163820 0x00563820 54  55   .rodata ascii   lead_zero <= (uintmax_t) (INTMAX_MAX - MAX_10_EXP - 1)
714  0x00163858 0x00563858 79  80   .rodata ascii   lead_zero <= (base == 16 ? (uintmax_t) INTMAX_MAX / 4 : (uintmax_t) INTMAX_MAX)
715  0x001638a8 0x005638a8 129 130  .rodata ascii   lead_zero <= (base == 16 ? ((uintmax_t) exponent - (uintmax_t) INTMAX_MIN) / 4 : ((uintmax_t) exponent - (uintmax_t) INTMAX_MIN))
716  0x00163930 0x00563930 107 108  .rodata ascii   int_no <= (uintmax_t) (exponent < 0 ? (INTMAX_MAX - bits + 1) / 4 : (INTMAX_MAX - exponent - bits + 1) / 4)
717  0x001639a0 0x005639a0 70  71   .rodata ascii   dig_no > int_no && exponent <= 0 && exponent >= MIN_10_EXP - (DIG + 2)
718  0x001639e8 0x005639e8 33  34   .rodata ascii   int_no == 0 && *startp != L_('0')
719  0x00163a10 0x00563a10 10  11   .rodata ascii   str_to_mpn
720  0x00163a60 0x00563a60 21  22   .rodata ascii   ____strtof_l_internal
721  0x00163b00 0x00563b00 21  22   .rodata ascii   ____strtod_l_internal
722  0x00163b50 0x00563b50 20  21   .rodata ascii   ../stdlib/strtod_l.c
723  0x00163b65 0x00563b65 10  11   .rodata ascii   empty == 1
724  0x00163bc0 0x00563bc0 22  23   .rodata ascii   ____strtold_l_internal
725  0x00163c8b 0x00563c8b 4   5    .rodata ascii   ]xEc
726  0x00163e7d 0x00563e7d 5   8    .rodata utf8    ﬅ[Am- blocks=Alphabetic Presentation Forms,Basic Latin
727  0x00163f2b 0x00563f2b 4   5    .rodata ascii   kpnJ
728  0x00163f39 0x00563f39 4   6    .rodata utf8    fƭ$6 blocks=Basic Latin,Latin Extended-B
729  0x00163fd6 0x00563fd6 4   5    .rodata ascii   uD;s
730  0x001640d3 0x005640d3 4   5    .rodata ascii   )r+[
731  0x001640d8 0x005640d8 4   5    .rodata ascii   [!|n
732  0x0016419d 0x0056419d 5   6    .rodata ascii   uYD?e
733  0x001641c9 0x005641c9 4   6    .rodata utf8    6IS blocks=Thaana,Basic Latin
734  0x001641e8 0x005641e8 5   7    .rodata utf8    I9C-ƣ blocks=Basic Latin,Latin Extended-B
735  0x00164317 0x00564317 4   5    .rodata ascii   I!G.
736  0x001643d1 0x005643d1 7   8    .rodata ascii   U^h6LU3
737  0x0016447e 0x0056447e 4   5    .rodata ascii   U.y`
738  0x00164496 0x00564496 4   5    .rodata ascii   3?Cy
739  0x001644b0 0x005644b0 5   6    .rodata ascii   '_Djz
740  0x001644f4 0x005644f4 5   6    .rodata ascii   $po?b
741  0x0016450f 0x0056450f 5   6    .rodata ascii   w};u\n
742  0x001647cb 0x005647cb 4   5    .rodata ascii   =t%j
743  0x0016482c 0x0056482c 4   5    .rodata ascii   MP0!
744  0x00164838 0x00564838 5   7    .rodata utf8    *ǎ?:7 blocks=Basic Latin,Latin Extended-B
745  0x0016486f 0x0056486f 5   7    .rodata utf8    +\f20 blocks=Basic Latin,Combining Diacritical Marks
746  0x001648c1 0x005648c1 4   5    .rodata ascii   t0tv
747  0x00164904 0x00564904 8   9    .rodata ascii   =u8Q)+\n9
748  0x00164933 0x00564933 4   6    .rodata utf8    \f9Ԣ7 blocks=Basic Latin,Cyrillic Supplement
749  0x00164942 0x00564942 6   7    .rodata ascii   {n \b$-
750  0x00164958 0x00564958 4   5    .rodata ascii   %?\vD
751  0x00164968 0x00564968 4   5    .rodata ascii   *~xx
752  0x001649aa 0x005649aa 5   7    .rodata utf8    Ѷ~j2= blocks=Cyrillic,Basic Latin
753  0x001649f7 0x005649f7 4   5    .rodata ascii   ?\fE,
754  0x00164a1b 0x00564a1b 4   5    .rodata ascii   MP#\e
755  0x00164a54 0x00564a54 4   5    .rodata ascii   |;#o
756  0x00164a7d 0x00564a7d 6   9    .rodata utf8    f%(炸r; blocks=Basic Latin,CJK Unified Ideographs
757  0x00164aa5 0x00564aa5 4   5    .rodata ascii   \r@SZ
758  0x00164ab8 0x00564ab8 6   8    .rodata utf8    TɤAc+; blocks=Basic Latin,IPA Extensions
759  0x00164acd 0x00564acd 4   5    .rodata ascii   \bU,i
760  0x00164ae7 0x00564ae7 5   6    .rodata ascii   ^2XX%
761  0x00164b1f 0x00564b1f 4   5    .rodata ascii   +}\\n
762  0x00164b65 0x00564b65 4   6    .rodata utf8    ٸZNh blocks=Arabic,Basic Latin
763  0x00164ba9 0x00564ba9 5   6    .rodata ascii   !{>;b
764  0x00164bc8 0x00564bc8 5   6    .rodata ascii   T\v]=!
765  0x00164bd2 0x00564bd2 4   5    .rodata ascii   dI@B
766  0x00164bfc 0x00564bfc 4   6    .rodata utf8    2I%%
767  0x0016501b 0x0056501b 4   5    .rodata ascii   d&R4
768  0x00165021 0x00565021 5   6    .rodata ascii   cIdSP
769  0x0016505c 0x0056505c 4   5    .rodata ascii   kDs,
770  0x00165083 0x00565083 8   9    .rodata ascii   "ZzY8<{j
771  0x0016511c 0x0056511c 4   6    .rodata utf8    1-1ݛ blocks=Basic Latin,Arabic Supplement
772  0x00165127 0x00565127 8   9    .rodata ascii   H%Mx7@.,
773  0x0016517a 0x0056517a 5   6    .rodata ascii   XP\epx
774  0x0016518e 0x0056518e 4   5    .rodata ascii   Gfn\a
775  0x001651b9 0x005651b9 4   5    .rodata ascii   <{O+
776  0x001651de 0x005651de 4   5    .rodata ascii   jrB\v
777  0x0016520d 0x0056520d 5   6    .rodata ascii   eUkJL
778  0x0016525c 0x0056525c 4   5    .rodata ascii   $~r<
779  0x0016528d 0x0056528d 4   5    .rodata ascii   \flA/
780  0x0016529f 0x0056529f 4   6    .rodata utf8    ~;EƖ blocks=Basic Latin,Latin Extended-B
781  0x001652b7 0x005652b7 5   6    .rodata ascii   =6Zn1
782  0x001652dc 0x005652dc 4   5    .rodata ascii   '\nN2
783  0x001652e3 0x005652e3 5   6    .rodata ascii   ]4%C(
784  0x001652fc 0x005652fc 6   9    .rodata utf8    צ6~W^Ǆ blocks=Hebrew,Basic Latin,Latin Extended-B
785  0x00165354 0x00565354 4   5    .rodata ascii   zZ W
786  0x00165359 0x00565359 4   5    .rodata ascii   $?!k
787  0x00165366 0x00565366 6   8    .rodata utf8    +XZ1J blocks=Basic Latin,Arabic
788  0x00165371 0x00565371 4   5    .rodata ascii   \e8s8
789  0x001653aa 0x005653aa 5   6    .rodata ascii   6:X6k
790  0x001654b3 0x005654b3 7   8    .rodata ascii   6Q"U757
791  0x001654e8 0x005654e8 7   8    .rodata ascii   1f\n*,W7
792  0x0016553a 0x0056553a 4   5    .rodata ascii   PEt\
793  0x0016557b 0x0056557b 6   7    .rodata ascii   HeS;JG
794  0x001655af 0x005655af 6   8    .rodata utf8    f9Du0є blocks=Basic Latin,Cyrillic
795  0x001655bd 0x005655bd 6   7    .rodata ascii   \rAa6ky
796  0x001655e1 0x005655e1 7   8    .rodata ascii   P\t\e_c\tZ
797  0x001655ed 0x005655ed 4   5    .rodata ascii   rTa\n
798  0x00165639 0x00565639 5   7    .rodata utf8    8ӧa*) blocks=Basic Latin,Cyrillic
799  0x00165645 0x00565645 4   5    .rodata ascii   LGBs
800  0x00165672 0x00565672 4   5    .rodata ascii   #`R(
801  0x0016569a 0x0056569a 10  11   .rodata ascii   %;oo3bEj3\f
802  0x00165716 0x00565716 4   5    .rodata ascii   ](9$
803  0x0016579b 0x0056579b 4   5    .rodata ascii   P831
804  0x001657a1 0x005657a1 4   5    .rodata ascii   S|YU
805  0x001657d3 0x005657d3 4   5    .rodata ascii   r#\e1
806  0x001657ff 0x005657ff 5   6    .rodata ascii   S-'g(
807  0x00165857 0x00565857 4   5    .rodata ascii   wN<G
808  0x00165883 0x00565883 4   5    .rodata ascii   :o9s
809  0x00165896 0x00565896 4   5    .rodata ascii   Nus^
810  0x001658f0 0x005658f0 6   7    .rodata ascii   w "_\bJ
811  0x001661c3 0x005661c3 4   6    .rodata utf8    Xe=٦ blocks=Basic Latin,Arabic
812  0x001661dc 0x005661dc 4   7    .rodata utf8    өLʥv blocks=Cyrillic,Basic Latin,IPA Extensions
813  0x001661f4 0x005661f4 4   6    .rodata utf8    Kߣbo blocks=Basic Latin,NKo
814  0x00166241 0x00566241 5   7    .rodata utf8    x{Z˫: blocks=Basic Latin,Spacing Modifier Letters
815  0x00166297 0x00566297 5   6    .rodata ascii   s%{^%
816  0x001662a4 0x005662a4 4   6    .rodata utf8    6șbx blocks=Basic Latin,Latin Extended-B
817  0x001662e6 0x005662e6 4   6    .rodata utf8    v\e(ǲ blocks=Basic Latin,Latin Extended-B
818  0x0016632b 0x0056632b 4   5    .rodata ascii   ~rf0
819  0x00166330 0x00566330 4   6    .rodata utf8    WԶ9h blocks=Basic Latin,Armenian
820  0x00166342 0x00566342 4   5    .rodata ascii   QB"U
821  0x001663e5 0x005663e5 4   5    .rodata ascii   ~4\\e
822  0x001663fc 0x005663fc 5   6    .rodata ascii   {[P`x
823  0x00166402 0x00566402 5   6    .rodata ascii   J3]Gm
824  0x0016640d 0x0056640d 4   5    .rodata ascii   us&`
825  0x00166441 0x00566441 4   5    .rodata ascii   HiW\a
826  0x00166451 0x00566451 4   5    .rodata ascii   ]\a=J
827  0x0016645f 0x0056645f 4   5    .rodata ascii   k_\vP
828  0x001664ae 0x005664ae 6   7    .rodata ascii   \t~3 Y2
829  0x001664c0 0x005664c0 5   6    .rodata ascii   pZ|<<
830  0x0016650c 0x0056650c 5   6    .rodata ascii   To<zV
831  0x00166580 0x00566580 5   6    .rodata ascii   RX>oP
832  0x001665c2 0x005665c2 7   8    .rodata ascii   go4b i)
833  0x001665fb 0x005665fb 5   6    .rodata ascii   NM?]P
834  0x0016660d 0x0056660d 4   6    .rodata utf8    ^LGݦ blocks=Basic Latin,Arabic Supplement
835  0x0016661d 0x0056661d 5   7    .rodata utf8    1ܘT^E blocks=Basic Latin,Syriac
836  0x00166635 0x00566635 4   5    .rodata ascii   \bzR!
837  0x0016663d 0x0056663d 4   5    .rodata ascii   r)hV
838  0x001666c9 0x005666c9 4   5    .rodata ascii   Cb6'
839  0x001666d0 0x005666d0 5   6    .rodata ascii   MW&f*
840  0x0016671e 0x0056671e 5   6    .rodata ascii   \nk1d5
841  0x00166736 0x00566736 7   9    .rodata utf8    B;)!Ӌk\e blocks=Basic Latin,Cyrillic
842  0x00166792 0x00566792 4   5    .rodata ascii   0m\b_
843  0x00166797 0x00566797 7   8    .rodata ascii   dISoy}h
844  0x001667cf 0x005667cf 4   6    .rodata utf8    V2\fѷ blocks=Basic Latin,Cyrillic
845  0x001667da 0x005667da 4   5    .rodata ascii   [@$>
846  0x001667e7 0x005667e7 5   6    .rodata ascii   *qx\e?
847  0x00166807 0x00566807 4   6    .rodata utf8    h7Ӝ% blocks=Basic Latin,Cyrillic
848  0x00166828 0x00566828 4   6    .rodata utf8    خ\nu# blocks=Arabic,Basic Latin
849  0x001668d5 0x005668d5 6   7    .rodata ascii   4otDHl
850  0x001668ff 0x005668ff 7   8    .rodata ascii   5pw-e\aF
851  0x00166969 0x00566969 5   6    .rodata ascii   zW5N=
852  0x00166970 0x00566970 4   5    .rodata ascii   Ols5
853  0x001669be 0x005669be 4   5    .rodata ascii   hk\vs
854  0x001669cc 0x005669cc 4   5    .rodata ascii   ct\tR
855  0x001669e4 0x005669e4 4   5    .rodata ascii   exK>
856  0x001669f3 0x005669f3 4   5    .rodata ascii   zGk\v
857  0x00166aaf 0x00566aaf 4   5    .rodata ascii   6Xg:
858  0x00166b3e 0x00566b3e 4   5    .rodata ascii   ~K(=
859  0x00166b98 0x00566b98 6   7    .rodata ascii   9\rI[Lm
860  0x00166bd5 0x00566bd5 4   6    .rodata utf8    @B% blocks=Syriac,Basic Latin
861  0x00166bff 0x00566bff 4   7    .rodata utf8    w[Aͳ blocks=Basic Latin,Greek and Coptic
862  0x00166c4f 0x00566c4f 7   9    .rodata utf8    %W@qÏcc blocks=Basic Latin,Latin-1 Supplement
863  0x00166c7a 0x00566c7a 4   5    .rodata ascii   qioq
864  0x00166c9b 0x00566c9b 4   6    .rodata utf8    .vˎ\ blocks=Basic Latin,Spacing Modifier Letters
865  0x00166ca4 0x00566ca4 4   5    .rodata ascii   \_\e@
866  0x00166ca9 0x00566ca9 5   6    .rodata ascii   c\n_\nV
867  0x00166cef 0x00566cef 4   6    .rodata utf8    m\tf\
868  0x00166cfc 0x00566cfc 6   8    .rodata utf8    \fl[ϙDi blocks=Basic Latin,Greek and Coptic
869  0x00166d1b 0x00566d1b 5   6    .rodata ascii   WFYa,
870  0x00166d3f 0x00566d3f 4   5    .rodata ascii   `9\f7
871  0x00166d4d 0x00566d4d 5   6    .rodata ascii   r/ZXk
872  0x00166d5b 0x00566d5b 5   7    .rodata utf8    xvԉ\e[ blocks=Basic Latin,Cyrillic Supplement
873  0x00166d9d 0x00566d9d 6   7    .rodata ascii   r1hTsN
874  0x00166dec 0x00566dec 4   6    .rodata utf8    Rhɩ\b blocks=Basic Latin,IPA Extensions
875  0x00166e19 0x00566e19 5   8    .rodata utf8    왨'wuH blocks=Hangul Syllables,Basic Latin
876  0x00166e23 0x00566e23 6   8    .rodata utf8    A}7ϸhN blocks=Basic Latin,Greek and Coptic
877  0x00166e38 0x00566e38 5   6    .rodata ascii   tLP|L
878  0x00166e7d 0x00566e7d 4   5    .rodata ascii   0Kuv
879  0x00166e86 0x00566e86 6   9    .rodata utf8    կ٪7]9\t blocks=Armenian,Arabic,Basic Latin
880  0x00166eee 0x00566eee 5   6    .rodata ascii   %:ShD
881  0x00166f6a 0x00566f6a 6   7    .rodata ascii   % Mqz<
882  0x00166f72 0x00566f72 4   5    .rodata ascii   hik;
883  0x00166f7c 0x00566f7c 6   7    .rodata ascii   _kI;j]
884  0x00166f86 0x00566f86 4   5    .rodata ascii   \r8<Q
885  0x00166fc2 0x00566fc2 4   5    .rodata ascii   d;Vg
886  0x00166ff0 0x00566ff0 4   6    .rodata utf8    \ttYЏ blocks=Basic Latin,Cyrillic
887  0x0016701c 0x0056701c 6   8    .rodata utf8    Ȭ\bG&.! blocks=Latin Extended-B,Basic Latin
888  0x00167092 0x00567092 4   5    .rodata ascii   `7>V
889  0x001670c4 0x005670c4 5   6    .rodata ascii   /T7B@
890  0x0016718d 0x0056718d 5   7    .rodata utf8    '=I&ņ blocks=Basic Latin,Latin Extended-A
891  0x0016719d 0x0056719d 4   6    .rodata utf8    (YϦ> blocks=Basic Latin,Greek and Coptic
892  0x0016724b 0x0056724b 7   11   .rodata utf8    UVx9ꖖ( blocks=Basic Latin,Combining Diacritical Marks,Vai
893  0x00167257 0x00567257 4   5    .rodata ascii   M@\e>
894  0x001672cf 0x005672cf 4   5    .rodata ascii   =G?R
895  0x001672f6 0x005672f6 4   6    .rodata utf8    Ѱe=1 blocks=Cyrillic,Basic Latin
896  0x001672fd 0x005672fd 4   5    .rodata ascii   ~DW&
897  0x00167324 0x00567324 4   5    .rodata ascii   qQ$m
898  0x0016734f 0x0056734f 4   5    .rodata ascii   MD}9
899  0x001673ab 0x005673ab 4   6    .rodata utf8    P)\fM
900  0x001673da 0x005673da 4   6    .rodata utf8    Z!ðs blocks=Basic Latin,Latin-1 Supplement
901  0x001673f0 0x005673f0 7   8    .rodata ascii   !%uGD6n
902  0x00167408 0x00567408 10  11   .rodata ascii   wfileops.c
903  0x00167413 0x00567413 27  28   .rodata ascii   status == __codecvt_partial
904  0x00167430 0x00567430 19  20   .rodata ascii   _IO_wfile_underflow
905  0x00167444 0x00567444 9   10   .rodata ascii   iofwide.c
906  0x0016744e 0x0056744e 21  22   .rodata ascii   fcts.towc_nsteps == 1
907  0x00167464 0x00567464 21  22   .rodata ascii   fcts.tomb_nsteps == 1
908  0x00167480 0x00567480 9   10   .rodata ascii   _IO_fwide
909  0x00167490 0x00567490 52  53   .rodata ascii   Fatal error: glibc detected an invalid stdio handle\n
910  0x001674c5 0x005674c5 5   6    .rodata ascii   ,ccs=
911  0x00167530 0x00567530 18  19   .rodata ascii   _IO_new_file_fopen
912  0x00167543 0x00567543 8   9    .rodata ascii   strops.c
913  0x0016754c 0x0056754c 16  17   .rodata ascii   offset >= oldend
914  0x00167560 0x00567560 15  16   .rodata ascii   enlarge_userbuf
915  0x00167570 0x00567570 54  55   .rodata ascii   The futex facility returned an unexpected error code.\n
916  0x001675a7 0x005675a7 28  29   .rodata ascii   malloc: top chunk is corrupt
917  0x001675c4 0x005675c4 8   9    .rodata ascii   malloc.c
918  0x001675cd 0x005675cd 20  21   .rodata ascii   chunk_is_mmapped (p)
919  0x001675e2 0x005675e2 29  30   .rodata ascii   aligned_OK (chunk2rawmem (p))
920  0x00167600 0x00567600 23  24   .rodata ascii   prev_size (p) == offset
921  0x00167618 0x00567618 7   8    .rodata ascii   arena.c
922  0x00167620 0x00567620 29  30   .rodata ascii   result->attached_threads == 0
923  0x0016763e 0x0056763e 23  24   .rodata ascii   <heap nr="%d">\n<sizes>\n
924  0x00167656 0x00567656 8   9    .rodata ascii   </heap>\n
925  0x0016765f 0x0056765f 28  29   .rodata ascii   corrupted size vs. prev_size
926  0x0016767c 0x0056767c 28  29   .rodata ascii   corrupted double-linked list
927  0x00167699 0x00567699 23  24   .rodata ascii   free(): invalid pointer
928  0x001676b1 0x005676b1 20  21   .rodata ascii   free(): invalid size
929  0x001676c6 0x005676c6 28  29   .rodata ascii   invalid fastbin entry (free)
930  0x001676e3 0x005676e3 18  19   .rodata ascii   heap->ar_ptr == av
931  0x001676f6 0x005676f6 15  16   .rodata ascii   correction >= 0
932  0x00167706 0x00567706 24  25   .rodata ascii   p->attached_threads == 0
933  0x0016771f 0x0056771f 26  27   .rodata ascii   chunk_main_arena (bck->bk)
934  0x0016773a 0x0056773a 22  23   .rodata ascii   chunk_main_arena (fwd)
935  0x00167751 0x00567751 8   9    .rodata ascii   bit != 0
936  0x0016775a 0x0056775a 28  29   .rodata ascii   malloc(): corrupted top size
937  0x00167777 0x00567777 27  28   .rodata ascii   realloc(): invalid old size
938  0x00167793 0x00567793 24  25   .rodata ascii   !chunk_is_mmapped (oldp)
939  0x001677ac 0x005677ac 28  29   .rodata ascii   realloc(): invalid next size
940  0x001677c9 0x005677c9 26  27   .rodata ascii   realloc(): invalid pointer
941  0x001677e4 0x005677e4 23  24   .rodata ascii   a->attached_threads > 0
942  0x001677fc 0x005677fc 12  13   .rodata ascii   nclears >= 3
943  0x00167809 0x00567809 10  11   .rodata ascii   Arena %d:\n
944  0x00167814 0x00567814 24  25   .rodata ascii   system bytes     = %10u\n
945  0x0016782d 0x0056782d 24  25   .rodata ascii   in use bytes     = %10u\n
946  0x00167846 0x00567846 20  21   .rodata ascii   Total (incl. mmap):\n
947  0x0016785b 0x0056785b 24  25   .rodata ascii   max mmap regions = %10u\n
948  0x00167874 0x00567874 25  26   .rodata ascii   max mmap bytes   = %10lu\n
949  0x0016788e 0x0056788e 21  22   .rodata ascii   <malloc version="1">\n
950  0x001678a4 0x005678a4 5   6    .rodata ascii   mtrim
951  0x001678b0 0x005678b0 48  49   .rodata ascii   int_mallinfo(): unaligned fastbin chunk detected
952  0x001678e8 0x005678e8 38  39   .rodata ascii   %s%s%s:%u: %s%sAssertion `%s' failed.\n
953  0x00167910 0x00567910 31  32   .rodata ascii   munmap_chunk(): invalid pointer
954  0x00167930 0x00567930 31  32   .rodata ascii   mremap_chunk(): invalid pointer
955  0x00167950 0x00567950 36  37   .rodata ascii   replaced_arena->attached_threads > 0
956  0x00167978 0x00567978 49  50   .rodata ascii   __malloc_info(): unaligned fastbin chunk detected
957  0x001679b0 0x005679b0 54  55   .rodata ascii     <size from="%zu" to="%zu" total="%zu" count="%zu"/>\n
958  0x001679e8 0x005679e8 58  59   .rodata ascii     <unsorted from="%zu" to="%zu" total="%zu" count="%zu"/>\n
959  0x00167a28 0x00567a28 165 166  .rodata ascii   </sizes>\n<total type="fast" count="%zu" size="%zu"/>\n<total type="rest" count="%zu" size="%zu"/>\n<system type="current" size="%zu"/>\n<system type="max" size="%zu"/>\n
960  0x00167ad0 0x00567ad0 108 109  .rodata ascii   <aspace type="total" size="%zu"/>\n<aspace type="mprotect" size="%zu"/>\n<aspace type="subheaps" size="%zu"/>\n
961  0x00167b40 0x00567b40 71  72   .rodata ascii   <aspace type="total" size="%zu"/>\n<aspace type="mprotect" size="%zu"/>\n
962  0x00167b88 0x00567b88 280 281  .rodata ascii   <total type="fast" count="%zu" size="%zu"/>\n<total type="rest" count="%zu" size="%zu"/>\n<total type="mmap" count="%d" size="%zu"/>\n<system type="current" size="%zu"/>\n<system type="max" size="%zu"/>\n<aspace type="total" size="%zu"/>\n<aspace type="mprotect" size="%zu"/>\n</malloc>\n
963  0x00167ca8 0x00567ca8 40  41   .rodata ascii   corrupted double-linked list (not small)
964  0x00167cd8 0x00567cd8 54  55   .rodata ascii   malloc_consolidate(): unaligned fastbin chunk detected
965  0x00167d10 0x00567d10 40  41   .rodata ascii   malloc_consolidate(): invalid chunk size
966  0x00167d40 0x00567d40 40  41   .rodata ascii   corrupted size vs. prev_size in fastbins
967  0x00167d70 0x00567d70 42  43   .rodata ascii   free(): too many chunks detected in tcache
968  0x00167da0 0x00567da0 44  45   .rodata ascii   free(): unaligned chunk detected in tcache 2
969  0x00167dd0 0x00567dd0 40  41   .rodata ascii   free(): double free detected in tcache 2
970  0x00167e00 0x00567e00 32  33   .rodata ascii   free(): invalid next size (fast)
971  0x00167e28 0x00567e28 35  36   .rodata ascii   double free or corruption (fasttop)
972  0x00167e50 0x00567e50 31  32   .rodata ascii   double free or corruption (top)
973  0x00167e70 0x00567e70 31  32   .rodata ascii   double free or corruption (out)
974  0x00167e90 0x00567e90 33  34   .rodata ascii   double free or corruption (!prev)
975  0x00167eb8 0x00567eb8 34  35   .rodata ascii   free(): invalid next size (normal)
976  0x00167ee0 0x00567ee0 48  49   .rodata ascii   corrupted size vs. prev_size while consolidating
977  0x00167f18 0x00567f18 33  34   .rodata ascii   free(): corrupted unsorted chunks
978  0x00167f40 0x00567f40 40  41   .rodata ascii   chunksize_nomask (p) == (0 | PREV_INUSE)
979  0x00167f70 0x00567f70 47  48   .rodata ascii   new_size > 0 && new_size < (long) (2 * MINSIZE)
980  0x00167fa0 0x00567fa0 40  41   .rodata ascii   new_size > 0 && new_size < HEAP_MAX_SIZE
981  0x00167fd0 0x00567fd0 61  62   .rodata ascii   ((unsigned long) ((char *) p + new_size) & (pagesz - 1)) == 0
982  0x00168010 0x00568010 55  56   .rodata ascii   ((char *) p + new_size) == ((char *) heap + heap->size)
983  0x00168048 0x00568048 30  31   .rodata ascii   /proc/sys/vm/overcommit_memory
984  0x00168068 0x00568068 62  63   .rodata ascii   ((INTERNAL_SIZE_T) chunk2rawmem (mm) & MALLOC_ALIGN_MASK) == 0
985  0x001680a8 0x005680a8 164 165  .rodata ascii   (old_top == initial_top (av) && old_size == 0) || ((unsigned long) (old_size) >= MINSIZE && prev_inuse (old_top) && ((unsigned long) old_end & (pagesize - 1)) == 0)
986  0x00168150 0x00568150 59  60   .rodata ascii   (unsigned long) (old_size) < (unsigned long) (nb + MINSIZE)
987  0x00168190 0x00568190 35  36   .rodata ascii   break adjusted to free malloc space
988  0x001681b8 0x005681b8 61  62   .rodata ascii   ((unsigned long) chunk2rawmem (brk) & MALLOC_ALIGN_MASK) == 0
989  0x001681f8 0x005681f8 44  45   .rodata ascii   malloc(): unaligned fastbin chunk detected 2
990  0x00168228 0x00568228 42  43   .rodata ascii   malloc(): unaligned fastbin chunk detected
991  0x00168258 0x00568258 34  35   .rodata ascii   malloc(): memory corruption (fast)
992  0x00168280 0x00568280 44  45   .rodata ascii   malloc(): unaligned fastbin chunk detected 3
993  0x001682b0 0x005682b0 47  48   .rodata ascii   malloc(): smallbin double linked list corrupted
994  0x001682e0 0x005682e0 33  34   .rodata ascii   malloc(): invalid size (unsorted)
995  0x00168308 0x00568308 38  39   .rodata ascii   malloc(): invalid next size (unsorted)
996  0x00168330 0x00568330 48  49   .rodata ascii   malloc(): mismatching next->prev_size (unsorted)
997  0x00168368 0x00568368 47  48   .rodata ascii   malloc(): unsorted double linked list corrupted
998  0x00168398 0x00568398 45  46   .rodata ascii   malloc(): invalid next->prev_inuse (unsorted)
999  0x001683c8 0x005683c8 58  59   .rodata ascii   malloc(): largebin double linked list corrupted (nextsize)
1000 0x00168408 0x00568408 52  53   .rodata ascii   malloc(): largebin double linked list corrupted (bk)
1001 0x00168440 0x00568440 41  42   .rodata ascii   malloc(): unaligned tcache chunk detected
1002 0x00168470 0x00568470 35  36   .rodata ascii   malloc(): corrupted unsorted chunks
1003 0x00168498 0x00568498 46  47   .rodata ascii   (unsigned long) (size) >= (unsigned long) (nb)
1004 0x001684c8 0x005684c8 37  38   .rodata ascii   malloc(): corrupted unsorted chunks 2
1005 0x001684f0 0x005684f0 72  73   .rodata ascii   newsize >= nb && (((unsigned long) (chunk2rawmem (p))) % alignment) == 0
1006 0x00168540 0x00568540 49  50   .rodata ascii   (unsigned long) (newsize) >= (unsigned long) (nb)
1007 0x00168578 0x00568578 103 104  .rodata ascii   !victim || chunk_is_mmapped (mem2chunk (victim)) || &main_arena == arena_for_chunk (mem2chunk (victim))
1008 0x001685e0 0x005685e0 98  99   .rodata ascii   !victim || chunk_is_mmapped (mem2chunk (victim)) || ar_ptr == arena_for_chunk (mem2chunk (victim))
1009 0x00168648 0x00568648 88  89   .rodata ascii   !p || chunk_is_mmapped (mem2chunk (p)) || &main_arena == arena_for_chunk (mem2chunk (p))
1010 0x001686a8 0x005686a8 83  84   .rodata ascii   !p || chunk_is_mmapped (mem2chunk (p)) || ar_ptr == arena_for_chunk (mem2chunk (p))
1011 0x00168700 0x00568700 57  58   .rodata ascii   tcache_thread_shutdown(): unaligned tcache chunk detected
1012 0x00168740 0x00568740 92  93   .rodata ascii   !newp || chunk_is_mmapped (mem2chunk (newp)) || ar_ptr == arena_for_chunk (mem2chunk (newp))
1013 0x001687a0 0x005687a0 85  86   .rodata ascii   !mem || chunk_is_mmapped (mem2chunk (mem)) || av == arena_for_chunk (mem2chunk (mem))
1014 0x001687f8 0x005687f8 60  61   .rodata ascii   (char *) chunk2rawmem (p) + 2 * CHUNK_HDR_SZ <= paligned_mem
1015 0x00168838 0x00568838 32  33   .rodata ascii   (char *) p + size > paligned_mem
1016 0x00168860 0x00568860 40  41   .rodata ascii   malloc_check_get_size: memory corruption
1017 0x00168890 0x00568890 13  14   .rodata ascii   __libc_calloc
1018 0x001688a0 0x005688a0 13  14   .rodata ascii   _mid_memalign
1019 0x001688b0 0x005688b0 14  15   .rodata ascii   __libc_realloc
1020 0x001688c0 0x005688c0 12  13   .rodata ascii   detach_arena
1021 0x001688d0 0x005688d0 13  14   .rodata ascii   get_free_list
1022 0x001688e0 0x005688e0 13  14   .rodata ascii   __libc_malloc
1023 0x001688f0 0x005688f0 12  13   .rodata ascii   _int_realloc
1024 0x00168900 0x00568900 12  13   .rodata ascii   mremap_chunk
1025 0x00168910 0x00568910 12  13   .rodata ascii   munmap_chunk
1026 0x00168920 0x00568920 9   10   .rodata ascii   heap_trim
1027 0x00168930 0x00568930 9   10   .rodata ascii   _int_free
1028 0x00168940 0x00568940 9   10   .rodata ascii   sysmalloc
1029 0x00168950 0x00568950 11  12   .rodata ascii   _int_malloc
1030 0x00168960 0x00568960 13  14   .rodata ascii   _int_memalign
1031 0x001689a0 0x005689a0 21  22   .rodata ascii   remove_from_free_list
1032 0x001689c0 0x005689c0 29  30   .rodata ascii   __malloc_arena_thread_freeres
1033 0x001689e0 0x005689e0 49  50   .rodata ascii   ((uintptr_t) table) % __alignof__ (table[0]) == 0
1034 0x00168a18 0x00568a18 55  56   .rodata ascii   ((uintptr_t) indirect) % __alignof__ (indirect[0]) == 0
1035 0x00168a50 0x00568a50 11  12   .rodata ascii   __strcoll_l
1036 0x00168a60 0x00568a60 63  64   .rodata ascii   ((uintptr_t) l_data.table) % __alignof__ (l_data.table[0]) == 0
1037 0x00168aa0 0x00568aa0 69  70   .rodata ascii   ((uintptr_t) l_data.indirect) % __alignof__ (l_data.indirect[0]) == 0
1038 0x00168ae8 0x00568ae8 11  12   .rodata ascii   __strxfrm_l
1039 0x00168af4 0x00568af4 14  15   .rodata ascii   Unknown error 
1040 0x00168b03 0x00568b03 4   5    .rodata ascii   %s%d
1041 0x00169b10 0x00569b10 48  49   .rodata ascii   @@@@@@@@@@@@@@@@[[[[[[[[[[[[[[[[                
1042 0x00169c00 0x00569c00 16  17   .rodata ascii   ZZZZZZZZZZZZZZZZ
1043 0x00169e57 0x00569e57 7   8    .rodata ascii   \a\b\t\n\v\f\r
1044 0x00169e6f 0x00569e6f 9   10   .rodata ascii   mbrtowc.c
1045 0x00169e79 0x00569e79 25  26   .rodata ascii   __mbsinit (data.__statep)
1046 0x00169e98 0x00569e98 159 160  .rodata ascii   status == __GCONV_OK || status == __GCONV_EMPTY_INPUT || status == __GCONV_ILLEGAL_INPUT || status == __GCONV_INCOMPLETE_INPUT || status == __GCONV_FULL_OUTPUT
1047 0x00169f38 0x00569f38 9   10   .rodata ascii   __mbrtowc
1048 0x00169f42 0x00569f42 9   10   .rodata ascii   wcrtomb.c
1049 0x00169f50 0x00569f50 9   10   .rodata ascii   __wcrtomb
1050 0x00169f5a 0x00569f5a 12  13   .rodata ascii   mbsnrtowcs.c
1051 0x00169f67 0x00569f67 10  11   .rodata ascii   result > 0
1052 0x00169f78 0x00569f78 12  13   .rodata ascii   __mbsnrtowcs
1053 0x00169f85 0x00569f85 12  13   .rodata ascii   wcsnrtombs.c
1054 0x00169f98 0x00569f98 38  39   .rodata ascii   data.__outbuf != (unsigned char *) dst
1055 0x00169fc0 0x00569fc0 12  13   .rodata ascii   __wcsnrtombs
1056 0x00169fcd 0x00569fcd 21  22   .rodata ascii   ../string/strcoll_l.c
1057 0x00169fe8 0x00569fe8 53  54   .rodata ascii   ((uintptr_t) weights) % __alignof__ (weights[0]) == 0
1058 0x0016a020 0x0056a020 49  50   .rodata ascii   ((uintptr_t) extra) % __alignof__ (extra[0]) == 0
1059 0x0016a058 0x0056a058 11  12   .rodata ascii   __wcscoll_l
1060 0x0016a064 0x0056a064 21  22   .rodata ascii   ../string/strxfrm_l.c
1061 0x0016a080 0x0056a080 67  68   .rodata ascii   ((uintptr_t) l_data.weights) % __alignof__ (l_data.weights[0]) == 0
1062 0x0016a0c8 0x0056a0c8 63  64   .rodata ascii   ((uintptr_t) l_data.extra) % __alignof__ (l_data.extra[0]) == 0
1063 0x0016a108 0x0056a108 11  12   .rodata ascii   __wcsxfrm_l
1064 0x0016a114 0x0056a114 24  25   .rodata ascii   ANSI_X3.4-1968//TRANSLIT
1065 0x0016a130 0x0056a130 59  60   .rodata ascii   Fatal glibc error: gconv module reference counter overflow\n
1066 0x0016a16c 0x0056a16c 13  14   .rodata ascii   mbsrtowcs_l.c
1067 0x0016a180 0x0056a180 40  41   .rodata ascii   ((wchar_t *) data.__outbuf)[-1] == L'\0'
1068 0x0016a1b0 0x0056a1b0 13  14   .rodata ascii   __mbsrtowcs_l
1069 0x0016a300 0x0056a300 11  12   .rodata ascii   %I:%M:%S %p
1070 0x0016a30c 0x0056a30c 8   9    .rodata ascii   %Y-%m-%d
1071 0x0016a6f0 0x0056a6f0 8   36   .rodata utf32le %Y-%m-%d
1072 0x0016a718 0x0056a718 11  48   .rodata utf32le %I:%M:%S %p
1073 0x0016a748 0x0056a748 5   24   .rodata utf32le %H:%M
1074 0x0016ad24 0x0056ad24 16  17   .rodata ascii   /usr/lib/getconf
1075 0x0016ad35 0x0056ad35 11  12   .rodata ascii   GETCONF_DIR
1076 0x0016ad41 0x0056ad41 26  27   .rodata ascii   /proc/sys/kernel/rtsig-max
1077 0x0016ad5c 0x0056ad5c 28  29   .rodata ascii   /proc/sys/kernel/ngroups_max
1078 0x0016ad79 0x0056ad79 11  12   .rodata ascii   ILP32_OFF32
1079 0x0016ad85 0x0056ad85 12  13   .rodata ascii   ILP32_OFFBIG
1080 0x0016b170 0x0056b170 35  36   .rodata ascii   ../sysdeps/unix/sysv/linux/getcwd.c
1081 0x0016b198 0x0056b198 43  44   .rodata ascii   errno != ERANGE || buf != NULL || size != 0
1082 0x0016b1c8 0x0056b1c8 8   9    .rodata ascii   __getcwd
1083 0x0016b1d8 0x0056b1d8 40  41   .rodata ascii   ../sysdeps/unix/sysv/linux/getpagesize.c
1084 0x0016b208 0x0056b208 13  14   .rodata ascii   __getpagesize
1085 0x0016b216 0x0056b216 22  23   .rodata ascii   GLRO(dl_pagesize) != 0
1086 0x0016b230 0x0056b230 40  41   .rodata ascii   ../sysdeps/unix/sysv/linux/getsysstats.c
1087 0x0016b260 0x0056b260 30  31   .rodata ascii   /sys/devices/system/cpu/online
1088 0x0016b280 0x0056b280 9   10   .rodata ascii   next_line
1089 0x0016b28a 0x0056b28a 10  11   .rodata ascii   *cp <= *re
1090 0x0016b295 0x0056b295 10  11   .rodata ascii   /proc/stat
1091 0x0016b2a0 0x0056b2a0 13  14   .rodata ascii   /proc/cpuinfo
1092 0x0016b2ae 0x0056b2ae 9   10   .rodata ascii   processor
1093 0x0016b2b8 0x0056b2b8 23  24   .rodata ascii   /sys/devices/system/cpu
1094 0x0016b2d0 0x0056b2d0 24  25   .rodata ascii   buffer overflow detected
1095 0x0016b2e9 0x0056b2e9 23  24   .rodata ascii   stack smashing detected
1096 0x0016b301 0x0056b301 23  24   .rodata ascii   *** %s ***: terminated\n
1097 0x0016b320 0x0056b320 53  54   .rodata ascii   Failed loading %lu audit modules, %lu are supported.\n
1098 0x0016b358 0x0056b358 36  37   .rodata ascii   result <= GL(dl_tls_max_dtv_idx) + 1
1099 0x0016b380 0x0056b380 36  37   .rodata ascii   result == GL(dl_tls_max_dtv_idx) + 1
1100 0x0016b3a8 0x0056b3a8 52  53   .rodata ascii   cannot allocate memory for thread-local data: ABORT\n
1101 0x0016b3e0 0x0056b3e0 49  50   .rodata ascii   listp->slotinfo[cnt].gen <= GL(dl_tls_generation)
1102 0x0016b418 0x0056b418 31  32   .rodata ascii   map->l_tls_modid == total + cnt
1103 0x0016b438 0x0056b438 49  50   .rodata ascii   map->l_tls_blocksize >= map->l_tls_initimage_size
1104 0x0016b470 0x0056b470 50  51   .rodata ascii   (size_t) map->l_tls_offset >= map->l_tls_blocksize
1105 0x0016b4a8 0x0056b4a8 33  34   .rodata ascii   cannot create TLS data structures
1106 0x0016b4ca 0x0056b4ca 15  16   .rodata ascii   ../elf/dl-tls.c
1107 0x0016b4da 0x0056b4da 13  14   .rodata ascii   listp != NULL
1108 0x0016b4e8 0x0056b4e8 8   9    .rodata ascii   idx == 0
1109 0x0016b4f1 0x0056b4f1 6   7    .rodata ascii   dlopen
1110 0x0016b500 0x0056b500 19  20   .rodata ascii   _dl_add_to_slotinfo
1111 0x0016b520 0x0056b520 21  22   .rodata ascii   _dl_allocate_tls_init
1112 0x0016b540 0x0056b540 18  19   .rodata ascii   _dl_next_tls_modid
1113 0x0016b553 0x0056b553 14  15   .rodata ascii   GLIBC_TUNABLES
1114 0x0016b562 0x0056b562 15  16   .rodata ascii   /etc/suid-debug
1115 0x0016b572 0x0056b572 4   5    .rodata ascii   %s:\n
1116 0x0016b577 0x0056b577 4   5    .rodata ascii   %s: 
1117 0x0016b57c 0x0056b57c 22  23   .rodata ascii   %d (min: %d, max: %d)\n
1118 0x0016b598 0x0056b598 41  42   .rodata ascii   sbrk() failure while processing tunables\n
1119 0x0016b5c8 0x0056b5c8 31  32   .rodata ascii   0x%lx (min: 0x%lx, max: 0x%lx)\n
1120 0x0016b5e8 0x0056b5e8 31  32   .rodata ascii   0x%Zx (min: 0x%Zx, max: 0x%Zx)\n
1121 0x0016b69c 0x0056b69c 8   9    .rodata ascii   /var/tmp
1122 0x0016b6a5 0x0056b6a5 12  13   .rodata ascii   /var/profile
1123 0x0016b6c0 0x0056b6c0 10  11   .rodata ascii   GCONV_PATH
1124 0x0016b6cb 0x0056b6cb 11  12   .rodata ascii   GETCONF_DIR
1125 0x0016b6d7 0x0056b6d7 11  12   .rodata ascii   HOSTALIASES
1126 0x0016b6e3 0x0056b6e3 8   9    .rodata ascii   LD_AUDIT
1127 0x0016b6ec 0x0056b6ec 8   9    .rodata ascii   LD_DEBUG
1128 0x0016b6f5 0x0056b6f5 15  16   .rodata ascii   LD_DEBUG_OUTPUT
1129 0x0016b705 0x0056b705 15  16   .rodata ascii   LD_DYNAMIC_WEAK
1130 0x0016b715 0x0056b715 13  14   .rodata ascii   LD_HWCAP_MASK
1131 0x0016b723 0x0056b723 15  16   .rodata ascii   LD_LIBRARY_PATH
1132 0x0016b733 0x0056b733 14  15   .rodata ascii   LD_ORIGIN_PATH
1133 0x0016b742 0x0056b742 10  11   .rodata ascii   LD_PRELOAD
1134 0x0016b74d 0x0056b74d 10  11   .rodata ascii   LD_PROFILE
1135 0x0016b758 0x0056b758 12  13   .rodata ascii   LD_SHOW_AUXV
1136 0x0016b765 0x0056b765 16  17   .rodata ascii   LD_USE_LOAD_BIAS
1137 0x0016b776 0x0056b776 11  12   .rodata ascii   LOCALDOMAIN
1138 0x0016b782 0x0056b782 7   8    .rodata ascii   LOCPATH
1139 0x0016b78a 0x0056b78a 12  13   .rodata ascii   MALLOC_TRACE
1140 0x0016b797 0x0056b797 8   9    .rodata ascii   NIS_PATH
1141 0x0016b7a0 0x0056b7a0 7   8    .rodata ascii   NLSPATH
1142 0x0016b7a8 0x0056b7a8 16  17   .rodata ascii   RESOLV_HOST_CONF
1143 0x0016b7b9 0x0056b7b9 11  12   .rodata ascii   RES_OPTIONS
1144 0x0016b7c5 0x0056b7c5 6   7    .rodata ascii   TMPDIR
1145 0x0016b7cc 0x0056b7cc 5   6    .rodata ascii   TZDIR
1146 0x0016b7d2 0x0056b7d2 24  25   .rodata ascii   LD_PREFER_MAP_32BIT_EXEC
1147 0x0016b800 0x0056b800 4   5    .rodata ascii   i586
1148 0x0016b809 0x0056b809 4   5    .rodata ascii   i686
1149 0x0016b812 0x0056b812 7   8    .rodata ascii   haswell
1150 0x0016b81b 0x0056b81b 8   9    .rodata ascii   xeon_phi
1151 0x0016b830 0x0056b830 4   5    .rodata ascii   sse2
1152 0x0016b839 0x0056b839 6   7    .rodata ascii   x86_64
1153 0x0016b842 0x0056b842 8   9    .rodata ascii   avx512_1
1154 0x0016b84b 0x0056b84b 7   8    .rodata ascii   LD_WARN
1155 0x0016b853 0x0056b853 12  13   .rodata ascii   setup-vdso.h
1156 0x0016b860 0x0056b860 20  21   .rodata ascii   ph->p_type != PT_TLS
1157 0x0016b875 0x0056b875 18  19   .rodata ascii   get-dynamic-info.h
1158 0x0016b888 0x0056b888 14  15   .rodata ascii   out of memory\n
1159 0x0016b897 0x0056b897 9   10   .rodata ascii   LINUX_2.6
1160 0x0016b8a1 0x0056b8a1 20  21   .rodata ascii   __vdso_clock_gettime
1161 0x0016b8b6 0x0056b8b6 19  20   .rodata ascii   __vdso_gettimeofday
1162 0x0016b8ca 0x0056b8ca 11  12   .rodata ascii   __vdso_time
1163 0x0016b8d6 0x0056b8d6 13  14   .rodata ascii   __vdso_getcpu
1164 0x0016b8e4 0x0056b8e4 19  20   .rodata ascii   __vdso_clock_getres
1165 0x0016b8f8 0x0056b8f8 15  16   .rodata ascii   LD_LIBRARY_PATH
1166 0x0016b908 0x0056b908 11  12   .rodata ascii   LD_BIND_NOW
1167 0x0016b914 0x0056b914 11  12   .rodata ascii   LD_BIND_NOT
1168 0x0016b920 0x0056b920 15  16   .rodata ascii   LD_DYNAMIC_WEAK
1169 0x0016b930 0x0056b930 17  18   .rodata ascii   LD_PROFILE_OUTPUT
1170 0x0016b942 0x0056b942 16  17   .rodata ascii   LD_ASSUME_KERNEL
1171 0x0016b958 0x0056b958 38  39   .rodata ascii   info[DT_PLTREL]->d_un.d_val == DT_RELA
1172 0x0016b980 0x0056b980 51  52   .rodata ascii   info[DT_RELAENT]->d_un.d_val == sizeof (ElfW(Rela))
1173 0x0016b9b8 0x0056b9b8 59  60   .rodata ascii   \nWARNING: Unsupported flag value(s) of 0x%x in DT_FLAGS_1.\n
1174 0x0016b9f8 0x0056b9f8 10  11   .rodata ascii   setup_vdso
1175 0x0016ba10 0x0056ba10 20  21   .rodata ascii   elf_get_dynamic_info
1176 0x0016ba25 0x0056ba25 13  14   .rodata ascii   GLIBC_PRIVATE
1177 0x0016ba33 0x0056ba33 13  14   .rodata ascii   _dl_open_hook
1178 0x0016ba41 0x0056ba41 14  15   .rodata ascii   _dl_open_hook2
1179 0x0016ba68 0x0056ba68 4   5    .rodata ascii   AVX2
1180 0x0016ba6d 0x0056ba6d 4   5    .rodata ascii   BMI1
1181 0x0016ba72 0x0056ba72 4   5    .rodata ascii   BMI2
1182 0x0016ba77 0x0056ba77 4   5    .rodata ascii   CMOV
1183 0x0016ba7c 0x0056ba7c 4   5    .rodata ascii   FMA4
1184 0x0016ba81 0x0056ba81 4   5    .rodata ascii   SSE2
1185 0x0016ba86 0x0056ba86 4   5    .rodata ascii   I586
1186 0x0016ba8b 0x0056ba8b 4   5    .rodata ascii   I686
1187 0x0016ba90 0x0056ba90 5   6    .rodata ascii   LZCNT
1188 0x0016ba96 0x0056ba96 5   6    .rodata ascii   MOVBE
1189 0x0016ba9c 0x0056ba9c 5   6    .rodata ascii   SHSTK
1190 0x0016baa2 0x0056baa2 5   6    .rodata ascii   SSSE3
1191 0x0016baa8 0x0056baa8 6   7    .rodata ascii   POPCNT
1192 0x0016baaf 0x0056baaf 6   7    .rodata ascii   SSE4_1
1193 0x0016bab6 0x0056bab6 6   7    .rodata ascii   XSAVEC
1194 0x0016babd 0x0056babd 7   8    .rodata ascii   AVX512F
1195 0x0016bac5 0x0056bac5 7   8    .rodata ascii   OSXSAVE
1196 0x0016bacd 0x0056bacd 8   9    .rodata ascii   AVX512CD
1197 0x0016bad6 0x0056bad6 8   9    .rodata ascii   AVX512BW
1198 0x0016badf 0x0056badf 8   9    .rodata ascii   AVX512DQ
1199 0x0016bae8 0x0056bae8 8   9    .rodata ascii   AVX512ER
1200 0x0016baf1 0x0056baf1 8   9    .rodata ascii   AVX512PF
1201 0x0016bafa 0x0056bafa 8   9    .rodata ascii   AVX512VL
1202 0x0016bb03 0x0056bb03 11  12   .rodata ascii   Prefer_ERMS
1203 0x0016bb0f 0x0056bb0f 11  12   .rodata ascii   Prefer_FSRM
1204 0x0016bb1b 0x0056bb1b 11  12   .rodata ascii   Slow_SSE4_2
1205 0x0016bb27 0x0056bb27 15  16   .rodata ascii   Fast_Rep_String
1206 0x0016bb37 0x0056bb37 18  19   .rodata ascii   Fast_Copy_Backward
1207 0x0016bb4a 0x0056bb4a 18  19   .rodata ascii   Prefer_AVX2_STRCMP
1208 0x0016bb5d 0x0056bb5d 19  20   .rodata ascii   Fast_Unaligned_Copy
1209 0x0016bb71 0x0056bb71 20  21   .rodata ascii   Prefer_No_VZEROUPPER
1210 0x0016bb86 0x0056bb86 21  22   .rodata ascii   Prefer_MAP_32BIT_EXEC
1211 0x0016bb9c 0x0056bb9c 23  24   .rodata ascii   AVX_Fast_Unaligned_Load
1212 0x0016bbb4 0x0056bbb4 24  25   .rodata ascii   MathVec_Prefer_No_AVX512
1213 0x0016bbcd 0x0056bbcd 26  27   .rodata ascii   Prefer_PMINUB_for_stringop
1214 0x0016bbe8 0x0056bbe8 8   9    .rodata ascii   Slow_BSF
1215 0x0016bbf1 0x0056bbf1 26  27   .rodata ascii   /proc/sys/kernel/osrelease
1216 0x0016bcc8 0x0056bcc8 22  23   .rodata ascii   <program name unknown>
1217 0x0016bcdf 0x0056bcdf 19  20   .rodata ascii   %s: %s: %s%s%s%s%s\n
1218 0x0016bcf3 0x0056bcf3 21  22   .rodata ascii   DYNAMIC LINKER BUG!!!
1219 0x0016bd10 0x0056bd10 36  37   .rodata ascii   error while loading shared libraries
1220 0x0016bd40 0x0056bd40 5   6    .rodata ascii   upper
1221 0x0016bd46 0x0056bd46 5   6    .rodata ascii   lower
1222 0x0016bd4c 0x0056bd4c 5   6    .rodata ascii   alpha
1223 0x0016bd52 0x0056bd52 5   6    .rodata ascii   digit
1224 0x0016bd58 0x0056bd58 6   7    .rodata ascii   xdigit
1225 0x0016bd5f 0x0056bd5f 5   6    .rodata ascii   space
1226 0x0016bd65 0x0056bd65 5   6    .rodata ascii   print
1227 0x0016bd6b 0x0056bd6b 5   6    .rodata ascii   graph
1228 0x0016bd71 0x0056bd71 5   6    .rodata ascii   blank
1229 0x0016bd77 0x0056bd77 5   6    .rodata ascii   cntrl
1230 0x0016bd7d 0x0056bd7d 5   6    .rodata ascii   punct
1231 0x0016bd83 0x0056bd83 5   6    .rodata ascii   alnum
1232 0x0016bd8a 0x0056bd8a 7   8    .rodata ascii   toupper
1233 0x0016bd92 0x0056bd92 7   8    .rodata ascii   tolower
1234 0x0016bdc0 0x0056bdc0 6   28   .rodata utf32le HHHHHI
1235 0x0016be2c 0x0056be2c 26  108  .rodata utf32le                           
1236 0x0016c61c 0x0056c61c 7   32   .rodata utf32le \a\b\t\n\v\f\r
1237 0x0016c680 0x0056c680 95  384  .rodata utf32le  !"#$%&'()*+,-./0123456789:;<=>?@abcdefghijklmnopqrstuvwxyz[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
1238 0x0016cc1c 0x0056cc1c 7   32   .rodata utf32le \a\b\t\n\v\f\r
1239 0x0016cc80 0x0056cc80 95  384  .rodata utf32le  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`ABCDEFGHIJKLMNOPQRSTUVWXYZ{|}~
1240 0x0016d778 0x0056d778 5   24   .rodata utf32le  1/4 
1241 0x0016d794 0x0056d794 5   24   .rodata utf32le  1/2 
1242 0x0016d7b0 0x0056d7b0 5   24   .rodata utf32le  3/4 
1243 0x0016edf8 0x0056edf8 4   20   .rodata utf32le (TM)
1244 0x0016eee4 0x0056eee4 5   24   .rodata utf32le  1/3 
1245 0x0016ef00 0x0056ef00 5   24   .rodata utf32le  2/3 
1246 0x0016ef1c 0x0056ef1c 5   24   .rodata utf32le  1/5 
1247 0x0016ef38 0x0056ef38 5   24   .rodata utf32le  2/5 
1248 0x0016ef54 0x0056ef54 5   24   .rodata utf32le  3/5 
1249 0x0016ef70 0x0056ef70 5   24   .rodata utf32le  4/5 
1250 0x0016ef8c 0x0056ef8c 5   24   .rodata utf32le  1/6 
1251 0x0016efa8 0x0056efa8 5   24   .rodata utf32le  5/6 
1252 0x0016efc4 0x0056efc4 5   24   .rodata utf32le  1/8 
1253 0x0016efe0 0x0056efe0 5   24   .rodata utf32le  3/8 
1254 0x0016effc 0x0056effc 5   24   .rodata utf32le  5/8 
1255 0x0016f018 0x0056f018 5   24   .rodata utf32le  7/8 
1256 0x0016f0b8 0x0056f0b8 4   20   .rodata utf32le VIII
1257 0x0016f1b0 0x0056f1b0 4   20   .rodata utf32le viii
1258 0x0016f69c 0x0056f69c 4   20   .rodata utf32le (10)
1259 0x0016f6b4 0x0056f6b4 4   20   .rodata utf32le (11)
1260 0x0016f6cc 0x0056f6cc 4   20   .rodata utf32le (12)
1261 0x0016f6e4 0x0056f6e4 4   20   .rodata utf32le (13)
1262 0x0016f6fc 0x0056f6fc 4   20   .rodata utf32le (14)
1263 0x0016f714 0x0056f714 4   20   .rodata utf32le (15)
1264 0x0016f72c 0x0056f72c 4   20   .rodata utf32le (16)
1265 0x0016f744 0x0056f744 4   20   .rodata utf32le (17)
1266 0x0016f75c 0x0056f75c 4   20   .rodata utf32le (18)
1267 0x0016f774 0x0056f774 4   20   .rodata utf32le (19)
1268 0x0016f78c 0x0056f78c 4   20   .rodata utf32le (20)
1269 0x0016f858 0x0056f858 4   20   .rodata utf32le (10)
1270 0x0016f870 0x0056f870 4   20   .rodata utf32le (11)
1271 0x0016f888 0x0056f888 4   20   .rodata utf32le (12)
1272 0x0016f8a0 0x0056f8a0 4   20   .rodata utf32le (13)
1273 0x0016f8b8 0x0056f8b8 4   20   .rodata utf32le (14)
1274 0x0016f8d0 0x0056f8d0 4   20   .rodata utf32le (15)
1275 0x0016f8e8 0x0056f8e8 4   20   .rodata utf32le (16)
1276 0x0016f900 0x0056f900 4   20   .rodata utf32le (17)
1277 0x0016f918 0x0056f918 4   20   .rodata utf32le (18)
1278 0x0016f930 0x0056f930 4   20   .rodata utf32le (19)
1279 0x0016f948 0x0056f948 4   20   .rodata utf32le (20)
1280 0x001701d8 0x005701d8 4   20   .rodata utf32le (21)
1281 0x001701f0 0x005701f0 4   20   .rodata utf32le (22)
1282 0x00170208 0x00570208 4   20   .rodata utf32le (23)
1283 0x00170220 0x00570220 4   20   .rodata utf32le (24)
1284 0x00170238 0x00570238 4   20   .rodata utf32le (25)
1285 0x00170250 0x00570250 4   20   .rodata utf32le (26)
1286 0x00170268 0x00570268 4   20   .rodata utf32le (27)
1287 0x00170280 0x00570280 4   20   .rodata utf32le (28)
1288 0x00170298 0x00570298 4   20   .rodata utf32le (29)
1289 0x001702b0 0x005702b0 4   20   .rodata utf32le (30)
1290 0x001702c8 0x005702c8 4   20   .rodata utf32le (31)
1291 0x001702e0 0x005702e0 4   20   .rodata utf32le (32)
1292 0x001702f8 0x005702f8 4   20   .rodata utf32le (33)
1293 0x00170310 0x00570310 4   20   .rodata utf32le (34)
1294 0x00170328 0x00570328 4   20   .rodata utf32le (35)
1295 0x00170340 0x00570340 4   20   .rodata utf32le (36)
1296 0x00170358 0x00570358 4   20   .rodata utf32le (37)
1297 0x00170370 0x00570370 4   20   .rodata utf32le (38)
1298 0x00170388 0x00570388 4   20   .rodata utf32le (39)
1299 0x001703a0 0x005703a0 4   20   .rodata utf32le (40)
1300 0x001703b8 0x005703b8 4   20   .rodata utf32le (41)
1301 0x001703d0 0x005703d0 4   20   .rodata utf32le (42)
1302 0x001703e8 0x005703e8 4   20   .rodata utf32le (43)
1303 0x00170400 0x00570400 4   20   .rodata utf32le (44)
1304 0x00170418 0x00570418 4   20   .rodata utf32le (45)
1305 0x00170430 0x00570430 4   20   .rodata utf32le (46)
1306 0x00170448 0x00570448 4   20   .rodata utf32le (47)
1307 0x00170460 0x00570460 4   20   .rodata utf32le (48)
1308 0x00170478 0x00570478 4   20   .rodata utf32le (49)
1309 0x00170490 0x00570490 4   20   .rodata utf32le (50)
1310 0x001705a4 0x005705a4 4   20   .rodata utf32le kcal
1311 0x0017071c 0x0057071c 4   20   .rodata utf32le mm^2
1312 0x00170734 0x00570734 4   20   .rodata utf32le cm^2
1313 0x00170760 0x00570760 4   20   .rodata utf32le km^2
1314 0x00170778 0x00570778 4   20   .rodata utf32le mm^3
1315 0x00170790 0x00570790 4   20   .rodata utf32le cm^3
1316 0x001707bc 0x005707bc 4   20   .rodata utf32le km^3
1317 0x001707e8 0x005707e8 5   24   .rodata utf32le m/s^2
1318 0x00170864 0x00570864 5   24   .rodata utf32le rad/s
1319 0x00170880 0x00570880 7   32   .rodata utf32le rad/s^2
1320 0x001709a4 0x005709a4 4   20   .rodata utf32le a.m.
1321 0x001709ec 0x005709ec 4   20   .rodata utf32le C/kg
1322 0x00170b24 0x00570b24 4   20   .rodata utf32le p.m.
1323 0x00173324 0x00573324 22  92   .rodata utf32le %,37:>BFJNRVY]aeimquy}
1324 0x00178120 0x00578120 48  196  .rodata utf32le  "$&(*,.02468:<>@BDFHJLNPRTVXZ\^`bdfhjlnprtvxz|~
1325 0x00179b20 0x00579b20 5   6    .rodata ascii   ^[yY]
1326 0x00179b26 0x00579b26 5   6    .rodata ascii   ^[nN]
1327 0x00179b38 0x00579b38 20  21   .rodata ascii   %a %b %e %H:%M:%S %Y
1328 0x00179b55 0x00579b55 23  24   .rodata ascii   %a %b %e %H:%M:%S %Z %Y
1329 0x00179b70 0x00579b70 20  84   .rodata utf32le %a %b %e %H:%M:%S %Y
1330 0x00179bc8 0x00579bc8 23  96   .rodata utf32le %a %b %e %H:%M:%S %Z %Y
1331 0x00179c28 0x00579c28 14  15   .rodata ascii   %p%t%g%t%m%t%f
1332 0x00179c38 0x00579c38 43  44   .rodata ascii   %a%N%f%N%d%N%b%N%s %h %e %r%N%C-%z %T%N%c%N
1333 0x00179c64 0x00579c64 9   10   .rodata ascii   +%c %a %l
1334 0x00179c6e 0x00579c6e 27  28   .rodata ascii   ISO/IEC 14652 i18n FDCC-set
1335 0x00179c8a 0x00579c8a 13  14   .rodata ascii   Keld Simonsen
1336 0x00179c98 0x00579c98 13  14   .rodata ascii   keld@dkuug.dk
1337 0x00179ca6 0x00579ca6 13  14   .rodata ascii   +45 3122-6543
1338 0x00179cb4 0x00579cb4 13  14   .rodata ascii   +45 3325-6543
1339 0x00179cca 0x00579cca 10  11   .rodata ascii   1997-12-20
1340 0x00179cd8 0x00579cd8 45  46   .rodata ascii   ISO/IEC JTC1/SC22/WG20 - internationalization
1341 0x00179d08 0x00579d08 59  60   .rodata ascii   C/o Keld Simonsen, Skt. Jorgens Alle 8, DK-1615 Kobenhavn V
1342 0x00179d48 0x00579d48 9   10   .rodata ascii   i18n:1999
1343 0x00179d52 0x00579d52 9   10   .rodata ascii   i18n:1999
1344 0x00179d5c 0x00579d5c 9   10   .rodata ascii   i18n:1999
1345 0x00179d66 0x00579d66 9   10   .rodata ascii   i18n:1999
1346 0x00179d70 0x00579d70 9   10   .rodata ascii   i18n:1999
1347 0x00179d7a 0x00579d7a 9   10   .rodata ascii   i18n:1999
1348 0x00179d85 0x00579d85 9   10   .rodata ascii   i18n:1999
1349 0x00179d8f 0x00579d8f 9   10   .rodata ascii   i18n:1999
1350 0x00179d99 0x00579d99 9   10   .rodata ascii   i18n:1999
1351 0x00179da3 0x00579da3 9   10   .rodata ascii   i18n:1999
1352 0x00179dad 0x00579dad 9   10   .rodata ascii   i18n:1999
1353 0x00179db7 0x00579db7 9   10   .rodata ascii   i18n:1999
1354 0x00179dc1 0x00579dc1 9   10   .rodata ascii   i18n:1999
1355 0x00179dcb 0x00579dcb 9   10   .rodata ascii   i18n:1999
1356 0x00179dd5 0x00579dd5 9   10   .rodata ascii   i18n:1999
1357 0x00179ddf 0x00579ddf 9   10   .rodata ascii   i18n:1999
1358 0x00179e38 0x00579e38 7   32   .rodata utf32le \a\b\t\n\v\f\r
1359 0x00179e9c 0x00579e9c 95  384  .rodata utf32le  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
1360 0x0017a227 0x0057a227 7   8    .rodata ascii   \a\b\t\n\v\f\r
1361 0x0017a240 0x0057a240 95  96   .rodata ascii    !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
1362 0x0017a320 0x0057a320 4   5    .rodata ascii   libc
1363 0x0017a325 0x0057a325 11  12   .rodata ascii   to_outpunct
1364 0x0017a331 0x0057a331 19  20   .rodata ascii   vfprintf-internal.c
1365 0x0017a345 0x0057a345 5   6    .rodata ascii   (nil)
1366 0x0017a34b 0x0057a34b 6   7    .rodata ascii   (null)
1367 0x0017a358 0x0057a358 33  34   .rodata ascii   (size_t) done <= (size_t) INT_MAX
1368 0x0017a380 0x0057a380 34  35   .rodata ascii   (mode_flags & PRINTF_FORTIFY) != 0
1369 0x0017a3a8 0x0057a3a8 33  34   .rodata ascii   *** invalid %N$ use detected ***\n
1370 0x0017a3d0 0x0057a3d0 40  41   .rodata ascii   *** %n in writable segment detected ***\n
1371 0x0017a400 0x0057a400 14  15   .rodata ascii   outstring_func
1372 0x0017a451 0x0057a451 9   10   .rodata ascii   \b\b\b\b\b\b\b\b\b
1373 0x0017a4a0 0x0057a4a0 17  18   .rodata ascii   printf_positional
1374 0x0017a4b4 0x0057a4b4 5   24   .rodata utf32le (nil)
1375 0x0017a511 0x0057a511 9   10   .rodata ascii   \b\b\b\b\b\b\b\b\b
1376 0x0017a560 0x0057a560 6   28   .rodata utf32le (null)
1377 0x0017a57c 0x0057a57c 7   8    .rodata ascii   Success
1378 0x0017a584 0x0057a584 23  24   .rodata ascii   Operation not permitted
1379 0x0017a59c 0x0057a59c 25  26   .rodata ascii   No such file or directory
1380 0x0017a5b6 0x0057a5b6 15  16   .rodata ascii   No such process
1381 0x0017a5c6 0x0057a5c6 23  24   .rodata ascii   Interrupted system call
1382 0x0017a5de 0x0057a5de 18  19   .rodata ascii   Input/output error
1383 0x0017a5f1 0x0057a5f1 25  26   .rodata ascii   No such device or address
1384 0x0017a60b 0x0057a60b 22  23   .rodata ascii   Argument list too long
1385 0x0017a622 0x0057a622 17  18   .rodata ascii   Exec format error
1386 0x0017a634 0x0057a634 19  20   .rodata ascii   Bad file descriptor
1387 0x0017a648 0x0057a648 18  19   .rodata ascii   No child processes
1388 0x0017a65b 0x0057a65b 22  23   .rodata ascii   Cannot allocate memory
1389 0x0017a672 0x0057a672 17  18   .rodata ascii   Permission denied
1390 0x0017a684 0x0057a684 11  12   .rodata ascii   Bad address
1391 0x0017a690 0x0057a690 21  22   .rodata ascii   Block device required
1392 0x0017a6a6 0x0057a6a6 23  24   .rodata ascii   Device or resource busy
1393 0x0017a6be 0x0057a6be 11  12   .rodata ascii   File exists
1394 0x0017a6ca 0x0057a6ca 25  26   .rodata ascii   Invalid cross-device link
1395 0x0017a6e4 0x0057a6e4 14  15   .rodata ascii   No such device
1396 0x0017a6f3 0x0057a6f3 15  16   .rodata ascii   Not a directory
1397 0x0017a703 0x0057a703 14  15   .rodata ascii   Is a directory
1398 0x0017a712 0x0057a712 16  17   .rodata ascii   Invalid argument
1399 0x0017a723 0x0057a723 29  30   .rodata ascii   Too many open files in system
1400 0x0017a741 0x0057a741 19  20   .rodata ascii   Too many open files
1401 0x0017a755 0x0057a755 14  15   .rodata ascii   Text file busy
1402 0x0017a764 0x0057a764 14  15   .rodata ascii   File too large
1403 0x0017a773 0x0057a773 23  24   .rodata ascii   No space left on device
1404 0x0017a78b 0x0057a78b 12  13   .rodata ascii   Illegal seek
1405 0x0017a798 0x0057a798 21  22   .rodata ascii   Read-only file system
1406 0x0017a7ae 0x0057a7ae 14  15   .rodata ascii   Too many links
1407 0x0017a7bd 0x0057a7bd 11  12   .rodata ascii   Broken pipe
1408 0x0017a7c9 0x0057a7c9 29  30   .rodata ascii   Numerical result out of range
1409 0x0017a7e7 0x0057a7e7 25  26   .rodata ascii   Resource deadlock avoided
1410 0x0017a801 0x0057a801 18  19   .rodata ascii   File name too long
1411 0x0017a814 0x0057a814 18  19   .rodata ascii   No locks available
1412 0x0017a827 0x0057a827 24  25   .rodata ascii   Function not implemented
1413 0x0017a840 0x0057a840 19  20   .rodata ascii   Directory not empty
1414 0x0017a854 0x0057a854 26  27   .rodata ascii   No message of desired type
1415 0x0017a86f 0x0057a86f 18  19   .rodata ascii   Identifier removed
1416 0x0017a882 0x0057a882 27  28   .rodata ascii   Channel number out of range
1417 0x0017a89e 0x0057a89e 24  25   .rodata ascii   Level 2 not synchronized
1418 0x0017a8b7 0x0057a8b7 14  15   .rodata ascii   Level 3 halted
1419 0x0017a8c6 0x0057a8c6 13  14   .rodata ascii   Level 3 reset
1420 0x0017a8d4 0x0057a8d4 24  25   .rodata ascii   Link number out of range
1421 0x0017a8ed 0x0057a8ed 28  29   .rodata ascii   Protocol driver not attached
1422 0x0017a90a 0x0057a90a 26  27   .rodata ascii   No CSI structure available
1423 0x0017a925 0x0057a925 14  15   .rodata ascii   Level 2 halted
1424 0x0017a934 0x0057a934 16  17   .rodata ascii   Invalid exchange
1425 0x0017a945 0x0057a945 26  27   .rodata ascii   Invalid request descriptor
1426 0x0017a960 0x0057a960 13  14   .rodata ascii   Exchange full
1427 0x0017a96e 0x0057a96e 8   9    .rodata ascii   No anode
1428 0x0017a977 0x0057a977 20  21   .rodata ascii   Invalid request code
1429 0x0017a98c 0x0057a98c 12  13   .rodata ascii   Invalid slot
1430 0x0017a999 0x0057a999 20  21   .rodata ascii   Bad font file format
1431 0x0017a9ae 0x0057a9ae 19  20   .rodata ascii   Device not a stream
1432 0x0017a9c2 0x0057a9c2 17  18   .rodata ascii   No data available
1433 0x0017a9d4 0x0057a9d4 13  14   .rodata ascii   Timer expired
1434 0x0017a9e2 0x0057a9e2 24  25   .rodata ascii   Out of streams resources
1435 0x0017a9fb 0x0057a9fb 29  30   .rodata ascii   Machine is not on the network
1436 0x0017aa19 0x0057aa19 21  22   .rodata ascii   Package not installed
1437 0x0017aa2f 0x0057aa2f 16  17   .rodata ascii   Object is remote
1438 0x0017aa40 0x0057aa40 21  22   .rodata ascii   Link has been severed
1439 0x0017aa56 0x0057aa56 15  16   .rodata ascii   Advertise error
1440 0x0017aa66 0x0057aa66 13  14   .rodata ascii   Srmount error
1441 0x0017aa74 0x0057aa74 27  28   .rodata ascii   Communication error on send
1442 0x0017aa90 0x0057aa90 14  15   .rodata ascii   Protocol error
1443 0x0017aa9f 0x0057aa9f 18  19   .rodata ascii   Multihop attempted
1444 0x0017aab2 0x0057aab2 18  19   .rodata ascii   RFS specific error
1445 0x0017aac5 0x0057aac5 11  12   .rodata ascii   Bad message
1446 0x0017aad1 0x0057aad1 26  27   .rodata ascii   Name not unique on network
1447 0x0017aaec 0x0057aaec 28  29   .rodata ascii   File descriptor in bad state
1448 0x0017ab09 0x0057ab09 22  23   .rodata ascii   Remote address changed
1449 0x0017ab20 0x0057ab20 18  19   .rodata ascii   Streams pipe error
1450 0x0017ab33 0x0057ab33 14  15   .rodata ascii   Too many users
1451 0x0017ab42 0x0057ab42 28  29   .rodata ascii   Destination address required
1452 0x0017ab5f 0x0057ab5f 16  17   .rodata ascii   Message too long
1453 0x0017ab70 0x0057ab70 22  23   .rodata ascii   Protocol not available
1454 0x0017ab87 0x0057ab87 22  23   .rodata ascii   Protocol not supported
1455 0x0017ab9e 0x0057ab9e 25  26   .rodata ascii   Socket type not supported
1456 0x0017abb8 0x0057abb8 23  24   .rodata ascii   Operation not supported
1457 0x0017abd0 0x0057abd0 29  30   .rodata ascii   Protocol family not supported
1458 0x0017abee 0x0057abee 22  23   .rodata ascii   Address already in use
1459 0x0017ac05 0x0057ac05 15  16   .rodata ascii   Network is down
1460 0x0017ac15 0x0057ac15 22  23   .rodata ascii   Network is unreachable
1461 0x0017ac2c 0x0057ac2c 24  25   .rodata ascii   Connection reset by peer
1462 0x0017ac45 0x0057ac45 25  26   .rodata ascii   No buffer space available
1463 0x0017ac5f 0x0057ac5f 20  21   .rodata ascii   Connection timed out
1464 0x0017ac74 0x0057ac74 18  19   .rodata ascii   Connection refused
1465 0x0017ac87 0x0057ac87 12  13   .rodata ascii   Host is down
1466 0x0017ac94 0x0057ac94 16  17   .rodata ascii   No route to host
1467 0x0017aca5 0x0057aca5 29  30   .rodata ascii   Operation already in progress
1468 0x0017acc3 0x0057acc3 25  26   .rodata ascii   Operation now in progress
1469 0x0017acdd 0x0057acdd 17  18   .rodata ascii   Stale file handle
1470 0x0017acef 0x0057acef 24  25   .rodata ascii   Structure needs cleaning
1471 0x0017ad08 0x0057ad08 27  28   .rodata ascii   Not a XENIX named type file
1472 0x0017ad24 0x0057ad24 29  30   .rodata ascii   No XENIX semaphores available
1473 0x0017ad42 0x0057ad42 20  21   .rodata ascii   Is a named type file
1474 0x0017ad57 0x0057ad57 16  17   .rodata ascii   Remote I/O error
1475 0x0017ad68 0x0057ad68 19  20   .rodata ascii   Disk quota exceeded
1476 0x0017ad7c 0x0057ad7c 15  16   .rodata ascii   No medium found
1477 0x0017ad8c 0x0057ad8c 17  18   .rodata ascii   Wrong medium type
1478 0x0017ad9e 0x0057ad9e 18  19   .rodata ascii   Operation canceled
1479 0x0017adb1 0x0057adb1 26  27   .rodata ascii   Required key not available
1480 0x0017adcc 0x0057adcc 15  16   .rodata ascii   Key has expired
1481 0x0017addc 0x0057addc 20  21   .rodata ascii   Key has been revoked
1482 0x0017adf1 0x0057adf1 27  28   .rodata ascii   Key was rejected by service
1483 0x0017ae0d 0x0057ae0d 10  11   .rodata ascii   Owner died
1484 0x0017ae18 0x0057ae18 21  22   .rodata ascii   State not recoverable
1485 0x0017ae30 0x0057ae30 32  33   .rodata ascii   Resource temporarily unavailable
1486 0x0017ae58 0x0057ae58 30  31   .rodata ascii   Inappropriate ioctl for device
1487 0x0017ae78 0x0057ae78 32  33   .rodata ascii   Numerical argument out of domain
1488 0x0017aea0 0x0057aea0 33  34   .rodata ascii   Too many levels of symbolic links
1489 0x0017aec8 0x0057aec8 37  38   .rodata ascii   Value too large for defined data type
1490 0x0017aef0 0x0057aef0 38  39   .rodata ascii   Can not access a needed shared library
1491 0x0017af18 0x0057af18 36  37   .rodata ascii   Accessing a corrupted shared library
1492 0x0017af40 0x0057af40 31  32   .rodata ascii   .lib section in a.out corrupted
1493 0x0017af60 0x0057af60 47  48   .rodata ascii   Attempting to link in too many shared libraries
1494 0x0017af90 0x0057af90 37  38   .rodata ascii   Cannot exec a shared library directly
1495 0x0017afb8 0x0057afb8 49  50   .rodata ascii   Invalid or incomplete multibyte or wide character
1496 0x0017aff0 0x0057aff0 43  44   .rodata ascii   Interrupted system call should be restarted
1497 0x0017b020 0x0057b020 30  31   .rodata ascii   Socket operation on non-socket
1498 0x0017b040 0x0057b040 30  31   .rodata ascii   Protocol wrong type for socket
1499 0x0017b060 0x0057b060 40  41   .rodata ascii   Address family not supported by protocol
1500 0x0017b090 0x0057b090 31  32   .rodata ascii   Cannot assign requested address
1501 0x0017b0b0 0x0057b0b0 35  36   .rodata ascii   Network dropped connection on reset
1502 0x0017b0d8 0x0057b0d8 32  33   .rodata ascii   Software caused connection abort
1503 0x0017b100 0x0057b100 39  40   .rodata ascii   Transport endpoint is already connected
1504 0x0017b128 0x0057b128 35  36   .rodata ascii   Transport endpoint is not connected
1505 0x0017b150 0x0057b150 45  46   .rodata ascii   Cannot send after transport endpoint shutdown
1506 0x0017b180 0x0057b180 34  35   .rodata ascii   Too many references: cannot splice
1507 0x0017b1a8 0x0057b1a8 37  38   .rodata ascii   Operation not possible due to RF-kill
1508 0x0017b1d0 0x0057b1d0 30  31   .rodata ascii   Memory page has hardware error
1509 0x0017b202 0x0057b202 5   6    .rodata ascii   EPERM
1510 0x0017b208 0x0057b208 6   7    .rodata ascii   ENOENT
1511 0x0017b20f 0x0057b20f 5   6    .rodata ascii   ESRCH
1512 0x0017b215 0x0057b215 5   6    .rodata ascii   EINTR
1513 0x0017b21f 0x0057b21f 5   6    .rodata ascii   ENXIO
1514 0x0017b225 0x0057b225 5   6    .rodata ascii   E2BIG
1515 0x0017b22b 0x0057b22b 7   8    .rodata ascii   ENOEXEC
1516 0x0017b233 0x0057b233 5   6    .rodata ascii   EBADF
1517 0x0017b239 0x0057b239 6   7    .rodata ascii   ECHILD
1518 0x0017b240 0x0057b240 7   8    .rodata ascii   EDEADLK
1519 0x0017b248 0x0057b248 6   7    .rodata ascii   ENOMEM
1520 0x0017b24f 0x0057b24f 6   7    .rodata ascii   EACCES
1521 0x0017b256 0x0057b256 6   7    .rodata ascii   EFAULT
1522 0x0017b25d 0x0057b25d 7   8    .rodata ascii   ENOTBLK
1523 0x0017b265 0x0057b265 5   6    .rodata ascii   EBUSY
1524 0x0017b26b 0x0057b26b 6   7    .rodata ascii   EEXIST
1525 0x0017b272 0x0057b272 5   6    .rodata ascii   EXDEV
1526 0x0017b278 0x0057b278 6   7    .rodata ascii   ENODEV
1527 0x0017b27f 0x0057b27f 7   8    .rodata ascii   ENOTDIR
1528 0x0017b287 0x0057b287 6   7    .rodata ascii   EISDIR
1529 0x0017b28e 0x0057b28e 6   7    .rodata ascii   EINVAL
1530 0x0017b295 0x0057b295 6   7    .rodata ascii   EMFILE
1531 0x0017b29c 0x0057b29c 6   7    .rodata ascii   ENFILE
1532 0x0017b2a3 0x0057b2a3 6   7    .rodata ascii   ENOTTY
1533 0x0017b2aa 0x0057b2aa 7   8    .rodata ascii   ETXTBSY
1534 0x0017b2b2 0x0057b2b2 5   6    .rodata ascii   EFBIG
1535 0x0017b2b8 0x0057b2b8 6   7    .rodata ascii   ENOSPC
1536 0x0017b2bf 0x0057b2bf 6   7    .rodata ascii   ESPIPE
1537 0x0017b2c6 0x0057b2c6 5   6    .rodata ascii   EROFS
1538 0x0017b2cc 0x0057b2cc 6   7    .rodata ascii   EMLINK
1539 0x0017b2d3 0x0057b2d3 5   6    .rodata ascii   EPIPE
1540 0x0017b2d9 0x0057b2d9 4   5    .rodata ascii   EDOM
1541 0x0017b2de 0x0057b2de 6   7    .rodata ascii   ERANGE
1542 0x0017b2e5 0x0057b2e5 6   7    .rodata ascii   EAGAIN
1543 0x0017b2ec 0x0057b2ec 11  12   .rodata ascii   EINPROGRESS
1544 0x0017b2f8 0x0057b2f8 8   9    .rodata ascii   EALREADY
1545 0x0017b301 0x0057b301 8   9    .rodata ascii   ENOTSOCK
1546 0x0017b30a 0x0057b30a 8   9    .rodata ascii   EMSGSIZE
1547 0x0017b313 0x0057b313 10  11   .rodata ascii   EPROTOTYPE
1548 0x0017b31e 0x0057b31e 11  12   .rodata ascii   ENOPROTOOPT
1549 0x0017b32a 0x0057b32a 15  16   .rodata ascii   EPROTONOSUPPORT
1550 0x0017b33a 0x0057b33a 15  16   .rodata ascii   ESOCKTNOSUPPORT
1551 0x0017b34a 0x0057b34a 10  11   .rodata ascii   EOPNOTSUPP
1552 0x0017b355 0x0057b355 12  13   .rodata ascii   EPFNOSUPPORT
1553 0x0017b362 0x0057b362 12  13   .rodata ascii   EAFNOSUPPORT
1554 0x0017b36f 0x0057b36f 10  11   .rodata ascii   EADDRINUSE
1555 0x0017b37a 0x0057b37a 13  14   .rodata ascii   EADDRNOTAVAIL
1556 0x0017b388 0x0057b388 8   9    .rodata ascii   ENETDOWN
1557 0x0017b391 0x0057b391 11  12   .rodata ascii   ENETUNREACH
1558 0x0017b39d 0x0057b39d 9   10   .rodata ascii   ENETRESET
1559 0x0017b3a7 0x0057b3a7 12  13   .rodata ascii   ECONNABORTED
1560 0x0017b3b4 0x0057b3b4 10  11   .rodata ascii   ECONNRESET
1561 0x0017b3bf 0x0057b3bf 7   8    .rodata ascii   ENOBUFS
1562 0x0017b3c7 0x0057b3c7 7   8    .rodata ascii   EISCONN
1563 0x0017b3cf 0x0057b3cf 8   9    .rodata ascii   ENOTCONN
1564 0x0017b3d8 0x0057b3d8 12  13   .rodata ascii   EDESTADDRREQ
1565 0x0017b3e5 0x0057b3e5 9   10   .rodata ascii   ESHUTDOWN
1566 0x0017b3ef 0x0057b3ef 12  13   .rodata ascii   ETOOMANYREFS
1567 0x0017b3fc 0x0057b3fc 9   10   .rodata ascii   ETIMEDOUT
1568 0x0017b406 0x0057b406 12  13   .rodata ascii   ECONNREFUSED
1569 0x0017b413 0x0057b413 5   6    .rodata ascii   ELOOP
1570 0x0017b419 0x0057b419 12  13   .rodata ascii   ENAMETOOLONG
1571 0x0017b426 0x0057b426 9   10   .rodata ascii   EHOSTDOWN
1572 0x0017b430 0x0057b430 12  13   .rodata ascii   EHOSTUNREACH
1573 0x0017b43d 0x0057b43d 9   10   .rodata ascii   ENOTEMPTY
1574 0x0017b447 0x0057b447 6   7    .rodata ascii   EUSERS
1575 0x0017b44e 0x0057b44e 6   7    .rodata ascii   EDQUOT
1576 0x0017b455 0x0057b455 6   7    .rodata ascii   ESTALE
1577 0x0017b45c 0x0057b45c 7   8    .rodata ascii   EREMOTE
1578 0x0017b464 0x0057b464 6   7    .rodata ascii   ENOLCK
1579 0x0017b46b 0x0057b46b 6   7    .rodata ascii   ENOSYS
1580 0x0017b472 0x0057b472 6   7    .rodata ascii   EILSEQ
1581 0x0017b479 0x0057b479 7   8    .rodata ascii   EBADMSG
1582 0x0017b481 0x0057b481 5   6    .rodata ascii   EIDRM
1583 0x0017b487 0x0057b487 9   10   .rodata ascii   EMULTIHOP
1584 0x0017b491 0x0057b491 7   8    .rodata ascii   ENODATA
1585 0x0017b499 0x0057b499 7   8    .rodata ascii   ENOLINK
1586 0x0017b4a1 0x0057b4a1 6   7    .rodata ascii   ENOMSG
1587 0x0017b4a8 0x0057b4a8 5   6    .rodata ascii   ENOSR
1588 0x0017b4ae 0x0057b4ae 6   7    .rodata ascii   ENOSTR
1589 0x0017b4b5 0x0057b4b5 9   10   .rodata ascii   EOVERFLOW
1590 0x0017b4bf 0x0057b4bf 6   7    .rodata ascii   EPROTO
1591 0x0017b4c6 0x0057b4c6 5   6    .rodata ascii   ETIME
1592 0x0017b4cc 0x0057b4cc 9   10   .rodata ascii   ECANCELED
1593 0x0017b4d6 0x0057b4d6 10  11   .rodata ascii   EOWNERDEAD
1594 0x0017b4e1 0x0057b4e1 15  16   .rodata ascii   ENOTRECOVERABLE
1595 0x0017b4f1 0x0057b4f1 8   9    .rodata ascii   ERESTART
1596 0x0017b4fa 0x0057b4fa 6   7    .rodata ascii   ECHRNG
1597 0x0017b501 0x0057b501 8   9    .rodata ascii   EL2NSYNC
1598 0x0017b50a 0x0057b50a 6   7    .rodata ascii   EL3HLT
1599 0x0017b511 0x0057b511 6   7    .rodata ascii   EL3RST
1600 0x0017b518 0x0057b518 6   7    .rodata ascii   ELNRNG
1601 0x0017b51f 0x0057b51f 7   8    .rodata ascii   EUNATCH
1602 0x0017b527 0x0057b527 6   7    .rodata ascii   ENOCSI
1603 0x0017b52e 0x0057b52e 6   7    .rodata ascii   EL2HLT
1604 0x0017b535 0x0057b535 5   6    .rodata ascii   EBADE
1605 0x0017b53b 0x0057b53b 5   6    .rodata ascii   EBADR
1606 0x0017b541 0x0057b541 6   7    .rodata ascii   EXFULL
1607 0x0017b548 0x0057b548 6   7    .rodata ascii   ENOANO
1608 0x0017b54f 0x0057b54f 7   8    .rodata ascii   EBADRQC
1609 0x0017b557 0x0057b557 7   8    .rodata ascii   EBADSLT
1610 0x0017b55f 0x0057b55f 6   7    .rodata ascii   EBFONT
1611 0x0017b566 0x0057b566 6   7    .rodata ascii   ENONET
1612 0x0017b56d 0x0057b56d 6   7    .rodata ascii   ENOPKG
1613 0x0017b574 0x0057b574 4   5    .rodata ascii   EADV
1614 0x0017b579 0x0057b579 6   7    .rodata ascii   ESRMNT
1615 0x0017b580 0x0057b580 5   6    .rodata ascii   ECOMM
1616 0x0017b586 0x0057b586 7   8    .rodata ascii   EDOTDOT
1617 0x0017b58e 0x0057b58e 8   9    .rodata ascii   ENOTUNIQ
1618 0x0017b597 0x0057b597 6   7    .rodata ascii   EBADFD
1619 0x0017b59e 0x0057b59e 7   8    .rodata ascii   EREMCHG
1620 0x0017b5a6 0x0057b5a6 7   8    .rodata ascii   ELIBACC
1621 0x0017b5ae 0x0057b5ae 7   8    .rodata ascii   ELIBBAD
1622 0x0017b5b6 0x0057b5b6 7   8    .rodata ascii   ELIBSCN
1623 0x0017b5be 0x0057b5be 7   8    .rodata ascii   ELIBMAX
1624 0x0017b5c6 0x0057b5c6 8   9    .rodata ascii   ELIBEXEC
1625 0x0017b5cf 0x0057b5cf 8   9    .rodata ascii   ESTRPIPE
1626 0x0017b5d8 0x0057b5d8 7   8    .rodata ascii   EUCLEAN
1627 0x0017b5e0 0x0057b5e0 7   8    .rodata ascii   ENOTNAM
1628 0x0017b5e8 0x0057b5e8 7   8    .rodata ascii   ENAVAIL
1629 0x0017b5f0 0x0057b5f0 6   7    .rodata ascii   EISNAM
1630 0x0017b5f7 0x0057b5f7 9   10   .rodata ascii   EREMOTEIO
1631 0x0017b601 0x0057b601 9   10   .rodata ascii   ENOMEDIUM
1632 0x0017b60b 0x0057b60b 11  12   .rodata ascii   EMEDIUMTYPE
1633 0x0017b617 0x0057b617 6   7    .rodata ascii   ENOKEY
1634 0x0017b61e 0x0057b61e 11  12   .rodata ascii   EKEYEXPIRED
1635 0x0017b62a 0x0057b62a 11  12   .rodata ascii   EKEYREVOKED
1636 0x0017b636 0x0057b636 12  13   .rodata ascii   EKEYREJECTED
1637 0x0017b643 0x0057b643 7   8    .rodata ascii   ERFKILL
1638 0x0017b64b 0x0057b64b 9   10   .rodata ascii   EHWPOISON
1639 0x0017b66e 0x0057b66e 4   9    .rodata utf16le %+39
1640 0x0017b678 0x0057b678 8   18   .rodata utf16le HOV]ekrx
1641 0x0017bc00 0x0057bc00 16  17   .rodata ascii   0000000000000000
1642 0x0017bc20 0x0057bc20 16  17   .rodata ascii                   
1643 0x0017bc40 0x0057bc40 32  132  .rodata utf32le 0000000000000000                
1644 0x0017bcc4 0x0057bcc4 9   10   .rodata ascii   of memory
1645 0x0017bcce 0x0057bcce 10  11   .rodata ascii   %s%s%s: %s
1646 0x0017bcd9 0x0057bcd9 11  12   .rodata ascii   _dlfcn_hook
1647 0x0017bce5 0x0057bce5 26  27   .rodata ascii   unsupported dlinfo request
1648 0x0017bd2c 0x0057bd2c 17  18   .rodata ascii   invalid namespace
1649 0x0017bec8 0x0057bec8 11  12   .rodata ascii   wcsrtombs.c
1650 0x0017bed4 0x0057bed4 25  26   .rodata ascii   data.__outbuf[-1] == '\0'
1651 0x0017bef0 0x0057bef0 11  12   .rodata ascii   __wcsrtombs
1652 0x0017bf34 0x0057bf34 17  18   .rodata ascii   %hu%n:%hu%n:%hu%n
1653 0x0017bf46 0x0057bf46 14  15   .rodata ascii   M%hu.%hu.%hu%n
1654 0x0017bf55 0x0057bf55 9   10   .rodata ascii   Universal
1655 0x0017bf66 0x0057bf66 14  15   .rodata ascii   /etc/localtime
1656 0x0017bf75 0x0057bf75 5   6    .rodata ascii   TZDIR
1657 0x0017bf7b 0x0057bf7b 8   9    .rodata ascii   tzfile.c
1658 0x0017bf84 0x0057bf84 14  15   .rodata ascii   tzspec_len > 0
1659 0x0017bf93 0x0057bf93 14  15   .rodata ascii   num_types == 1
1660 0x0017bfa2 0x0057bfa2 10  11   .rodata ascii   posixrules
1661 0x0017bfad 0x0057bfad 14  15   .rodata ascii   num_types == 2
1662 0x0017bfc0 0x0057bfc0 60  61   .rodata ascii   strcmp (&zone_names[info->idx], __tzname[tp->tm_isdst]) == 0
1663 0x0017c000 0x0057c000 13  14   .rodata ascii   __tzfile_read
1664 0x0017c010 0x0057c010 16  17   .rodata ascii   __tzfile_compute
1665 0x0017c030 0x0057c030 19  20   .rodata ascii   /usr/share/zoneinfo
1666 0x0017c044 0x0057c044 15  16   .rodata ascii   /proc/self/maps
1667 0x0017c054 0x0057c054 14  15   .rodata ascii   file too short
1668 0x0017c063 0x0057c063 21  22   .rodata ascii   cannot read file data
1669 0x0017c079 0x0057c079 23  24   .rodata ascii   ELF file OS ABI invalid
1670 0x0017c091 0x0057c091 28  29   .rodata ascii   ELF file ABI version invalid
1671 0x0017c0ae 0x0057c0ae 26  27   .rodata ascii   nonzero padding in e_ident
1672 0x0017c0c9 0x0057c0c9 18  19   .rodata ascii   invalid ELF header
1673 0x0017c0dc 0x0057c0dc 14  15   .rodata ascii   internal error
1674 0x0017c0ef 0x0057c0ef 14  15   .rodata ascii   <main program>
1675 0x0017c0fe 0x0057c0fe 13  14   .rodata ascii    search path=
1676 0x0017c10c 0x0057c10c 20  21   .rodata ascii   \t\t(%s from file %s)\n
1677 0x0017c121 0x0057c121 7   8    .rodata ascii   \t\t(%s)\n
1678 0x0017c129 0x0057c129 17  18   .rodata ascii     trying file=%s\n
1679 0x0017c13b 0x0057c13b 27  28   .rodata ascii   cannot allocate name record
1680 0x0017c157 0x0057c157 9   10   .rodata ascii   dl-load.c
1681 0x0017c161 0x0057c161 13  14   .rodata ascii   lastp != NULL
1682 0x0017c16f 0x0057c16f 6   7    .rodata ascii   ORIGIN
1683 0x0017c176 0x0057c176 8   9    .rodata ascii   PLATFORM
1684 0x0017c183 0x0057c183 20  21   .rodata ascii   lib/x86_64-linux-gnu
1685 0x0017c198 0x0057c198 18  19   .rodata ascii   system search path
1686 0x0017c1ab 0x0057c1ab 22  23   .rodata ascii   l->l_type != lt_loaded
1687 0x0017c1c2 0x0057c1c2 7   8    .rodata ascii   RUNPATH
1688 0x0017c1ca 0x0057c1ca 5   6    .rodata ascii   RPATH
1689 0x0017c1d3 0x0057c1d3 25  26   .rodata ascii   cannot stat shared object
1690 0x0017c1ed 0x0057c1ed 26  27   .rodata ascii   cannot map zero-fill pages
1691 0x0017c208 0x0057c208 28  29   .rodata ascii   cannot close file descriptor
1692 0x0017c225 0x0057c225 18  19   .rodata ascii   nsid == LM_ID_BASE
1693 0x0017c238 0x0057c238 20  21   .rodata ascii   r->r_state == RT_ADD
1694 0x0017c24d 0x0057c24d 9   10   .rodata ascii   libc.so.6
1695 0x0017c257 0x0057c257 9   10   .rodata ascii   nsid >= 0
1696 0x0017c261 0x0057c261 17  18   .rodata ascii   nsid < GL(dl_nns)
1697 0x0017c273 0x0057c273 27  28   .rodata ascii   wrong ELF class: ELFCLASS32
1698 0x0017c290 0x0057c290 37  38   .rodata ascii   only ET_DYN and ET_EXEC can be loaded
1699 0x0017c2b8 0x0057c2b8 43  44   .rodata ascii   ELF file version does not match current one
1700 0x0017c2e8 0x0057c2e8 49  50   .rodata ascii   ELF file version ident does not match current one
1701 0x0017c320 0x0057c320 40  41   .rodata ascii   ELF file data encoding not little-endian
1702 0x0017c350 0x0057c350 42  43   .rodata ascii   ELF file's phentsize not the expected size
1703 0x0017c380 0x0057c380 37  38   .rodata ascii   (l)->l_name[0] == '\0' || IS_RTLD (l)
1704 0x0017c3a8 0x0057c3a8 35  36   .rodata ascii   cannot create cache for search path
1705 0x0017c3d0 0x0057c3d0 32  33   .rodata ascii   cannot create RUNPATH/RPATH copy
1706 0x0017c3f8 0x0057c3f8 31  32   .rodata ascii   cannot create search path array
1707 0x0017c418 0x0057c418 38  39   .rodata ascii   cannot create shared object descriptor
1708 0x0017c440 0x0057c440 43  44   .rodata ascii   ELF load command alignment not page-aligned
1709 0x0017c470 0x0057c470 36  37   .rodata ascii   object file has no loadable segments
1710 0x0017c498 0x0057c498 52  53   .rodata ascii   ELF load command address/offset not properly aligned
1711 0x0017c4d0 0x0057c4d0 34  35   .rodata ascii   cannot dynamically load executable
1712 0x0017c4f8 0x0057c4f8 34  35   .rodata ascii   shared object cannot be dlopen()ed
1713 0x0017c520 0x0057c520 34  35   .rodata ascii   object file has no dynamic section
1714 0x0017c548 0x0057c548 55  56   .rodata ascii   cannot dynamically load position-independent executable
1715 0x0017c580 0x0057c580 56  57   .rodata ascii   cannot enable executable stack as shared object requires
1716 0x0017c5c0 0x0057c5c0 40  41   .rodata ascii   failed to map segment from shared object
1717 0x0017c5f0 0x0057c5f0 32  33   .rodata ascii   cannot change memory protections
1718 0x0017c618 0x0057c618 41  42   .rodata ascii   cannot allocate memory for program header
1719 0x0017c648 0x0057c648 36  37   .rodata ascii   file=%s [%lu];  generating link map\n
1720 0x0017c670 0x0057c670 52  53   .rodata ascii   false && "TLS not initialized in static application"
1721 0x0017c6a8 0x0057c6a8 45  46   .rodata ascii   type != ET_EXEC || l->l_type == lt_executable
1722 0x0017c6d8 0x0057c6d8 99  100  .rodata ascii     dynamic: 0x%0*lx  base: 0x%0*lx   size: 0x%0*Zx\n    entry: 0x%0*lx  phdr: 0x%0*lx  phnum:   %*u\n\n
1723 0x0017c740 0x0057c740 36  37   .rodata ascii   \nfile=%s [%lu];  needed by %s [%lu]\n
1724 0x0017c768 0x0057c768 48  49   .rodata ascii   \nfile=%s [%lu];  dynamically loaded by %s [%lu]\n
1725 0x0017c7a0 0x0057c7a0 33  34   .rodata ascii   find library=%s [%lu]; searching\n
1726 0x0017c7c8 0x0057c7c8 30  31   .rodata ascii   cannot open shared object file
1727 0x0017c7e8 0x0057c7e8 14  15   .rodata ascii   _dl_map_object
1728 0x0017c7f8 0x0057c7f8 14  15   .rodata ascii   _dl_init_paths
1729 0x0017c810 0x0057c810 22  23   .rodata ascii   _dl_map_object_from_fd
1730 0x0017c830 0x0057c830 18  19   .rodata ascii   add_name_to_object
1731 0x0017c850 0x0057c850 27  28   .rodata ascii   expand_dynamic_string_token
1732 0x0017c8c0 0x0057c8c0 22  23   .rodata ascii   /lib/x86_64-linux-gnu/
1733 0x0017c8d7 0x0057c8d7 26  27   .rodata ascii   /usr/lib/x86_64-linux-gnu/
1734 0x0017c8f2 0x0057c8f2 5   6    .rodata ascii   /lib/
1735 0x0017c8f8 0x0057c8f8 9   10   .rodata ascii   /usr/lib/
1736 0x0017c908 0x0057c908 11  12   .rodata ascii   dl-lookup.c
1737 0x0017c914 0x0057c914 10  11   .rodata ascii   , version 
1738 0x0017c91f 0x0057c91f 9   10   .rodata ascii   protected
1739 0x0017c929 0x0057c929 6   7    .rodata ascii   normal
1740 0x0017c930 0x0057c930 24  25   .rodata ascii   undefined symbol: %s%s%s
1741 0x0017c949 0x0057c949 19  20   .rodata ascii   symbol lookup error
1742 0x0017c95d 0x0057c95d 6   7    .rodata ascii    [%s]\n
1743 0x0017c968 0x0057c968 72  73   .rodata ascii   version->filename == NULL || ! _dl_name_match_p (version->filename, map)
1744 0x0017c9b8 0x0057c9b8 36  37   .rodata ascii   symbol=%s;  lookup in file=%s [%lu]\n
1745 0x0017c9e0 0x0057c9e0 50  51   .rodata ascii   marking %s [%lu] as NODELETE due to unique symbol\n
1746 0x0017ca18 0x0057ca18 53  54   .rodata ascii   version == NULL || !(flags & DL_LOOKUP_RETURN_NEWEST)
1747 0x0017ca50 0x0057ca50 62  63   .rodata ascii   marking %s [%lu] as NODELETE due to reference to main program\n
1748 0x0017ca90 0x0057ca90 58  59   .rodata ascii   marking %s [%lu] as NODELETE due to reference to %s [%lu]\n
1749 0x0017cad0 0x0057cad0 61  62   .rodata ascii   \nfile=%s [%lu];  needed by %s [%lu] (relocation dependency)\n\n
1750 0x0017cb10 0x0057cb10 49  50   .rodata ascii   binding file %s [%lu] to %s [%lu]: %s symbol `%s'
1751 0x0017cb48 0x0057cb48 62  63   .rodata ascii   marking %s [%lu] as NODELETE due to memory allocation failure\n
1752 0x0017cb88 0x0057cb88 44  45   .rodata ascii   (bitmask_nwords & (bitmask_nwords - 1)) == 0
1753 0x0017cbb8 0x0057cbb8 14  15   .rodata ascii   _dl_setup_hash
1754 0x0017cbc8 0x0057cbc8 11  12   .rodata ascii   check_match
1755 0x0017cbe0 0x0057cbe0 19  20   .rodata ascii   _dl_lookup_symbol_x
1756 0x0017cbf8 0x0057cbf8 42  43   .rodata ascii   cannot allocate memory in static TLS block
1757 0x0017cc28 0x0057cc28 43  44   .rodata ascii   cannot make segment writable for relocation
1758 0x0017cc58 0x0057cc58 39  40   .rodata ascii   cannot restore segment prot after reloc
1759 0x0017cc80 0x0057cc80 58  59   .rodata ascii   %s: Symbol `%s' causes overflow in R_X86_64_32 relocation\n
1760 0x0017ccc0 0x0057ccc0 60  61   .rodata ascii   %s: Symbol `%s' causes overflow in R_X86_64_PC32 relocation\n
1761 0x0017cd00 0x0057cd00 73  74   .rodata ascii   %s: Symbol `%s' has different size in shared object, consider re-linking\n
1762 0x0017cd50 0x0057cd50 30  31   .rodata ascii   ../sysdeps/x86_64/dl-machine.h
1763 0x0017cd70 0x0057cd70 49  50   .rodata ascii   ELFW(R_TYPE) (reloc->r_info) == R_X86_64_RELATIVE
1764 0x0017cda8 0x0057cda8 120 121  .rodata ascii   %s: IFUNC symbol '%s' referenced in '%s' is defined in the executable and creates an unsatisfiable circular dependency.\n
1765 0x0017ce28 0x0057ce28 48  49   .rodata ascii   %s: Relink `%s' with `%s' for IFUNC symbol `%s'\n
1766 0x0017ce60 0x0057ce60 53  54   .rodata ascii   %s: out of memory to store relocation results for %s\n
1767 0x0017ce96 0x0057ce96 7   8    .rodata ascii    (lazy)
1768 0x0017ce9e 0x0057ce9e 29  30   .rodata ascii   \nrelocation processing: %s%s\n
1769 0x0017d000 0x0057d000 24  25   .rodata ascii   unexpected reloc type 0x
1770 0x0017d026 0x0057d026 28  29   .rodata ascii   unexpected PLT reloc type 0x
1771 0x0017d060 0x0057d060 58  59   .rodata ascii   cannot apply additional memory protection after relocation
1772 0x0017d0a0 0x0057d0a0 25  26   .rodata ascii   elf_machine_rela_relative
1773 0x0017d0ba 0x0057d0ba 9   10   .rodata ascii   dl-misc.c
1774 0x0017d0c4 0x0057d0c4 14  15   .rodata ascii   niov < NIOVMAX
1775 0x0017d0d3 0x0057d0d3 28  29   .rodata ascii   ! "invalid format specifier"
1776 0x0017d0f0 0x0057d0f0 31  32   .rodata ascii   pid >= 0 && sizeof (pid_t) <= 4
1777 0x0017d1a0 0x0057d1a0 18  19   .rodata ascii   _dl_debug_vdprintf
1778 0x0017d1b3 0x0057d1b3 25  26   .rodata ascii   %s: cannot open file: %s\n
1779 0x0017d1cd 0x0057d1cd 25  26   .rodata ascii   %s: cannot stat file: %s\n
1780 0x0017d1e7 0x0057d1e7 27  28   .rodata ascii   %s: cannot create file: %s\n
1781 0x0017d203 0x0057d203 24  25   .rodata ascii   %s: cannot map file: %s\n
1782 0x0017d220 0x0057d220 50  51   .rodata ascii   %s: file is no correct profile data file for `%s'\n
1783 0x0017d258 0x0057d258 42  43   .rodata ascii   Out of memory while initializing profiler\n
1784 0x0017d283 0x0057d283 14  15   .rodata ascii   /proc/self/exe
1785 0x0017d292 0x0057d292 17  18   .rodata ascii   linkval[0] == '/'
1786 0x0017d2a8 0x0057d2a8 38  39   .rodata ascii   ../sysdeps/unix/sysv/linux/dl-origin.c
1787 0x0017d2d0 0x0057d2d0 14  15   .rodata ascii   _dl_get_origin
1788 0x0017d2df 0x0057d2df 9   10   .rodata ascii   dl-open.c
1789 0x0017d2e9 0x0057d2e9 26  27   .rodata ascii   cannot extend global scope
1790 0x0017d304 0x0057d304 13  14   .rodata ascii   ns == l->l_ns
1791 0x0017d312 0x0057d312 25  26   .rodata ascii   invalid mode for dlopen()
1792 0x0017d32c 0x0057d32c 16  17   .rodata ascii   object=%s [%lu]\n
1793 0x0017d33d 0x0057d33d 10  11   .rodata ascii    scope %u:
1794 0x0017d348 0x0057d348 10  11   .rodata ascii    no scope\n
1795 0x0017d353 0x0057d353 18  19   .rodata ascii   mode & RTLD_NOLOAD
1796 0x0017d366 0x0057d366 24  25   .rodata ascii   cannot create scope list
1797 0x0017d37f 0x0057d37f 27  28   .rodata ascii   cnt + 1 < imap->l_scope_max
1798 0x0017d39b 0x0057d39b 26  27   .rodata ascii   imap->l_need_tls_init == 0
1799 0x0017d3b6 0x0057d3b6 29  30   .rodata ascii   marking %s [%lu] as NODELETE\n
1800 0x0017d3d8 0x0057d3d8 38  39   .rodata ascii   new_nlist < ns->_ns_global_scope_alloc
1801 0x0017d400 0x0057d400 30  31   .rodata ascii   \nadd %s [%lu] to global scope\n
1802 0x0017d420 0x0057d420 42  43   .rodata ascii   added <= ns->_ns_global_scope_pending_adds
1803 0x0017d450 0x0057d450 42  43   .rodata ascii   no more namespaces available for dlmopen()
1804 0x0017d480 0x0057d480 37  38   .rodata ascii   invalid target namespace in dlmopen()
1805 0x0017d4a8 0x0057d4a8 61  62   .rodata ascii   _dl_debug_initialize (0, args.nsid)->r_state == RT_CONSISTENT
1806 0x0017d4e8 0x0057d4e8 44  45   .rodata ascii   opening file=%s [%lu]; direct_opencount=%u\n\n
1807 0x0017d518 0x0057d518 62  63   .rodata ascii   _dl_debug_initialize (0, args->nsid)->r_state == RT_CONSISTENT
1808 0x0017d558 0x0057d558 36  37   .rodata ascii   CPU ISA level is lower than required
1809 0x0017d580 0x0057d580 33  34   .rodata ascii   activating NODELETE for %s [%lu]\n
1810 0x0017d5a8 0x0057d5a8 52  53   .rodata ascii   TLS generation counter wrapped!  Please report this.
1811 0x0017d5e0 0x0057d5e0 13  14   .rodata ascii   update_scopes
1812 0x0017d5f0 0x0057d5f0 14  15   .rodata ascii   dl_open_worker
1813 0x0017d600 0x0057d600 8   9    .rodata ascii   _dl_open
1814 0x0017d610 0x0057d610 20  21   .rodata ascii   add_to_global_update
1815 0x0017d630 0x0057d630 19  20   .rodata ascii   update_tls_slotinfo
1816 0x0017d650 0x0057d650 23  24   .rodata ascii   _dl_find_dso_for_object
1817 0x0017d668 0x0057d668 10  11   .rodata ascii   dl-close.c
1818 0x0017d673 0x0057d673 17  18   .rodata ascii   ! should_be_there
1819 0x0017d685 0x0057d685 27  28   .rodata ascii   old_map->l_tls_modid == idx
1820 0x0017d6a1 0x0057d6a1 14  15   .rodata ascii   idx == nloaded
1821 0x0017d6b0 0x0057d6b0 18  19   .rodata ascii   imap->l_ns == nsid
1822 0x0017d6c3 0x0057d6c3 25  26   .rodata ascii   \ncalling fini: %s [%lu]\n\n
1823 0x0017d6dd 0x0057d6dd 18  19   .rodata ascii   tmap->l_ns == nsid
1824 0x0017d6f0 0x0057d6f0 7   8    .rodata ascii   dlclose
1825 0x0017d6f8 0x0057d6f8 25  26   .rodata ascii   imap->l_type == lt_loaded
1826 0x0017d712 0x0057d712 20  21   .rodata ascii   imap->l_prev != NULL
1827 0x0017d727 0x0057d727 22  23   .rodata ascii   shared object not open
1828 0x0017d740 0x0057d740 38  39   .rodata ascii   \nclosing file=%s; direct_opencount=%u\n
1829 0x0017d768 0x0057d768 43  44   .rodata ascii   (*lp)->l_idx >= 0 && (*lp)->l_idx < nloaded
1830 0x0017d798 0x0057d798 41  42   .rodata ascii   jmap->l_idx >= 0 && jmap->l_idx < nloaded
1831 0x0017d7c8 0x0057d7c8 53  54   .rodata ascii   imap->l_type == lt_loaded && !imap->l_nodelete_active
1832 0x0017d800 0x0057d800 37  38   .rodata ascii   \nfile=%s [%lu];  destroying link map\n
1833 0x0017d828 0x0057d828 94  95   .rodata ascii   TLS generation counter wrapped!  Please report as described in <http://www.debian.org/Bugs/>.\n
1834 0x0017d890 0x0057d890 15  16   .rodata ascii   remove_slotinfo
1835 0x0017d8a0 0x0057d8a0 16  17   .rodata ascii   _dl_close_worker
1836 0x0017d8b8 0x0057d8b8 62  63   .rodata ascii   Fatal error: length accounting in _dl_exception_create_format\n
1837 0x0017d8f8 0x0057d8f8 48  49   .rodata ascii   Fatal error: invalid format in exception string\n
1838 0x0017d930 0x0057d930 13  14   .rodata ascii   out of memory
1839 0x0017d93e 0x0057d93e 17  18   .rodata ascii   __libc_early_init
1840 0x0017d950 0x0057d950 25  26   .rodata ascii   dl-call-libc-early-init.c
1841 0x0017d96a 0x0057d96a 11  12   .rodata ascii   sym != NULL
1842 0x0017d980 0x0057d980 24  25   .rodata ascii   _dl_call_libc_early_init
1843 0x0017d999 0x0057d999 16  17   .rodata ascii   /etc/ld.so.cache
1844 0x0017d9aa 0x0057d9aa 17  18   .rodata ascii    search cache=%s\n
1845 0x0017d9bc 0x0057d9bc 20  21   .rodata ascii   glibc-ld.so.cache1.1
1846 0x0017d9d1 0x0057d9d1 11  12   .rodata ascii   ld.so-1.7.0
1847 0x0017d9dd 0x0057d9dd 10  11   .rodata ascii   dl-cache.c
1848 0x0017d9e8 0x0057d9e8 13  14   .rodata ascii   cache != NULL
1849 0x0017da00 0x0057da00 21  22   .rodata ascii   _dl_load_cache_lookup
1850 0x0017da20 0x0057da20 36  37   .rodata ascii   0123456789abcdefghijklmnopqrstuvwxyz
1851 0x0017da60 0x0057da60 36  37   .rodata ascii   0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
1852 0x0017daa0 0x0057daa0 36  148  .rodata utf32le 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
1853 0x0017db40 0x0057db40 36  148  .rodata utf32le 0123456789abcdefghijklmnopqrstuvwxyz
1854 0x0017dc18 0x0057dc18 6   28   .rodata utf32le 0.0001
1855 0x0017dc70 0x0057dc70 30  31   .rodata ascii   ../stdio-common/printf_fphex.c
1856 0x0017dc90 0x0057dc90 38  39   .rodata ascii   *decimal != '\0' && decimalwc != L'\0'
1857 0x0017dcb8 0x0057dcb8 14  15   .rodata ascii   __printf_fphex
1858 0x0017dcc7 0x0057dcc7 10  11   .rodata ascii   to_inpunct
1859 0x0017dcd2 0x0057dcd2 18  19   .rodata ascii   vfscanf-internal.c
1860 0x0017dce5 0x0057dce5 16  17   .rodata ascii   cnt < MB_LEN_MAX
1861 0x0017e110 0x0057e110 18  19   .rodata ascii   __vfscanf_internal
1862 0x0017e123 0x0057e123 22  23   .rodata ascii   invalid mode parameter
1863 0x0017e140 0x0057e140 57  58   .rodata ascii   Fatal glibc error: invalid allocation buffer of size %zu\n
1864 0x0017e17a 0x0057e17a 9   10   .rodata ascii   dl-deps.c
1865 0x0017e184 0x0057e184 12  13   .rodata ascii   cnt <= nlist
1866 0x0017e191 0x0057e191 17  18   .rodata ascii   map_index < nlist
1867 0x0017e1a8 0x0057e1a8 33  34   .rodata ascii   cannot allocate dependency buffer
1868 0x0017e1d0 0x0057e1d0 37  38   .rodata ascii   DST not allowed in SUID/SGID programs
1869 0x0017e1f8 0x0057e1f8 78  79   .rodata ascii   cannot load auxiliary `%s' because of empty dynamic string token substitution\n
1870 0x0017e248 0x0057e248 39  40   .rodata ascii   empty dynamic string token substitution
1871 0x0017e270 0x0057e270 46  47   .rodata ascii   load auxiliary object=%s requested by file=%s\n
1872 0x0017e2a0 0x0057e2a0 31  32   .rodata ascii   cannot allocate dependency list
1873 0x0017e2c0 0x0057e2c0 32  33   .rodata ascii   map->l_searchlist.r_list == NULL
1874 0x0017e2e8 0x0057e2e8 34  35   .rodata ascii   cannot allocate symbol search list
1875 0x0017e310 0x0057e310 46  47   .rodata ascii   Filters not supported with LD_TRACE_PRELINKING
1876 0x0017e340 0x0057e340 19  20   .rodata ascii   _dl_map_object_deps
1877 0x0017e354 0x0057e354 12  13   .rodata ascii   dl-runtime.c
1878 0x0017e368 0x0057e368 51  52   .rodata ascii   ELFW(R_TYPE)(reloc->r_info) == ELF_MACHINE_JMP_SLOT
1879 0x0017e3a0 0x0057e3a0 9   10   .rodata ascii   _dl_fixup
1880 0x0017e3b0 0x0057e3b0 17  18   .rodata ascii   _dl_profile_fixup
1881 0x0017e3c2 0x0057e3c2 19  20   .rodata ascii   \ncalling init: %s\n\n
1882 0x0017e3d6 0x0057e3d6 9   10   .rodata ascii   dl-init.c
1883 0x0017e3e0 0x0057e3e0 22  23   .rodata ascii   \ncalling preinit: %s\n\n
1884 0x0017e3f8 0x0057e3f8 60  61   .rodata ascii   l->l_real->l_relocated || l->l_real->l_type == lt_executable
1885 0x0017e438 0x0057e438 9   10   .rodata ascii   call_init
1886 0x0017e442 0x0057e442 12  13   .rodata ascii   dl-version.c
1887 0x0017e44f 0x0057e44f 14  15   .rodata ascii   needed != NULL
1888 0x0017e45e 0x0057e45e 15  16   .rodata ascii   def_offset != 0
1889 0x0017e46e 0x0057e46e 20  21   .rodata ascii   version lookup error
1890 0x0017e488 0x0057e488 40  41   .rodata ascii   unsupported version %s of Verneed record
1891 0x0017e4b8 0x0057e4b8 69  70   .rodata ascii   checking for version `%s' in file %s [%lu] required by file %s [%lu]\n
1892 0x0017e500 0x0057e500 49  50   .rodata ascii   no version information available (required by %s)
1893 0x0017e538 0x0057e538 39  40   .rodata ascii   unsupported version %s of Verdef record
1894 0x0017e560 0x0057e560 44  45   .rodata ascii   weak version `%s' not found (required by %s)
1895 0x0017e590 0x0057e590 39  40   .rodata ascii   version `%s' not found (required by %s)
1896 0x0017e5b8 0x0057e5b8 39  40   .rodata ascii   cannot allocate version reference table
1897 0x0017e5e0 0x0057e5e0 12  13   .rodata ascii   match_symbol
1898 0x0017e5f0 0x0057e5f0 22  23   .rodata ascii   _dl_check_map_versions
1899 0x0017e608 0x0057e608 45  46   .rodata ascii   RTLD_NEXT used in code not dynamically loaded
1900 0x0017e636 0x0057e636 26  27   .rodata ascii   numsize < RETURN_LIMB_SIZE
1901 0x0017e6a0 0x0057e6a0 24  25   .rodata ascii   ____strtof128_l_internal

[0x00404460]> 

```

0    0x0015c008 0x0055c008 32  33   .rodata ascii   e6722920bab2326f8217e4bf6b1b58ac
1    0x0015c030 0x0055c030 32  33   .rodata ascii   dd2921cc76ee3abfd2beb60709056cfb
2    0x0015c058 0x0055c058 36  37   .rodata ascii   Welcome to Valley Inc. Authenticator
3    0x0015c07d 0x0055c07d 23  24   .rodata ascii   What is your username: 
4    0x0015c095 0x0055c095 23  24   .rodata ascii   What is your password: 
5    0x0015c0ad 0x0055c0ad 13  14   .rodata ascii   Authenticated
6    0x0015c0bb 0x0055c0bb 26  27   .rodata ascii   Wrong Password or Username

Looking good

![[Images/Pasted image 20240517183317.png|800]]
![[Images/Pasted image 20240517183209.png|800]]

valley is one of the users!

user: valley
pass: liberty123
