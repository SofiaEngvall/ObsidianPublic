
robots.txt
```
# If the Joomla site is installed within a folder 
# eg www.example.com/joomla/ then the robots.txt file 
# MUST be moved to the site root 
# eg www.example.com/robots.txt
# AND the joomla folder name MUST be prefixed to all of the
# paths. 
# eg the Disallow rule for the /administrator/ folder MUST 
# be changed to read 
# Disallow: /joomla/administrator/
#
# For more information about the robots.txt standard, see:
# http://www.robotstxt.org/orig.html
#
# For syntax checking, see:
# http://tool.motoricerca.info/robots-checker.phtml

User-agent: *
Disallow: /administrator/
Disallow: /bin/
Disallow: /cache/
Disallow: /cli/
Disallow: /components/
Disallow: /includes/
Disallow: /installation/
Disallow: /language/
Disallow: /layouts/
Disallow: /libraries/
Disallow: /logs/
Disallow: /modules/
Disallow: /plugins/
Disallow: /tmp/
```

`http://dailybugle.thm/README.txt`
```sh
1- What is this?
	* This is a Joomla! installation/upgrade package to version 3.x
	* Joomla! Official site: https://www.joomla.org
	* Joomla! 3.7 version history - https://docs.joomla.org/Joomla_3.7_version_history
	* Detailed changes in the Changelog: https://github.com/joomla/joomla-cms/commits/master

...
...

Copyright:
	* Copyright (C) 2005 - 2017 Open Source Matters. All rights reserved.
	* Special Thanks: https://docs.joomla.org/Joomla!_Credits_and_Thanks
	* Distributed under the GNU General Public License version 2 or later
	* See Licenses details at https://docs.joomla.org/Joomla_Licenses
```

`http://dailybugle.thm/administrator/manifests/files/joomla.xml`
```xml
<extension version="3.6" type="file" method="upgrade">
<name>files_joomla</name>
<author>Joomla! Project</author>
<authorEmail>admin@joomla.org</authorEmail>
<authorUrl>www.joomla.org</authorUrl>
<copyright>
(C) 2005 - 2017 Open Source Matters. All rights reserved
</copyright>
<license>
GNU General Public License version 2 or later; see LICENSE.txt
</license>
<version>3.7.0</version>
<creationDate>April 2017</creationDate>
<description>FILES_JOOMLA_XML_DESCRIPTION</description>
<scriptfile>administrator/components/com_admin/script.php</scriptfile>
<update>
<schemas>
<schemapath type="mysql">
administrator/components/com_admin/sql/updates/mysql
</schemapath>
<schemapath type="sqlsrv">
administrator/components/com_admin/sql/updates/sqlazure
</schemapath>
<schemapath type="sqlazure">
administrator/components/com_admin/sql/updates/sqlazure
</schemapath>
<schemapath type="postgresql">
administrator/components/com_admin/sql/updates/postgresql
</schemapath>
</schemas>
</update>
<fileset>
<files>
<folder>administrator</folder>
<folder>bin</folder>
<folder>cache</folder>
<folder>cli</folder>
<folder>components</folder>
<folder>images</folder>
<folder>includes</folder>
<folder>language</folder>
<folder>layouts</folder>
<folder>libraries</folder>
<folder>media</folder>
<folder>modules</folder>
<folder>plugins</folder>
<folder>templates</folder>
<folder>tmp</folder>
<file>htaccess.txt</file>
<file>web.config.txt</file>
<file>LICENSE.txt</file>
<file>README.txt</file>
<file>index.php</file>
</files>
</fileset>
<updateservers>
<server name="Joomla! Core" type="collection">https://update.joomla.org/core/list.xml</server>
</updateservers>
</extension>
```

`http://dailybugle.thm/language/en-GB/en-GB.xml`
```xml
<metafile version="3.7" client="site">
<name>English (en-GB)</name>
<version>3.7.0</version>
<creationDate>April 2017</creationDate>
<author>Joomla! Project</author>
<authorEmail>admin@joomla.org</authorEmail>
<authorUrl>www.joomla.org</authorUrl>
<copyright>
Copyright (C) 2005 - 2017 Open Source Matters. All rights reserved.
</copyright>
<license>
GNU General Public License version 2 or later; see LICENSE.txt
</license>
<description>en-GB site language</description>
<metadata>
<name>English (en-GB)</name>
<nativeName>English (United Kingdom)</nativeName>
<tag>en-GB</tag>
<rtl>0</rtl>
<locale>
en_GB.utf8, en_GB.UTF-8, en_GB, eng_GB, en, english, english-uk, uk, gbr, britain, england, great britain, uk, united kingdom, united-kingdom
</locale>
<firstDay>0</firstDay>
<weekEnd>0,6</weekEnd>
<calendar>gregorian</calendar>
</metadata>
<params/>
</metafile>
```

`http://dailybugle.thm/plugins/system/cache/cache.xml` - obs! wrong version number
```xml
<extension version="3.1" type="plugin" group="system" method="upgrade">
<name>plg_system_cache</name>
<author>Joomla! Project</author>
<creationDate>February 2007</creationDate>
<copyright>
Copyright (C) 2005 - 2017 Open Source Matters. All rights reserved.
</copyright>
<license>
GNU General Public License version 2 or later; see LICENSE.txt
</license>
<authorEmail>admin@joomla.org</authorEmail>
<authorUrl>www.joomla.org</authorUrl>
<version>3.0.0</version>
<description>PLG_CACHE_XML_DESCRIPTION</description>
<files>
<filename plugin="cache">cache.php</filename>
</files>
<languages>
<language tag="en-GB">en-GB.plg_system_cache.ini</language>
<language tag="en-GB">en-GB.plg_system_cache.sys.ini</language>
</languages>
<config>
<fields name="params">
<fieldset name="basic">
<field name="browsercache" type="radio" label="PLG_CACHE_FIELD_BROWSERCACHE_LABEL" description="PLG_CACHE_FIELD_BROWSERCACHE_DESC" class="btn-group btn-group-yesno" default="0">
<option value="1">JYES</option>
<option value="0">JNO</option>
</field>
<field name="exclude_menu_items" type="menuitem" label="PLG_CACHE_FIELD_EXCLUDE_MENU_ITEMS_LABEL" description="PLG_CACHE_FIELD_EXCLUDE_MENU_ITEMS_DESC" default="" multiple="multiple"/>
</fieldset>
<fieldset name="advanced">
<field name="exclude" type="textarea" label="PLG_CACHE_FIELD_EXCLUDE_LABEL" description="PLG_CACHE_FIELD_EXCLUDE_DESC" class="input-xxlarge" rows="15" filter="raw" default=""/>
</fieldset>
</fields>
</config>
</extension>
```

