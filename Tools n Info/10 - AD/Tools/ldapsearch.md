
to make searches we need the base naming context - we can request this:
`ldapsearch -x -H ldap://10.129.170.211 -s base namingContexts`

get ALL data - warning ;)
`ldapsearch -x -H ldap://10.129.170.211 -D "svc-printer@return.local" -w '1edFg43012!!' -b "DC=return,DC=local"`

all users
`ldapsearch -x -H ldap://dc -D "user@domain.com" -w 'password' -b "dc=domain,dc=com" "(objectClass=user)" sAMAccountName description memberof`

user names for password spray:
`ldapsearch -x -H ldap://10.129.170.211 -D "svc-printer@return.local" -w '1edFg43012!!' -b "DC=return,DC=local" "(objectClass=person)"|grep sAMAccountName`


the first bit stays the same - here are some other search + filter examples:

computers
`"(objectClass=computer)" cn`

groups
`"(objectClass=group)" cn`

specific user
`"(sAMAccountName=john.doe)"`

members of a group
`"(cn=Admins)" member`

find users with SPNs (Kerberoast)
`"(&(objectClass=user)(servicePrincipalName=*))" sAMAccountName servicePrincipalName`

domain admins
`"(memberOf=CN=Domain Admins,CN=Users,DC=domain,DC=com)" sAMAccountName`

check for unconstrained delegation
`"(&(userAccountControl:1.2.840.113556.1.4.803:=524288))" sAMAccountName userAccountControl`
- `userAccountControl`: Bitmask attribute controlling account behavior
- `:1.2.840.113556.1.4.803:=524288`: Bitwise AND match for flag `TRUSTED_FOR_DELEGATION` (0x80000 = 524288)




`ldapsearch -x -H ldap://dc.example.com -D "user@example.com" -W -b "dc=example,dc=com"`
- `-x`: Simple bind
- `-H`: LDAP URI
- (`-h`): old syntax! replace with `-H`
- `-D`: Bind DN (user)
- `-W`: Prompt for password
- `-b`: Base DN

### Examples

```sh
┌──(fixit42㉿kali)-[~/shells]
└─$ ldapsearch -x -H ldap://10.129.170.211 -s base namingContexts 
# extended LDIF
#
# LDAPv3
# base <> (default) with scope baseObject
# filter: (objectclass=*)
# requesting: namingContexts 
#

#
dn:
namingContexts: DC=return,DC=local
namingContexts: CN=Configuration,DC=return,DC=local
namingContexts: CN=Schema,CN=Configuration,DC=return,DC=local
namingContexts: DC=DomainDnsZones,DC=return,DC=local
namingContexts: DC=ForestDnsZones,DC=return,DC=local

# search result
search: 2
result: 0 Success

# numResponses: 2
# numEntries: 1

```

```sh
┌──(fixit42㉿kali)-[~/shells]
└─$ ldapsearch -x -H ldap://printer -D "svc-printer@return.local" -w '1edFg43012!!' -b "dc=return,dc=local" "(objectClass=user)" sAMAccountName description
# extended LDIF
#
# LDAPv3
# base <dc=return,dc=local> with scope subtree
# filter: (objectClass=user)
# requesting: sAMAccountName description 
#

# Administrator, Users, return.local
dn: CN=Administrator,CN=Users,DC=return,DC=local
description: Built-in account for administering the computer/domain
sAMAccountName: Administrator

# Guest, Users, return.local
dn: CN=Guest,CN=Users,DC=return,DC=local
description: Built-in account for guest access to the computer/domain
sAMAccountName: Guest

# PRINTER, Domain Controllers, return.local
dn: CN=PRINTER,OU=Domain Controllers,DC=return,DC=local
sAMAccountName: PRINTER$

# krbtgt, Users, return.local
dn: CN=krbtgt,CN=Users,DC=return,DC=local
description: Key Distribution Center Service Account
sAMAccountName: krbtgt

# SVCPrinter, Users, return.local
dn: CN=SVCPrinter,CN=Users,DC=return,DC=local
description: Service Account for Printer
sAMAccountName: svc-printer

# search reference
ref: ldap://ForestDnsZones.return.local/DC=ForestDnsZones,DC=return,DC=local

# search reference
ref: ldap://DomainDnsZones.return.local/DC=DomainDnsZones,DC=return,DC=local

# search reference
ref: ldap://return.local/CN=Configuration,DC=return,DC=local

# search result
search: 2
result: 0 Success

# numResponses: 9
# numEntries: 5
# numReferences: 3
```

```sh
┌──(fixit42㉿kali)-[~/shells]
└─$ ldapsearch -x -H ldap://10.129.170.211 -D "svc-printer@return.local" -w '1edFg43012!!' -b "DC=return,DC=local" "(objectClass=person)"|grep sAMAccountName
sAMAccountName: Administrator
sAMAccountName: Guest
sAMAccountName: PRINTER$
sAMAccountName: krbtgt
sAMAccountName: svc-printer
```

### Help

```sh
┌──(fixit42㉿kali)-[~/shells]
└─$ ldapsearch -h                                                                  
ldapsearch: invalid option -- 'h'
ldapsearch: unrecognized option -h
usage: ldapsearch [options] [filter [attributes...]]
where:
  filter        RFC 4515 compliant LDAP search filter
  attributes    whitespace-separated list of attribute descriptions
    which may include:
      1.1   no attributes
      *     all user attributes
      +     all operational attributes
Search options:
  -a deref   one of never (default), always, search, or find
  -A         retrieve attribute names only (no values)
  -b basedn  base dn for search
  -c         continuous operation mode (do not stop on errors)
  -E [!]<ext>[=<extparam>] search extensions (! indicates criticality)
             [!]accountUsability         (NetScape Account usability)
             [!]domainScope              (domain scope)
             !dontUseCopy                (Don´t Use Copy)
             [!]mv=<filter>              (RFC 3876 matched values filter)
             [!]pr=<size>[/prompt|noprompt] (RFC 2696 paged results/prompt)
             [!]ps=<changetypes>/<changesonly>/<echg> (draft persistent search)
             [!]sss=[-]<attr[:OID]>[/[-]<attr[:OID]>...]
                                         (RFC 2891 server side sorting)
             [!]subentries[=true|false]  (RFC 3672 subentries)
             [!]sync=ro[/<cookie>]       (RFC 4533 LDAP Sync refreshOnly)
                     rp[/<cookie>][/<slimit>] (refreshAndPersist)
             [!]vlv=<before>/<after>(/<offset>/<count>|:<value>)
                                         (ldapv3-vlv-09 virtual list views)
             [!]deref=derefAttr:attr[,...][;derefAttr:attr[,...][;...]]
             !dirSync=<flags>/<maxAttrCount>[/<cookie>]
                                         (MS AD DirSync)
             [!]extendedDn=<flag>        (MS AD Extended DN
             [!]showDeleted              (MS AD Show Deleted)
             [!]serverNotif              (MS AD Server Notification)
             [!]<oid>[=:<value>|::<b64value>] (generic control; no response handling)
  -f file    read operations from 'file'
  -F prefix  URL prefix for files (default: file:///tmp/)
  -l limit   time limit (in seconds, or "none" or "max") for search
  -L         print responses in LDIFv1 format
  -LL        print responses in LDIF format without comments
  -LLL       print responses in LDIF format without comments
             and version
  -M         enable Manage DSA IT control (-MM to make critical)
  -P version protocol version (default: 3)
  -s scope   one of base, one, sub or children (search scope)
  -S attr    sort the results by attribute 'attr'
  -t         write binary values to files in temporary directory
  -tt        write all values to files in temporary directory
  -T path    write files to directory specified by path (default: /tmp)
  -u         include User Friendly entry names in the output
  -z limit   size limit (in entries, or "none" or "max") for search
Common options:
  -d level   set LDAP debugging level to 'level'
  -D binddn  bind DN
  -e [!]<ext>[=<extparam>] general extensions (! indicates criticality)
             [!]assert=<filter>     (RFC 4528; a RFC 4515 Filter string)
             [!]authzid=<authzid>   (RFC 4370; "dn:<dn>" or "u:<user>")
             [!]bauthzid            (RFC 3829)
             [!]chaining[=<resolveBehavior>[/<continuationBehavior>]]
                     one of "chainingPreferred", "chainingRequired",
                     "referralsPreferred", "referralsRequired"
             [!]manageDSAit         (RFC 3296)
             [!]noop
             ppolicy
             [!]postread[=<attrs>]  (RFC 4527; comma-separated attr list)
             [!]preread[=<attrs>]   (RFC 4527; comma-separated attr list)
             [!]relax
             [!]sessiontracking[=<username>]
             abandon, cancel, ignore (SIGINT sends abandon/cancel,
             or ignores response; if critical, doesn´t wait for SIGINT.
             not really controls)
  -H URI     LDAP Uniform Resource Identifier(s)
  -I         use SASL Interactive mode
  -n         show what would be done but don´t actually do it
  -N         do not use reverse DNS to canonicalize SASL host name
  -O props   SASL security properties
  -o <opt>[=<optparam>] any libldap ldap.conf options, plus
             ldif_wrap=<width> (in columns, or "no" for no wrapping)
             nettimeout=<timeout> (in seconds, or "none" or "max")
  -Q         use SASL Quiet mode
  -R realm   SASL realm
  -U authcid SASL authentication identity
  -v         run in verbose mode (diagnostics to standard output)
  -V         print version info (-VV only)
  -w passwd  bind password (for simple authentication)
  -W         prompt for bind password
  -x         Simple authentication
  -X authzid SASL authorization identity ("dn:<dn>" or "u:<user>")
  -y file    Read password from file
  -Y mech    SASL mechanism
  -Z         Start TLS request (-ZZ to require successful response)
```

