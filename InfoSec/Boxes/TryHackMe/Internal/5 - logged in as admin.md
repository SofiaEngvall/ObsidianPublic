
![[Images/Pasted image 20240730142614.png]]
Don’t forget to reset Will’s credentials. william:arnold147


Most things in the admin interface were locked:
- we couldn't edit plugins
- we couldn't upload plugins, themes, images or anything else
- we couldn't even link images from url

Finally we found that we could edit theme files!! There are a lot of php files to choose from!

![[Images/Pasted image 20240730162557.png|700]]

we got shell by changing one of the theme php files to pentestmonkey
http://internal.thm/blog/wp-admin/theme-editor.php?file=index.php&theme=twentyseventeen

and went to the url http://internal.thm/blog/wp-content/themes/twentyseventeen/index.php

