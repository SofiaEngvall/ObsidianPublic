
downloaded two files from the repo, the `joomlascan.py` and `comptotestdb.txt`

```sh
┌──(kali㉿kali)-[~]
└─$ python2.7 joomlascan.py -u http://dailybugle.thm
-------------------------------------------
             Joomla Scan                  
   Usage: python joomlascan.py <target>    
    Version 0.5beta - Database Entries 1235
         created by Andrea Draghetti       
-------------------------------------------
Robots file found:               > http://dailybugle.thm/robots.txt
No Error Log found

Start scan...with 10 concurrent threads!
Component found: com_admin       > http://dailybugle.thm/index.php?option=com_admin
         On the administrator components
Component found: com_ajax        > http://dailybugle.thm/index.php?option=com_ajax
         But possibly it is not active or protected
         LICENSE file found      > http://dailybugle.thm/administrator/components/com_admin/admin.xml
         LICENSE file found      > http://dailybugle.thm/administrator/components/com_ajax/ajax.xml
         Explorable Directory    > http://dailybugle.thm/components/com_admin/
         Explorable Directory    > http://dailybugle.thm/administrator/components/com_admin/
         Explorable Directory    > http://dailybugle.thm/components/com_ajax/
         Explorable Directory    > http://dailybugle.thm/administrator/components/com_ajax/
Component found: com_banners     > http://dailybugle.thm/index.php?option=com_banners
         But possibly it is not active or protected
         LICENSE file found      > http://dailybugle.thm/administrator/components/com_banners/banners.xml
         Explorable Directory    > http://dailybugle.thm/components/com_banners/
         Explorable Directory    > http://dailybugle.thm/administrator/components/com_banners/
Component found: com_config      > http://dailybugle.thm/index.php?option=com_config
Component found: com_contact     > http://dailybugle.thm/index.php?option=com_contact
Component found: com_content     > http://dailybugle.thm/index.php?option=com_content
Component found: com_contenthistory      > http://dailybugle.thm/index.php?option=com_contenthistory
         But possibly it is not active or protected
         LICENSE file found      > http://dailybugle.thm/administrator/components/com_config/config.xml
         LICENSE file found      > http://dailybugle.thm/administrator/components/com_contact/contact.xml
         LICENSE file found      > http://dailybugle.thm/administrator/components/com_content/content.xml
         LICENSE file found      > http://dailybugle.thm/administrator/components/com_contenthistory/contenthistory.xml
         Explorable Directory    > http://dailybugle.thm/components/com_config/
         Explorable Directory    > http://dailybugle.thm/components/com_contact/
         Explorable Directory    > http://dailybugle.thm/administrator/components/com_config/
         Explorable Directory    > http://dailybugle.thm/components/com_content/
         Explorable Directory    > http://dailybugle.thm/administrator/components/com_contact/
         Explorable Directory    > http://dailybugle.thm/administrator/components/com_content/
         Explorable Directory    > http://dailybugle.thm/components/com_contenthistory/
         Explorable Directory    > http://dailybugle.thm/administrator/components/com_contenthistory/
Component found: com_fields      > http://dailybugle.thm/index.php?option=com_fields
         But possibly it is not active or protected
         LICENSE file found      > http://dailybugle.thm/administrator/components/com_fields/fields.xml
         Explorable Directory    > http://dailybugle.thm/components/com_fields/
         Explorable Directory    > http://dailybugle.thm/administrator/components/com_fields/
Component found: com_installer   > http://dailybugle.thm/index.php?option=com_installer
         On the administrator components
         LICENSE file found      > http://dailybugle.thm/administrator/components/com_installer/installer.xml
         Explorable Directory    > http://dailybugle.thm/components/com_installer/
         Explorable Directory    > http://dailybugle.thm/administrator/components/com_installer/
Component found: com_joomlaupdate        > http://dailybugle.thm/index.php?option=com_joomlaupdate
         On the administrator components
         LICENSE file found      > http://dailybugle.thm/administrator/components/com_joomlaupdate/joomlaupdate.xml
         Explorable Directory    > http://dailybugle.thm/components/com_joomlaupdate/
         Explorable Directory    > http://dailybugle.thm/administrator/components/com_joomlaupdate/
Component found: com_mailto      > http://dailybugle.thm/index.php?option=com_mailto
         But possibly it is not active or protected
         LICENSE file found      > http://dailybugle.thm/components/com_mailto/mailto.xml
Component found: com_media       > http://dailybugle.thm/index.php?option=com_media
         But possibly it is not active or protected
         Explorable Directory    > http://dailybugle.thm/components/com_mailto/
         LICENSE file found      > http://dailybugle.thm/administrator/components/com_media/media.xml
         Explorable Directory    > http://dailybugle.thm/components/com_media/
         Explorable Directory    > http://dailybugle.thm/administrator/components/com_media/
Component found: com_newsfeeds   > http://dailybugle.thm/index.php?option=com_newsfeeds
         LICENSE file found      > http://dailybugle.thm/administrator/components/com_newsfeeds/newsfeeds.xml
         Explorable Directory    > http://dailybugle.thm/components/com_newsfeeds/
         Explorable Directory    > http://dailybugle.thm/administrator/components/com_newsfeeds/
Component found: com_search      > http://dailybugle.thm/index.php?option=com_search
         But possibly it is not active or protected
         LICENSE file found      > http://dailybugle.thm/administrator/components/com_search/search.xml
         Explorable Directory    > http://dailybugle.thm/components/com_search/
         Explorable Directory    > http://dailybugle.thm/administrator/components/com_search/
Component found: com_users       > http://dailybugle.thm/index.php?option=com_users
         But possibly it is not active or protected
         LICENSE file found      > http://dailybugle.thm/administrator/components/com_users/users.xml
         Explorable Directory    > http://dailybugle.thm/components/com_users/
         Explorable Directory    > http://dailybugle.thm/administrator/components/com_users/
Component found: com_wrapper     > http://dailybugle.thm/index.php?option=com_wrapper
         LICENSE file found      > http://dailybugle.thm/components/com_wrapper/wrapper.xml
         Explorable Directory    > http://dailybugle.thm/components/com_wrapper/
End Scanner

```