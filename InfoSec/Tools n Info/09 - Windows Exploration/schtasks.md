
`schtasks` lists all tasks

`schtasks /query /tn vulntask /fo list /v` get more info on one task

`schtasks /run /tn vulntask` start task (if perms)


start elevated command prompt - permissions needed
`schtasks /create /tn "Elevated Command Prompt" /tr "cmd.exe" /sc onlogon /rl highest`
`schtasks /run /tn "Elevated Command Prompt"`

`schtasks /create /tn "ElevatedCMD" /tr "cmd.exe" /sc once /st 00:00 /f /rl highest`
`schtasks /run /tn "ElevatedCMD"`

### Help Query

```sh
C:\Users\sofia>schtasks /query /?

SCHTASKS /Query [/S system [/U username [/P [password]]]]
         [/FO format | /XML [xml_type]] [/NH] [/V]
         [/TN taskname] [/HRESULT] [/?]

Description:
    Enables an administrator to display the scheduled tasks on the
    local or remote system.

Parameter List:
    /S    system         Specifies the remote system to connect to.

    /U    username       Specifies the user context under
                         which schtasks.exe should execute.

    /P    [password]     Specifies the password for the given
                         user context. Prompts for input if omitted.

    /FO   format         Specifies the format for the output.
                         Valid values: TABLE, LIST, CSV.

    /NH                  Specifies that the column header should not
                         be displayed in the output. This is
                         valid only for TABLE and CSV format.

    /V                   Displays verbose task output.

    /TN   taskname       Specifies the task path\name for which
                         to retrieve the information, else all of them.

    /XML  [xml_type]     Displays task definitions in XML format.

                         If xml_type is ONE then the output will be one valid XML file.

                         If xml_type is not present then the output will be

                         the concatenation of all XML task definitions.

    /HRESULT             For better diagnosability, the process exit code
                         will be in the HRESULT format.

    /?                   Displays this help message.

Examples:
    SCHTASKS /Query
    SCHTASKS /Query /?
    SCHTASKS /Query /S system /U user /P password
    SCHTASKS /Query /FO LIST /V /S system /U user /P password
    SCHTASKS /Query /FO TABLE /NH /V
```

### Help Create

```sh
C:\Users\THMBackup>schtasks /create /?

SCHTASKS /Create [/S system [/U username [/P [password]]]]
    [/RU username [/RP password]] /SC schedule [/MO modifier] [/D day]
    [/M months] [/I idletime] /TN taskname /TR taskrun [/ST starttime]
    [/RI interval] [ {/ET endtime | /DU duration} [/K] [/XML xmlfile] [/V1]]
    [/SD startdate] [/ED enddate] [/IT | /NP] [/Z] [/F] [/HRESULT] [/?]

Description:
    Enables an administrator to create scheduled tasks on a local or
    remote system.

Parameter List:
    /S   system        Specifies the remote system to connect to. If omitted
                       the system parameter defaults to the local system.

    /U   username      Specifies the user context under which SchTasks.exe
                       should execute.

    /P   [password]    Specifies the password for the given user context.
                       Prompts for input if omitted.

    /RU  username      Specifies the "run as" user account (user context)
                       under which the task runs. For the system account,
                       valid values are "", "NT AUTHORITY\SYSTEM"
                       or "SYSTEM".
                       For v2 tasks, "NT AUTHORITY\LOCALSERVICE" and
                       "NT AUTHORITY\NETWORKSERVICE" are also available as well
                       as the well known SIDs for all three.

    /RP  [password]    Specifies the password for the "run as" user.
                       To prompt for the password, the value must be either
                       "*" or none. This password is ignored for the
                       system account. Must be combined with either /RU or
                       /XML switch.

    /SC   schedule     Specifies the schedule frequency.
                       Valid schedule types: MINUTE, HOURLY, DAILY, WEEKLY,
                       MONTHLY, ONCE, ONSTART, ONLOGON, ONIDLE, ONEVENT.

    /MO   modifier     Refines the schedule type to allow finer control over
                       schedule recurrence. Valid values are listed in the
                       "Modifiers" section below.

    /D    days         Specifies the day of the week to run the task. Valid
                       values: MON, TUE, WED, THU, FRI, SAT, SUN and for
                       MONTHLY schedules 1 - 31 (days of the month).
                       Wildcard "*" specifies all days.

    /M    months       Specifies month(s) of the year. Defaults to the first
                       day of the month. Valid values: JAN, FEB, MAR, APR,
                       MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC. Wildcard "*"
                       specifies all months.

    /I    idletime     Specifies the amount of idle time to wait before
                       running a scheduled ONIDLE task.
                       Valid range: 1 - 999 minutes.

    /TN   taskname     Specifies the string in the form of path\name
                       which uniquely identifies this scheduled task.

    /TR   taskrun      Specifies the path and file name of the program to be
                       run at the scheduled time.
                       Example: C:\windows\system32\calc.exe

    /ST   starttime    Specifies the start time to run the task. The time
                       format is HH:mm (24 hour time) for example, 14:30 for
                       2:30 PM. Defaults to current time if /ST is not
                       specified.  This option is required with /SC ONCE.

    /RI   interval     Specifies the repetition interval in minutes. This is
                       not applicable for schedule types: MINUTE, HOURLY,
                       ONSTART, ONLOGON, ONIDLE, ONEVENT.
                       Valid range: 1 - 599940 minutes.
                       If either /ET or /DU is specified, then it defaults to
                       10 minutes.

    /ET   endtime      Specifies the end time to run the task. The time format
                       is HH:mm (24 hour time) for example, 14:50 for 2:50 PM.
                       This is not applicable for schedule types: ONSTART,
                       ONLOGON, ONIDLE, ONEVENT.

    /DU   duration     Specifies the duration to run the task. The time
                       format is HH:mm. This is not applicable with /ET and
                       for schedule types: ONSTART, ONLOGON, ONIDLE, ONEVENT.
                       For /V1 tasks, if /RI is specified, duration defaults
                       to 1 hour.

    /K                 Terminates the task at the endtime or duration time.
                       This is not applicable for schedule types: ONSTART,
                       ONLOGON, ONIDLE, ONEVENT. Either /ET or /DU must be
                       specified.

    /SD   startdate    Specifies the first date on which the task runs. The
                       format is mm/dd/yyyy. Defaults to the current
                       date. This is not applicable for schedule types: ONCE,
                       ONSTART, ONLOGON, ONIDLE, ONEVENT.

    /ED   enddate      Specifies the last date when the task should run. The
                       format is mm/dd/yyyy. This is not applicable for
                       schedule types: ONCE, ONSTART, ONLOGON, ONIDLE, ONEVENT.

    /EC   ChannelName  Specifies the event channel for OnEvent triggers.

    /IT                Enables the task to run interactively only if the /RU
                       user is currently logged on at the time the job runs.
                       This task runs only if the user is logged in.

    /NP                No password is stored.  The task runs non-interactively
                       as the given user.  Only local resources are available.

    /Z                 Marks the task for deletion after its final run.

    /XML  xmlfile      Creates a task from the task XML specified in a file.
                       Can be combined with /RU and /RP switches, or with /RP
                       alone, when task XML already contains the principal.

    /V1                Creates a task visible to pre-Vista platforms.
                       Not compatible with /XML.

    /F                 Forcefully creates the task and suppresses warnings if
                       the specified task already exists.

    /RL   level        Sets the Run Level for the job. Valid values are
                       LIMITED and HIGHEST. The default is LIMITED.

    /DELAY delaytime   Specifies the wait time to delay the running of the
                       task after the trigger is fired.  The time format is
                       mmmm:ss.  This option is only valid for schedule types
                       ONSTART, ONLOGON, ONEVENT.

    /HRESULT           For better diagnosability, the process exit code
                       will be in the HRESULT format.

    /?                 Displays this help message.

Modifiers: Valid values for the /MO switch per schedule type:
    MINUTE:  1 - 1439 minutes.
    HOURLY:  1 - 23 hours.
    DAILY:   1 - 365 days.
    WEEKLY:  weeks 1 - 52.
    ONCE:    No modifiers.
    ONSTART: No modifiers.
    ONLOGON: No modifiers.
    ONIDLE:  No modifiers.
    MONTHLY: 1 - 12, or
             FIRST, SECOND, THIRD, FOURTH, LAST, LASTDAY.

    ONEVENT:  XPath event query string.
Examples:
    ==> Creates a scheduled task "doc" on the remote machine "ABC"
        which runs notepad.exe every hour under user "runasuser".

        SCHTASKS /Create /S ABC /U user /P password /RU runasuser
                 /RP runaspassword /SC HOURLY /TN doc /TR notepad

    ==> Creates a scheduled task "accountant" on the remote machine
        "ABC" to run calc.exe every five minutes from the specified
        start time to end time between the start date and end date.

        SCHTASKS /Create /S ABC /U domain\user /P password /SC MINUTE
                 /MO 5 /TN accountant /TR calc.exe /ST 12:00 /ET 14:00
                 /SD 06/06/2006 /ED 06/06/2006 /RU runasuser /RP userpassword

    ==> Creates a scheduled task "gametime" to run freecell on the
        first Sunday of every month.

        SCHTASKS /Create /SC MONTHLY /MO first /D SUN /TN gametime
                 /TR c:\windows\system32\freecell

    ==> Creates a scheduled task "report" on remote machine "ABC"
        to run notepad.exe every week.

        SCHTASKS /Create /S ABC /U user /P password /RU runasuser
                 /RP runaspassword /SC WEEKLY /TN report /TR notepad.exe

    ==> Creates a scheduled task "logtracker" on remote machine "ABC"
        to run notepad.exe every five minutes starting from the
        specified start time with no end time. The /RP password will be
        prompted for.

        SCHTASKS /Create /S ABC /U domain\user /P password /SC MINUTE
                 /MO 5 /TN logtracker
                 /TR c:\windows\system32\notepad.exe /ST 18:30
                 /RU runasuser /RP

    ==> Creates a scheduled task "gaming" to run freecell.exe starting
        at 12:00 and automatically terminating at 14:00 hours every day

        SCHTASKS /Create /SC DAILY /TN gaming /TR c:\freecell /ST 12:00
                 /ET 14:00 /K
    ==> Creates a scheduled task "EventLog" to run wevtvwr.msc starting
        whenever event 101 is published in the System channel

        SCHTASKS /Create /TN EventLog /TR wevtvwr.msc /SC ONEVENT
                 /EC System /MO *[System/EventID=101]
    ==> Spaces in file paths can be used by using two sets of quotes, one
        set for CMD.EXE and one for SchTasks.exe.  The outer quotes for CMD
        need to be double quotes; the inner quotes can be single quotes or
        escaped double quotes:
        SCHTASKS /Create
           /tr "'c:\program files\internet explorer\iexplorer.exe'
           \"c:\log data\today.xml\"" ...
```