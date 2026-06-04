
https://github.com/volatilityfoundation/volatility

[[../../../Courses/Antisyphon Labs/Intro to SOC/2 - Memory Analysis (Volatility)|2 - Memory Analysis (Volatility)]]

Tool to check out volatile memory and hibernation files

Version 2 uses python 2 but sometimes works when ver 3 does not

https://github.com/MagnetForensics/Hibr2Bin

### volatility3 (python3)

https://github.com/volatilityfoundation/volatility3

`python3 vol.py -h`

demo environment 
#### help

```
thmanalyst@ip-10-114-169-218:/opt/volatility3$ python3 vol.py -h
Volatility 3 Framework 1.0.1
usage: volatility [-h] [-c CONFIG] [--parallelism [{processes,threads,off}]] [-e EXTEND] [-p PLUGIN_DIRS] [-s SYMBOL_DIRS]
                  [-v] [-l LOG] [-o OUTPUT_DIR] [-q] [-r RENDERER] [-f FILE] [--write-config] [--clear-cache]
                  [--cache-path CACHE_PATH] [--single-location SINGLE_LOCATION] [--stackers [STACKERS [STACKERS ...]]]
                  [--single-swap-locations [SINGLE_SWAP_LOCATIONS [SINGLE_SWAP_LOCATIONS ...]]]
                  plugin ...

An open-source memory forensics framework

optional arguments:
  -h, --help            Show this help message and exit, for specific plugin options use 'volatility <pluginname> --help'
  -c CONFIG, --config CONFIG
                        Load the configuration from a json file
  --parallelism [{processes,threads,off}]
                        Enables parallelism (defaults to off if no argument given)
  -e EXTEND, --extend EXTEND
                        Extend the configuration with a new (or changed) setting
  -p PLUGIN_DIRS, --plugin-dirs PLUGIN_DIRS
                        Semi-colon separated list of paths to find plugins
  -s SYMBOL_DIRS, --symbol-dirs SYMBOL_DIRS
                        Semi-colon separated list of paths to find symbols
  -v, --verbosity       Increase output verbosity
  -l LOG, --log LOG     Log output to a file as well as the console
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Directory in which to output any generated files
  -q, --quiet           Remove progress feedback
  -r RENDERER, --renderer RENDERER
                        Determines how to render the output (quick, csv, pretty, json, jsonl)
  -f FILE, --file FILE  Shorthand for --single-location=file:// if single-location is not defined
  --write-config        Write configuration JSON file out to config.json
  --clear-cache         Clears out all short-term cached items
  --cache-path CACHE_PATH
                        Change the default path (/home/thmanalyst/.cache/volatility3) used to store the cache
  --single-location SINGLE_LOCATION
                        Specifies a base location on which to stack
  --stackers [STACKERS [STACKERS ...]]
                        List of stackers
  --single-swap-locations [SINGLE_SWAP_LOCATIONS [SINGLE_SWAP_LOCATIONS ...]]
                        Specifies a list of swap layer URIs for use with single-location

Plugins:
  For plugin specific options, run 'volatility <plugin> --help'

  plugin
    banners.Banners     Attempts to identify potential linux banners in an image
    configwriter.ConfigWriter
                        Runs the automagics and both prints and outputs configuration in the output directory.
    frameworkinfo.FrameworkInfo
                        Plugin to list the various modular components of Volatility
    isfinfo.IsfInfo     Determines information about the currently available ISF files, or a specific one
    layerwriter.LayerWriter
                        Runs the automagics and writes out the primary layer produced by the stacker.
    linux.bash.Bash     Recovers bash command history from memory.
    linux.check_afinfo.Check_afinfo
                        Verifies the operation function pointers of network protocols.
    linux.check_creds.Check_creds
                        Checks if any processes are sharing credential structures
    linux.check_idt.Check_idt
                        Checks if the IDT has been altered
    linux.check_modules.Check_modules
                        Compares module list to sysfs info, if available
    linux.check_syscall.Check_syscall
                        Check system call table for hooks.
    linux.elfs.Elfs     Lists all memory mapped ELF files for all processes.
    linux.keyboard_notifiers.Keyboard_notifiers
                        Parses the keyboard notifier call chain
    linux.lsmod.Lsmod   Lists loaded kernel modules.
    linux.lsof.Lsof     Lists all memory maps for all processes.
    linux.malfind.Malfind
                        Lists process memory ranges that potentially contain injected code.
    linux.proc.Maps     Lists all memory maps for all processes.
    linux.pslist.PsList
                        Lists the processes present in a particular linux memory image.
    linux.pstree.PsTree
                        Plugin for listing processes in a tree based on their parent process ID.
    linux.tty_check.tty_check
                        Checks tty devices for hooks
    mac.bash.Bash       Recovers bash command history from memory.
    mac.check_syscall.Check_syscall
                        Check system call table for hooks.
    mac.check_sysctl.Check_sysctl
                        Check sysctl handlers for hooks.
    mac.check_trap_table.Check_trap_table
                        Check mach trap table for hooks.
    mac.ifconfig.Ifconfig
                        Lists loaded kernel modules
    mac.kauth_listeners.Kauth_listeners
                        Lists kauth listeners and their status
    mac.kauth_scopes.Kauth_scopes
                        Lists kauth scopes and their status
    mac.kevents.Kevents
                        Lists event handlers registered by processes
    mac.list_files.List_Files
                        Lists all open file descriptors for all processes.
    mac.lsmod.Lsmod     Lists loaded kernel modules.
    mac.lsof.Lsof       Lists all open file descriptors for all processes.
    mac.malfind.Malfind
                        Lists process memory ranges that potentially contain injected code.
    mac.mount.Mount     A module containing a collection of plugins that produce data typically foundin Mac's mount command
    mac.netstat.Netstat
                        Lists all network connections for all processes.
    mac.proc_maps.Maps  Lists process memory ranges that potentially contain injected code.
    mac.psaux.Psaux     Recovers program command line arguments.
    mac.pslist.PsList   Lists the processes present in a particular mac memory image.
    mac.pstree.PsTree   Plugin for listing processes in a tree based on their parent process ID.
    mac.socket_filters.Socket_filters
                        Enumerates kernel socket filters.
    mac.timers.Timers   Check for malicious kernel timers.
    mac.trustedbsd.Trustedbsd
                        Checks for malicious trustedbsd modules
    mac.vfsevents.VFSevents
                        Lists processes that are filtering file system events
    timeliner.Timeliner
                        Runs all relevant plugins that provide time related information and orders the results by time.
    windows.bigpools.BigPools
                        List big page pools.
    windows.cmdline.CmdLine
                        Lists process command line arguments.
    windows.dlllist.DllList
                        Lists the loaded modules in a particular windows memory image.
    windows.driverirp.DriverIrp
                        List IRPs for drivers in a particular windows memory image.
    windows.driverscan.DriverScan
                        Scans for drivers present in a particular windows memory image.
    windows.dumpfiles.DumpFiles
                        Dumps cached file contents from Windows memory samples.
    windows.envars.Envars
                        Display process environment variables
    windows.filescan.FileScan
                        Scans for file objects present in a particular windows memory image.
    windows.getservicesids.GetServiceSIDs
                        Lists process token sids.
    windows.getsids.GetSIDs
                        Print the SIDs owning each process
    windows.handles.Handles
                        Lists process open handles.
    windows.info.Info   Show OS & kernel details of the memory sample being analyzed.
    windows.malfind.Malfind
                        Lists process memory ranges that potentially contain injected code.
    windows.memmap.Memmap
                        Prints the memory map
    windows.modscan.ModScan
                        Scans for modules present in a particular windows memory image.
    windows.modules.Modules
                        Lists the loaded kernel modules.
    windows.mutantscan.MutantScan
                        Scans for mutexes present in a particular windows memory image.
    windows.netscan.NetScan
                        Scans for network objects present in a particular windows memory image.
    windows.netstat.NetStat
                        Traverses network tracking structures present in a particular windows memory image.
    windows.poolscanner.PoolScanner
                        A generic pool scanner plugin.
    windows.privileges.Privs
                        Lists process token privileges
    windows.pslist.PsList
                        Lists the processes present in a particular windows memory image.
    windows.psscan.PsScan
                        Scans for processes present in a particular windows memory image.
    windows.pstree.PsTree
                        Plugin for listing processes in a tree based on their parent process ID.
    windows.registry.certificates.Certificates
                        Lists the certificates in the registry's Certificate Store.
    windows.registry.hivelist.HiveList
                        Lists the registry hives present in a particular memory image.
    windows.registry.hivescan.HiveScan
                        Scans for registry hives present in a particular windows memory image.
    windows.registry.printkey.PrintKey
                        Lists the registry keys under a hive or specific key value.
    windows.registry.userassist.UserAssist
                        Print userassist registry keys and information.
    windows.ssdt.SSDT   Lists the system call table.
    windows.statistics.Statistics
    windows.strings.Strings
                        Reads output from the strings command and indicates which process(es) each string belongs to.
    windows.symlinkscan.SymlinkScan
                        Scans for links present in a particular windows memory image.
    windows.vadinfo.VadInfo
                        Lists process memory ranges.
    windows.virtmap.VirtMap
                        Lists virtual mapped sections.

The following plugins could not be loaded (use -vv to see why): volatility3.plugins.windows.cachedump,
volatility3.plugins.windows.callbacks, volatility3.plugins.windows.hashdump, volatility3.plugins.windows.lsadump,
volatility3.plugins.windows.svcscan, volatility3.plugins.windows.vadyarascan, volatility3.plugins.windows.verinfo,
volatility3.plugins.yarascan

```