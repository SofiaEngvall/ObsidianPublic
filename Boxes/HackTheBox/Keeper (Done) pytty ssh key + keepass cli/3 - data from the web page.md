
(this was not used in solving the box)

DatabaseAdmin 	'postgres'
DatabaseHost 	'localhost'
DatabaseName 	'rtdb'
DatabasePassword 	Password not printed
DatabasePort 	'3306'
DatabaseRTHost 	'localhost'
DatabaseType 	'mysql'
DatabaseUser 	'rtuser'

Loaded perl modules - perl is running this
Summary of my perl5 (revision 5 version 34 subversion 0) configuration:
  Platform:
    osname=linux
    osvers=4.19.0
...

Environment variables - Running as root?
HOME 	/root
LOGNAME 	root

Server version: Apache/2.4.52 (Ubuntu)
nginx version: nginx/1.18.0 (Ubuntu)

```

Request Tracker logo RT for tickets.keeper.htb
System Configuration

    Home »
    Search »
    Reports »
    Articles »
    Assets »
    Tools »
    Admin »
    Logged in as root »

 
RT Configuration
Option 	Value 	Source
Active_MakeClicky 	[
  'httpurl_overwrite'
]
	core config
AdminSearchResultFormat 	{
  'Queues' => '\'<a href="__WebPath__/Admin/Queues/Modify.html?id=__id__">__id__</a>/TITLE:#\',\'<a href="__WebPath__/Admin/Queues/Modify.html?id=__id__">__Name__</a>/TITLE:Name\',__Description__,__Address__,__Priority__,__DefaultDueIn__,__Lifecycle__,__SubjectTag__,__Disabled__,__SortOrder__',
  'CustomRoles' => '\'<a href="__WebPath__/Admin/CustomRoles/Modify.html?id=__id__">__id__</a>/TITLE:#\',\'<a href="__WebPath__/Admin/CustomRoles/Modify.html?id=__id__">__Name__</a>/TITLE:Name\',__Description__,__MaxValues__,__Disabled__',
  'CustomFields' => '\'<a href="__WebPath__/Admin/CustomFields/Modify.html?id=__id__">__id__</a>/TITLE:#\',\'<a href="__WebPath__/Admin/CustomFields/Modify.html?id=__id__">__Name__</a>/TITLE:Name\',__AddedTo__, __EntryHint__, __FriendlyPattern__,__Disabled__',
  'Templates' => '\'<a href="__WebPath__/__WebRequestPathDir__/Template.html?Queue=__QueueId__&Template=__id__">__id__</a>/TITLE:#\',\'<a href="__WebPath__/__WebRequestPathDir__/Template.html?Queue=__QueueId__&Template=__id__">__Name__</a>/TITLE:Name\',\'__Description__\',\'__UsedBy__\',\'__IsEmpty__\'',
  'Catalogs' => '\'<a href="__WebPath__/Admin/Assets/Catalogs/Modify.html?id=__id__">__id__</a>/TITLE:#\',\'<a href="__WebPath__/Admin/Assets/Catalogs/Modify.html?id=__id__">__Name__</a>/TITLE:Name\',__Description__,__Lifecycle__,__Disabled__',
  'Users' => '\'<a href="__WebPath__/Admin/Users/Modify.html?id=__id__">__id__</a>/TITLE:#\',\'<a href="__WebPath__/Admin/Users/Modify.html?id=__id__">__Name__</a>/TITLE:Name\',__RealName__, __EmailAddress__,__Disabled__',
  'Groups' => '\'<a href="__WebPath__/Admin/Groups/Modify.html?id=__id__">__id__</a>/TITLE:#\',\'<a href="__WebPath__/Admin/Groups/Modify.html?id=__id__">__Name__</a>/TITLE:Name\',\'__Description__\',__Disabled__',
  'Scrips' => '\'<a href="__WebPath__/Admin/Scrips/Modify.html?id=__id____From__">__id__</a>/TITLE:#\',\'<a href="__WebPath__/Admin/Scrips/Modify.html?id=__id____From__">__Description__</a>/TITLE:Description\',__Condition__, __Action__, __Template__, __Disabled__',
  'Classes' => ' \'<a href="__WebPath__/Admin/Articles/Classes/Modify.html?id=__id__">__id__</a>/TITLE:#\',\'<a href="__WebPath__/Admin/Articles/Classes/Modify.html?id=__id__">__Name__</a>/TITLE:Name\',__Description__,__Disabled__'
}
	core config
AdminSearchResultRows 	{
  'CustomRoles' => 50,
  'CustomFields' => 50,
  'Assets' => 50,
  'Groups' => 50,
  'Classes' => 50,
  'Queues' => 50,
  'Templates' => 50,
  'Catalogs' => 50,
  'Users' => 50,
  'Scrips' => 50
}
	core config
AllowUserAutocompleteForUnprivileged 	0
	core config
AmbiguousDayInFuture 	0
	core config
AmbiguousDayInPast 	0
	core config
ApprovalRejectionNotes 	1
	core config
ArticleOnTicketCreate 	0
	core config
AssetSearchFields 	{
  'id' => '=',
  'Description' => 'LIKE',
  'Name' => 'LIKE'
}
	core config
AssetSearchFormat 	'
    \'<a href="__WebHomePath__/Asset/Display.html?id=__id__">__Name__</a>/TITLE:Name\',
    Description,
    \'__Status__ (__Catalog__)/TITLE:Status\',
    Owner,
    HeldBy,
    Contacts,
    \'__ActiveTickets__ __InactiveTickets__/TITLE:Related tickets\',
'
	core config
AssetSummaryFormat 	'
    \'<a href="__WebHomePath__/Asset/Display.html?id=__id__">__Name__</a>/TITLE:Name\',
    Description,
    \'__Status__ (__Catalog__)/TITLE:Status\',
    Owner,
    HeldBy,
    Contacts,
    \'__ActiveTickets__ __InactiveTickets__/TITLE:Related tickets\',
'
	core config
AssetSummaryRelatedTicketsFormat 	'
    \'<a href="__WebPath__/Ticket/Display.html?id=__id__">__id__</a>\',
    \'(__OwnerName__)\',
    \'<a href="__WebPath__/Ticket/Display.html?id=__id__">__Subject__</a>\',
    QueueName,
    Status,
'
	core config
AutoLogoff 	0
	core config
AutocompleteOwners 	0
	core config
AutocompleteOwnersForSearch 	0
	core config
AutocompleteQueues 	0
	core config
BcryptCost 	12
	core config
CSSFiles 	[]
	core config
CanonicalizeRedirectURLs 	0
	core config
CanonicalizeURLsInFeeds 	0
	core config
ChartColors 	[
  '66cc66',
  'ff6666',
  'ffcc66',
  '663399',
  '3333cc',
  '339933',
  '993333',
  '996633',
  '33cc33',
  'cc3333',
  'cc9933',
  '6633cc'
]
	core config
ChartFont 	{
  'ja' => '/usr/share/request-tracker4/fonts/DroidSansFallback.ttf',
  'zh-tw' => '/usr/share/request-tracker4/fonts/DroidSansFallback.ttf',
  'zh-cn' => '/usr/share/request-tracker4/fonts/DroidSansFallback.ttf',
  'others' => '/usr/share/request-tracker4/fonts/NotoSans-Regular.ttf'
}
	core config
ChartsTimezonesInDB 	0
	core config
CheckMoreMSMailHeaders 	0
	core config
CommentAddress 	'rt-comment@keeper.htb'
	site config
CorrespondAddress 	'rt@keeper.htb'
	site config
Crypt 	{
  'AllowEncryptDataInDB' => 0,
  'RejectOnBadData' => 1,
  'Enable' => 0,
  'Incoming' => [],
  'RejectOnMissingPrivateKey' => 1,
  'Dashboards' => {
                    'Sign' => 0,
                    'Encrypt' => 0
                  },
  'Outgoing' => undef
}
	core config
CustomFieldGroupings 	{
  'RT::Ticket' => [],
  'RT::Asset' => []
}
	core config
CustomFieldValuesCanonicalizers 	[
  'RT::CustomFieldValues::Canonicalizer::Uppercase',
  'RT::CustomFieldValues::Canonicalizer::Lowercase'
]
	core config
CustomFieldValuesSources 	[]
	core config
DashboardAddress 	''
	core config
DashboardSubject 	'%s Dashboard: %s'
	core config
DatabaseAdmin 	'postgres'
	core config
DatabaseExtraDSN 	{}
	core config
DatabaseHost 	'localhost'
	site config
DatabaseName 	'rtdb'
	site config
DatabasePassword 	Password not printed 	site config
DatabasePort 	'3306'
	site config
DatabaseRTHost 	'localhost'
	core config
DatabaseType 	'mysql'
	site config
DatabaseUser 	'rtuser'
	site config
DateDayBeforeMonth 	1
	core config
DateTimeFormat 	'DefaultFormat'
	core config
DefaultErrorMailPrecedence 	'bulk'
	core config
DefaultMailPrecedence 	'bulk'
	core config
DefaultSearchResultFormat 	'
   \'<B><A HREF="__WebPath__/Ticket/Display.html?id=__id__">__id__</a></B>/TITLE:#\',
   \'<B><A HREF="__WebPath__/Ticket/Display.html?id=__id__">__Subject__</a></B>/TITLE:Subject\',
   Status,
   QueueName,
   Owner,
   Priority,
   \'__NEWLINE__\',
   \'__NBSP__\',
   \'<small>__Requestors__</small>\',
   \'<small>__CreatedRelative__</small>\',
   \'<small>__ToldRelative__</small>\',
   \'<small>__LastUpdatedRelative__</small>\',
   \'<small>__TimeLeft__</small>\''
	core config
DefaultSearchResultOrder 	'ASC'
	core config
DefaultSearchResultOrderBy 	'id'
	core config
DefaultSelfServiceSearchResultFormat 	'
   \'<B><A HREF="__WebPath__/SelfService/Display.html?id=__id__">__id__</a></B>/TITLE:#\',
   \'<B><A HREF="__WebPath__/SelfService/Display.html?id=__id__">__Subject__</a></B>/TITLE:Subject\',
   Status,
   Requestors,
   Owner'
	core config
DefaultSummaryRows 	10
	core config
DefaultTimeUnitsToHours 	0
	core config
DevelMode 	0
	core config
DisallowExecuteCode 	0
	core config
DisplayTicketAfterQuickCreate 	0
	core config
DropdownMenuLimit 	50
	core config
EditCustomFieldsSingleColumn 	0
	core config
EmailDashboardLanguageOrder 	[
  '_subscription',
  '_recipient',
  '_subscriber',
  'en'
]
	core config
EmailDashboardRemove 	[]
	core config
EmailFrequency 	'Individual messages'
	core config
EmailInputEncodings 	[
  'utf-8-strict',
  'iso-8859-1',
  'ascii'
]
	core config
EmailOutputEncoding 	'utf-8'
	core config
EnableReminders 	1
	core config
ExternalSettings 	{}
	core config
ExternalStorage 	{}
	core config
ExternalStorageCutoffSize 	10485760
	core config
ExternalStorageDirectLink 	0
	core config
ExtractSubjectTagMatch 	qr/\[[^\]]+? #\d+\]/
	core config
ExtractSubjectTagNoMatch 	qr/\[tickets\.keeper\.htb #\d+\]/
	core config
ForceApprovalsView 	1
	core config
ForwardFromUser 	0
	core config
Framebusting 	1
	core config
FriendlyFromLineFormat 	'"%s via RT" <%s>'
	core config
FriendlyToLineFormat 	'"%s of tickets.keeper.htb Ticket #%s":;'
	core config
FullTextSearch 	{
  'Enable' => 0,
  'Indexed' => 0
}
	core config
GnuPG 	{
  'OutgoingMessagesFormat' => 'RFC',
  'GnuPG' => 'gpg',
  'Passphrase' => undef,
  'Enable' => 0
}
	core config
GnuPGOptions 	{
  'homedir' => '/var/lib/request-tracker4/data/gpg'
}
	core config
HTMLFormatter 	'w3m'
	core config
HideArticleSearchOnReplyCreate 	0
	core config
HideOneTimeSuggestions 	0
	core config
HideResolveActionsWithDependencies 	0
	core config
HideTimeFieldsFromUnprivilegedUsers 	0
	core config
HideUnsetFieldsOnDisplay 	0
	core config
HomePageRefreshInterval 	0
	core config
HomepageComponents 	[
  'QuickCreate',
  'QueueList',
  'MyAdminQueues',
  'MySupportQueues',
  'MyReminders',
  'RefreshHomepage',
  'Dashboards',
  'SavedSearches',
  'FindUser',
  'MyAssets',
  'FindAsset'
]
	core config
InitialdataFormatHandlers 	[
  'perl'
]
	core config
JSFiles 	[]
	core config
LexiconLanguages 	[
  '*'
]
	core config
Lifecycles 	{
  'assets' => {
                'actions' => {
                               '* -> allocated' => {
                                                     'label' => 'Allocate'
                                                   },
                               '* -> in-use' => {
                                                  'label' => 'Now in-use'
                                                },
                               '* -> stolen' => {
                                                  'label' => 'Report stolen'
                                                },
                               '* -> recycled' => {
                                                    'label' => 'Recycle'
                                                  }
                             },
                'initial' => [
                               'new'
                             ],
                'rights' => {
                              '* -> *' => 'ModifyAsset'
                            },
                'type' => 'asset',
                'defaults' => {
                                'on_create' => 'new'
                              },
                'active' => [
                              'allocated',
                              'in-use'
                            ],
                'inactive' => [
                                'recycled',
                                'stolen',
                                'deleted'
                              ],
                'transitions' => {
                                   'recycled' => [
                                                   'allocated'
                                                 ],
                                   'stolen' => [
                                                 'allocated'
                                               ],
                                   '' => [
                                           'new',
                                           'allocated',
                                           'in-use'
                                         ],
                                   'deleted' => [
                                                  'allocated'
                                                ],
                                   'new' => [
                                              'allocated',
                                              'in-use',
                                              'stolen',
                                              'deleted'
                                            ],
                                   'in-use' => [
                                                 'allocated',
                                                 'recycled',
                                                 'stolen',
                                                 'deleted'
                                               ],
                                   'allocated' => [
                                                    'in-use',
                                                    'recycled',
                                                    'stolen',
                                                    'deleted'
                                                  ]
                                 }
              },
  'default' => {
                 'rights' => {
                               '* -> deleted' => 'DeleteTicket',
                               '* -> *' => 'ModifyTicket'
                             },
                 'inactive' => [
                                 'resolved',
                                 'rejected',
                                 'deleted'
                               ],
                 'active' => [
                               'open',
                               'stalled'
                             ],
                 'transitions' => {
                                    'open' => [
                                                'new',
                                                'stalled',
                                                'resolved',
                                                'rejected',
                                                'deleted'
                                              ],
                                    'deleted' => [
                                                   'new',
                                                   'open',
                                                   'stalled',
                                                   'resolved',
                                                   'rejected'
                                                 ],
                                    '' => [
                                            'new',
                                            'open',
                                            'resolved'
                                          ],
                                    'new' => [
                                               'open',
                                               'stalled',
                                               'resolved',
                                               'rejected',
                                               'deleted'
                                             ],
                                    'stalled' => [
                                                   'new',
                                                   'open',
                                                   'resolved',
                                                   'rejected',
                                                   'deleted'
                                                 ],
                                    'resolved' => [
                                                    'new',
                                                    'open',
                                                    'stalled',
                                                    'rejected',
                                                    'deleted'
                                                  ],
                                    'rejected' => [
                                                    'new',
                                                    'open',
                                                    'stalled',
                                                    'resolved',
                                                    'deleted'
                                                  ]
                                  },
                 'actions' => [
                                'new -> open',
                                {
                                  'label' => 'Open It',
                                  'update' => 'Respond'
                                },
                                'new -> resolved',
                                {
                                  'label' => 'Resolve',
                                  'update' => 'Comment'
                                },
                                'new -> rejected',
                                {
                                  'label' => 'Reject',
                                  'update' => 'Respond'
                                },
                                'new -> deleted',
                                {
                                  'label' => 'Delete'
                                },
                                'open -> stalled',
                                {
                                  'update' => 'Comment',
                                  'label' => 'Stall'
                                },
                                'open -> resolved',
                                {
                                  'label' => 'Resolve',
                                  'update' => 'Comment'
                                },
                                'open -> rejected',
                                {
                                  'update' => 'Respond',
                                  'label' => 'Reject'
                                },
                                'stalled -> open',
                                {
                                  'label' => 'Open It'
                                },
                                'resolved -> open',
                                {
                                  'update' => 'Comment',
                                  'label' => 'Re-open'
                                },
                                'rejected -> open',
                                {
                                  'update' => 'Comment',
                                  'label' => 'Re-open'
                                },
                                'deleted -> open',
                                {
                                  'label' => 'Undelete'
                                }
                              ],
                 'initial' => [
                                'new'
                              ],
                 'defaults' => {
                                 'reminder_on_open' => 'open',
                                 'denied' => 'rejected',
                                 'reminder_on_resolve' => 'resolved',
                                 'approved' => 'open',
                                 'on_create' => 'new'
                               }
               },
  'approvals' => {
                   'transitions' => {
                                      'open' => [
                                                  'new',
                                                  'stalled',
                                                  'resolved',
                                                  'rejected',
                                                  'deleted'
                                                ],
                                      '' => [
                                              'new',
                                              'open',
                                              'resolved'
                                            ],
                                      'deleted' => [
                                                     'new',
                                                     'open',
                                                     'stalled',
                                                     'rejected',
                                                     'resolved'
                                                   ],
                                      'stalled' => [
                                                     'new',
                                                     'open',
                                                     'rejected',
                                                     'resolved',
                                                     'deleted'
                                                   ],
                                      'new' => [
                                                 'open',
                                                 'stalled',
                                                 'resolved',
                                                 'rejected',
                                                 'deleted'
                                               ],
                                      'rejected' => [
                                                      'new',
                                                      'open',
                                                      'stalled',
                                                      'resolved',
                                                      'deleted'
                                                    ],
                                      'resolved' => [
                                                      'new',
                                                      'open',
                                                      'stalled',
                                                      'rejected',
                                                      'deleted'
                                                    ]
                                    },
                   'active' => [
                                 'open',
                                 'stalled'
                               ],
                   'inactive' => [
                                   'resolved',
                                   'rejected',
                                   'deleted'
                                 ],
                   'rights' => {
                                 '* -> *' => 'ModifyTicket',
                                 '* -> rejected' => 'ModifyTicket',
                                 '* -> deleted' => 'DeleteTicket'
                               },
                   'defaults' => {
                                   'on_create' => 'new',
                                   'reminder_on_open' => 'open',
                                   'reminder_on_resolve' => 'resolved'
                                 },
                   'initial' => [
                                  'new'
                                ],
                   'actions' => [
                                  'new -> open',
                                  {
                                    'label' => 'Open It',
                                    'update' => 'Respond'
                                  },
                                  'new -> resolved',
                                  {
                                    'label' => 'Resolve',
                                    'update' => 'Comment'
                                  },
                                  'new -> rejected',
                                  {
                                    'label' => 'Reject',
                                    'update' => 'Respond'
                                  },
                                  'new -> deleted',
                                  {
                                    'label' => 'Delete'
                                  },
                                  'open -> stalled',
                                  {
                                    'update' => 'Comment',
                                    'label' => 'Stall'
                                  },
                                  'open -> resolved',
                                  {
                                    'update' => 'Comment',
                                    'label' => 'Resolve'
                                  },
                                  'open -> rejected',
                                  {
                                    'update' => 'Respond',
                                    'label' => 'Reject'
                                  },
                                  'stalled -> open',
                                  {
                                    'label' => 'Open It'
                                  },
                                  'resolved -> open',
                                  {
                                    'label' => 'Re-open',
                                    'update' => 'Comment'
                                  },
                                  'rejected -> open',
                                  {
                                    'label' => 'Re-open',
                                    'update' => 'Comment'
                                  },
                                  'deleted -> open',
                                  {
                                    'label' => 'Undelete'
                                  }
                                ]
                 }
}
	core config
LinkArticlesOnInclude 	1
	core config
LogDir 	'/var/log/request-tracker4'
	site config
LogStackTraces 	''
	core config
LogToFileNamed 	'rt.log'
	site config
LogToSTDERR 	'info'
	core config
LogToSyslog 	'warning'
	site config
LogToSyslogConf 	[]
	core config
LogoAltText 	'Request Tracker logo'
	core config
LogoLinkURL 	'http://bestpractical.com'
	core config
LogoURL 	'/rt/static/images/request-tracker-logo.png'
	core config
LogoutRefresh 	1
	core config
LoopsToRTOwner 	1
	core config
MailCommand 	'sendmailpipe'
	core config
MailParams 	[]
	core config
MasonParameters 	[]
	core config
MaxAttachmentSize 	10485760
	core config
MaxFulltextAttachmentSize 	0
	core config
MaxInlineBody 	25600
	core config
MessageBoxHeight 	15
	core config
MessageBoxIncludeSignature 	1
	core config
MessageBoxIncludeSignatureOnComment 	1
	core config
MessageBoxRichText 	1
	core config
MessageBoxRichTextHeight 	200
	core config
MessageBoxUseSystemContextMenu 	0
	core config
MinimumPasswordLength 	5
	core config
MoreAboutRequestorExtraInfo 	''
	core config
MoreAboutRequestorGroupsLimit 	0
	core config
MoreAboutRequestorTicketList 	'Active'
	core config
MoreAboutRequestorTicketListFormat 	'
       \'<a href="__WebPath__/Ticket/Display.html?id=__id__">__id__</a>\',
       \'__Owner__\',
       \'<a href="__WebPath__/Ticket/Display.html?id=__id__">__Subject__</a>\',
       \'__Status__\',
'
	core config
NotifyActor 	0
	core config
OldestTransactionsFirst 	1
	core config
OnlySearchActiveTicketsInSimpleSearch 	1
	core config
Organization 	'keeper.htb'
	site config
OverrideMailPrecedence 	{}
	core config
OverrideOutgoingMailFrom 	{}
	core config
OwnerEmail 	'root'
	core config
PlainTextMono 	0
	core config
Plugins 	[]
	core config
PreferDateTimeFormatNatural 	0
	core config
PreferDropzone 	1
	core config
PreferRichText 	1
	core config
PreviewScripMessages 	0
	core config
QuoteFolding 	1
	core config
RecordBaseClass 	'DBIx::SearchBuilder::Record::Cachable'
	core config
RecordOutgoingEmail 	1
	core config
RedistributeAutoGeneratedMessages 	'privileged'
	core config
ReferrerComponents 	{}
	core config
ReferrerWhitelist 	[]
	core config
RefreshIntervals 	[
  '120',
  '300',
  '600',
  '1200',
  '3600',
  '7200'
]
	core config
RestrictLoginReferrer 	0
	core config
RestrictReferrer 	1
	core config
SMIME 	{
  'AcceptUntrustedCAs' => undef,
  'OpenSSL' => 'openssl',
  'Enable' => 0,
  'Passphrase' => undef,
  'CAPath' => undef,
  'Keyring' => '/var/lib/request-tracker4/data/smime'
}
	core config
SearchResultsAutoRedirect 	0
	core config
SearchResultsRefreshInterval 	0
	core config
SelfServiceCorrespondenceOnly 	0
	core config
SelfServiceDownloadUserData 	0
	core config
SelfServiceRegex 	qr/^(?:\/+SelfService\/)/x
	core config
SelfServiceUserPrefs 	'edit-prefs'
	core config
SendmailArguments 	'-oi'
	core config
SendmailBounceArguments 	'-f "<>"'
	core config
SendmailPath 	'/usr/sbin/sendmail'
	core config
ServiceAgreements 	{}
	core config
ServiceBusinessHours 	{}
	core config
SetOutgoingMailFrom 	0
	core config
ShowBccHeader 	0
	core config
ShowHistory 	'delay'
	core config
ShowMoreAboutPrivilegedUsers 	0
	core config
ShowRTPortal 	1
	core config
ShowRemoteImages 	0
	core config
ShowSearchResultCount 	0
	core config
ShowTransactionImages 	1
	core config
ShowUnreadMessageNotifications 	0
	core config
SignatureAboveQuote 	0
	core config
SimplifiedRecipients 	0
	core config
SquelchedRecipients 	0
	core config
StaticRoots 	[]
	core config
StrictLinkACL 	1
	core config
TicketAutocompleteFields 	{
  'Subject' => 'LIKE',
  'id' => 'STARTSWITH'
}
	core config
TicketsItemMapSize 	1000
	core config
TimeInICal 	0
	core config
Timezone 	'Europe/Berlin'
	site config
TreatAttachedEmailAsFiles 	0
	core config
UseFriendlyFromLine 	1
	core config
UseFriendlyToLine 	0
	core config
UseOriginatorHeader 	1
	core config
UseSQLForACLChecks 	1
	core config
UseSideBySideLayout 	1
	core config
UseTransactionBatch 	1
	core config
UserDataResultFormat 	'\'__id__\', \'__Name__\', \'__EmailAddress__\', \'__RealName__\',
                            \'__NickName__\', \'__Organization__\', \'__HomePhone__\', \'__WorkPhone__\',
                            \'__MobilePhone__\', \'__PagerPhone__\', \'__Address1__\', \'__Address2__\',
                            \'__City__\', \'__State__\',\'__Zip__\', \'__Country__\', \'__Gecos__\', \'__Lang__\',
                            \'__Timezone__\', \'__FreeFormContactInfo__\''
	core config
UserSearchFields 	{
  'Name' => 'STARTSWITH',
  'EmailAddress' => 'STARTSWITH',
  'RealName' => 'LIKE'
}
	core config
UserSearchResultFormat 	' \'<a href="__WebPath__/User/Summary.html?id=__id__">__id__</a>/TITLE:#\',\'<a href="__WebPath__/User/Summary.html?id=__id__">__Name__</a>/TITLE:Name\',__RealName__, __EmailAddress__'
	core config
UserSummaryExtraInfo 	'RealName, EmailAddress, Name'
	core config
UserSummaryPortlets 	[
  'ExtraInfo',
  'CreateTicket',
  'ActiveTickets',
  'InactiveTickets',
  'UserAssets'
]
	core config
UserSummaryTicketListFormat 	'
       \'<B><A HREF="__WebPath__/Ticket/Display.html?id=__id__">__id__</a></B>/TITLE:#\',
       \'<B><A HREF="__WebPath__/Ticket/Display.html?id=__id__">__Subject__</a></B>/TITLE:Subject\',
       Status,
       QueueName,
       Owner,
       Priority,
       \'__NEWLINE__\',
       \'\',
       \'<small>__Requestors__</small>\',
       \'<small>__CreatedRelative__</small>\',
       \'<small>__ToldRelative__</small>\',
       \'<small>__LastUpdatedRelative__</small>\',
       \'<small>__TimeLeft__</small>\'
'
	core config
UserTransactionDataResultFormat 	'\'__ObjectId__/TITLE:Ticket Id\', \'__id__\', \'__Created__\', \'__Description__\',
                                        \'__OldValue__\', \'__NewValue__\', \'__Content__\''
	core config
UsernameFormat 	'role'
	core config
ValidateUserEmailAddresses 	1
	core config
WebBaseURL 	'http://keeper.htb'
	site config
WebDefaultStylesheet 	'rudder'
	core config
WebDomain 	'localhost'
	core config
WebFlushDbCacheEveryRequest 	1
	core config
WebHttpOnlyCookies 	1
	core config
WebImagesURL 	'/rt/static/images/'
	core config
WebNoAuthRegex 	qr/^ (?:\/+NoAuth\/ | \/+REST\/\d+\.\d+\/NoAuth\/) /x
	core config
WebPath 	'/rt'
	site config
WebPort 	80
	core config
WebRemoteUserContinuous 	1
	core config
WebSecureCookies 	0
	core config
WebSessionProperties 	{}
	core config
WebURL 	'http://keeper.htb/rt/'
	core config
WikiImplicitLinks 	0
	core config
rtname 	'tickets.keeper.htb'
	site config
RT core variables
Variable 	Value
RT::BasePath 	/usr/share/request-tracker4
RT::BinPath 	/usr/bin
RT::EtcPath 	/usr/share/request-tracker4/etc
RT::FontPath 	/usr/share/request-tracker4/fonts
RT::LexiconPath 	/usr/share/request-tracker4/po
RT::LocalEtcPath 	/etc/request-tracker4
RT::LocalLexiconPath 	/usr/local/share/request-tracker4/po
RT::LocalLibPath 	/usr/local/share/request-tracker4/lib
RT::LocalPath 	/usr/local/share/request-tracker4
RT::LocalPluginPath 	/usr/local/share/request-tracker4/plugins
RT::LocalStaticPath 	/usr/local/share/request-tracker4/static
RT::MAJOR_VERSION 	4
RT::MINOR_VERSION 	4
RT::MasonComponentRoot 	/usr/share/request-tracker4/html
RT::MasonDataDir 	/var/cache/request-tracker4/mason_data
RT::MasonLocalComponentRoot 	/usr/local/share/request-tracker4/html
RT::MasonSessionDir 	/var/cache/request-tracker4/session_data
RT::PluginPath 	/usr/share/request-tracker4/plugins
RT::REVISION 	4
RT::SbinPath 	/usr/sbin
RT::StaticPath 	/usr/share/request-tracker4/static
RT::VERSION 	4.4.4+dfsg-2ubuntu1
RT::VarPath 	/var/lib/request-tracker4
RT Size
Object 	Size
Tickets 	1
Queues 	2
Transactions 	39
Groups 	29
PrivilegedUsers 	2
UnprivilegedUsers 	3
	
Mason template search order

    /usr/local/share/request-tracker4/html
    /usr/share/request-tracker4/html

Static file search order

    /usr/local/share/request-tracker4/static
    /usr/share/request-tracker4/static

Perl library search order

    /usr/local/share/request-tracker4/lib
    /usr/share/request-tracker4/lib
    /etc/perl
    /usr/lib/x86_64-linux-gnu/perl5/5.34
    /usr/share/perl5
    /usr/lib/x86_64-linux-gnu/perl-base
    /usr/lib/x86_64-linux-gnu/perl/5.34
    /usr/share/perl/5.34
    /usr/local/lib/site_perl

Loaded config files

    /etc/request-tracker4/RT_SiteConfig.d/40-timezone.pm
    /etc/request-tracker4/RT_SiteConfig.d/50-debconf.pm
    /etc/request-tracker4/RT_SiteConfig.d/51-dbconfig-common.pm
    /etc/request-tracker4/RT_SiteConfig.d/60-logging.pm
    /usr/share/request-tracker4/etc/RT_Config.pm

Logging summary

RT's logging configuration is summarized below:

    Logging info level messages and higher to STDERR, which will usually end up in your webserver's error logs.
    Logging warning level messages and higher to syslog.
    Stack traces are not logged.
    SQL queries are not logged.

Global Attributes
Name 	Value
QueueCacheNeedsUpdate	'1684924011'
CatalogCacheNeedsUpdate	'1684851343'
Search - My Tickets	{
  'Order' => 'DESC',
  'Format' => '\'<a href="__WebPath__/Ticket/Display.html?id=__id__">__id__</a>/TITLE:#\',\'<a href="__WebPath__/Ticket/Display.html?id=__id__">__Subject__</a>/TITLE:Subject\',Priority, QueueName, ExtendedStatus',
  'OrderBy' => 'Priority',
  'Query' => ' Owner = \'__CurrentUser__\' AND Status = \'__Active__\''
}
Search - Unowned Tickets	{
  'Order' => 'DESC',
  'OrderBy' => 'Created',
  'Query' => ' Owner = \'Nobody\' AND Status = \'__Active__\'',
  'Format' => '\'<a href="__WebPath__/Ticket/Display.html?id=__id__">__id__</a>/TITLE:#\',\'<a href="__WebPath__/Ticket/Display.html?id=__id__">__Subject__</a>/TITLE:Subject\',QueueName, ExtendedStatus, CreatedRelative, \'<A HREF="__WebPath__/Ticket/Display.html?Action=Take&id=__id__">__loc(Take)__</a>/TITLE:NBSP\''
}
Search - Bookmarked Tickets	{
  'Order' => 'DESC',
  'Format' => '\'<a href="__WebPath__/Ticket/Display.html?id=__id__">__id__</a>/TITLE:#\',\'<a href="__WebPath__/Ticket/Display.html?id=__id__">__Subject__</a>/TITLE:Subject\',Priority, QueueName, ExtendedStatus, Bookmark',
  'OrderBy' => 'LastUpdated',
  'Query' => 'id = \'__Bookmarked__\''
}
HomepageSettings	{
  'body' => [
              {
                'name' => 'My Tickets',
                'type' => 'system'
              },
              {
                'name' => 'Unowned Tickets',
                'type' => 'system'
              },
              {
                'name' => 'Bookmarked Tickets',
                'type' => 'system'
              },
              {
                'name' => 'QuickCreate',
                'type' => 'component'
              }
            ],
  'sidebar' => [
                 {
                   'name' => 'MyReminders',
                   'type' => 'component'
                 },
                 {
                   'name' => 'QueueList',
                   'type' => 'component'
                 },
                 {
                   'type' => 'component',
                   'name' => 'Dashboards'
                 },
                 {
                   'type' => 'component',
                   'name' => 'RefreshHomepage'
                 }
               ]
}
Loaded RT Extensions
Extension 	Version
Loaded perl modules
Module 	Version 	Source
_charnames 	1.48 	/usr/share/perl/5.34/_charnames.pm
Apache::Session 	1.94 	/usr/share/perl5/Apache/Session.pm
Apache::Session::Generate::MD5 	2.12 	/usr/share/perl5/Apache/Session/Generate/MD5.pm
Apache::Session::Lock::MySQL 	1.01 	/usr/share/perl5/Apache/Session/Lock/MySQL.pm
Apache::Session::MySQL 	1.01 	/usr/share/perl5/Apache/Session/MySQL.pm
Apache::Session::Serialize::Storable 	1.01 	/usr/share/perl5/Apache/Session/Serialize/Storable.pm
Apache::Session::Store::DBI 	1.02 	/usr/share/perl5/Apache/Session/Store/DBI.pm
Apache::Session::Store::MySQL 	1.04 	/usr/share/perl5/Apache/Session/Store/MySQL.pm
attributes 	0.33 	/usr/lib/x86_64-linux-gnu/perl-base/attributes.pm
AutoLoader 	5.74 	/usr/lib/x86_64-linux-gnu/perl-base/AutoLoader.pm
B 	1.82 	/usr/lib/x86_64-linux-gnu/perl/5.34/B.pm
B::Hooks::EndOfScope 	0.25 	/usr/share/perl5/B/Hooks/EndOfScope.pm
B::Hooks::EndOfScope::XS 	0.25 	/usr/share/perl5/B/Hooks/EndOfScope/XS.pm
base 	2.27 	/usr/lib/x86_64-linux-gnu/perl-base/base.pm
bytes 	1.08 	/usr/lib/x86_64-linux-gnu/perl-base/bytes.pm
Cache::Simple::TimedExpiry 	0.27 	/usr/share/perl5/Cache/Simple/TimedExpiry.pm
Carp 	1.52 	/usr/lib/x86_64-linux-gnu/perl-base/Carp.pm
Carp::Heavy 	1.52 	/usr/lib/x86_64-linux-gnu/perl-base/Carp/Heavy.pm
CGI 	4.54 	/usr/share/perl5/CGI.pm
CGI::Cookie 	4.54 	/usr/share/perl5/CGI/Cookie.pm
CGI::Emulate::PSGI 	0.23 	/usr/share/perl5/CGI/Emulate/PSGI.pm
CGI::PSGI 	0.15 	/usr/share/perl5/CGI/PSGI.pm
CGI::Util 	4.54 	/usr/share/perl5/CGI/Util.pm
charnames 	1.48 	/usr/share/perl/5.34/charnames.pm
Class::Accessor 	0.51 	/usr/share/perl5/Class/Accessor.pm
Class::Accessor::Fast 	0.51 	/usr/share/perl5/Class/Accessor/Fast.pm
Class::Container 	0.13 	/usr/share/perl5/Class/Container.pm
Class::Data::Inheritable 	0.08 	/usr/share/perl5/Class/Data/Inheritable.pm
Class::Inspector 	1.36 	/usr/share/perl5/Class/Inspector.pm
Class::ReturnValue 	0.55 	/usr/share/perl5/Class/ReturnValue.pm
Class::Singleton 	1.6 	/usr/share/perl5/Class/Singleton.pm
Class::XSAccessor 	1.19 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Class/XSAccessor.pm
Class::XSAccessor::Heavy 	1.19 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Class/XSAccessor/Heavy.pm
Clone 	0.45 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Clone.pm
Config 	5.034000 	/usr/lib/x86_64-linux-gnu/perl-base/Config.pm
constant 	1.33 	/usr/lib/x86_64-linux-gnu/perl-base/constant.pm
Cookie::Baker 	0.11 	/usr/share/perl5/Cookie/Baker.pm
Cookie::Baker::XS 	0.11 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Cookie/Baker/XS.pm
Cpanel::JSON::XS 	4.27 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Cpanel/JSON/XS.pm
Crypt::Eksblowfish 	0.009 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Crypt/Eksblowfish.pm
Crypt::Eksblowfish::Bcrypt 	0.009 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Crypt/Eksblowfish/Bcrypt.pm
Crypt::Eksblowfish::Subkeyed 	0.009 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Crypt/Eksblowfish/Subkeyed.pm
Crypt::URandom 	0.36 	/usr/share/perl5/Crypt/URandom.pm
CSS::Minifier::XS 	0.13 	/usr/lib/x86_64-linux-gnu/perl5/5.34/CSS/Minifier/XS.pm
CSS::Squish 	0.10 	/usr/share/perl5/CSS/Squish.pm
Cwd 	3.80 	/usr/lib/x86_64-linux-gnu/perl-base/Cwd.pm
Data::Dumper 	2.179 	/usr/lib/x86_64-linux-gnu/perl/5.34/Data/Dumper.pm
Data::GUID 	0.049 	/usr/share/perl5/Data/GUID.pm
Data::OptList 	0.112 	/usr/share/perl5/Data/OptList.pm
Data::UUID 	1.0602 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Data/UUID.pm
Date::Format 	2.24 	/usr/share/perl5/Date/Format.pm
Date::Parse 	2.33 	/usr/share/perl5/Date/Parse.pm
DateTime 	1.55 	/usr/lib/x86_64-linux-gnu/perl5/5.34/DateTime.pm
DateTime::Duration 	1.55 	/usr/lib/x86_64-linux-gnu/perl5/5.34/DateTime/Duration.pm
DateTime::Helpers 	1.55 	/usr/lib/x86_64-linux-gnu/perl5/5.34/DateTime/Helpers.pm
DateTime::Infinite 	1.55 	/usr/lib/x86_64-linux-gnu/perl5/5.34/DateTime/Infinite.pm
DateTime::Locale 	1.33 	/usr/share/perl5/DateTime/Locale.pm
DateTime::Locale::Data 	1.33 	/usr/share/perl5/DateTime/Locale/Data.pm
DateTime::Locale::FromData 	1.33 	/usr/share/perl5/DateTime/Locale/FromData.pm
DateTime::Locale::Util 	1.33 	/usr/share/perl5/DateTime/Locale/Util.pm
DateTime::TimeZone 	2.51 	/usr/share/perl5/DateTime/TimeZone.pm
DateTime::TimeZone::Catalog 	2.51 	/usr/share/perl5/DateTime/TimeZone/Catalog.pm
DateTime::TimeZone::Floating 	2.51 	/usr/share/perl5/DateTime/TimeZone/Floating.pm
DateTime::TimeZone::Local 	2.51 	/usr/share/perl5/DateTime/TimeZone/Local.pm
DateTime::TimeZone::OffsetOnly 	2.51 	/usr/share/perl5/DateTime/TimeZone/OffsetOnly.pm
DateTime::TimeZone::OlsonDB::Change 	2.51 	/usr/share/perl5/DateTime/TimeZone/OlsonDB/Change.pm
DateTime::TimeZone::UTC 	2.51 	/usr/share/perl5/DateTime/TimeZone/UTC.pm
DateTime::Types 	1.55 	/usr/lib/x86_64-linux-gnu/perl5/5.34/DateTime/Types.pm
DBD::mysql 	4.050 	/usr/lib/x86_64-linux-gnu/perl5/5.34/DBD/mysql.pm
DBI 	1.643 	/usr/lib/x86_64-linux-gnu/perl5/5.34/DBI.pm
DBIx::SearchBuilder 	1.71 	/usr/share/perl5/DBIx/SearchBuilder.pm
DBIx::SearchBuilder::Union 	0 	/usr/share/perl5/DBIx/SearchBuilder/Union.pm
Devel::GlobalDestruction 	0.14 	/usr/share/perl5/Devel/GlobalDestruction.pm
Devel::StackTrace 	2.04 	/usr/share/perl5/Devel/StackTrace.pm
Devel::StackTrace::Frame 	2.04 	/usr/share/perl5/Devel/StackTrace/Frame.pm
Digest::base 	1.19 	/usr/share/perl/5.34/Digest/base.pm
Digest::MD5 	2.58 	/usr/lib/x86_64-linux-gnu/perl/5.34/Digest/MD5.pm
Digest::SHA 	6.02 	/usr/lib/x86_64-linux-gnu/perl/5.34/Digest/SHA.pm
DynaLoader 	1.50 	/usr/lib/x86_64-linux-gnu/perl-base/DynaLoader.pm
Email::Address 	1.912 	/usr/share/perl5/Email/Address.pm
Email::Address::List 	0.06 	/usr/share/perl5/Email/Address/List.pm
Encode 	3.08 	/usr/lib/x86_64-linux-gnu/perl/5.34/Encode.pm
Encode::Alias 	2.24 	/usr/lib/x86_64-linux-gnu/perl/5.34/Encode/Alias.pm
Encode::Config 	2.05 	/usr/lib/x86_64-linux-gnu/perl/5.34/Encode/Config.pm
Encode::Encoding 	2.08 	/usr/lib/x86_64-linux-gnu/perl/5.34/Encode/Encoding.pm
Encode::Guess 	2.08 	/usr/lib/x86_64-linux-gnu/perl/5.34/Encode/Guess.pm
Encode::MIME::Name 	1.03 	/usr/lib/x86_64-linux-gnu/perl/5.34/Encode/MIME/Name.pm
Encode::Unicode 	2.18 	/usr/lib/x86_64-linux-gnu/perl/5.34/Encode/Unicode.pm
English 	1.11 	/usr/share/perl/5.34/English.pm
Errno 	1.33 	/usr/lib/x86_64-linux-gnu/perl-base/Errno.pm
Eval::Closure 	0.14 	/usr/share/perl5/Eval/Closure.pm
Exception::Class 	1.45 	/usr/share/perl5/Exception/Class.pm
Exception::Class::Base 	1.45 	/usr/share/perl5/Exception/Class/Base.pm
Exporter 	5.76 	/usr/lib/x86_64-linux-gnu/perl-base/Exporter.pm
Exporter::Heavy 	5.76 	/usr/lib/x86_64-linux-gnu/perl-base/Exporter/Heavy.pm
Exporter::Tiny 	1.002002 	/usr/share/perl5/Exporter/Tiny.pm
FCGI 	0.82 	/usr/lib/x86_64-linux-gnu/perl5/5.34/FCGI.pm
Fcntl 	1.14 	/usr/lib/x86_64-linux-gnu/perl-base/Fcntl.pm
File::Basename 	2.85 	/usr/lib/x86_64-linux-gnu/perl-base/File/Basename.pm
File::Glob 	1.33 	/usr/lib/x86_64-linux-gnu/perl-base/File/Glob.pm
File::Path 	2.18 	/usr/lib/x86_64-linux-gnu/perl-base/File/Path.pm
File::ShareDir 	1.118 	/usr/share/perl5/File/ShareDir.pm
File::Spec 	3.80 	/usr/lib/x86_64-linux-gnu/perl-base/File/Spec.pm
File::Spec::Unix 	3.80 	/usr/lib/x86_64-linux-gnu/perl-base/File/Spec/Unix.pm
File::Temp 	0.2311 	/usr/lib/x86_64-linux-gnu/perl-base/File/Temp.pm
File::Temp::Dir 	0.2311 	
FileHandle 	2.03 	/usr/lib/x86_64-linux-gnu/perl-base/FileHandle.pm
GD 	2.76 	/usr/lib/x86_64-linux-gnu/perl5/5.34/GD.pm
GD::Image 	2.75 	/usr/lib/x86_64-linux-gnu/perl5/5.34/GD/Image.pm
GD::Polygon 	2.76 	/usr/lib/x86_64-linux-gnu/perl5/5.34/GD/Polygon.pm
Getopt::Long 	2.52 	/usr/lib/x86_64-linux-gnu/perl-base/Getopt/Long.pm
GraphViz 	2.24 	/usr/share/perl5/GraphViz.pm
Hash::MultiValue 	0.16 	/usr/share/perl5/Hash/MultiValue.pm
HTML::Element 	5.07 	/usr/share/perl5/HTML/Element.pm
HTML::Entities 	3.76 	/usr/lib/x86_64-linux-gnu/perl5/5.34/HTML/Entities.pm
HTML::FormatExternal 	26 	/usr/share/perl5/HTML/FormatExternal.pm
HTML::Formatter 	2.12 	/usr/share/perl5/HTML/Formatter.pm
HTML::FormatText 	2.12 	/usr/share/perl5/HTML/FormatText.pm
HTML::FormatText::W3m 	26 	/usr/share/perl5/HTML/FormatText/W3m.pm
HTML::FormatText::WithLinks 	0.15 	/usr/share/perl5/HTML/FormatText/WithLinks.pm
HTML::FormatText::WithLinks::AndTables 	0.07 	/usr/share/perl5/HTML/FormatText/WithLinks/AndTables.pm
HTML::Gumbo 	0.18 	/usr/lib/x86_64-linux-gnu/perl5/5.34/HTML/Gumbo.pm
HTML::Mason 	1.59 	/usr/share/perl5/HTML/Mason.pm
HTML::Mason::Cache::BaseCache 	1.59 	/usr/share/perl5/HTML/Mason/Cache/BaseCache.pm
HTML::Mason::CGIHandler 	1.59 	/usr/share/perl5/HTML/Mason/CGIHandler.pm
HTML::Mason::Compiler 	1.59 	/usr/share/perl5/HTML/Mason/Compiler.pm
HTML::Mason::Compiler::ToObject 	1.59 	/usr/share/perl5/HTML/Mason/Compiler/ToObject.pm
HTML::Mason::Component 	1.59 	/usr/share/perl5/HTML/Mason/Component.pm
HTML::Mason::Component::FileBased 	1.59 	/usr/share/perl5/HTML/Mason/Component/FileBased.pm
HTML::Mason::Component::Subcomponent 	1.59 	/usr/share/perl5/HTML/Mason/Component/Subcomponent.pm
HTML::Mason::ComponentSource 	1.59 	/usr/share/perl5/HTML/Mason/ComponentSource.pm
HTML::Mason::Escapes 	1.59 	/usr/share/perl5/HTML/Mason/Escapes.pm
HTML::Mason::Exception 	1.59 	/usr/share/perl5/Exception/Class.pm
HTML::Mason::Exception::Abort 	1.1 	/usr/share/perl5/Exception/Class.pm
HTML::Mason::Exception::Compilation 	1.59 	/usr/share/perl5/Exception/Class.pm
HTML::Mason::Exception::Compilation::IncompatibleCompiler 	1.1 	/usr/share/perl5/Exception/Class.pm
HTML::Mason::Exception::Compiler 	1.1 	/usr/share/perl5/Exception/Class.pm
HTML::Mason::Exception::Decline 	1.1 	/usr/share/perl5/Exception/Class.pm
HTML::Mason::Exception::Params 	1.1 	/usr/share/perl5/Exception/Class.pm
HTML::Mason::Exception::Syntax 	1.59 	/usr/share/perl5/Exception/Class.pm
HTML::Mason::Exception::System 	1.1 	/usr/share/perl5/Exception/Class.pm
HTML::Mason::Exception::TopLevelNotFound 	1.1 	/usr/share/perl5/Exception/Class.pm
HTML::Mason::Exception::VirtualMethod 	1.1 	/usr/share/perl5/Exception/Class.pm
HTML::Mason::Exceptions 	1.59 	/usr/share/perl5/HTML/Mason/Exceptions.pm
HTML::Mason::FakeApache 	1.59 	/usr/share/perl5/HTML/Mason/FakeApache.pm
HTML::Mason::FakeTable 	1.59 	
HTML::Mason::FakeTableHash 	1.59 	
HTML::Mason::Interp 	1.59 	/usr/share/perl5/HTML/Mason/Interp.pm
HTML::Mason::Lexer 	1.59 	/usr/share/perl5/HTML/Mason/Lexer.pm
HTML::Mason::MethodMaker 	1.59 	/usr/share/perl5/HTML/Mason/MethodMaker.pm
HTML::Mason::Plugin::Context 	1.59 	/usr/share/perl5/HTML/Mason/Plugin/Context.pm
HTML::Mason::Plugin::Context::EndComponent 	1.59 	
HTML::Mason::Plugin::Context::EndRequest 	1.59 	
HTML::Mason::Plugin::Context::StartComponent 	1.59 	
HTML::Mason::Plugin::Context::StartRequest 	1.59 	
HTML::Mason::PSGIHandler 	0.53 	/usr/share/perl5/HTML/Mason/PSGIHandler.pm
HTML::Mason::PSGIHandler::Streamy 	0.53 	/usr/share/perl5/HTML/Mason/PSGIHandler/Streamy.pm
HTML::Mason::Request 	1.59 	/usr/share/perl5/HTML/Mason/Request.pm
HTML::Mason::Request::CGI 	1.59 	
HTML::Mason::Request::PSGI 	0.53 	
HTML::Mason::Resolver 	1.59 	/usr/share/perl5/HTML/Mason/Resolver.pm
HTML::Mason::Resolver::File 	1.59 	/usr/share/perl5/HTML/Mason/Resolver/File.pm
HTML::Mason::Tools 	1.59 	/usr/share/perl5/HTML/Mason/Tools.pm
HTML::Mason::Utils 	1.59 	/usr/share/perl5/HTML/Mason/Utils.pm
HTML::Parser 	3.76 	/usr/lib/x86_64-linux-gnu/perl5/5.34/HTML/Parser.pm
HTML::Quoted 	0.04 	/usr/share/perl5/HTML/Quoted.pm
HTML::Scrubber 	0.19 	/usr/share/perl5/HTML/Scrubber.pm
HTML::Tagset 	3.20 	/usr/share/perl5/HTML/Tagset.pm
HTML::TreeBuilder 	5.07 	/usr/share/perl5/HTML/TreeBuilder.pm
HTTP::Date 	6.05 	/usr/share/perl5/HTTP/Date.pm
HTTP::Entity::Parser 	0.25 	/usr/share/perl5/HTTP/Entity/Parser.pm
HTTP::Headers 	6.36 	/usr/share/perl5/HTTP/Headers.pm
HTTP::Headers::Fast 	0.22 	/usr/share/perl5/HTTP/Headers/Fast.pm
HTTP::Message 	6.36 	/usr/share/perl5/HTTP/Message.pm
HTTP::MultiPartParser 	0.02 	/usr/share/perl5/HTTP/MultiPartParser.pm
HTTP::Request 	6.36 	/usr/share/perl5/HTTP/Request.pm
HTTP::Response 	6.36 	/usr/share/perl5/HTTP/Response.pm
HTTP::Status 	6.36 	/usr/share/perl5/HTTP/Status.pm
I18N::LangTags 	0.45 	/usr/share/perl/5.34/I18N/LangTags.pm
I18N::LangTags::Detect 	1.08 	/usr/share/perl/5.34/I18N/LangTags/Detect.pm
integer 	1.01 	/usr/lib/x86_64-linux-gnu/perl-base/integer.pm
IO 	1.46 	/usr/lib/x86_64-linux-gnu/perl-base/IO.pm
IO::File 	1.46 	/usr/lib/x86_64-linux-gnu/perl-base/IO/File.pm
IO::Handle 	1.46 	/usr/lib/x86_64-linux-gnu/perl-base/IO/Handle.pm
IO::Seekable 	1.46 	/usr/lib/x86_64-linux-gnu/perl-base/IO/Seekable.pm
IO::Select 	1.46 	/usr/lib/x86_64-linux-gnu/perl-base/IO/Select.pm
IPC::Open2 	1.05 	/usr/lib/x86_64-linux-gnu/perl-base/IPC/Open2.pm
IPC::Open3 	1.21 	/usr/lib/x86_64-linux-gnu/perl-base/IPC/Open3.pm
IPC::Run 	20200505.0 	/usr/share/perl5/IPC/Run.pm
IPC::Run::Debug 	20200505.0 	/usr/share/perl5/IPC/Run/Debug.pm
IPC::Run::IO 	20200505.0 	/usr/share/perl5/IPC/Run/IO.pm
IPC::Run::Timer 	20200505.0 	/usr/share/perl5/IPC/Run/Timer.pm
JavaScript::Minifier::XS 	0.15 	/usr/lib/x86_64-linux-gnu/perl5/5.34/JavaScript/Minifier/XS.pm
JSON 	4.04 	/usr/share/perl5/JSON.pm
JSON::Backend::XS 	4.27 	
JSON::MaybeXS 	1.004003 	/usr/share/perl5/JSON/MaybeXS.pm
List::MoreUtils 	0.430 	/usr/share/perl5/List/MoreUtils.pm
List::MoreUtils::PP 	0.430 	/usr/share/perl5/List/MoreUtils/PP.pm
List::MoreUtils::XS 	0.430 	/usr/lib/x86_64-linux-gnu/perl5/5.34/List/MoreUtils/XS.pm
List::Util 	1.61 	/usr/lib/x86_64-linux-gnu/perl5/5.34/List/Util.pm
Locale::Maketext 	1.29 	/usr/share/perl/5.34/Locale/Maketext.pm
Locale::Maketext::Fuzzy 	0.11 	/usr/share/perl5/Locale/Maketext/Fuzzy.pm
Locale::Maketext::Lexicon 	1.00 	/usr/share/perl5/Locale/Maketext/Lexicon.pm
Locale::Maketext::Lexicon::Gettext 	1.00 	/usr/share/perl5/Locale/Maketext/Lexicon/Gettext.pm
Log::Any 	1.710 	/usr/share/perl5/Log/Any.pm
Log::Any::Adapter::Base 	1.710 	/usr/share/perl5/Log/Any/Adapter/Base.pm
Log::Any::Adapter::Null 	1.710 	/usr/share/perl5/Log/Any/Adapter/Null.pm
Log::Any::Adapter::Util 	1.710 	/usr/share/perl5/Log/Any/Adapter/Util.pm
Log::Any::Manager 	1.710 	/usr/share/perl5/Log/Any/Manager.pm
Log::Any::Proxy 	1.710 	/usr/share/perl5/Log/Any/Proxy.pm
Log::Any::Proxy::Null 	1.710 	/usr/share/perl5/Log/Any/Proxy/Null.pm
Log::Dispatch 	2.70 	/usr/share/perl5/Log/Dispatch.pm
Log::Dispatch::Base 	2.70 	/usr/share/perl5/Log/Dispatch/Base.pm
Log::Dispatch::Output 	2.70 	/usr/share/perl5/Log/Dispatch/Output.pm
Log::Dispatch::Screen 	2.70 	/usr/share/perl5/Log/Dispatch/Screen.pm
Log::Dispatch::Syslog 	2.70 	/usr/share/perl5/Log/Dispatch/Syslog.pm
Log::Dispatch::Types 	2.70 	/usr/share/perl5/Log/Dispatch/Types.pm
Log::Dispatch::Vars 	2.70 	/usr/share/perl5/Log/Dispatch/Vars.pm
Mail::Address 	2.21 	/usr/share/perl5/Mail/Address.pm
Mail::Field 	2.21 	/usr/share/perl5/Mail/Field.pm
Mail::Field::AddrList 	2.21 	/usr/share/perl5/Mail/Field/AddrList.pm
Mail::Field::Date 	2.21 	/usr/share/perl5/Mail/Field/Date.pm
Mail::Field::Generic 	2.21 	/usr/share/perl5/Mail/Field/Generic.pm
Mail::Header 	2.21 	/usr/share/perl5/Mail/Header.pm
Mail::Internet 	2.21 	/usr/share/perl5/Mail/Internet.pm
Mail::Mailer 	2.21 	/usr/share/perl5/Mail/Mailer.pm
Mail::Util 	2.21 	/usr/share/perl5/Mail/Util.pm
MIME::Base64 	3.16 	/usr/lib/x86_64-linux-gnu/perl/5.34/MIME/Base64.pm
MIME::Body 	5.509 	/usr/share/perl5/MIME/Body.pm
MIME::Decoder 	5.509 	/usr/share/perl5/MIME/Decoder.pm
MIME::Entity 	5.509 	/usr/share/perl5/MIME/Entity.pm
MIME::Field::ContDisp 	5.509 	/usr/share/perl5/MIME/Field/ContDisp.pm
MIME::Field::ConTraEnc 	5.509 	/usr/share/perl5/MIME/Field/ConTraEnc.pm
MIME::Field::ContType 	5.509 	/usr/share/perl5/MIME/Field/ContType.pm
MIME::Field::ParamVal 	5.509 	/usr/share/perl5/MIME/Field/ParamVal.pm
MIME::Head 	5.509 	/usr/share/perl5/MIME/Head.pm
MIME::Parser 	5.509 	/usr/share/perl5/MIME/Parser.pm
MIME::QuotedPrint 	3.16 	/usr/lib/x86_64-linux-gnu/perl/5.34/MIME/QuotedPrint.pm
MIME::Tools 	5.509 	/usr/share/perl5/MIME/Tools.pm
MIME::Type 	2.22 	/usr/share/perl5/MIME/Type.pm
MIME::Types 	2.22 	/usr/share/perl5/MIME/Types.pm
MIME::Words 	5.509 	/usr/share/perl5/MIME/Words.pm
Module::Implementation 	0.09 	/usr/share/perl5/Module/Implementation.pm
Module::Load 	0.36 	/usr/share/perl/5.34/Module/Load.pm
Module::Runtime 	0.016 	/usr/share/perl5/Module/Runtime.pm
Module::Versions::Report 	1.06 	/usr/share/perl5/Module/Versions/Report.pm
mro 	1.25_001 	/usr/lib/x86_64-linux-gnu/perl/5.34/mro.pm
MRO::Compat 	0.15 	/usr/share/perl5/MRO/Compat.pm
namespace::autoclean 	0.29 	/usr/share/perl5/namespace/autoclean.pm
namespace::clean 	0.27 	/usr/share/perl5/namespace/clean.pm
Net::CIDR 	0.21 	/usr/share/perl5/Net/CIDR.pm
OSSP::uuid 	1.0602 	/usr/lib/x86_64-linux-gnu/perl5/5.34/OSSP/uuid.pm
overload 	1.33 	/usr/lib/x86_64-linux-gnu/perl-base/overload.pm
overloading 	0.02 	/usr/lib/x86_64-linux-gnu/perl-base/overloading.pm
Package::Stash 	0.39 	/usr/share/perl5/Package/Stash.pm
Package::Stash::XS 	0.29 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Package/Stash/XS.pm
Params::Util 	1.102 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Params/Util.pm
Params::Util::PP 	1.102 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Params/Util/PP.pm
Params::Validate 	1.30 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Params/Validate.pm
Params::Validate::Constants 	1.30 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Params/Validate/Constants.pm
Params::Validate::XS 	1.30 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Params/Validate/XS.pm
Params::ValidationCompiler 	0.30 	/usr/share/perl5/Params/ValidationCompiler.pm
Params::ValidationCompiler::Compiler 	0.30 	/usr/share/perl5/Params/ValidationCompiler/Compiler.pm
Params::ValidationCompiler::Exception::BadArguments 	1.1 	/usr/share/perl5/Exception/Class.pm
Params::ValidationCompiler::Exception::Named::Extra 	1.1 	/usr/share/perl5/Exception/Class.pm
Params::ValidationCompiler::Exception::Named::Required 	1.1 	/usr/share/perl5/Exception/Class.pm
Params::ValidationCompiler::Exception::Positional::Extra 	1.1 	/usr/share/perl5/Exception/Class.pm
Params::ValidationCompiler::Exception::Positional::Required 	1.1 	/usr/share/perl5/Exception/Class.pm
Params::ValidationCompiler::Exception::ValidationFailedForMooseTypeConstraint 	1.1 	/usr/share/perl5/Exception/Class.pm
Params::ValidationCompiler::Exceptions 	0.30 	/usr/share/perl5/Params/ValidationCompiler/Exceptions.pm
parent 	0.238 	/usr/lib/x86_64-linux-gnu/perl-base/parent.pm
PerlIO 	1.11 	/usr/share/perl/5.34/PerlIO.pm
PerlIO::encoding 	0.30 	/usr/lib/x86_64-linux-gnu/perl/5.34/PerlIO/encoding.pm
PerlIO::scalar 	0.31 	/usr/lib/x86_64-linux-gnu/perl/5.34/PerlIO/scalar.pm
Plack::Request 	1.0048 	/usr/share/perl5/Plack/Request.pm
Plack::Response 	1.0048 	/usr/share/perl5/Plack/Response.pm
POSIX 	1.97 	/usr/lib/x86_64-linux-gnu/perl-base/POSIX.pm
re 	0.41 	/usr/lib/x86_64-linux-gnu/perl-base/re.pm
Ref::Util 	0.204 	/usr/share/perl5/Ref/Util.pm
Ref::Util::XS 	0.117 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Ref/Util/XS.pm
Regexp::Common 	2017060201 	/usr/share/perl5/Regexp/Common.pm
Regexp::Common::_support 	2017060201 	/usr/share/perl5/Regexp/Common/_support.pm
Regexp::Common::balanced 	2017060201 	/usr/share/perl5/Regexp/Common/balanced.pm
Regexp::Common::CC 	2017060201 	/usr/share/perl5/Regexp/Common/CC.pm
Regexp::Common::comment 	2017060201 	/usr/share/perl5/Regexp/Common/comment.pm
Regexp::Common::delimited 	2017060201 	/usr/share/perl5/Regexp/Common/delimited.pm
Regexp::Common::lingua 	2017060201 	/usr/share/perl5/Regexp/Common/lingua.pm
Regexp::Common::list 	2017060201 	/usr/share/perl5/Regexp/Common/list.pm
Regexp::Common::net 	2017060201 	/usr/share/perl5/Regexp/Common/net.pm
Regexp::Common::net::CIDR 	0.03 	/usr/share/perl5/Regexp/Common/net/CIDR.pm
Regexp::Common::number 	2017060201 	/usr/share/perl5/Regexp/Common/number.pm
Regexp::Common::profanity 	2017060201 	/usr/share/perl5/Regexp/Common/profanity.pm
Regexp::Common::SEN 	2017060201 	/usr/share/perl5/Regexp/Common/SEN.pm
Regexp::Common::URI 	2017060201 	/usr/share/perl5/Regexp/Common/URI.pm
Regexp::Common::URI::fax 	2017060201 	/usr/share/perl5/Regexp/Common/URI/fax.pm
Regexp::Common::URI::file 	2017060201 	/usr/share/perl5/Regexp/Common/URI/file.pm
Regexp::Common::URI::ftp 	2017060201 	/usr/share/perl5/Regexp/Common/URI/ftp.pm
Regexp::Common::URI::gopher 	2017060201 	/usr/share/perl5/Regexp/Common/URI/gopher.pm
Regexp::Common::URI::http 	2017060201 	/usr/share/perl5/Regexp/Common/URI/http.pm
Regexp::Common::URI::news 	2017060201 	/usr/share/perl5/Regexp/Common/URI/news.pm
Regexp::Common::URI::pop 	2017060201 	/usr/share/perl5/Regexp/Common/URI/pop.pm
Regexp::Common::URI::prospero 	2017060201 	/usr/share/perl5/Regexp/Common/URI/prospero.pm
Regexp::Common::URI::RFC1035 	2017060201 	/usr/share/perl5/Regexp/Common/URI/RFC1035.pm
Regexp::Common::URI::RFC1738 	2017060201 	/usr/share/perl5/Regexp/Common/URI/RFC1738.pm
Regexp::Common::URI::RFC1808 	2017060201 	/usr/share/perl5/Regexp/Common/URI/RFC1808.pm
Regexp::Common::URI::RFC2384 	2017060201 	/usr/share/perl5/Regexp/Common/URI/RFC2384.pm
Regexp::Common::URI::RFC2396 	2017060201 	/usr/share/perl5/Regexp/Common/URI/RFC2396.pm
Regexp::Common::URI::RFC2806 	2017060201 	/usr/share/perl5/Regexp/Common/URI/RFC2806.pm
Regexp::Common::URI::tel 	2017060201 	/usr/share/perl5/Regexp/Common/URI/tel.pm
Regexp::Common::URI::telnet 	2017060201 	/usr/share/perl5/Regexp/Common/URI/telnet.pm
Regexp::Common::URI::tv 	2017060201 	/usr/share/perl5/Regexp/Common/URI/tv.pm
Regexp::Common::URI::wais 	2017060201 	/usr/share/perl5/Regexp/Common/URI/wais.pm
Regexp::Common::whitespace 	2017060201 	/usr/share/perl5/Regexp/Common/whitespace.pm
Regexp::Common::zip 	2017060201 	/usr/share/perl5/Regexp/Common/zip.pm
Regexp::IPv6 	0.03 	/usr/share/perl5/Regexp/IPv6.pm
Role::Basic 	0.13 	/usr/share/perl5/Role/Basic.pm
Role::Tiny 	2.002004 	/usr/share/perl5/Role/Tiny.pm
Role::Tiny::With 	2.002004 	/usr/share/perl5/Role/Tiny/With.pm
RT 	4.4.4+dfsg-2ubuntu1 	/usr/share/request-tracker4/lib/RT.pm
Scalar::Util 	1.61 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Scalar/Util.pm
Scope::Upper 	0.33 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Scope/Upper.pm
SelectSaver 	1.02 	/usr/lib/x86_64-linux-gnu/perl-base/SelectSaver.pm
Socket 	2.031 	/usr/lib/x86_64-linux-gnu/perl-base/Socket.pm
Specio 	0.47 	/usr/share/perl5/Specio.pm
Specio::Coercion 	0.47 	/usr/share/perl5/Specio/Coercion.pm
Specio::Constraint::AnyCan 	0.47 	/usr/share/perl5/Specio/Constraint/AnyCan.pm
Specio::Constraint::Enum 	0.47 	/usr/share/perl5/Specio/Constraint/Enum.pm
Specio::Constraint::ObjectCan 	0.47 	/usr/share/perl5/Specio/Constraint/ObjectCan.pm
Specio::Constraint::ObjectIsa 	0.47 	/usr/share/perl5/Specio/Constraint/ObjectIsa.pm
Specio::Constraint::Parameterizable 	0.47 	/usr/share/perl5/Specio/Constraint/Parameterizable.pm
Specio::Constraint::Parameterized 	0.47 	/usr/share/perl5/Specio/Constraint/Parameterized.pm
Specio::Constraint::Role::CanType 	0.47 	/usr/share/perl5/Specio/Constraint/Role/CanType.pm
Specio::Constraint::Role::Interface 	0.47 	/usr/share/perl5/Specio/Constraint/Role/Interface.pm
Specio::Constraint::Role::IsaType 	0.47 	/usr/share/perl5/Specio/Constraint/Role/IsaType.pm
Specio::Constraint::Simple 	0.47 	/usr/share/perl5/Specio/Constraint/Simple.pm
Specio::Constraint::Union 	0.47 	/usr/share/perl5/Specio/Constraint/Union.pm
Specio::Declare 	0.47 	/usr/share/perl5/Specio/Declare.pm
Specio::DeclaredAt 	0.47 	/usr/share/perl5/Specio/DeclaredAt.pm
Specio::Exception 	0.47 	/usr/share/perl5/Specio/Exception.pm
Specio::Exporter 	0.47 	/usr/share/perl5/Specio/Exporter.pm
Specio::Helpers 	0.47 	/usr/share/perl5/Specio/Helpers.pm
Specio::Library::Builtins 	0.47 	/usr/share/perl5/Specio/Library/Builtins.pm
Specio::Library::Numeric 	0.47 	/usr/share/perl5/Specio/Library/Numeric.pm
Specio::Library::String 	0.47 	/usr/share/perl5/Specio/Library/String.pm
Specio::OO 	0.47 	/usr/share/perl5/Specio/OO.pm
Specio::PartialDump 	0.47 	/usr/share/perl5/Specio/PartialDump.pm
Specio::Registry 	0.47 	/usr/share/perl5/Specio/Registry.pm
Specio::Role::Inlinable 	0.47 	/usr/share/perl5/Specio/Role/Inlinable.pm
Specio::TypeChecks 	0.47 	/usr/share/perl5/Specio/TypeChecks.pm
Storable 	3.23 	/usr/lib/x86_64-linux-gnu/perl/5.34/Storable.pm
Stream::Buffered 	0.03 	/usr/share/perl5/Stream/Buffered.pm
strict 	1.12 	/usr/lib/x86_64-linux-gnu/perl-base/strict.pm
Sub::Exporter 	0.988 	/usr/share/perl5/Sub/Exporter.pm
Sub::Exporter::Progressive 	0.001013 	/usr/share/perl5/Sub/Exporter/Progressive.pm
Sub::Identify 	0.14 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Sub/Identify.pm
Sub::Install 	0.928 	/usr/share/perl5/Sub/Install.pm
Sub::Name 	0.26 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Sub/Name.pm
Sub::Util 	1.61 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Sub/Util.pm
Symbol 	1.09 	/usr/lib/x86_64-linux-gnu/perl-base/Symbol.pm
Symbol::Global::Name 	0.05 	/usr/share/perl5/Symbol/Global/Name.pm
Sys::Syslog 	0.36 	/usr/lib/x86_64-linux-gnu/perl/5.34/Sys/Syslog.pm
Text::ParseWords 	3.30 	/usr/lib/x86_64-linux-gnu/perl-base/Text/ParseWords.pm
Text::Password::Pronounceable 	0.30 	/usr/share/perl5/Text/Password/Pronounceable.pm
Text::Template 	1.60 	/usr/share/perl5/Text/Template.pm
Text::Wrapper 	1.05 	/usr/share/perl5/Text/Wrapper.pm
Tie::Handle::Mason 	1.59 	
Tie::Hash 	1.05 	/usr/lib/x86_64-linux-gnu/perl-base/Tie/Hash.pm
Tie::Scalar 	1.05 	/usr/share/perl/5.34/Tie/Scalar.pm
Time::HiRes 	1.9767 	/usr/lib/x86_64-linux-gnu/perl/5.34/Time/HiRes.pm
Time::Local 	1.30 	/usr/share/perl/5.34/Time/Local.pm
Time::Zone 	2.24 	/usr/share/perl5/Time/Zone.pm
Tree::Simple 	1.34 	/usr/share/perl5/Tree/Simple.pm
Try::Tiny 	0.31 	/usr/share/perl5/Try/Tiny.pm
UNIVERSAL 	1.13 	/usr/share/perl/5.34/UNIVERSAL.pm
UNIVERSAL::require 	0.19 	/usr/share/perl5/UNIVERSAL/require.pm
URI 	5.10 	/usr/share/perl5/URI.pm
URI::_generic 	5.10 	/usr/share/perl5/URI/_generic.pm
URI::_query 	5.10 	/usr/share/perl5/URI/_query.pm
URI::_server 	5.10 	/usr/share/perl5/URI/_server.pm
URI::Escape 	5.10 	/usr/share/perl5/URI/Escape.pm
URI::file 	5.10 	/usr/share/perl5/URI/file.pm
URI::file::Base 	5.10 	/usr/share/perl5/URI/file/Base.pm
URI::file::Unix 	5.10 	/usr/share/perl5/URI/file/Unix.pm
URI::http 	5.10 	/usr/share/perl5/URI/http.pm
URI::WithBase 	5.10 	/usr/share/perl5/URI/WithBase.pm
utf8 	1.24 	/usr/lib/x86_64-linux-gnu/perl-base/utf8.pm
Variable::Magic 	0.62 	/usr/lib/x86_64-linux-gnu/perl5/5.34/Variable/Magic.pm
vars 	1.05 	/usr/lib/x86_64-linux-gnu/perl-base/vars.pm
warnings 	1.51 	/usr/lib/x86_64-linux-gnu/perl-base/warnings.pm
warnings::register 	1.04 	/usr/lib/x86_64-linux-gnu/perl-base/warnings/register.pm
WWW::Form::UrlEncoded 	0.26 	/usr/share/perl5/WWW/Form/UrlEncoded.pm
WWW::Form::UrlEncoded::XS 	0.26 	/usr/lib/x86_64-linux-gnu/perl5/5.34/WWW/Form/UrlEncoded/XS.pm
XSLoader 	0.30 	/usr/lib/x86_64-linux-gnu/perl-base/XSLoader.pm
XString 	0.005 	/usr/lib/x86_64-linux-gnu/perl5/5.34/XString.pm
RT upgrade history
RT (Current version: 4.4.4+dfsg-2ubuntu1)
  	Action 	Date 	Elapsed 	RT Version
	Insert from /usr/share/request-tracker4/etc/initialdata 	Tue May 23 16:15:43 2023 	0 seconds 	4.4.4+dfsg-2ubuntu1
Perl configuration

Summary of my perl5 (revision 5 version 34 subversion 0) configuration:
   
  Platform:
    osname=linux
    osvers=4.19.0
    archname=x86_64-linux-gnu-thread-multi
    uname='linux localhost 4.19.0 #1 smp debian 4.19.0 x86_64 gnulinux '
    config_args='-Dmksymlinks -Dusethreads -Duselargefiles -Dcc=x86_64-linux-gnu-gcc -Dcpp=x86_64-linux-gnu-cpp -Dld=x86_64-linux-gnu-gcc -Dccflags=-DDEBIAN -Wdate-time -D_FORTIFY_SOURCE=2 -g -O2 -ffile-prefix-map=/dummy/build/dir=. -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security -Dldflags= -Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -flto=auto -Wl,-z,relro -Dlddlflags=-shared -Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -flto=auto -Wl,-z,relro -Dcccdlflags=-fPIC -Darchname=x86_64-linux-gnu -Dprefix=/usr -Dprivlib=/usr/share/perl/5.34 -Darchlib=/usr/lib/x86_64-linux-gnu/perl/5.34 -Dvendorprefix=/usr -Dvendorlib=/usr/share/perl5 -Dvendorarch=/usr/lib/x86_64-linux-gnu/perl5/5.34 -Dsiteprefix=/usr/local -Dsitelib=/usr/local/share/perl/5.34.0 -Dsitearch=/usr/local/lib/x86_64-linux-gnu/perl/5.34.0 -Dman1dir=/usr/share/man/man1 -Dman3dir=/usr/share/man/man3 -Dsiteman1dir=/usr/local/man/man1 -Dsiteman3dir=/usr/local/man/man3 -Duse64bitint -Dman1ext=1 -Dman3ext=3perl -Dpager=/usr/bin/sensible-pager -Uafs -Ud_csh -Ud_ualarm -Uusesfio -Uusenm -Ui_libutil -Ui_xlocale -Uversiononly -DDEBUGGING=-g -Doptimize=-O2 -dEs -Duseshrplib -Dlibperl=libperl.so.5.34.0'
    hint=recommended
    useposix=true
    d_sigaction=define
    useithreads=define
    usemultiplicity=define
    use64bitint=define
    use64bitall=define
    uselongdouble=undef
    usemymalloc=n
    default_inc_excludes_dot=define
  Compiler:
    cc='x86_64-linux-gnu-gcc'
    ccflags ='-D_REENTRANT -D_GNU_SOURCE -DDEBIAN -fwrapv -fno-strict-aliasing -pipe -I/usr/local/include -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'
    optimize='-O2 -g'
    cppflags='-D_REENTRANT -D_GNU_SOURCE -DDEBIAN -fwrapv -fno-strict-aliasing -pipe -I/usr/local/include'
    ccversion=''
    gccversion='11.3.0'
    gccosandvers=''
    intsize=4
    longsize=8
    ptrsize=8
    doublesize=8
    byteorder=12345678
    doublekind=3
    d_longlong=define
    longlongsize=8
    d_longdbl=define
    longdblsize=16
    longdblkind=3
    ivtype='long'
    ivsize=8
    nvtype='double'
    nvsize=8
    Off_t='off_t'
    lseeksize=8
    alignbytes=8
    prototype=define
  Linker and Libraries:
    ld='x86_64-linux-gnu-gcc'
    ldflags =' -fstack-protector-strong -L/usr/local/lib'
    libpth=/usr/local/lib /usr/lib/x86_64-linux-gnu /usr/lib /lib/x86_64-linux-gnu /lib
    libs=-lgdbm -lgdbm_compat -ldb -ldl -lm -lpthread -lc -lcrypt
    perllibs=-ldl -lm -lpthread -lc -lcrypt
    libc=/lib/x86_64-linux-gnu/libc.so.6
    so=so
    useshrplib=true
    libperl=libperl.so.5.34
    gnulibc_version='2.35'
  Dynamic Linking:
    dlsrc=dl_dlopen.xs
    dlext=so
    d_dlsymun=undef
    ccdlflags='-Wl,-E'
    cccdlflags='-fPIC'
    lddlflags='-shared -L/usr/local/lib -fstack-protector-strong'


Environment variables
Variable 	Value
HOME 	/root
LANG 	en_GB.UTF-8
LANGUAGE 	en_GB:en
LOGNAME 	root
PATH 	/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
PERL_JSON_BACKEND 	Cpanel::JSON::XS
PHP_FCGI_CHILDREN 	15
PLACK_ENV 	deployment
PWD 	/root
QUERY_STRING 	
SHELL 	/bin/sh
Operating System
Deployment type 	fastcgi
Distribution 	Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.3 LTS
Release:	22.04
Codename:	jammy
uname -a 	Linux keeper 5.15.0-78-generic #85-Ubuntu SMP Fri Jul 7 15:25:09 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
Apache 	Server version: Apache/2.4.52 (Ubuntu)
Server built:   2023-05-03T20:02:51
Server's Module Magic Number: 20120211:126
Server loaded:  APR 1.7.0, APR-UTIL 1.6.1
Compiled using: APR 1.7.0, APR-UTIL 1.6.1
Architecture:   64-bit
Server MPM:     event
  threaded:     yes (fixed thread count)
    forked:     yes (variable process count)
Server compiled with....
 -D APR_HAS_SENDFILE
 -D APR_HAS_MMAP
 -D APR_HAVE_IPV6 (IPv4-mapped addresses enabled)
 -D APR_USE_PROC_PTHREAD_SERIALIZE
 -D APR_USE_PTHREAD_SERIALIZE
 -D SINGLE_LISTEN_UNSERIALIZED_ACCEPT
 -D APR_HAS_OTHER_CHILD
 -D AP_HAVE_RELIABLE_PIPED_LOGS
 -D DYNAMIC_MODULE_LIMIT=256
 -D HTTPD_ROOT="/etc/apache2"
 -D SUEXEC_BIN="/usr/lib/apache2/suexec"
 -D DEFAULT_PIDLOG="/var/run/apache2.pid"
 -D DEFAULT_SCOREBOARD="logs/apache_runtime_status"
 -D DEFAULT_ERRORLOG="logs/error_log"
 -D AP_TYPES_CONFIG_FILE="mime.types"
 -D SERVER_CONFIG_FILE="apache2.conf"
nginx 	nginx version: nginx/1.18.0 (Ubuntu)
built with OpenSSL 3.0.2 15 Mar 2022
TLS SNI support enabled
configure arguments: --with-cc-opt='-g -O2 -ffile-prefix-map=/build/nginx-zctdR4/nginx-1.18.0=. -flto=auto -ffat-lto-objects -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security -fPIC -Wdate-time -D_FORTIFY_SOURCE=2' --with-ld-opt='-Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -flto=auto -Wl,-z,relro -Wl,-z,now -fPIC' --prefix=/usr/share/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=/var/log/nginx/error.log --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --modules-path=/usr/lib/nginx/modules --http-client-body-temp-path=/var/lib/nginx/body --http-fastcgi-temp-path=/var/lib/nginx/fastcgi --http-proxy-temp-path=/var/lib/nginx/proxy --http-scgi-temp-path=/var/lib/nginx/scgi --http-uwsgi-temp-path=/var/lib/nginx/uwsgi --with-compat --with-debug --with-pcre-jit --with-http_ssl_module --with-http_stub_status_module --with-http_realip_module --with-http_auth_request_module --with-http_v2_module --with-http_dav_module --with-http_slice_module --with-threads --add-dynamic-module=/build/nginx-zctdR4/nginx-1.18.0/debian/modules/http-geoip2 --with-http_addition_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_sub_module

»|« RT 4.4.4+dfsg-2ubuntu1 (Debian) Copyright 1996-2019 Best Practical Solutions, LLC.

```