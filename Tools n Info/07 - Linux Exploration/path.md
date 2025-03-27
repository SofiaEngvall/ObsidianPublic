
What folders are located under $PATH
	`$PATH`
Does your current user have write privileges for any of these folders?
	`find / -writable 2>/dev/null`
	Can quickly find if we don't have permission with:
		`find / -writable 2>/dev/null | cut -d "/" -f 2,3 | grep -v proc | sort -u`
Can you modify $PATH?
	`export PATH=/tmp:$PATH`
Is there a script/application you can start that will be affected by this vulnerability?
