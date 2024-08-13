
GNU Debugger
https://www.sourceware.org/gdb/

`gdb ./myexecutable`

gdb commands

`run` or r  Runs the program
`run <input to program>`
`start`  Starts the program but stopps at the start of main
`quit` or q  Quit gdb

`break [function name]` or b  Add breakpoint
`b test.c:10`  Example of setting breakpoint on C files line number!!  (probably requires compilation with debug info)
`next` or n Step one line
`nexti` or ni Step exactly one instruction
`continue` or c  Continue normal execution
`jump [address]` or `j`  Jump to address

`info frame`  Get register info
`info functions`  Get function info
`info registers` or `i r` Get register info

`disassemble [function name]`  disassemble a function

`print &[var name]` or `p` print adress of variable  (might require compilation with debug info)
`p [var name]`
`p/x` print in hex format, s for string... https://ftp.gnu.org/old-gnu/Manuals/gdb/html_node/gdb_54.html

`&sp`  Stack pointer ESP

`x/200 $rsp-200`

cool reverse commands!

## Examples

Starting program using start which sets an automatic break point at the start of main
```sh
(gdb) start
Temporary breakpoint 1 at 0x1161: file stack-heap.c, line 5.
Starting program: /home/kali/programming/c/stack-heap 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Temporary breakpoint 1, main () at stack-heap.c:5
5           char stack_string[10] = "stack";
```

Printing variable addresses and some contents (before var init)
```sh
(gdb) p &x
$1 = (int *) 0x7fffffffdd4c
(gdb) p x
$2 = 32767
(gdb) p &heap_string
$3 = (char **) 0x7fffffffdd40
(gdb) p heap_string
$4 = 0x0
(gdb) p &stack_string
$5 = (char (*)[10]) 0x7fffffffdd36
(gdb) p stack_string
$6 = "\000\000@l\376\367\377\177\000"
(gdb) p $sp
$7 = (void *) 0x7fffffffdd30
```

Printing 40 words in hex format starting at ESP position
```sh
(gdb) x/40x $sp
0x7fffffffdd30: 0x00000000      0x00000000      0xf7fe6c40      0x00007fff
0x7fffffffdd40: 0x00000000      0x00000000      0xf7ffdab0      0x00007fff
0x7fffffffdd50: 0x00000001      0x00000000      0xf7decc8a      0x00007fff
0x7fffffffdd60: 0xffffde50      0x00007fff      0x55555159      0x00005555
0x7fffffffdd70: 0x55554040      0x00000001      0xffffde68      0x00007fff
0x7fffffffdd80: 0xffffde68      0x00007fff      0xf0d81924      0x7f0b0946
0x7fffffffdd90: 0x00000000      0x00000000      0xffffde78      0x00007fff
0x7fffffffdda0: 0xf7ffd000      0x00007fff      0x55557dd8      0x00005555
0x7fffffffddb0: 0x4a1a1924      0x80f4f6b9      0x685e1924      0x80f4e6fb
0x7fffffffddc0: 0x00000000      0x00000000      0x00000000      0x00000000
```

## Help

```sh
Command class: running

advance -- Continue the program up to the given location (same form as args for break command).
attach -- Attach to a process or file outside of GDB.
continue, fg, c -- Continue program being debugged, after signal or breakpoint.
detach -- Detach a process or file previously attached.
detach checkpoint -- Detach from a checkpoint (experimental).
detach inferiors -- Detach from inferior ID (or list of IDS).
disconnect -- Disconnect from a target.
finish, fin -- Execute until selected stack frame returns.
handle -- Specify how to handle signals.
inferior -- Use this command to switch between inferiors.
interrupt -- Interrupt the execution of the debugged program.
jump, j -- Continue program being debugged at specified line or address.
kill -- Kill execution of program being debugged.
kill inferiors -- Kill inferior ID (or list of IDs).
next, n -- Step program, proceeding through subroutine calls.
nexti, ni -- Step one instruction, but proceed through subroutine calls.
queue-signal -- Queue a signal to be delivered to the current thread when it is resumed.
reverse-continue, rc -- Continue program being debugged but run it in reverse.
reverse-finish -- Execute backward until just before selected stack frame is called.
reverse-next, rn -- Step program backward, proceeding through subroutine calls.
reverse-nexti, rni -- Step backward one instruction, but proceed through called subroutines.
reverse-step, rs -- Step program backward until it reaches the beginning of another source line.
reverse-stepi, rsi -- Step backward exactly one instruction.
run, r -- Start debugged program.
signal -- Continue program with the specified signal.
start -- Start the debugged program stopping at the beginning of the main procedure.
starti -- Start the debugged program stopping at the first instruction.
step, s -- Step program until it reaches a different source line.
stepi, si -- Step one instruction exactly.
taas -- Apply a command to all threads (ignoring errors and empty output).
target -- Connect to a target machine or process.
target core -- Use a core file as a target.
target ctf -- (Use a CTF directory as a target.
target exec -- Use an executable file as a target.
target extended-remote -- Use a remote computer via a serial line, using a gdb-specific protocol.
target native -- Native process (started by the "run" command).
target record-btrace -- Collect control-flow trace and provide the execution history.
target record-core -- Log program while executing and replay execution from log.
target record-full -- Log program while executing and replay execution from log.
target remote -- Use a remote computer via a serial line, using a gdb-specific protocol.
target tfile -- Use a trace file as a target.
task -- Use this command to switch between Ada tasks.
task apply -- Apply a command to a list of tasks.
task apply all -- Apply a command to all tasks in the current inferior.
tfaas -- Apply a command to all frames of all threads (ignoring errors and empty output).
thread, t -- Use this command to switch between threads.
thread apply -- Apply a command to a list of threads.
thread apply all -- Apply a command to all threads.
thread find -- Find threads that match a regular expression.
thread name -- Set the current thread´s name.
until, u -- Execute until past the current line or past a LOCATION.
```

```sh
┌──(kali㉿kali)-[~]
└─$ gdb -h                
This is the GNU debugger.  Usage:

    gdb [options] [executable-file [core-file or process-id]]
    gdb [options] --args executable-file [inferior-arguments ...]

Selection of debuggee and its files:

  --args             Arguments after executable-file are passed to inferior.
  --core=COREFILE    Analyze the core dump COREFILE.
  --exec=EXECFILE    Use EXECFILE as the executable.
  --pid=PID          Attach to running process PID.
  --directory=DIR    Search for source files in DIR.
  --se=FILE          Use FILE as symbol file and executable file.
  --symbols=SYMFILE  Read symbols from SYMFILE.
  --readnow          Fully read symbol files on first access.
  --readnever        Do not read symbol files.
  --write            Set writing into executable and core files.

Initial commands and command files:

  --command=FILE, -x Execute GDB commands from FILE.
  --init-command=FILE, -ix
                     Like -x but execute commands before loading inferior.
  --eval-command=COMMAND, -ex
                     Execute a single GDB command.
                     May be used multiple times and in conjunction
                     with --command.
  --init-eval-command=COMMAND, -iex
                     Like -ex but before loading inferior.
  --nh               Do not read ~/.gdbinit.
  --nx               Do not read any .gdbinit files in any directory.

Output and user interface control:

  --fullname         Output information used by emacs-GDB interface.
  --interpreter=INTERP
                     Select a specific interpreter / user interface.
  --tty=TTY          Use TTY for input/output by the program being debugged.
  -w                 Use the GUI interface.
  --nw               Do not use the GUI interface.
  --tui              Use a terminal user interface.
  -q, --quiet, --silent
                     Do not print version number on startup.

Operating modes:

  --batch            Exit after processing options.
  --batch-silent     Like --batch, but suppress all gdb stdout output.
  --return-child-result
                     GDB exit code will be the child´s exit code.
  --configuration    Print details about GDB configuration and then exit.
  --help             Print this message and then exit.
  --version          Print version information and then exit.

Remote debugging options:

  -b BAUDRATE        Set serial port baud rate used for remote debugging.
  -l TIMEOUT         Set timeout in seconds for remote debugging.

Other options:

  --cd=DIR           Change current directory to DIR.
  --data-directory=DIR, -D
                     Set GDB´s data-directory to DIR.

At startup, GDB reads the following early init files and executes their
commands:
   None found.

At startup, GDB reads the following init files and executes their commands:
   * system-wide init files: /etc/gdb/gdbinit

For more information, type "help" from within GDB, or consult the
GDB manual (available as on-line info or a printed manual).

Report bugs to <https://www.gnu.org/software/gdb/bugs/>.

You can ask GDB-related questions on the GDB users mailing list
(gdb@sourceware.org) or on GDB´s IRC channel (#gdb on Freenode).

```

```sh
aliases -- User-defined aliases of other commands.
breakpoints -- Making program stop at certain points.
data -- Examining data.
files -- Specifying and examining files.
internals -- Maintenance commands.
obscure -- Obscure features.
running -- Running the program.
stack -- Examining the stack.
status -- Status inquiries.
support -- Support facilities.
text-user-interface -- TUI is the GDB text based interface.
tracepoints -- Tracing of program execution without stopping the program.
user-defined -- User-defined commands.
```

```sh
(gdb) help all

Command class: aliases


Command class: breakpoints

awatch -- Set an access watchpoint for EXPRESSION.
break, brea, bre, br, b -- Set breakpoint at specified location.
break-range -- Set a breakpoint for an address range.
catch -- Set catchpoints to catch events.
catch assert -- Catch failed Ada assertions, when raised.
catch catch -- Catch an exception, when caught.
catch exception -- Catch Ada exceptions, when raised.
catch exec -- Catch calls to exec.
catch fork -- Catch calls to fork.
catch handlers -- Catch Ada exceptions, when handled.
catch load -- Catch loads of shared libraries.
catch rethrow -- Catch an exception, when rethrown.
catch signal -- Catch signals by their names and/or numbers.
catch syscall -- Catch system calls by their names, groups and/or numbers.
catch throw -- Catch an exception, when thrown.
catch unload -- Catch unloads of shared libraries.
catch vfork -- Catch calls to vfork.
clear, cl -- Clear breakpoint at specified location.
commands -- Set commands to be executed when the given breakpoints are hit.
condition -- Specify breakpoint number N to break only if COND is true.
delete, del, d -- Delete all or some breakpoints.
delete bookmark -- Delete a bookmark from the bookmark list.
delete breakpoints -- Delete all or some breakpoints or auto-display expressions.
delete checkpoint -- Delete a checkpoint (experimental).
delete display -- Cancel some expressions to be displayed when program stops.
delete mem -- Delete memory region.
delete tracepoints, delete tr -- Delete specified tracepoints.
delete tvariable -- Delete one or more trace state variables.
disable, disa, dis -- Disable all or some breakpoints.
disable breakpoints -- Disable all or some breakpoints.
disable display -- Disable some expressions to be displayed when program stops.
disable frame-filter -- GDB command to disable the specified frame-filter.
disable mem -- Disable memory region.
disable pretty-printer -- GDB command to disable the specified pretty-printer.
disable probes -- Disable probes.
disable type-printer -- GDB command to disable the specified type-printer.
disable unwinder -- GDB command to disable the specified unwinder.
disable xmethod -- GDB command to disable a specified (group of) xmethod(s).
dprintf -- Set a dynamic printf at specified location.
enable, en -- Enable all or some breakpoints.
enable breakpoints -- Enable all or some breakpoints.
enable breakpoints count -- Enable some breakpoints for COUNT hits.
enable breakpoints delete -- Enable some breakpoints and delete when hit.
enable breakpoints once -- Enable some breakpoints for one hit.
enable count -- Enable some breakpoints for COUNT hits.
enable delete -- Enable some breakpoints and delete when hit.
enable display -- Enable some expressions to be displayed when program stops.
enable frame-filter -- GDB command to enable the specified frame-filter.
enable mem -- Enable memory region.
enable once -- Enable some breakpoints for one hit.
enable pretty-printer -- GDB command to enable the specified pretty-printer.
enable probes -- Enable probes.
enable type-printer -- GDB command to enable the specified type printer.
enable unwinder -- GDB command to enable unwinders.
enable xmethod -- GDB command to enable a specified (group of) xmethod(s).
ftrace -- Set a fast tracepoint at specified location.
hbreak -- Set a hardware assisted breakpoint.
ignore -- Set ignore-count of breakpoint number N to COUNT.
rbreak -- Set a breakpoint for all functions matching REGEXP.
rwatch -- Set a read watchpoint for EXPRESSION.
save -- Save breakpoint definitions as a script.
save breakpoints -- Save current breakpoint definitions as a script.
save gdb-index -- Save a gdb-index file.
save tracepoints -- Save current tracepoint definitions as a script.
skip -- Ignore a function while stepping.
skip delete -- Delete skip entries.
skip disable -- Disable skip entries.
skip enable -- Enable skip entries.
skip file -- Ignore a file while stepping.
skip function -- Ignore a function while stepping.
strace -- Set a static tracepoint at location or marker.
tbreak -- Set a temporary breakpoint.
tcatch -- Set temporary catchpoints to catch events.
tcatch assert -- Catch failed Ada assertions, when raised.
tcatch catch -- Catch an exception, when caught.
tcatch exception -- Catch Ada exceptions, when raised.
tcatch exec -- Catch calls to exec.
tcatch fork -- Catch calls to fork.
tcatch handlers -- Catch Ada exceptions, when handled.
tcatch load -- Catch loads of shared libraries.
tcatch rethrow -- Catch an exception, when rethrown.
tcatch signal -- Catch signals by their names and/or numbers.
tcatch syscall -- Catch system calls by their names, groups and/or numbers.
tcatch throw -- Catch an exception, when thrown.
tcatch unload -- Catch unloads of shared libraries.
tcatch vfork -- Catch calls to vfork.
thbreak -- Set a temporary hardware assisted breakpoint.
trace, trac, tra, tr, tp -- Set a tracepoint at specified location.
watch -- Set a watchpoint for EXPRESSION.

Command class: data

agent-printf -- Target agent only formatted printing, like the C "printf" function.
append -- Append target code/data to a local file.
append binary -- Append target code/data to a raw binary file.
append binary memory -- Append contents of memory to a raw binary file.
append binary value -- Append the value of an expression to a raw binary file.
append memory -- Append contents of memory to a raw binary file.
append value -- Append the value of an expression to a raw binary file.
call -- Call a function in the program.
disassemble -- Disassemble a specified section of memory.
display -- Print value of expression EXP each time the program stops.
dump -- Dump target code/data to a local file.
dump binary -- Write target code/data to a raw binary file.
dump binary memory -- Write contents of memory to a raw binary file.
dump binary value -- Write the value of an expression to a raw binary file.
dump ihex -- Write target code/data to an intel hex file.
dump ihex memory -- Write contents of memory to an ihex file.
dump ihex value -- Write the value of an expression to an ihex file.
dump memory -- Write contents of memory to a raw binary file.
dump srec -- Write target code/data to an srec file.
dump srec memory -- Write contents of memory to an srec file.
dump srec value -- Write the value of an expression to an srec file.
dump tekhex -- Write target code/data to a tekhex file.
dump tekhex memory -- Write contents of memory to a tekhex file.
dump tekhex value -- Write the value of an expression to a tekhex file.
dump value -- Write the value of an expression to a raw binary file.
dump verilog -- Write target code/data to a verilog hex file.
dump verilog memory -- Write contents of memory to a verilog hex file.
dump verilog value -- Write the value of an expression to a verilog hex file.
explore -- Explore a value or a type valid in the current context.
explore type -- Explore a type or the type of an expression.
explore value -- Explore value of an expression valid in the current context.
find -- Search memory for a sequence of bytes.
init-if-undefined -- Initialize a convenience variable if necessary.
mem -- Define attributes for memory region or reset memory region handling to target-based.
memory-tag -- Generic command for printing and manipulating memory tag properties.
memory-tag check -- Validate a pointer´s logical tag against the allocation tag.
memory-tag print-allocation-tag -- Print the allocation tag for ADDRESS.
memory-tag print-logical-tag -- Print the logical tag from POINTER.
memory-tag set-allocation-tag -- Set the allocation tag(s) for a memory range.
memory-tag with-logical-tag -- Print a POINTER with a specific logical TAG.
output -- Like "print" but don't put in value history and don't print newline.
print, inspect, p -- Print value of expression EXP.
print-object, po -- Ask an Objective-C object to print itself.
printf -- Formatted printing, like the C "printf" function.
ptype -- Print definition of type TYPE.
restore -- Restore the contents of FILE to target memory.
set -- Evaluate expression EXP and assign result to variable VAR.
set ada -- Prefix command for changing Ada-specific settings.
set ada print-signatures -- Enable or disable the output of formal and return types for functions in the overloads selection menu.
set ada source-charset -- Set the Ada source character set.
set ada trust-PAD-over-XVS -- Enable or disable an optimization trusting PAD types over XVS types.
set agent -- Set debugger´s willingness to use agent as a helper.
set annotate -- Set annotation_level.
set architecture, set processor -- Set architecture of target.
set args -- Set argument list to give program being debugged when it is started.
set auto-connect-native-target -- Set whether GDB may automatically connect to the native target.
set auto-load -- Auto-loading specific settings.
set auto-load gdb-scripts -- Enable or disable auto-loading of canned sequences of commands scripts.
set auto-load libthread-db -- Enable or disable auto-loading of inferior specific libthread_db.
set auto-load local-gdbinit -- Enable or disable auto-loading of .gdbinit script in current directory.
set auto-load python-scripts -- Set the debugger´s behaviour regarding auto-loaded Python scripts.
set auto-load safe-path -- Set the list of files and directories that are safe for auto-loading.
set auto-load scripts-directory -- Set the list of directories from which to load auto-loaded scripts.
set auto-solib-add -- Set autoloading of shared library symbols.
set backtrace -- Set backtrace specific variables.
set backtrace limit -- Set an upper bound on the number of backtrace levels.
set backtrace past-entry -- Set whether backtraces should continue past the entry point of a program.
set backtrace past-main -- Set whether backtraces should continue past "main".
set basenames-may-differ -- Set whether a source file may have multiple base names.
set breakpoint -- Breakpoint specific settings.
set breakpoint always-inserted -- Set mode for inserting breakpoints.
set breakpoint auto-hw -- Set automatic usage of hardware breakpoints.
set breakpoint condition-evaluation -- Set mode of breakpoint condition evaluation.
set breakpoint pending -- Set debugger´s behavior regarding pending breakpoints.
set can-use-hw-watchpoints -- Set debugger´s willingness to use watchpoint hardware.
set case-sensitive -- Set case sensitivity in name search (on/off/auto).
set charset -- Set the host and target character sets.
set check, set ch, set c -- Set the status of the type/range checker.
set check range -- Set range checking (on/warn/off/auto).
set check type -- Set strict type checking.
set circular-trace-buffer -- Set target´s use of circular trace buffer.
set code-cache -- Set cache use for code segment access.
set coerce-float-to-double -- Set coercion of floats to doubles when calling functions.
set compile-args -- Set compile command GCC command-line arguments.
set compile-gcc -- Set compile command GCC driver filename.
set complaints -- Set max number of complaints about incorrect symbols.
set confirm -- Set whether to confirm potentially dangerous operations.
set cp-abi -- Set the ABI used for inspecting C++ objects.
set cwd -- Set the current working directory to be used when the inferior is started.
set data-directory -- Set GDB´s data directory.
set dcache -- Use this command to set number of lines in dcache and line-size.
set dcache line-size -- Set dcache line size in bytes (must be power of 2).
set dcache size -- Set number of dcache lines.
set debug -- Generic command for setting gdb debugging flags.
set debug arch -- Set architecture debugging.
set debug auto-load -- Set auto-load verifications debugging.
set debug bfd-cache -- Set bfd cache debugging.
set debug check-physname -- Set cross-checking of "physname" code against demangler.
set debug coff-pe-read -- Set coff PE read debugging.
set debug compile -- Set compile command debugging.
set debug compile-cplus-scopes -- Set debugging of C++ compile scopes.
set debug compile-cplus-types -- Set debugging of C++ compile type conversion.
set debug displaced -- Set displaced stepping debugging.
set debug dwarf-die -- Set debugging of the DWARF DIE reader.
set debug dwarf-line -- Set debugging of the dwarf line reader.
set debug dwarf-read -- Set debugging of the DWARF reader.
set debug entry-values -- Set entry values and tail call frames debugging.
set debug event-loop -- Set event-loop debugging.
set debug expression -- Set expression debugging.
set debug fortran-array-slicing -- Set debugging of Fortran array slicing.
set debug frame -- Set frame debugging.
set debug index-cache -- Set display of index-cache debug messages.
set debug infcall -- Set inferior call debugging.
set debug infrun -- Set inferior debugging.
set debug jit -- Set JIT debugging.
set debug libthread-db -- Set libthread-db debugging.
set debug linux-namespaces -- Set debugging of GNU/Linux namespaces module.
set debug linux-nat -- Set debugging of GNU/Linux native target.
set debug notification -- Set debugging of async remote notification.
set debug observer -- Set observer debugging.
set debug overload -- Set debugging of C++ overloading.
set debug parser -- Set parser debugging.
set debug py-breakpoint -- Set Python breakpoint debugging.
set debug py-micmd -- Set Python micmd debugging.
set debug py-unwind -- Set Python unwinder debugging.
set debug record -- Set debugging of record/replay feature.
set debug remote -- Set debugging of remote protocol.
set debug remote-packet-max-chars -- Set the maximum number of characters to display for each remote packet.
set debug separate-debug-file -- Set printing of separate debug info file search debug.
set debug serial -- Set serial debugging.
set debug skip -- Set whether to print the debug output about skipping files and functions.
set debug solib -- Set solib debugging.
set debug stap-expression -- Set SystemTap expression debugging.
set debug symbol-lookup -- Set debugging of symbol lookup.
set debug symfile -- Set debugging of the symfile functions.
set debug symtab-create -- Set debugging of symbol table creation.
set debug target -- Set target debugging.
set debug threads -- Set thread debugging.
set debug timestamp -- Set timestamping of debugging messages.
set debug tui -- Set tui debugging.
set debug varobj -- Set varobj debugging.
set debug xml -- Set XML parser debugging.
set debug-file-directory -- Set the directories where separate debug symbols are searched for.
set debuginfod -- Set debuginfod options.
set debuginfod enabled -- Set whether to use debuginfod.
set debuginfod urls -- Set the list of debuginfod server URLs.
set debuginfod verbose -- Set verbosity of debuginfod output.
set default-collect -- Set the list of expressions to collect by default.
set demangle-style -- Set the current C++ demangling style.
set detach-on-fork -- Set whether gdb will detach the child of a fork.
set directories -- Set the search path for finding source files.
set disable-randomization -- Set disabling of debuggee´s virtual address space randomization.
set disassemble-next-line -- Set whether to disassemble next source line or insn when execution stops.
set disassembler-options -- Set the disassembler options.
set disassembly-flavor -- Set the disassembly flavor.
set disconnected-dprintf -- Set whether dprintf continues after GDB disconnects.
set disconnected-tracing -- Set whether tracing continues after GDB disconnects.
set displaced-stepping -- Set debugger´s willingness to use displaced stepping.
set dprintf-channel -- Set the channel to use for dynamic printf.
set dprintf-function -- Set the function to use for dynamic printf.
set dprintf-style -- Set the style of usage for dynamic printf.
set dump-excluded-mappings -- Set whether gcore should dump mappings marked with the VM_DONTDUMP flag.
set editing -- Set editing of command lines as they are typed.
set endian -- Set endianness of target.
set environment -- Set environment variable value to give the program.
set exec-direction -- Set direction of execution.
set exec-done-display -- Set notification of completion for asynchronous execution commands.
set exec-file-mismatch -- Set exec-file-mismatch handling (ask|warn|off).
set exec-wrapper -- Set a wrapper for running programs.
set extended-prompt -- Set the extended prompt.
set extension-language -- Set mapping between filename extension and source language.
set filename-display -- Set how to display filenames.
set follow-exec-mode -- Set debugger response to a program call of exec.
set follow-fork-mode -- Set debugger response to a program call of fork or vfork.
set fortran -- Prefix command for changing Fortran-specific settings.
set fortran repack-array-slices -- Enable or disable repacking of non-contiguous array slices.
set frame-filter -- Prefix command for 'set' frame-filter related operations.
set frame-filter priority -- GDB command to set the priority of the specified frame-filter.
set gnutarget, set g -- Set the current BFD target.
set guile, set gu -- Prefix command for Guile preference settings.
set guile print-stack -- Set mode for Guile exception printing on error.
set height -- Set number of lines in a page for GDB output pagination.
set history -- Generic command for setting command history parameters.
set history expansion -- Set history expansion on command input.
set history filename -- Set the filename in which to record the command history.
set history remove-duplicates -- Set how far back in history to look for and remove duplicate entries.
set history save -- Set saving of the history record on exit.
set history size -- Set the size of the command history.
set host-charset -- Set the host character set.
set index-cache -- Set index-cache options.
set index-cache directory -- Set the directory of the index cache.
set index-cache enabled -- Enable the index cache.
set inferior-tty, tty -- Set terminal for future runs of program being debugged.
set input-radix -- Set default input radix for entering numbers.
set interactive-mode -- Set whether GDB´s standard input is a terminal.
set language -- Set the current source language.
set libthread-db-search-path -- Set search path for libthread_db.
set listsize -- Set number of source lines gdb will list by default.
set logging -- Set logging options.
set logging debugredirect -- Set the logging debug output mode.
set logging enabled -- Enable logging.
set logging file -- Set the current logfile.
set logging overwrite -- Set whether logging overwrites or appends to the log file.
set logging redirect -- Set the logging output mode.
set max-completions -- Set maximum number of completion candidates.
set max-user-call-depth -- Set the max call depth for non-python/scheme user-defined commands.
set max-value-size -- Set maximum sized value gdb will load from the inferior.
set may-call-functions -- Set permission to call functions in the program.
set may-insert-breakpoints -- Set permission to insert breakpoints in the target.
set may-insert-fast-tracepoints -- Set permission to insert fast tracepoints in the target.
set may-insert-tracepoints -- Set permission to insert tracepoints in the target.
set may-interrupt -- Set permission to interrupt or signal the target.
set may-write-memory -- Set permission to write into target memory.
set may-write-registers -- Set permission to write into registers.
set mem -- Memory regions settings.
set mem inaccessible-by-default -- Set handling of unknown memory regions.
set mi-async -- Set whether MI asynchronous mode is enabled.
set mpx -- Set Intel Memory Protection Extensions specific variables.
set mpx bound -- Set the memory bounds for a given array/pointer storage in the bound table.
set multiple-symbols -- Set how the debugger handles ambiguities in expressions.
set non-stop -- Set whether gdb controls the inferior in non-stop mode.
set observer -- Set whether gdb controls the inferior in observer mode.
set opaque-type-resolution -- Set resolution of opaque struct/class/union types (if set before loading symbols).
set osabi -- Set OS ABI of target.
set output-radix -- Set default output radix for printing of values.
set overload-resolution -- Set overload resolution in evaluating C++ functions.
set pagination -- Set state of GDB output pagination.
set print, set pr, set p -- Generic command for setting how things print.
set print address -- Set printing of addresses.
set print array -- Set pretty formatting of arrays.
set print array-indexes -- Set printing of array indexes.
set print asm-demangle -- Set demangling of C++/ObjC names in disassembly listings.
set print demangle -- Set demangling of encoded C++/ObjC names when displaying symbols.
set print elements -- Set limit on string chars or array elements to print.
set print entry-values -- Set printing of function arguments at function entry.
set print finish -- Set whether 'finish' prints the return value.
set print frame-arguments -- Set printing of non-scalar frame arguments.
set print frame-info -- Set printing of frame information.
set print inferior-events -- Set printing of inferior events (such as inferior start and exit).
set print max-depth -- Set maximum print depth for nested structures, unions and arrays.
set print max-symbolic-offset -- Set the largest offset that will be printed in <SYMBOL+1234> form.
set print memory-tag-violations -- Set printing of memory tag violations for pointers.
set print nibbles -- Set whether to print binary values in groups of four bits.
set print null-stop -- Set printing of char arrays to stop at first null char.
set print object -- Set printing of C++ virtual function tables.
set print pascal_static-members -- Set printing of pascal static members.
set print pretty -- Set pretty formatting of structures.
set print raw-frame-arguments -- Set whether to print frame arguments in raw form.
set print raw-values -- Set whether to print values in raw form.
set print repeats -- Set threshold for repeated print elements.
set print sevenbit-strings -- Set printing of 8-bit characters in strings as \nnn.
set print static-members -- Set printing of C++ static members.
set print symbol -- Set printing of symbol names when printing pointers.
set print symbol-filename -- Set printing of source filename and line number with <SYMBOL>.
set print symbol-loading -- Set printing of symbol loading messages.
set print thread-events -- Set printing of thread events (such as thread start and exit).
set print type -- Generic command for showing type-printing settings.
set print type hex -- Set printing of struct members sizes and offsets using hex notation.
set print type methods -- Set printing of methods defined in classes.
set print type nested-type-limit -- Set the number of recursive nested type definitions to print ("unlimited" or -1 to show all).
set print type typedefs -- Set printing of typedefs defined in classes.
set print union -- Set printing of unions interior to structures.
set print vtbl -- Set printing of C++ virtual function tables.
set prompt -- Set gdb´s prompt.
set python -- Prefix command for python preference settings.
set python dont-write-bytecode -- Set whether the Python interpreter should avoid byte-compiling python modules.
set python ignore-environment -- Set whether the Python interpreter should ignore environment variables.
set python print-stack -- Set mode for Python stack dump on error.
set radix -- Set default input and output number radices.
set range-stepping -- Enable or disable range stepping.
set ravenscar -- Prefix command for changing Ravenscar-specific settings.
set ravenscar task-switching -- Enable or disable support for GNAT Ravenscar tasks.
set record, set rec -- Set record options.
set record btrace -- Set record options.
set record btrace bts -- Set record btrace bts options.
set record btrace bts buffer-size -- Set the record/replay bts buffer size.
set record btrace cpu -- Set the cpu to be used for trace decode.
set record btrace cpu auto -- Automatically determine the cpu to be used for trace decode.
set record btrace cpu none -- Do not enable errata workarounds for trace decode.
set record btrace pt -- Set record btrace pt options.
set record btrace pt buffer-size -- Set the record/replay pt buffer size.
set record btrace replay-memory-access -- Set what memory accesses are allowed during replay.
set record full -- Set record options.
set record full insn-number-max -- Set record/replay buffer limit.
set record full memory-query -- Set whether query if PREC cannot record memory change of next instruction.
set record full stop-at-limit -- Set whether record/replay stops when record/replay buffer becomes full.
set record function-call-history-size -- Set number of function to print in "record function-call-history".
set record instruction-history-size -- Set number of instructions to print in "record instruction-history".
set remote -- Remote protocol specific variables.
set remote TracepointSource-packet -- Set use of remote protocol `TracepointSource' (TracepointSource) packet.
set remote Z-packet -- Set use of remote protocol `Z' packets.
set remote access-watchpoint-packet -- Set use of remote protocol `Z4' (access-watchpoint) packet.
set remote agent-packet -- Set use of remote protocol `QAgent' (agent) packet.
set remote allow-packet -- Set use of remote protocol `QAllow' (allow) packet.
set remote attach-packet -- Set use of remote protocol `vAttach' (attach) packet.
set remote binary-download-packet, set remote X-packet -- Set use of remote protocol `X' (binary-download) packet.
set remote breakpoint-commands-packet -- Set use of remote protocol `BreakpointCommands' (breakpoint-commands) packet.
set remote btrace-conf-bts-size-packet -- Set use of remote protocol `Qbtrace-conf:bts:size' (btrace-conf-bts-size) packet.
set remote btrace-conf-pt-size-packet -- Set use of remote protocol `Qbtrace-conf:pt:size' (btrace-conf-pt-size) packet.
set remote catch-syscalls-packet -- Set use of remote protocol `QCatchSyscalls' (catch-syscalls) packet.
set remote conditional-breakpoints-packet -- Set use of remote protocol `ConditionalBreakpoints' (conditional-breakpoints) packet.
set remote conditional-tracepoints-packet -- Set use of remote protocol `ConditionalTracepoints' (conditional-tracepoints) packet.
set remote ctrl-c-packet -- Set use of remote protocol `vCtrlC' (ctrl-c) packet.
set remote disable-btrace-packet -- Set use of remote protocol `Qbtrace:off' (disable-btrace) packet.
set remote disable-randomization-packet -- Set use of remote protocol `QDisableRandomization' (disable-randomization) packet.
set remote enable-btrace-bts-packet -- Set use of remote protocol `Qbtrace:bts' (enable-btrace-bts) packet.
set remote enable-btrace-pt-packet -- Set use of remote protocol `Qbtrace:pt' (enable-btrace-pt) packet.
set remote environment-hex-encoded-packet -- Set use of remote protocol `QEnvironmentHexEncoded' (environment-hex-encoded) packet.
set remote environment-reset-packet -- Set use of remote protocol `QEnvironmentReset' (environment-reset) packet.
set remote environment-unset-packet -- Set use of remote protocol `QEnvironmentUnset' (environment-unset) packet.
set remote exec-event-feature-packet -- Set use of remote protocol `exec-event-feature' (exec-event-feature) packet.
set remote exec-file -- Set the remote pathname for "run".
set remote fast-tracepoints-packet -- Set use of remote protocol `FastTracepoints' (fast-tracepoints) packet.
set remote fetch-register-packet, set remote p-packet -- Set use of remote protocol `p' (fetch-register) packet.
set remote fork-event-feature-packet -- Set use of remote protocol `fork-event-feature' (fork-event-feature) packet.
set remote get-thread-information-block-address-packet -- Set use of remote protocol `qGetTIBAddr' (get-thread-information-block-address) packet.
set remote get-thread-local-storage-address-packet -- Set use of remote protocol `qGetTLSAddr' (get-thread-local-storage-address) packet.
set remote hardware-breakpoint-limit -- Set the maximum number of target hardware breakpoints.
set remote hardware-breakpoint-packet -- Set use of remote protocol `Z1' (hardware-breakpoint) packet.
set remote hardware-watchpoint-length-limit -- Set the maximum length (in bytes) of a target hardware watchpoint.
set remote hardware-watchpoint-limit -- Set the maximum number of target hardware watchpoints.
set remote hostio-close-packet -- Set use of remote protocol `vFile:close' (hostio-close) packet.
set remote hostio-fstat-packet -- Set use of remote protocol `vFile:fstat' (hostio-fstat) packet.
set remote hostio-open-packet -- Set use of remote protocol `vFile:open' (hostio-open) packet.
set remote hostio-pread-packet -- Set use of remote protocol `vFile:pread' (hostio-pread) packet.
set remote hostio-pwrite-packet -- Set use of remote protocol `vFile:pwrite' (hostio-pwrite) packet.
set remote hostio-readlink-packet -- Set use of remote protocol `vFile:readlink' (hostio-readlink) packet.
set remote hostio-setfs-packet -- Set use of remote protocol `vFile:setfs' (hostio-setfs) packet.
set remote hostio-unlink-packet -- Set use of remote protocol `vFile:unlink' (hostio-unlink) packet.
set remote hwbreak-feature-packet -- Set use of remote protocol `hwbreak-feature' (hwbreak-feature) packet.
set remote install-in-trace-packet -- Set use of remote protocol `InstallInTrace' (install-in-trace) packet.
set remote interrupt-on-connect -- Set whether interrupt-sequence is sent to remote target when gdb connects to.
set remote interrupt-sequence -- Set interrupt sequence to remote target.
set remote kill-packet -- Set use of remote protocol `vKill' (kill) packet.
set remote library-info-packet -- Set use of remote protocol `qXfer:libraries:read' (library-info) packet.
set remote library-info-svr4-packet -- Set use of remote protocol `qXfer:libraries-svr4:read' (library-info-svr4) packet.
set remote memory-map-packet -- Set use of remote protocol `qXfer:memory-map:read' (memory-map) packet.
set remote memory-read-packet-size -- Set the maximum number of bytes per memory-read packet.
set remote memory-tagging-feature-packet -- Set use of remote protocol `memory-tagging-feature' (memory-tagging-feature) packet.
set remote memory-write-packet-size -- Set the maximum number of bytes per memory-write packet.
set remote multiprocess-feature-packet -- Set use of remote protocol `multiprocess-feature' (multiprocess-feature) packet.
set remote no-resumed-stop-reply-packet -- Set use of remote protocol `N stop reply' (no-resumed-stop-reply) packet.
set remote noack-packet -- Set use of remote protocol `QStartNoAckMode' (noack) packet.
set remote osdata-packet -- Set use of remote protocol `qXfer:osdata:read' (osdata) packet.
set remote pass-signals-packet -- Set use of remote protocol `QPassSignals' (pass-signals) packet.
set remote pid-to-exec-file-packet -- Set use of remote protocol `qXfer:exec-file:read' (pid-to-exec-file) packet.
set remote program-signals-packet -- Set use of remote protocol `QProgramSignals' (program-signals) packet.
set remote query-attached-packet -- Set use of remote protocol `qAttached' (query-attached) packet.
set remote read-aux-vector-packet -- Set use of remote protocol `qXfer:auxv:read' (read-aux-vector) packet.
set remote read-btrace-conf-packet -- Set use of remote protocol `qXfer:btrace-conf' (read-btrace-conf) packet.
set remote read-btrace-packet -- Set use of remote protocol `qXfer:btrace' (read-btrace) packet.
set remote read-fdpic-loadmap-packet -- Set use of remote protocol `qXfer:fdpic:read' (read-fdpic-loadmap) packet.
set remote read-sdata-object-packet -- Set use of remote protocol `qXfer:statictrace:read' (read-sdata-object) packet.
set remote read-siginfo-object-packet -- Set use of remote protocol `qXfer:siginfo:read' (read-siginfo-object) packet.
set remote read-watchpoint-packet -- Set use of remote protocol `Z3' (read-watchpoint) packet.
set remote reverse-continue-packet -- Set use of remote protocol `bc' (reverse-continue) packet.
set remote reverse-step-packet -- Set use of remote protocol `bs' (reverse-step) packet.
set remote run-packet -- Set use of remote protocol `vRun' (run) packet.
set remote search-memory-packet -- Set use of remote protocol `qSearch:memory' (search-memory) packet.
set remote set-register-packet, set remote P-packet -- Set use of remote protocol `P' (set-register) packet.
set remote set-working-dir-packet -- Set use of remote protocol `QSetWorkingDir' (set-working-dir) packet.
set remote software-breakpoint-packet -- Set use of remote protocol `Z0' (software-breakpoint) packet.
set remote startup-with-shell-packet -- Set use of remote protocol `QStartupWithShell' (startup-with-shell) packet.
set remote static-tracepoints-packet -- Set use of remote protocol `StaticTracepoints' (static-tracepoints) packet.
set remote supported-packets-packet -- Set use of remote protocol `qSupported' (supported-packets) packet.
set remote swbreak-feature-packet -- Set use of remote protocol `swbreak-feature' (swbreak-feature) packet.
set remote symbol-lookup-packet -- Set use of remote protocol `qSymbol' (symbol-lookup) packet.
set remote system-call-allowed -- Set if the host system(3) call is allowed for the target.
set remote target-features-packet -- Set use of remote protocol `qXfer:features:read' (target-features) packet.
set remote thread-events-packet -- Set use of remote protocol `QThreadEvents' (thread-events) packet.
set remote threads-packet -- Set use of remote protocol `qXfer:threads:read' (threads) packet.
set remote trace-buffer-size-packet -- Set use of remote protocol `QTBuffer:size' (trace-buffer-size) packet.
set remote trace-status-packet -- Set use of remote protocol `qTStatus' (trace-status) packet.
set remote traceframe-info-packet -- Set use of remote protocol `qXfer:traceframe-info:read' (traceframe-info) packet.
set remote unwind-info-block-packet -- Set use of remote protocol `qXfer:uib:read' (unwind-info-block) packet.
set remote verbose-resume-packet -- Set use of remote protocol `vCont' (verbose-resume) packet.
set remote verbose-resume-supported-packet -- Set use of remote protocol `vContSupported' (verbose-resume-supported) packet.
set remote vfork-event-feature-packet -- Set use of remote protocol `vfork-event-feature' (vfork-event-feature) packet.
set remote write-siginfo-object-packet -- Set use of remote protocol `qXfer:siginfo:write' (write-siginfo-object) packet.
set remote write-watchpoint-packet -- Set use of remote protocol `Z2' (write-watchpoint) packet.
set remoteaddresssize -- Set the maximum size of the address (in bits) in a memory packet.
set remotecache -- Set cache use for remote targets.
set remoteflow -- Set use of hardware flow control for remote serial I/O.
set remotelogbase -- Set numerical base for remote session logging.
set remotelogfile -- Set filename for remote session recording.
set remotetimeout -- Set timeout limit to wait for target to respond.
set remotewritesize -- Set the maximum number of bytes per memory write packet (deprecated).
set schedule-multiple -- Set mode for resuming threads of all processes.
set scheduler-locking -- Set mode for locking scheduler during execution.
set script-extension -- Set mode for script filename extension recognition.
set serial -- Set default serial/parallel port configuration.
set serial baud -- Set baud rate for remote serial I/O.
set serial parity -- Set parity for remote serial I/O.
set solib-search-path -- Set the search path for loading non-absolute shared library symbol files.
set source -- Generic command for setting how sources are handled.
set source open -- Set whether GDB should open source files.
set stack-cache -- Set cache use for stack access.
set startup-quietly -- Set whether GDB should start up quietly.
set startup-with-shell -- Set use of shell to start subprocesses.  The default is on.
set step-mode -- Set mode of the step operation.
set stop-on-solib-events -- Set stopping for shared library events.
set struct-convention -- Set the convention for returning small structs.
set style -- Style-specific settings.
set style address, set style disassembler address -- Address display styling.
set style address background -- Set the background color for this property.
set style address foreground -- Set the foreground color for this property.
set style address intensity -- Set the display intensity for this property.
set style disassembler -- Style-specific settings for the disassembler.
set style disassembler comment -- Disassembler comment display styling.
set style disassembler comment background -- Set the background color for this property.
set style disassembler comment foreground -- Set the foreground color for this property.
set style disassembler comment intensity -- Set the display intensity for this property.
set style disassembler enabled -- Set whether disassembler output styling is enabled.
set style disassembler immediate -- Disassembler immediate display styling.
set style disassembler immediate background -- Set the background color for this property.
set style disassembler immediate foreground -- Set the foreground color for this property.
set style disassembler immediate intensity -- Set the display intensity for this property.
set style disassembler mnemonic -- Disassembler mnemonic display styling.
set style disassembler mnemonic background -- Set the background color for this property.
set style disassembler mnemonic foreground -- Set the foreground color for this property.
set style disassembler mnemonic intensity -- Set the display intensity for this property.
set style disassembler register -- Disassembler register display styling.
set style disassembler register background -- Set the background color for this property.
set style disassembler register foreground -- Set the foreground color for this property.
set style disassembler register intensity -- Set the display intensity for this property.
set style enabled -- Set whether CLI styling is enabled.
set style filename -- Filename display styling.
set style filename background -- Set the background color for this property.
set style filename foreground -- Set the foreground color for this property.
set style filename intensity -- Set the display intensity for this property.
set style function, set style disassembler symbol -- Function name display styling.
set style function background -- Set the background color for this property.
set style function foreground -- Set the foreground color for this property.
set style function intensity -- Set the display intensity for this property.
set style highlight -- Highlight display styling.
set style highlight background -- Set the background color for this property.
set style highlight foreground -- Set the foreground color for this property.
set style highlight intensity -- Set the display intensity for this property.
set style metadata -- Metadata display styling.
set style metadata background -- Set the background color for this property.
set style metadata foreground -- Set the foreground color for this property.
set style metadata intensity -- Set the display intensity for this property.
set style sources -- Set whether source code styling is enabled.
set style title -- Title display styling.
set style title background -- Set the background color for this property.
set style title foreground -- Set the foreground color for this property.
set style title intensity -- Set the display intensity for this property.
set style tui-active-border -- TUI active border display styling.
set style tui-active-border background -- Set the background color for this property.
set style tui-active-border foreground -- Set the foreground color for this property.
set style tui-border -- TUI border display styling.
set style tui-border background -- Set the background color for this property.
set style tui-border foreground -- Set the foreground color for this property.
set style tui-current-position -- Set whether to style text highlighted by the TUI´s current position indicator.
set style variable -- Variable name display styling.
set style variable background -- Set the background color for this property.
set style variable foreground -- Set the foreground color for this property.
set style variable intensity -- Set the display intensity for this property.
set style version -- Version string display styling.
set style version background -- Set the background color for this property.
set style version foreground -- Set the foreground color for this property.
set style version intensity -- Set the display intensity for this property.
set substitute-path -- Add a substitution rule to rewrite the source directories.
set suppress-cli-notifications -- Set whether printing notifications on CLI is suppressed.
set sysroot, set solib-absolute-prefix -- Set an alternate system root.
set target-charset -- Set the target character set.
set target-file-system-kind -- Set assumed file system kind for target reported file names.
set target-wide-charset -- Set the target wide character set.
set tcp -- TCP protocol specific variables.
set tcp auto-retry -- Set auto-retry on socket connect.
set tcp connect-timeout -- Set timeout limit in seconds for socket connection.
set tdesc -- Set target description specific variables.
set tdesc filename -- Set the file to read for an XML target description.
set trace-buffer-size -- Set requested size of trace buffer.
set trace-commands -- Set tracing of GDB CLI commands.
set trace-notes -- Set notes string to use for current and future trace runs.
set trace-stop-notes -- Set notes string to use for future tstop commands.
set trace-user -- Set the user name to use for current and future trace runs.
set trust-readonly-sections -- Set mode for reading from readonly sections.
set tui -- TUI configuration variables.
set tui active-border-mode -- Set the attribute mode to use for the active TUI window border.
set tui border-kind -- Set the kind of border for TUI windows.
set tui border-mode -- Set the attribute mode to use for the TUI window borders.
set tui compact-source -- Set whether the TUI source window is compact.
set tui tab-width -- Set the tab width, in characters, for the TUI.
set unwind-on-terminating-exception -- Set unwinding of stack if std::terminate is called while in call dummy.
set unwindonsignal -- Set unwinding of stack if a signal is received while in a call dummy.
set use-coredump-filter -- Set whether gcore should consider /proc/PID/coredump_filter.
set use-deprecated-index-sections -- Set whether to use deprecated gdb_index sections.
set variable, set var -- Evaluate expression EXP and assign result to variable VAR.
set verbose -- Set verbosity.
set watchdog -- Set watchdog timer.
set width -- Set number of characters where GDB should wrap lines of its output.
set write -- Set writing into executable and core files.
undisplay -- Cancel some expressions to be displayed when program stops.
whatis -- Print data type of expression EXP.
with, w -- Temporarily set SETTING to VALUE, run COMMAND, and restore SETTING.
x -- Examine memory: x/FMT ADDRESS.

Command class: files

add-symbol-file -- Load symbols from FILE, assuming FILE has been dynamically loaded.
add-symbol-file-from-memory -- Load the symbols out of memory from a dynamically loaded object file.
cd -- Set working directory to DIR for debugger.
core-file -- Use FILE as core dump for examining memory and registers.
directory -- Add directory DIR to beginning of search path for source files.
edit -- Edit specified file or function.
exec-file -- Use FILE as program for getting contents of pure memory.
file -- Use FILE as program to be debugged.
forward-search, fo, search -- Search for regular expression (see regex(3)) from last line listed.
generate-core-file, gcore -- Save a core file with the current state of the debugged process.
list, l -- List specified function or line.
load -- Dynamically load FILE into the running program.
nosharedlibrary -- Unload all shared object library symbols.
path -- Add directory DIR(s) to beginning of search path for object files.
pwd -- Print working directory.
remote -- Manipulate files on the remote system.
remote delete -- Delete a remote file.
remote get -- Copy a remote file to the local system.
remote put -- Copy a local file to the remote system.
remove-symbol-file -- Remove a symbol file added via the add-symbol-file command.
reverse-search, rev -- Search backward for regular expression (see regex(3)) from last line listed.
section -- Change the base address of section SECTION of the exec file to ADDR.
sharedlibrary -- Load shared object library symbols for files matching REGEXP.
symbol-file -- Load symbol table from executable file FILE.

Command class: internals

maintenance, mt -- Commands for use by GDB maintainers.
maintenance agent -- Translate an expression into remote agent bytecode for tracing.
maintenance agent-eval -- Translate an expression into remote agent bytecode for evaluation.
maintenance agent-printf -- Translate an expression into remote agent bytecode for evaluation and display the bytecodes.
maintenance btrace -- Branch tracing maintenance commands.
maintenance btrace clear -- Clears the branch tracing data.
maintenance btrace clear-packet-history -- Clears the branch tracing packet history.
maintenance btrace packet-history -- Print the raw branch tracing data.
maintenance check -- Commands for checking internal gdb state.
maintenance check libthread-db -- Run integrity checks on the current inferior´s libthread_db.
maintenance check xml-descriptions -- Check equality of GDB target descriptions and XML created descriptions.
maintenance check-psymtabs -- Check consistency of currently expanded psymtabs versus symtabs.
maintenance check-symtabs -- Check consistency of currently expanded symtabs.
maintenance cplus, maintenance cp -- C++ maintenance commands.
maintenance cplus first_component -- Print the first class/namespace component of NAME.
maintenance demangler-warning -- Give GDB a demangler warning.
maintenance deprecate -- Deprecate a command (for testing purposes).
maintenance dump-me -- Get fatal error; make debugger dump its core.
maintenance expand-symtabs -- Expand symbol tables.
maintenance flush -- Maintenance command for flushing GDB internal caches.
maintenance flush dcache -- Force gdb to flush its target memory data cache.
maintenance flush register-cache -- Force gdb to flush its register and frame cache.
maintenance flush source-cache -- Force gdb to flush its source code cache.
maintenance flush symbol-cache -- Flush the symbol cache for each program space.
maintenance info, maintenance i -- Commands for showing internal info about the program being debugged.
maintenance info bfds -- List the BFDs that are currently open.
maintenance info breakpoints -- Status of all breakpoints, or breakpoint number NUMBER.
maintenance info btrace -- Info about branch tracing data.
maintenance info jit -- Print information about JIT-ed code objects.
maintenance info line-table -- List the contents of all line tables, from all symbol tables.
maintenance info program-spaces -- Info about currently known program spaces.
maintenance info psymtabs -- List the partial symbol tables for all object files.
maintenance info sections -- List the BFD sections of the exec and core files.
maintenance info selftests -- List the registered selftests.
maintenance info symtabs -- List the full symbol tables for all object files.
maintenance info target-sections -- List GDB´s internal section table.
maintenance internal-error -- Give GDB an internal error.
maintenance internal-warning -- Give GDB an internal warning.
maintenance packet -- Send an arbitrary packet to a remote target.
maintenance print -- Maintenance command for printing GDB internal state.
maintenance print architecture -- Print the internal architecture configuration.
maintenance print c-tdesc -- Print the current target description as a C source file.
maintenance print cooked-registers -- Print the internal register configuration including cooked values.
maintenance print core-file-backed-mappings -- Print core file´s file-backed mappings.
maintenance print dummy-frames -- Print the contents of the internal dummy-frame stack.
maintenance print frame-id -- Print the current frame-id.
maintenance print msymbols -- Print dump of current minimal symbol definitions.
maintenance print objfiles -- Print dump of current object file definitions.
maintenance print psymbols -- Print dump of current partial symbol definitions.
maintenance print raw-registers -- Print the internal register configuration including raw values.
maintenance print reggroups -- Print the internal register group names.
maintenance print register-groups -- Print the internal register configuration including each register´s group.
maintenance print registers -- Print the internal register configuration.
maintenance print remote-registers -- Print the internal register configuration including remote register number and g/G packets offset.
maintenance print statistics -- Print statistics about internal gdb state.
maintenance print symbol-cache -- Dump the symbol cache for each program space.
maintenance print symbol-cache-statistics -- Print symbol cache statistics for each program space.
maintenance print symbols -- Print dump of current symbol definitions.
maintenance print target-stack -- Print the name of each layer of the internal target stack.
maintenance print type -- Print a type chain for a given symbol.
maintenance print user-registers -- List the names of the current user registers.
maintenance print xml-tdesc -- Print the current target description as an XML file.
maintenance selftest -- Run gdb´s unit tests.
maintenance set -- Set GDB internal variables used by the GDB maintainer.
maintenance set ada -- Set Ada maintenance-related variables.
maintenance set ada ignore-descriptive-types -- Set whether descriptive types generated by GNAT should be ignored.
maintenance set backtrace-on-fatal-signal -- Set whether to produce a backtrace if GDB receives a fatal signal.
maintenance set bfd-sharing -- Set whether gdb will share bfds that appear to be the same file.
maintenance set btrace -- Set branch tracing specific variables.
maintenance set btrace pt -- Set Intel Processor Trace specific variables.
maintenance set btrace pt skip-pad -- Set whether PAD packets should be skipped in the btrace packet history.
maintenance set catch-demangler-crashes -- Set whether to attempt to catch demangler crashes.
maintenance set check-libthread-db -- Set whether to check libthread_db at load time.
maintenance set demangler-warning -- Configure what GDB does when demangler-warning is detected.
maintenance set demangler-warning quit -- Set whether GDB should quit when an demangler-warning is detected.
maintenance set dwarf -- Set DWARF specific variables.
maintenance set dwarf always-disassemble -- Set whether 'info address' always disassembles DWARF expressions.
maintenance set dwarf max-cache-age -- Set the upper bound on the age of cached DWARF compilation units.
maintenance set dwarf unwinders -- Set whether the DWARF stack frame unwinders are used.
maintenance set gnu-source-highlight -- Set gnu-source-highlight specific variables.
maintenance set gnu-source-highlight enabled -- Set whether the GNU Source Highlight library should be used.
maintenance set ignore-prologue-end-flag -- Set if the PROLOGUE-END flag is ignored.
maintenance set internal-error -- Configure what GDB does when internal-error is detected.
maintenance set internal-error backtrace -- Set whether GDB should print a backtrace of GDB when internal-error is detected.
maintenance set internal-error corefile -- Set whether GDB should create a core file of GDB when internal-error is detected.
maintenance set internal-error quit -- Set whether GDB should quit when an internal-error is detected.
maintenance set internal-warning -- Configure what GDB does when internal-warning is detected.
maintenance set internal-warning backtrace -- Set whether GDB should print a backtrace of GDB when internal-warning is detected.
maintenance set internal-warning corefile -- Set whether GDB should create a core file of GDB when internal-warning is detected.
maintenance set internal-warning quit -- Set whether GDB should quit when an internal-warning is detected.
maintenance set libopcodes-styling -- Set libopcodes-styling specific variables.
maintenance set libopcodes-styling enabled -- Set whether the libopcodes styling support should be used.
maintenance set per-command -- Per-command statistics settings.
maintenance set per-command space -- Set whether to display per-command space usage.
maintenance set per-command symtab -- Set whether to display per-command symtab statistics.
maintenance set per-command time -- Set whether to display per-command execution time.
maintenance set profile -- Set internal profiling.
maintenance set selftest -- Self tests-related settings.
maintenance set selftest verbose -- Set whether selftests run in verbose mode.
maintenance set show-debug-regs -- Set whether to show variables that mirror the x86 debug registers.
maintenance set symbol-cache-size -- Set the size of the symbol cache.
maintenance set target-async -- Set whether gdb controls the inferior in asynchronous mode.
maintenance set target-non-stop -- Set whether gdb always controls the inferior in non-stop mode.
maintenance set test-settings -- Set GDB internal variables used for set/show command infrastructure testing.
maintenance set test-settings auto-boolean -- command used for internal testing.
maintenance set test-settings boolean -- command used for internal testing.
maintenance set test-settings enum -- command used for internal testing.
maintenance set test-settings filename -- command used for internal testing.
maintenance set test-settings integer -- command used for internal testing.
maintenance set test-settings optional-filename -- command used for internal testing.
maintenance set test-settings string -- command used for internal testing.
maintenance set test-settings string-noescape -- command used for internal testing.
maintenance set test-settings uinteger -- command used for internal testing.
maintenance set test-settings zinteger -- command used for internal testing.
maintenance set test-settings zuinteger -- command used for internal testing.
maintenance set test-settings zuinteger-unlimited -- command used for internal testing.
maintenance set tui-resize-message -- Set TUI resize messaging.
maintenance set worker-threads -- Set the number of worker threads GDB can use.
maintenance show -- Show GDB internal variables used by the GDB maintainer.
maintenance show ada -- Show Ada maintenance-related variables.
maintenance show ada ignore-descriptive-types -- Show whether descriptive types generated by GNAT should be ignored.
maintenance show backtrace-on-fatal-signal -- Show whether GDB will produce a backtrace if it receives a fatal signal.
maintenance show bfd-sharing -- Show whether gdb will share bfds that appear to be the same file.
maintenance show btrace -- Show branch tracing specific variables.
maintenance show btrace pt -- Show Intel Processor Trace specific variables.
maintenance show btrace pt skip-pad -- Show whether PAD packets should be skipped in the btrace packet history.
maintenance show catch-demangler-crashes -- Show whether to attempt to catch demangler crashes.
maintenance show check-libthread-db -- Show whether to check libthread_db at load time.
maintenance show demangler-warning -- Show what GDB does when demangler-warning is detected.
maintenance show demangler-warning quit -- Show whether GDB will quit when an demangler-warning is detected.
maintenance show dwarf -- Show DWARF specific variables.
maintenance show dwarf always-disassemble -- Show whether 'info address' always disassembles DWARF expressions.
maintenance show dwarf max-cache-age -- Show the upper bound on the age of cached DWARF compilation units.
maintenance show dwarf unwinders -- Show whether the DWARF stack frame unwinders are used.
maintenance show gnu-source-highlight -- Show gnu-source-highlight specific variables.
maintenance show gnu-source-highlight enabled -- Show whether the GNU Source Highlight library is being used.
maintenance show ignore-prologue-end-flag -- Show if the PROLOGUE-END flag is ignored.
maintenance show internal-error -- Show what GDB does when internal-error is detected.
maintenance show internal-error backtrace -- Show whether GDB will print a backtrace of GDB when internal-error is detected.
maintenance show internal-error corefile -- Show whether GDB will create a core file of GDB when internal-error is detected.
maintenance show internal-error quit -- Show whether GDB will quit when an internal-error is detected.
maintenance show internal-warning -- Show what GDB does when internal-warning is detected.
maintenance show internal-warning backtrace -- Show whether GDB will print a backtrace of GDB when internal-warning is detected.
maintenance show internal-warning corefile -- Show whether GDB will create a core file of GDB when internal-warning is detected.
maintenance show internal-warning quit -- Show whether GDB will quit when an internal-warning is detected.
maintenance show libopcodes-styling -- Show libopcodes-styling specific variables.
maintenance show libopcodes-styling enabled -- Show whether the libopcodes styling support should be used.
maintenance show per-command -- Show per-command statistics settings.
maintenance show per-command space -- Show whether to display per-command space usage.
maintenance show per-command symtab -- Show whether to display per-command symtab statistics.
maintenance show per-command time -- Show whether to display per-command execution time.
maintenance show profile -- Show internal profiling.
maintenance show selftest -- Self tests-related settings.
maintenance show selftest verbose -- Show whether selftests run in verbose mode.
maintenance show show-debug-regs -- Show whether to show variables that mirror the x86 debug registers.
maintenance show symbol-cache-size -- Show the size of the symbol cache.
maintenance show target-async -- Show whether gdb controls the inferior in asynchronous mode.
maintenance show target-non-stop -- Show whether gdb always controls the inferior in non-stop mode.
maintenance show test-options-completion-result -- Show maintenance test-options completion result.
maintenance show test-settings -- Show GDB internal variables used for set/show command infrastructure testing.
maintenance show test-settings auto-boolean -- command used for internal testing.
maintenance show test-settings boolean -- command used for internal testing.
maintenance show test-settings enum -- command used for internal testing.
maintenance show test-settings filename -- command used for internal testing.
maintenance show test-settings integer -- command used for internal testing.
maintenance show test-settings optional-filename -- command used for internal testing.
maintenance show test-settings string -- command used for internal testing.
maintenance show test-settings string-noescape -- command used for internal testing.
maintenance show test-settings uinteger -- command used for internal testing.
maintenance show test-settings zinteger -- command used for internal testing.
maintenance show test-settings zuinteger -- command used for internal testing.
maintenance show test-settings zuinteger-unlimited -- command used for internal testing.
maintenance show tui-resize-message -- Show TUI resize messaging.
maintenance show worker-threads -- Show the number of worker threads GDB can use.
maintenance space -- Set the display of space usage.
maintenance test-options -- Generic command for testing the options infrastructure.
maintenance test-options require-delimiter -- Command used for testing options processing.
maintenance test-options unknown-is-error -- Command used for testing options processing.
maintenance test-options unknown-is-operand -- Command used for testing options processing.
maintenance time -- Set the display of time usage.
maintenance translate-address -- Translate a section name and address to a symbol.
maintenance undeprecate -- Undeprecate a command (for testing purposes).
maintenance with -- Like "with", but works with "maintenance set" variables.

Command class: obscure

checkpoint -- Fork a duplicate process (experimental).
compare-sections -- Compare section data on target to the exec file.
compile, expression -- Command to compile source code and inject it into the inferior.
compile code -- Compile, inject, and execute code.
compile file -- Evaluate a file containing source code.
compile print -- Evaluate EXPR by using the compiler and print result.
complete -- List the completions for the rest of the line as a command.
guile, gu -- Evaluate a Guile expression.
guile-repl, gr -- Start a Guile interactive prompt.
monitor -- Send a command to the remote monitor (remote targets only).
python, py -- Evaluate a Python command.
python-interactive, pi -- Start an interactive Python prompt.
record, rec -- Start recording.
record btrace, record b -- Start branch trace recording.
record btrace bts, record bts -- Start branch trace recording in Branch Trace Store (BTS) format.
record btrace pt, record pt -- Start branch trace recording in Intel Processor Trace format.
record delete, record del, record d -- Delete the rest of execution log and start recording it anew.
record full -- Start full execution recording.
record full restore -- Restore the execution log from a file.
record function-call-history -- Prints the execution history at function granularity.
record goto -- Restore the program to its state at instruction number N.
record goto begin, record goto start -- Go to the beginning of the execution log.
record goto end -- Go to the end of the execution log.
record instruction-history -- Print disassembled instructions stored in the execution log.
record save -- Save the execution log to a file.
record stop, record s -- Stop the record/replay target.
restart -- Restore program context from a checkpoint.
stop -- There is no `stop' command, but you can set a hook on `stop'.

Command class: running

advance -- Continue the program up to the given location (same form as args for break command).
attach -- Attach to a process or file outside of GDB.
continue, fg, c -- Continue program being debugged, after signal or breakpoint.
detach -- Detach a process or file previously attached.
detach checkpoint -- Detach from a checkpoint (experimental).
detach inferiors -- Detach from inferior ID (or list of IDS).
disconnect -- Disconnect from a target.
finish, fin -- Execute until selected stack frame returns.
handle -- Specify how to handle signals.
inferior -- Use this command to switch between inferiors.
interrupt -- Interrupt the execution of the debugged program.
jump, j -- Continue program being debugged at specified line or address.
kill -- Kill execution of program being debugged.
kill inferiors -- Kill inferior ID (or list of IDs).
next, n -- Step program, proceeding through subroutine calls.
nexti, ni -- Step one instruction, but proceed through subroutine calls.
queue-signal -- Queue a signal to be delivered to the current thread when it is resumed.
reverse-continue, rc -- Continue program being debugged but run it in reverse.
reverse-finish -- Execute backward until just before selected stack frame is called.
reverse-next, rn -- Step program backward, proceeding through subroutine calls.
reverse-nexti, rni -- Step backward one instruction, but proceed through called subroutines.
reverse-step, rs -- Step program backward until it reaches the beginning of another source line.
reverse-stepi, rsi -- Step backward exactly one instruction.
run, r -- Start debugged program.
signal -- Continue program with the specified signal.
start -- Start the debugged program stopping at the beginning of the main procedure.
starti -- Start the debugged program stopping at the first instruction.
step, s -- Step program until it reaches a different source line.
stepi, si -- Step one instruction exactly.
taas -- Apply a command to all threads (ignoring errors and empty output).
target -- Connect to a target machine or process.
target core -- Use a core file as a target.
target ctf -- (Use a CTF directory as a target.
target exec -- Use an executable file as a target.
target extended-remote -- Use a remote computer via a serial line, using a gdb-specific protocol.
target native -- Native process (started by the "run" command).
target record-btrace -- Collect control-flow trace and provide the execution history.
target record-core -- Log program while executing and replay execution from log.
target record-full -- Log program while executing and replay execution from log.
target remote -- Use a remote computer via a serial line, using a gdb-specific protocol.
target tfile -- Use a trace file as a target.
task -- Use this command to switch between Ada tasks.
task apply -- Apply a command to a list of tasks.
task apply all -- Apply a command to all tasks in the current inferior.
tfaas -- Apply a command to all frames of all threads (ignoring errors and empty output).
thread, t -- Use this command to switch between threads.
thread apply -- Apply a command to a list of threads.
thread apply all -- Apply a command to all threads.
thread find -- Find threads that match a regular expression.
thread name -- Set the current thread´s name.
until, u -- Execute until past the current line or past a LOCATION.

Command class: stack

backtrace, where, bt -- Print backtrace of all stack frames, or innermost COUNT frames.
down, dow, do -- Select and print stack frame called by this one.
faas -- Apply a command to all frames (ignoring errors and empty output).
frame, f -- Select and print a stack frame.
frame address -- Select and print a stack frame by stack address.
frame apply -- Apply a command to a number of frames.
frame apply all -- Apply a command to all frames.
frame apply level -- Apply a command to a list of frames.
frame function -- Select and print a stack frame by function name.
frame level -- Select and print a stack frame by level.
frame view -- View a stack frame that might be outside the current backtrace.
return -- Make selected stack frame return to its caller.
select-frame -- Select a stack frame without printing anything.
select-frame address -- Select a stack frame by stack address.
select-frame function -- Select a stack frame by function name.
select-frame level -- Select a stack frame by level.
select-frame view -- Select a stack frame that might be outside the current backtrace.
up -- Select and print stack frame that called this one.

Command class: status

info, inf, i -- Generic command for showing things about the program being debugged.
info address -- Describe where symbol SYM is stored.
info all-registers -- List of all registers and their contents, for selected stack frame.
info args -- All argument variables of current stack frame or those matching REGEXPs.
info auto-load -- Print current status of auto-loaded files.
info auto-load gdb-scripts -- Print the list of automatically loaded sequences of commands.
info auto-load libthread-db -- Print the list of loaded inferior specific libthread_db.
info auto-load local-gdbinit -- Print whether current directory .gdbinit file has been loaded.
info auto-load python-scripts -- Print the list of automatically loaded Python scripts.
info auxv -- Display the inferior´s auxiliary vector.
info bookmarks -- Status of user-settable bookmarks.
info breakpoints, info b -- Status of specified breakpoints (all user-settable breakpoints if no argument).
info checkpoints -- IDs of currently known checkpoints.
info classes -- All Objective-C classes, or those matching REGEXP.
info common -- Print out the values contained in a Fortran COMMON block.
info connections -- Target connections in use.
info copying -- Conditions for redistributing copies of GDB.
info dcache -- Print information on the dcache performance.
info display -- Expressions to display when program stops, with code numbers.
info exceptions -- List all Ada exception names.
info extensions -- All filename extensions associated with a source language.
info files -- Names of targets and files being debugged.
info float -- Print the status of the floating point unit.
info frame, info f -- All about the selected stack frame.
info frame address -- Print information about a stack frame selected by stack address.
info frame function -- Print information about a stack frame selected by function name.
info frame level -- Print information about a stack frame selected by level.
info frame view -- Print information about a stack frame outside the current backtrace.
info frame-filter -- List all registered Python frame-filters.
info functions -- All function names or those matching REGEXPs.
info guile, info gu -- Prefix command for Guile info displays.
info inferiors -- Print a list of inferiors being managed.
info line -- Core addresses of the code for a source line.
info locals -- All local variables of current stack frame or those matching REGEXPs.
info macro -- Show the definition of MACRO, and it´s source location.
info macros -- Show the definitions of all macros at LINESPEC, or the current source location.
info mem -- Memory region attributes.
info module -- Print information about modules.
info module functions -- Display functions arranged by modules.
info module variables -- Display variables arranged by modules.
info modules -- All module names, or those matching REGEXP.
info os -- Show OS data ARG.
info pretty-printer -- GDB command to list all registered pretty-printers.
info probes -- Show available static probes.
info probes all -- Show information about all type of probes.
info probes dtrace -- Show information about DTrace static probes.
info probes stap -- Show information about SystemTap static probes.
info proc -- Show additional information about a process.
info proc all -- List all available info about the specified process.
info proc cmdline -- List command line arguments of the specified process.
info proc cwd -- List current working directory of the specified process.
info proc exe -- List absolute filename for executable of the specified process.
info proc files -- List files opened by the specified process.
info proc mappings -- List memory regions mapped by the specified process.
info proc stat -- List process info from /proc/PID/stat.
info proc status -- List process info from /proc/PID/status.
info program -- Execution status of the program.
info record, info rec -- Info record options.
info registers, info r -- List of integer registers and their contents, for selected stack frame.
info scope -- List the variables local to a scope.
info selectors -- All Objective-C selectors, or those matching REGEXP.
info sharedlibrary, info dll -- Status of loaded shared object libraries.
info signals, info handle -- What debugger does when program gets various signals.
info skip -- Display the status of skips.
info source -- Information about the current source file.
info sources -- All source files in the program or those matching REGEXP.
info stack, info s -- Backtrace of the stack, or innermost COUNT frames.
info static-tracepoint-markers -- List target static tracepoints markers.
info symbol -- Describe what symbol is at location ADDR.
info target -- Names of targets and files being debugged.
info tasks -- Provide information about all known Ada tasks.
info terminal -- Print inferior´s saved terminal status.
info threads -- Display currently known threads.
info tracepoints, info tp -- Status of specified tracepoints (all tracepoints if no argument).
info tvariables -- Status of trace state variables and their values.
info type-printers -- GDB command to list all registered type-printers.
info types -- All type names, or those matching REGEXP.
info unwinder -- GDB command to list unwinders.
info variables -- All global and static variable names or those matching REGEXPs.
info vector -- Print the status of the vector unit.
info vtbl -- Show the virtual function table for a C++ object.
info warranty -- Various kinds of warranty you do not have.
info watchpoints -- Status of specified watchpoints (all watchpoints if no argument).
info win -- List of all displayed windows.
info xmethod -- GDB command to list registered xmethod matchers.
macro -- Prefix for commands dealing with C preprocessor macros.
macro define -- Define a new C/C++ preprocessor macro.
macro expand, macro exp -- Fully expand any C/C++ preprocessor macro invocations in EXPRESSION.
macro expand-once, macro exp1 -- Expand C/C++ preprocessor macro invocations appearing directly in EXPRESSION.
macro list -- List all the macros defined using the `macro define' command.
macro undef -- Remove the definition of the C/C++ preprocessor macro with the given name.
show, info set -- Generic command for showing things about the debugger.
show ada -- Generic command for showing Ada-specific settings.
show ada print-signatures -- Show whether the output of formal and return types for functions in the overloads selection menu is activated.
show ada source-charset -- Show the Ada source character set.
show ada trust-PAD-over-XVS -- Show whether an optimization trusting PAD types over XVS types is activated.
show agent -- Show debugger´s willingness to use agent as a helper.
show annotate -- Show annotation_level.
show architecture -- Show architecture of target.
show args -- Show argument list to give program being debugged when it is started.
show auto-connect-native-target -- Show whether GDB may automatically connect to the native target.
show auto-load -- Show auto-loading specific settings.
show auto-load gdb-scripts -- Show whether auto-loading of canned sequences of commands scripts is enabled.
show auto-load libthread-db -- Show whether auto-loading inferior specific libthread_db is enabled.
show auto-load local-gdbinit -- Show whether auto-loading .gdbinit script in current directory is enabled.
show auto-load python-scripts -- Show the debugger´s behaviour regarding auto-loaded Python scripts.
show auto-load safe-path -- Show the list of files and directories that are safe for auto-loading.
show auto-load scripts-directory -- Show the list of directories from which to load auto-loaded scripts.
show auto-solib-add -- Show autoloading of shared library symbols.
show backtrace -- Show backtrace specific variables.
show backtrace limit -- Show the upper bound on the number of backtrace levels.
show backtrace past-entry -- Show whether backtraces should continue past the entry point of a program.
show backtrace past-main -- Show whether backtraces should continue past "main".
show basenames-may-differ -- Show whether a source file may have multiple base names.
show breakpoint -- Breakpoint specific settings.
show breakpoint always-inserted -- Show mode for inserting breakpoints.
show breakpoint auto-hw -- Show automatic usage of hardware breakpoints.
show breakpoint condition-evaluation -- Show mode of breakpoint condition evaluation.
show breakpoint pending -- Show debugger´s behavior regarding pending breakpoints.
show can-use-hw-watchpoints -- Show debugger´s willingness to use watchpoint hardware.
show case-sensitive -- Show case sensitivity in name search (on/off/auto).
show charset -- Show the host and target character sets.
show check, show ch, show c -- Show the status of the type/range checker.
show check range -- Show range checking (on/warn/off/auto).
show check type -- Show strict type checking.
show circular-trace-buffer -- Show target´s use of circular trace buffer.
show code-cache -- Show cache use for code segment access.
show coerce-float-to-double -- Show coercion of floats to doubles when calling functions.
show commands -- Show the history of commands you typed.
show compile-args -- Show compile command GCC command-line arguments.
show compile-gcc -- Show compile command GCC driver filename.
show complaints -- Show max number of complaints about incorrect symbols.
show configuration -- Show how GDB was configured at build time.
show confirm -- Show whether to confirm potentially dangerous operations.
show convenience, show conv -- Debugger convenience ("$foo") variables and functions.
show copying -- Conditions for redistributing copies of GDB.
show cp-abi -- Show the ABI used for inspecting C++ objects.
show cwd -- Show the current working directory that is used when the inferior is started.
show data-directory -- Show GDB´s data directory.
show dcache -- Show dcache settings.
show dcache line-size -- Show dcache line size.
show dcache size -- Show number of dcache lines.
show debug -- Generic command for showing gdb debugging flags.
show debug arch -- Show architecture debugging.
show debug auto-load -- Show auto-load verifications debugging.
show debug bfd-cache -- Show bfd cache debugging.
show debug check-physname -- Show cross-checking of "physname" code against demangler.
show debug coff-pe-read -- Show coff PE read debugging.
show debug compile -- Show compile command debugging.
show debug compile-cplus-scopes -- Show debugging of C++ compile scopes.
show debug compile-cplus-types -- Show debugging of C++ compile type conversion.
show debug displaced -- Show displaced stepping debugging.
show debug dwarf-die -- Show debugging of the DWARF DIE reader.
show debug dwarf-line -- Show debugging of the dwarf line reader.
show debug dwarf-read -- Show debugging of the DWARF reader.
show debug entry-values -- Show entry values and tail call frames debugging.
show debug event-loop -- Show event-loop debugging.
show debug expression -- Show expression debugging.
show debug fortran-array-slicing -- Show debugging of Fortran array slicing.
show debug frame -- Show frame debugging.
show debug index-cache -- Show display of index-cache debug messages.
show debug infcall -- Show inferior call debugging.
show debug infrun -- Show inferior debugging.
show debug jit -- Show JIT debugging.
show debug libthread-db -- Show libthread-db debugging.
show debug linux-namespaces -- Show debugging of GNU/Linux namespaces module.
show debug linux-nat --         Show debugging of GNU/Linux native target.
show debug notification -- Show debugging of async remote notification.
show debug observer -- Show observer debugging.
show debug overload -- Show debugging of C++ overloading.
show debug parser -- Show parser debugging.
show debug py-breakpoint -- Show Python breakpoint debugging.
show debug py-micmd -- Show Python micmd debugging.
show debug py-unwind -- Show Python unwinder debugging.
show debug record -- Show debugging of record/replay feature.
show debug remote -- Show debugging of remote protocol.
show debug remote-packet-max-chars -- Show the maximum number of characters to display for each remote packet.
show debug separate-debug-file -- Show printing of separate debug info file search debug.
show debug serial -- Show serial debugging.
show debug skip -- Show whether the debug output about skipping files and functions is printed.
show debug solib -- Show solib debugging.
show debug stap-expression -- Show SystemTap expression debugging.
show debug symbol-lookup -- Show debugging of symbol lookup.
show debug symfile -- Show debugging of the symfile functions.
show debug symtab-create -- Show debugging of symbol table creation.
show debug target -- Show target debugging.
show debug threads -- Show thread debugging.
show debug timestamp -- Show timestamping of debugging messages.
show debug tui -- Show tui debugging.
show debug varobj -- Show varobj debugging.
show debug xml -- Show XML parser debugging.
show debug-file-directory -- Show the directories where separate debug symbols are searched for.
show debuginfod -- Show debuginfod options.
show debuginfod enabled -- Show whether to use debuginfod.
show debuginfod urls -- Show the list of debuginfod server URLs.
show debuginfod verbose -- Show debuginfod debugging.
show default-collect -- Show the list of expressions to collect by default.
show demangle-style -- Show the current C++ demangling style.
show detach-on-fork -- Show whether gdb will detach the child of a fork.
show directories -- Show the search path for finding source files.
show disable-randomization -- Show disabling of debuggee´s virtual address space randomization.
show disassemble-next-line -- Show whether to disassemble next source line or insn when execution stops.
show disassembler-options -- Show the disassembler options.
show disassembly-flavor -- Show the disassembly flavor.
show disconnected-dprintf -- Show whether dprintf continues after GDB disconnects.
show disconnected-tracing -- Show whether tracing continues after GDB disconnects.
show displaced-stepping -- Show debugger´s willingness to use displaced stepping.
show dprintf-channel -- Show the channel to use for dynamic printf.
show dprintf-function -- Show the function to use for dynamic printf.
show dprintf-style -- Show the style of usage for dynamic printf.
show dump-excluded-mappings -- Show whether gcore should dump mappings marked with the VM_DONTDUMP flag.
show editing -- Show editing of command lines as they are typed.
show endian -- Show endianness of target.
show environment -- The environment to give the program, or one variable´s value.
show exec-direction -- Show direction of execution (forward/reverse).
show exec-done-display -- Show notification of completion for asynchronous execution commands.
show exec-file-mismatch -- Show exec-file-mismatch handling (ask|warn|off).
show exec-wrapper -- Show the wrapper for running programs.
show extended-prompt -- Show the extended prompt.
show extension-language -- Show mapping between filename extension and source language.
show filename-display -- Show how to display filenames.
show follow-exec-mode -- Show debugger response to a program call of exec.
show follow-fork-mode -- Show debugger response to a program call of fork or vfork.
show fortran -- Generic command for showing Fortran-specific settings.
show fortran repack-array-slices -- Show whether non-contiguous array slices are repacked.
show frame-filter -- Prefix command for 'show' frame-filter related operations.
show frame-filter priority -- GDB command to show the priority of the specified frame-filter.
show gnutarget -- Show the current BFD target.
show guile, show gu -- Prefix command for Guile preference settings.
show guile print-stack -- Show the mode of Guile exception printing on error.
show height -- Show number of lines in a page for GDB output pagination.
show history -- Generic command for showing command history parameters.
show history expansion -- Show history expansion on command input.
show history filename -- Show the filename in which to record the command history.
show history remove-duplicates -- Show how far back in history to look for and remove duplicate entries.
show history save -- Show saving of the history record on exit.
show history size -- Show the size of the command history.
show host-charset -- Show the host character set.
show index-cache -- Show index-cache options.
show index-cache directory -- Show the directory of the index cache.
show index-cache enabled -- Show whether the index cache is enabled.
show index-cache stats -- Show some stats about the index cache.
show inferior-tty -- Show terminal for future runs of program being debugged.
show input-radix -- Show default input radix for entering numbers.
show interactive-mode -- Show whether GDB´s standard input is a terminal.
show language -- Show the current source language.
show libthread-db-search-path -- Show the current search path or libthread_db.
show listsize -- Show number of source lines gdb will list by default.
show logging -- Show logging options.
show logging debugredirect -- Show the logging debug output mode.
show logging enabled -- Show whether logging is enabled.
show logging file -- Show the current logfile.
show logging overwrite -- Show whether logging overwrites or appends to the log file.
show logging redirect -- Show the logging output mode.
show max-completions -- Show maximum number of completion candidates.
show max-user-call-depth -- Show the max call depth for non-python/scheme user-defined commands.
show max-value-size -- Show maximum sized value gdb will load from the inferior.
show may-call-functions -- Show permission to call functions in the program.
show may-insert-breakpoints -- Show permission to insert breakpoints in the target.
show may-insert-fast-tracepoints -- Show permission to insert fast tracepoints in the target.
show may-insert-tracepoints -- Show permission to insert tracepoints in the target.
show may-interrupt -- Show permission to interrupt or signal the target.
show may-write-memory -- Show permission to write into target memory.
show may-write-registers -- Show permission to write into registers.
show mem -- Memory regions settings.
show mem inaccessible-by-default -- Show handling of unknown memory regions.
show mi-async -- Show whether MI asynchronous mode is enabled.
show mpx -- Show Intel Memory Protection Extensions specific variables.
show mpx bound -- Show the memory bounds for a given array/pointer storage in the bound table.
show multiple-symbols -- Show how the debugger handles ambiguities in expressions.
show non-stop -- Show whether gdb controls the inferior in non-stop mode.
show observer -- Show whether gdb controls the inferior in observer mode.
show opaque-type-resolution -- Show resolution of opaque struct/class/union types (if set before loading symbols).
show osabi -- Show OS ABI of target.
show output-radix -- Show default output radix for printing of values.
show overload-resolution -- Show overload resolution in evaluating C++ functions.
show pagination -- Show state of GDB output pagination.
show paths -- Current search path for finding object files.
show print, show pr, show p -- Generic command for showing print settings.
show print address -- Show printing of addresses.
show print array -- Show pretty formatting of arrays.
show print array-indexes -- Show printing of array indexes.
show print asm-demangle -- Show demangling of C++/ObjC names in disassembly listings.
show print demangle -- Show demangling of encoded C++/ObjC names when displaying symbols.
show print elements -- Show limit on string chars or array elements to print.
show print entry-values -- Show printing of function arguments at function entry.
show print finish -- Show whether `finish' prints the return value.
show print frame-arguments -- Show printing of non-scalar frame arguments.
show print frame-info -- Show printing of frame information.
show print inferior-events -- Show printing of inferior events (such as inferior start and exit).
show print max-depth -- Show maximum print depth for nested structures, unions, and arrays.
show print max-symbolic-offset -- Show the largest offset that will be printed in <SYMBOL+1234> form.
show print memory-tag-violations -- Show printing of memory tag violations for pointers.
show print nibbles -- Show whether to print binary values in groups of four bits.
show print null-stop -- Show printing of char arrays to stop at first null char.
show print object -- Show printing of C++ virtual function tables.
show print pascal_static-members -- Show printing of pascal static members.
show print pretty -- Show pretty formatting of structures.
show print raw-frame-arguments -- Show whether to print frame arguments in raw form.
show print raw-values -- Show whether to print values in raw form.
show print repeats -- Show threshold for repeated print elements.
show print sevenbit-strings -- Show printing of 8-bit characters in strings as \nnn.
show print static-members -- Show printing of C++ static members.
show print symbol -- Show printing of symbol names when printing pointers.
show print symbol-filename -- Show printing of source filename and line number with <SYMBOL>.
show print symbol-loading -- Show printing of symbol loading messages.
show print thread-events -- Show printing of thread events (such as thread start and exit).
show print type -- Generic command for setting how types print.
show print type hex -- Show whether sizes and offsets of struct members are printed using hex notation.
show print type methods -- Show printing of methods defined in classes.
show print type nested-type-limit -- Show the number of recursive nested type definitions to print.
show print type typedefs -- Show printing of typedefs defined in classes.
show print union -- Show printing of unions interior to structures.
show print vtbl -- Show printing of C++ virtual function tables.
show prompt -- Show gdb´s prompt.
show python -- Prefix command for python preference settings.
show python dont-write-bytecode -- Show whether the Python interpreter should avoid byte-compiling python modules.
show python ignore-environment --  Show whether the Python interpreter showlist ignore environment variables.
show python print-stack -- Show the mode of Python stack printing on error.
show radix -- Show the default input and output number radices.
show range-stepping -- Show whether target-assisted range stepping is enabled.
show ravenscar -- Prefix command for showing Ravenscar-specific settings.
show ravenscar task-switching -- Show whether support for GNAT Ravenscar tasks is enabled.
show record, show rec -- Show record options.
show record btrace -- Show record options.
show record btrace bts -- Show record btrace bts options.
show record btrace bts buffer-size -- Show the record/replay bts buffer size.
show record btrace cpu -- Show the cpu to be used for trace decode.
show record btrace pt -- Show record btrace pt options.
show record btrace pt buffer-size -- Show the record/replay pt buffer size.
show record btrace replay-memory-access -- Show what memory accesses are allowed during replay.
show record full -- Show record options.
show record full insn-number-max -- Show record/replay buffer limit.
show record full memory-query -- Show whether query if PREC cannot record memory change of next instruction.
show record full stop-at-limit -- Show whether record/replay stops when record/replay buffer becomes full.
show record function-call-history-size -- Show number of functions to print in "record function-call-history".
show record instruction-history-size -- Show number of instructions to print in "record instruction-history".
show remote -- Remote protocol specific variables.
show remote TracepointSource-packet -- Show current use of remote protocol `TracepointSource' (TracepointSource) packet.
show remote Z-packet -- Show use of remote protocol `Z' packets.
show remote access-watchpoint-packet -- Show current use of remote protocol `Z4' (access-watchpoint) packet.
show remote agent-packet -- Show current use of remote protocol `QAgent' (agent) packet.
show remote allow-packet -- Show current use of remote protocol `QAllow' (allow) packet.
show remote attach-packet -- Show current use of remote protocol `vAttach' (attach) packet.
show remote binary-download-packet, show remote X-packet -- Show current use of remote protocol `X' (binary-download) packet.
show remote breakpoint-commands-packet -- Show current use of remote protocol `BreakpointCommands' (breakpoint-commands) packet.
show remote btrace-conf-bts-size-packet -- Show current use of remote protocol `Qbtrace-conf:bts:size' (btrace-conf-bts-size) packet.
show remote btrace-conf-pt-size-packet -- Show current use of remote protocol `Qbtrace-conf:pt:size' (btrace-conf-pt-size) packet.
show remote catch-syscalls-packet -- Show current use of remote protocol `QCatchSyscalls' (catch-syscalls) packet.
show remote conditional-breakpoints-packet -- Show current use of remote protocol `ConditionalBreakpoints' (conditional-breakpoints) packet.
show remote conditional-tracepoints-packet -- Show current use of remote protocol `ConditionalTracepoints' (conditional-tracepoints) packet.
show remote ctrl-c-packet -- Show current use of remote protocol `vCtrlC' (ctrl-c) packet.
show remote disable-btrace-packet -- Show current use of remote protocol `Qbtrace:off' (disable-btrace) packet.
show remote disable-randomization-packet -- Show current use of remote protocol `QDisableRandomization' (disable-randomization) packet.
show remote enable-btrace-bts-packet -- Show current use of remote protocol `Qbtrace:bts' (enable-btrace-bts) packet.
show remote enable-btrace-pt-packet -- Show current use of remote protocol `Qbtrace:pt' (enable-btrace-pt) packet.
show remote environment-hex-encoded-packet -- Show current use of remote protocol `QEnvironmentHexEncoded' (environment-hex-encoded) packet.
show remote environment-reset-packet -- Show current use of remote protocol `QEnvironmentReset' (environment-reset) packet.
show remote environment-unset-packet -- Show current use of remote protocol `QEnvironmentUnset' (environment-unset) packet.
show remote exec-event-feature-packet -- Show current use of remote protocol `exec-event-feature' (exec-event-feature) packet.
show remote exec-file -- Show the remote pathname for "run".
show remote fast-tracepoints-packet -- Show current use of remote protocol `FastTracepoints' (fast-tracepoints) packet.
show remote fetch-register-packet, show remote p-packet -- Show current use of remote protocol `p' (fetch-register) packet.
show remote fork-event-feature-packet -- Show current use of remote protocol `fork-event-feature' (fork-event-feature) packet.
show remote get-thread-information-block-address-packet -- Show current use of remote protocol `qGetTIBAddr' (get-thread-information-block-address) packet.
show remote get-thread-local-storage-address-packet -- Show current use of remote protocol `qGetTLSAddr' (get-thread-local-storage-address) packet.
show remote hardware-breakpoint-limit -- Show the maximum number of target hardware breakpoints.
show remote hardware-breakpoint-packet -- Show current use of remote protocol `Z1' (hardware-breakpoint) packet.
show remote hardware-watchpoint-length-limit -- Show the maximum length (in bytes) of a target hardware watchpoint.
show remote hardware-watchpoint-limit -- Show the maximum number of target hardware watchpoints.
show remote hostio-close-packet -- Show current use of remote protocol `vFile:close' (hostio-close) packet.
show remote hostio-fstat-packet -- Show current use of remote protocol `vFile:fstat' (hostio-fstat) packet.
show remote hostio-open-packet -- Show current use of remote protocol `vFile:open' (hostio-open) packet.
show remote hostio-pread-packet -- Show current use of remote protocol `vFile:pread' (hostio-pread) packet.
show remote hostio-pwrite-packet -- Show current use of remote protocol `vFile:pwrite' (hostio-pwrite) packet.
show remote hostio-readlink-packet -- Show current use of remote protocol `vFile:readlink' (hostio-readlink) packet.
show remote hostio-setfs-packet -- Show current use of remote protocol `vFile:setfs' (hostio-setfs) packet.
show remote hostio-unlink-packet -- Show current use of remote protocol `vFile:unlink' (hostio-unlink) packet.
show remote hwbreak-feature-packet -- Show current use of remote protocol `hwbreak-feature' (hwbreak-feature) packet.
show remote install-in-trace-packet -- Show current use of remote protocol `InstallInTrace' (install-in-trace) packet.
show remote interrupt-on-connect -- Show whether interrupt-sequence is sent to remote target when gdb connects to.
show remote interrupt-sequence -- Show interrupt sequence to remote target.
show remote kill-packet -- Show current use of remote protocol `vKill' (kill) packet.
show remote library-info-packet -- Show current use of remote protocol `qXfer:libraries:read' (library-info) packet.
show remote library-info-svr4-packet -- Show current use of remote protocol `qXfer:libraries-svr4:read' (library-info-svr4) packet.
show remote memory-map-packet -- Show current use of remote protocol `qXfer:memory-map:read' (memory-map) packet.
show remote memory-read-packet-size -- Show the maximum number of bytes per memory-read packet.
show remote memory-tagging-feature-packet -- Show current use of remote protocol `memory-tagging-feature' (memory-tagging-feature) packet.
show remote memory-write-packet-size -- Show the maximum number of bytes per memory-write packet.
show remote multiprocess-feature-packet -- Show current use of remote protocol `multiprocess-feature' (multiprocess-feature) packet.
show remote no-resumed-stop-reply-packet -- Show current use of remote protocol `N stop reply' (no-resumed-stop-reply) packet.
show remote noack-packet -- Show current use of remote protocol `QStartNoAckMode' (noack) packet.
show remote osdata-packet -- Show current use of remote protocol `qXfer:osdata:read' (osdata) packet.
show remote pass-signals-packet -- Show current use of remote protocol `QPassSignals' (pass-signals) packet.
show remote pid-to-exec-file-packet -- Show current use of remote protocol `qXfer:exec-file:read' (pid-to-exec-file) packet.
show remote program-signals-packet -- Show current use of remote protocol `QProgramSignals' (program-signals) packet.
show remote query-attached-packet -- Show current use of remote protocol `qAttached' (query-attached) packet.
show remote read-aux-vector-packet -- Show current use of remote protocol `qXfer:auxv:read' (read-aux-vector) packet.
show remote read-btrace-conf-packet -- Show current use of remote protocol `qXfer:btrace-conf' (read-btrace-conf) packet.
show remote read-btrace-packet -- Show current use of remote protocol `qXfer:btrace' (read-btrace) packet.
show remote read-fdpic-loadmap-packet -- Show current use of remote protocol `qXfer:fdpic:read' (read-fdpic-loadmap) packet.
show remote read-sdata-object-packet -- Show current use of remote protocol `qXfer:statictrace:read' (read-sdata-object) packet.
show remote read-siginfo-object-packet -- Show current use of remote protocol `qXfer:siginfo:read' (read-siginfo-object) packet.
show remote read-watchpoint-packet -- Show current use of remote protocol `Z3' (read-watchpoint) packet.
show remote reverse-continue-packet -- Show current use of remote protocol `bc' (reverse-continue) packet.
show remote reverse-step-packet -- Show current use of remote protocol `bs' (reverse-step) packet.
show remote run-packet -- Show current use of remote protocol `vRun' (run) packet.
show remote search-memory-packet -- Show current use of remote protocol `qSearch:memory' (search-memory) packet.
show remote set-register-packet, show remote P-packet -- Show current use of remote protocol `P' (set-register) packet.
show remote set-working-dir-packet -- Show current use of remote protocol `QSetWorkingDir' (set-working-dir) packet.
show remote software-breakpoint-packet -- Show current use of remote protocol `Z0' (software-breakpoint) packet.
show remote startup-with-shell-packet -- Show current use of remote protocol `QStartupWithShell' (startup-with-shell) packet.
show remote static-tracepoints-packet -- Show current use of remote protocol `StaticTracepoints' (static-tracepoints) packet.
show remote supported-packets-packet -- Show current use of remote protocol `qSupported' (supported-packets) packet.
show remote swbreak-feature-packet -- Show current use of remote protocol `swbreak-feature' (swbreak-feature) packet.
show remote symbol-lookup-packet -- Show current use of remote protocol `qSymbol' (symbol-lookup) packet.
show remote system-call-allowed -- Show if the host system(3) call is allowed for the target.
show remote target-features-packet -- Show current use of remote protocol `qXfer:features:read' (target-features) packet.
show remote thread-events-packet -- Show current use of remote protocol `QThreadEvents' (thread-events) packet.
show remote threads-packet -- Show current use of remote protocol `qXfer:threads:read' (threads) packet.
show remote trace-buffer-size-packet -- Show current use of remote protocol `QTBuffer:size' (trace-buffer-size) packet.
show remote trace-status-packet -- Show current use of remote protocol `qTStatus' (trace-status) packet.
show remote traceframe-info-packet -- Show current use of remote protocol `qXfer:traceframe-info:read' (traceframe-info) packet.
show remote unwind-info-block-packet -- Show current use of remote protocol `qXfer:uib:read' (unwind-info-block) packet.
show remote verbose-resume-packet -- Show current use of remote protocol `vCont' (verbose-resume) packet.
show remote verbose-resume-supported-packet -- Show current use of remote protocol `vContSupported' (verbose-resume-supported) packet.
show remote vfork-event-feature-packet -- Show current use of remote protocol `vfork-event-feature' (vfork-event-feature) packet.
show remote write-siginfo-object-packet -- Show current use of remote protocol `qXfer:siginfo:write' (write-siginfo-object) packet.
show remote write-watchpoint-packet -- Show current use of remote protocol `Z2' (write-watchpoint) packet.
show remoteaddresssize -- Show the maximum size of the address (in bits) in a memory packet.
show remotecache -- Show cache use for remote targets.
show remoteflow -- Show use of hardware flow control for remote serial I/O.
show remotelogbase -- Show numerical base for remote session logging.
show remotelogfile -- Show filename for remote session recording.
show remotetimeout -- Show timeout limit to wait for target to respond.
show remotewritesize -- Show the maximum number of bytes per memory write packet (deprecated).
show schedule-multiple -- Show mode for resuming threads of all processes.
show scheduler-locking -- Show mode for locking scheduler during execution.
show script-extension -- Show mode for script filename extension recognition.
show serial -- Show default serial/parallel port configuration.
show serial baud -- Show baud rate for remote serial I/O.
show serial parity -- Show parity for remote serial I/O.
show solib-search-path -- Show the search path for loading non-absolute shared library symbol files.
show source -- Generic command for showing source settings.
show source open -- Show whether GDB should open source files.
show stack-cache -- Show cache use for stack access.
show startup-quietly --                 Show whether GDB should start up quietly.
show startup-with-shell -- Show use of shell to start subprocesses.
show step-mode -- Show mode of the step operation.
show stop-on-solib-events -- Show stopping for shared library events.
show struct-convention -- Show the convention for returning small structs.
show style -- Style-specific settings.
show style address, show style disassembler address -- Address display styling.
show style address background -- Show the background color for this property.
show style address foreground -- Show the foreground color for this property.
show style address intensity -- Show the display intensity for this property.
show style disassembler -- Style-specific settings for the disassembler.
show style disassembler comment -- Disassembler comment display styling.
show style disassembler comment background -- Show the background color for this property.
show style disassembler comment foreground -- Show the foreground color for this property.
show style disassembler comment intensity -- Show the display intensity for this property.
show style disassembler enabled -- Show whether disassembler output styling is enabled.
show style disassembler immediate -- Disassembler immediate display styling.
show style disassembler immediate background -- Show the background color for this property.
show style disassembler immediate foreground -- Show the foreground color for this property.
show style disassembler immediate intensity -- Show the display intensity for this property.
show style disassembler mnemonic -- Disassembler mnemonic display styling.
show style disassembler mnemonic background -- Show the background color for this property.
show style disassembler mnemonic foreground -- Show the foreground color for this property.
show style disassembler mnemonic intensity -- Show the display intensity for this property.
show style disassembler register -- Disassembler register display styling.
show style disassembler register background -- Show the background color for this property.
show style disassembler register foreground -- Show the foreground color for this property.
show style disassembler register intensity -- Show the display intensity for this property.
show style enabled -- Show whether CLI is enabled.
show style filename -- Filename display styling.
show style filename background -- Show the background color for this property.
show style filename foreground -- Show the foreground color for this property.
show style filename intensity -- Show the display intensity for this property.
show style function, show style disassembler symbol -- Function name display styling.
show style function background -- Show the background color for this property.
show style function foreground -- Show the foreground color for this property.
show style function intensity -- Show the display intensity for this property.
show style highlight -- Highlight display styling.
show style highlight background -- Show the background color for this property.
show style highlight foreground -- Show the foreground color for this property.
show style highlight intensity -- Show the display intensity for this property.
show style metadata -- Metadata display styling.
show style metadata background -- Show the background color for this property.
show style metadata foreground -- Show the foreground color for this property.
show style metadata intensity -- Show the display intensity for this property.
show style sources -- Show whether source code styling is enabled.
show style title -- Title display styling.
show style title background -- Show the background color for this property.
show style title foreground -- Show the foreground color for this property.
show style title intensity -- Show the display intensity for this property.
show style tui-active-border -- TUI active border display styling.
show style tui-active-border background -- Show the background color for this property.
show style tui-active-border foreground -- Show the foreground color for this property.
show style tui-border -- TUI border display styling.
show style tui-border background -- Show the background color for this property.
show style tui-border foreground -- Show the foreground color for this property.
show style tui-current-position -- Show whether to style text highlighted by the TUI´s current position indicator.
show style variable -- Variable name display styling.
show style variable background -- Show the background color for this property.
show style variable foreground -- Show the foreground color for this property.
show style variable intensity -- Show the display intensity for this property.
show style version -- Version string display styling.
show style version background -- Show the background color for this property.
show style version foreground -- Show the foreground color for this property.
show style version intensity -- Show the display intensity for this property.
show substitute-path -- Show one or all substitution rules rewriting the source directories.
show suppress-cli-notifications -- Show whether printing notifications on CLI is suppressed.
show sysroot, show solib-absolute-prefix -- Show the current system root.
show target-charset -- Show the target character set.
show target-file-system-kind -- Show assumed file system kind for target reported file names.
show target-wide-charset -- Show the target wide character set.
show tcp -- TCP protocol specific variables.
show tcp auto-retry -- Show auto-retry on socket connect.
show tcp connect-timeout -- Show timeout limit in seconds for socket connection.
show tdesc -- Show target description specific variables.
show tdesc filename -- Show the file to read for an XML target description.
show trace-buffer-size -- Show requested size of trace buffer.
show trace-commands -- Show state of GDB CLI command tracing.
show trace-notes -- Show the notes string to use for current and future trace runs.
show trace-stop-notes -- Show the notes string to use for future tstop commands.
show trace-user -- Show the user name to use for current and future trace runs.
show trust-readonly-sections -- Show mode for reading from readonly sections.
show tui -- TUI configuration variables.
show tui active-border-mode -- Show the attribute mode to use for the active TUI window border.
show tui border-kind -- Show the kind of border for TUI windows.
show tui border-mode -- Show the attribute mode to use for the TUI window borders.
show tui compact-source -- Show whether the TUI source window is compact.
show tui tab-width -- Show the tab witdh, in characters, for the TUI.
show unwind-on-terminating-exception -- Show unwinding of stack if std::terminate() is called while in a call dummy.
show unwindonsignal -- Show unwinding of stack if a signal is received while in a call dummy.
show use-coredump-filter -- Show whether gcore should consider /proc/PID/coredump_filter.
show use-deprecated-index-sections -- Show whether to use deprecated gdb_index sections.
show user -- Show definitions of non-python/scheme user defined commands.
show values -- Elements of value history around item number IDX (or last ten).
show varsize-limit -- Show the maximum number of bytes allowed in a variable-size object.
show verbose -- Show verbosity.
show version -- Show what version of GDB this is.
show warranty -- Various kinds of warranty you do not have.
show watchdog -- Show watchdog timer.
show width -- Show number of characters where GDB should wrap lines of its output.
show write -- Show writing into executable and core files.

Command class: support

add-auto-load-safe-path -- Add entries to the list of directories from which it is safe to auto-load files.
add-auto-load-scripts-directory -- Add entries to the list of directories from which to load auto-loaded scripts.
alias -- Define a new command that is an alias of an existing command.
apropos -- Search for commands matching a REGEXP.
define -- Define a new command name.  Command name is argument.
define-prefix -- Define or mark a command as a user-defined prefix command.
demangle -- Demangle a mangled name.
document -- Document a user-defined command or user-defined alias.
dont-repeat -- Don't repeat this command.
down-silently -- Same as the `down' command, but does not print anything.
echo -- Print a constant string.  Give string as argument.
help, h -- Print list of commands.
if -- Execute nested commands once IF the conditional expression is non zero.
interpreter-exec -- Execute a command in an interpreter.
make -- Run the ``make'' program using the rest of the line as arguments.
new-ui -- Create a new UI.
overlay, ov, ovly -- Commands for debugging overlays.
overlay auto -- Enable automatic overlay debugging.
overlay list-overlays -- List mappings of overlay sections.
overlay load-target -- Read the overlay mapping state from the target.
overlay manual -- Enable overlay debugging.
overlay map-overlay -- Assert that an overlay section is mapped.
overlay off -- Disable overlay debugging.
overlay unmap-overlay -- Assert that an overlay section is unmapped.
pipe, | -- Send the output of a gdb command to a shell command.
quit, exit, q -- Exit gdb.
shell, ! -- Execute the rest of the line as a shell command.
source -- Read commands from a file named FILE.
up-silently -- Same as the `up' command, but does not print anything.
while -- Execute nested commands WHILE the conditional expression is non zero.

Command class: text-user-interface

+ -- Scroll window forward.
- -- Scroll window backward.
< -- Scroll window text to the left.
> -- Scroll window text to the right.
tui -- Text User Interface commands.
tui disable -- Disable TUI display mode.
tui enable -- Enable TUI display mode.
tui focus, fs, focus -- Set focus to named window or next/prev window.
tui layout, layout -- Change the layout of windows.
tui layout asm -- Apply the "asm" layout.
tui layout next -- Apply the next TUI layout.
tui layout prev -- Apply the previous TUI layout.
tui layout regs -- Apply the TUI register layout.
tui layout split -- Apply the "split" layout.
tui layout src -- Apply the "src" layout.
tui new-layout -- Create a new TUI layout.
tui refresh, refresh -- Refresh the terminal display.
tui reg -- TUI command to control the register window.
tui window -- Text User Interface window commands.
tui window height, wh, winheight -- Set or modify the height of a specified window.
tui window width, winwidth -- Set or modify the width of a specified window.
update -- Update the source window and locator to display the current execution point.

Command class: tracepoints

actions -- Specify the actions to be taken at a tracepoint.
collect -- Specify one or more data items to be collected at a tracepoint.
end -- Ends a list of commands or actions.
passcount -- Set the passcount for a tracepoint.
tdump -- Print everything collected at the current tracepoint.
teval -- Specify one or more expressions to be evaluated at a tracepoint.
tfind -- Select a trace frame.
tfind end, tfind none -- De-select any trace frame and resume 'live' debugging.
tfind line -- Select a trace frame by source line.
tfind outside -- Select a trace frame whose PC is outside the given range (exclusive).
tfind pc -- Select a trace frame by PC.
tfind range -- Select a trace frame whose PC is in the given range (inclusive).
tfind start -- Select the first trace frame in the trace buffer.
tfind tracepoint -- Select a trace frame by tracepoint number.
tsave -- Save the trace data to a file.
tstart -- Start trace data collection.
tstatus -- Display the status of the current trace data collection.
tstop -- Stop trace data collection.
tvariable -- Define a trace state variable.
while-stepping, stepping, ws -- Specify single-stepping behavior at a tracepoint.

Command class: user-defined


Unclassified commands

add-inferior -- Add a new inferior.
clone-inferior -- Clone inferior ID.
eval -- Construct a GDB command and then evaluate it.
flash-erase -- Erase all flash memory regions.
function -- Placeholder command for showing help on convenience functions.
function _any_caller_is -- Check all calling function´s names.
function _any_caller_matches -- Compare all calling function´s names with a regexp.
function _as_string -- Return the string representation of a value.
function _caller_is -- Check the calling function´s name.
function _caller_matches -- Compare the calling function´s name with a regexp.
function _cimag -- Extract the imaginary part of a complex number.
function _creal -- Extract the real part of a complex number.
function _gdb_maint_setting -- $_gdb_maint_setting - returns the value of a GDB maintenance setting.
function _gdb_maint_setting_str -- $_gdb_maint_setting_str - returns the value of a GDB maintenance setting as a string.
function _gdb_setting -- $_gdb_setting - returns the value of a GDB setting.
function _gdb_setting_str -- $_gdb_setting_str - returns the value of a GDB setting as a string.
function _isvoid -- Check whether an expression is void.
function _memeq -- $_memeq - compare bytes of memory.
function _regex -- $_regex - check if a string matches a regular expression.
function _streq -- $_streq - check string equality.
function _strlen -- $_strlen - compute string length.
jit-reader-load -- Load FILE as debug info reader and unwinder for JIT compiled code.
jit-reader-unload -- Unload the currently loaded JIT debug info reader.
remove-inferiors -- Remove inferior ID (or list of IDs).
unset -- Complement to certain "set" commands.
unset environment -- Cancel environment variable VAR for the program.
unset exec-wrapper -- Disable use of an execution wrapper.
unset substitute-path -- Delete one or all substitution rules rewriting the source directories.
unset tdesc -- Unset target description specific variables.
unset tdesc filename -- Unset the file to read for an XML target description.
```