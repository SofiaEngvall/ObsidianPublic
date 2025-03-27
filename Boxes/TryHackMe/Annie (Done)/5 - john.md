
```sh
┌──(kali㉿kali)-[~/thm/annie]
└─$ ssh annie@10.10.245.157 -i ./id_rsa
The authenticity of host '10.10.245.157 (10.10.245.157)' can´t be established.
ED25519 key fingerprint is SHA256:psjvqDXPWOqLQKlK8kRzSuqVtvSrfysL/TwPGnhb2Jw.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:59: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.245.157' (ED25519) to the list of known hosts.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0664 for './id_rsa' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "./id_rsa": bad permissions
annie@10.10.245.157: Permission denied (publickey).
                                                                                    
┌──(kali㉿kali)-[~/thm/annie]
└─$ ssh2john id_rsa > sshpass      
                                                                                    
┌──(kali㉿kali)-[~/thm/annie]
└─$ cat sshpass                 
id_rsa:$sshng$6$16$fdad97937c78a386cf869ac387c59151$1894$6f70656e7373682d6b65792d7631000000000a6165733235362d637472000000066263727970740000001800000010fdad97937c78a386cf869ac387c59151000000010000000100000197000000077373682d727361000000030100010000018100d12a2622fd6f564076e42cbc2902d7883caefc9a5ad6d6f482eda5f68aa58f05fc5c8090bd242cd76a2ed3edeb51c4d5fb10361422009126b8b177d8d58ea0369ada939ea93a2e650ff6bd6907e5fc73de2e10ae8a4f9f17bc3ba5e2e0bf250206ba7f35951b0155e074ebab6dfa852e6da4e8efc6abc8f858a13ff821064ec1805e4721abe9cac4ecf97fd72e282e8f040259485f5534bf4e3d10730b10d6c4038700c5abd75b1fb3e5302b6d21b31fe5420c7655b69d932471312b3dcdb02d2c63b296a44c59dc3bb08140a87a890394fc17eb28ffa7a6ff21851f3ccf0259d8f8988bfcd7e402f16f79cbb88ed295572a8a6cd2c7a0037625e66faadbe3f5159f06a58f2d533762066f7a684a59ae75824c4358287e8d1d494527452c95997e10dddc74d0a1d79a3193b0322ce3064812a895196b86d5e1fd0c9c6d2663ea2b2e79973f0dcc63896c6c74c1393e0c7b16b8f98415d9158483d2b73ecfc9bc979ada04a45ee8251197bc5f103cfdf1056f2ce6c34302ac9d610d45a41a1f8d000005807b6a93dc517cedf364789bcf5c9264efd264ab805eaee8539985ef3f76d75d82684ce59e28cc3e8d0a1c9de6b977cfb2252269fd3156d06c765631439fc58e7a86d768c9b836953016f256f4a841d2cf3592c4439855dbef79f84e33a5214df4da1faa26da86285d2dde0ac719e100a80c4cc97a2a931d21a1459371bac23c1a24e2ce09d64cdb4feb228d7f7833ce2be1603766f46978f29100619143f71361bc3691e36f74e11094fbd409f0ead1990b31e2d9db30e04300dc074608d4920024ff2f6e7511c189b5ed40505e683b47bd143f7a7bb8f0f80d96ccee5f797e8178278f06544e0061cdcdc21fca1ad9df6ec1b48a3d664e5ee19089e899e24bc9f66fa3f18401889d3a92a35494736c1b78f0479c245e329f66017c5a13052cdc8de083763706cd095201557c6833a2b4162a36d295ae169fe28ba627a442adc75574ac105513219e12b55e049b626cc9194db50758a8c47b7c1655b432c6d376c7062fa9354d266c94eaa9c76f2d393d487e3e6db737079097e81f88fc6f99b142b34f67b27085af66de4c293e988a2b57f2d12f3261dd2a2de0bd87e4e5b3becdc83eff371e8e0cd19fede37e75ae13cae3e64776976b8e047a42a0359585371e6ea7654597f7bb54cac7752ceb2c8c6b735ed6856cc9c5c23f88de698d8ca883951a01bd396a98019574b9b788263dfa9420643f38102ed9ad1aa317cefdfc0baa3dbf20bbc453dc421957b7750ee5eba264718019819ae7aeb8e617ce67dd7294299acb103aae8263480df491b5bfb2e9816eaaf843b4f263bbf2f17da3834a69ce8bfa8cc76debcdcf3398c6409234e6f5d88cb2b55fd3ae4bf3314ff75c2220f7e98c45adcc0a9d5a3e657f339920b05bed540089d9ae19e4297393e138bc7c177a3dce94501daa084e0149fe97ca60d91ee00ea4a3334c20e1e80100a2d7ef8774450c43486b0a7105eab072383d992c0143d2d3510292390cbd9dabf4f1516373a8ffa34f32879ff8c078dbe9e3dee484ff10b7e84930d4567e6837b101773da2f8e15754a0600fb35cae864cec0770f1d1dc60764ef60d41644a209e86a5eb66e85653d68faef60caed20e161295316503cc4187711a115d013cc5ff3f8871857c5a68be1cb8f294b435b4b8ebbfed24ba282e0b3739737f429e749007e6e2909988b49dccf95c95fe6fde3504b58040fbee57d5e61a282b8c564454f067c3fe9c5626bee7c4be37d1dfa1a149704aa8039c1c2dcd7bb14037342722095a17a775b08f3ef755f6bd7f2cd54e366ec27d02c88e28dd9452b284dd6387f68250ac15c5e9d3c623897c122535e0929225ba7ebbf613d7762297df7ef74b54349f9ea3f13546df07396858658fab84b79d5fee9aaf887ee3f008a552cad5fd4192bf8d70ab351e14473c0dfe47c75d52068f6853a1c5def39226dda54ac76943cfa5da9a271b8707a4509b6ece5416115a00850760b5ece8170fac9ea214b75df91336860cdfd91609b95a9531a3e47a5fd089106ad5b6738ee395af542d0b6526ec1f23747326d67a033d51a3eaf6da2458ee643e5ee87bb179c801d79b1e58edd92234c371476d8aed2a3920a0eb04ed30d90a9a11a8a20bf40bbcc6244adf874aa42603cffe87a86c3a891721abc152fc6b6408c1fffab454928dac80429c0ee7c9a1aed8d9dbcaafd3e3043e8bc606943f87411f720534619b95ef8f1589f29699676513ac55cd79a69463b72e4678e69f3c11a0faebc83676ffa2ca51cf329ecdb5e7d06a9d39b56d79cc37957fa84516925826d861b7b51def365b35b6e3b026a8ff1c4b831a065a18532231eb3f32938523aac4ea53195fd3a5f07e8c31809681dc886a1415b2e3cea1deaa813e25590df0b726c9930557d4a9d97e2eac7eab8517528d6c6ab2cdae3f8af40c88660ddcde2bd89e90d21d6af1b97207b773fc2f99965d2f8d2db4e30c339c7d4cde573cb9e0736937d96f50daf7$1$486
                                                                                    
┌──(kali㉿kali)-[~/thm/annie]
└─$ john sshpass --wordlist=/usr/share/wordlists/rockyou.txt          
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 2 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
annie123         (id_rsa)     
1g 0:00:01:11 DONE (2024-06-13 22:40) 0.01407g/s 286.4p/s 286.4c/s 286.4C/s bibles..ailyn
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```
