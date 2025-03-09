
```powershell
PS C:\Users\Administrator> Get-NetTCPconnection -State Listen

LocalAddress                        LocalPort RemoteAddress                       RemotePort State       AppliedSetting OwningProcess
------------                        --------- -------------                       ---------- -----       -------------- -------------
::                                  49676     ::                                  0          Listen                     716
::                                  49668     ::                                  0          Listen                     708
::                                  49667     ::                                  0          Listen                     1712
::                                  49666     ::                                  0          Listen                     972
::                                  49665     ::                                  0          Listen                     96
::                                  49664     ::                                  0          Listen                     608
::                                  47001     ::                                  0          Listen                     4
::                                  5985      ::                                  0          Listen                     4
::                                  3389      ::                                  0          Listen                     1008
::                                  445       ::                                  0          Listen                     4
::                                  135       ::                                  0          Listen                     836
0.0.0.0                             49676     0.0.0.0                             0          Listen                     716
0.0.0.0                             49668     0.0.0.0                             0          Listen                     708
0.0.0.0                             49667     0.0.0.0                             0          Listen                     1712
0.0.0.0                             49666     0.0.0.0                             0          Listen                     972
0.0.0.0                             49665     0.0.0.0                             0          Listen                     96
0.0.0.0                             49664     0.0.0.0                             0          Listen                     608
0.0.0.0                             3389      0.0.0.0                             0          Listen                     1008
10.10.172.32                        139       0.0.0.0                             0          Listen                     4
0.0.0.0                             135       0.0.0.0                             0          Listen                     836
```