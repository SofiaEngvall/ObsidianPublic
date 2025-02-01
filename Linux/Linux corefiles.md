
command to find current corefile size setting. if 0 no files will be created:
`ulimit -c`

files can be created in `/var/crash/`





from chatgpt, to fix and expand:

The Linux core dump format is an **ELF (Executable and Linkable Format) file** that contains a snapshot of a crashed process's memory and execution state. It is primarily used for post-mortem debugging.

### **Core File Structure**

A core file consists of:

1. **ELF Header** – Identifies the file as an ELF core dump.
2. **Program Headers** – Describe memory regions dumped from the process.
3. **Note Segments (`PT_NOTE`)** – Store metadata such as process registers, signal information, and auxiliary vector.
4. **Memory Segments (`PT_LOAD`)** – Contain raw memory regions, including stack, heap, and mapped shared libraries.

### **Key Components in Detail**

#### **1. ELF Header**

- Specifies the file type (`ET_CORE`).
- Defines target architecture and byte order.

#### **2. Program Headers**

- Mark sections of the core dump.
- Typically includes `PT_NOTE` for metadata and `PT_LOAD` for memory contents.

#### **3. Note Segments (`PT_NOTE`)**

These contain important information about the process:

- **`NT_PRSTATUS`** – General-purpose register state.
- **`NT_PRFPREG`** – Floating-point registers (if applicable).
- **`NT_SIGINFO`** – Signal that caused the crash.
- **`NT_AUXV`** – Auxiliary vector (runtime environment info).
- **`NT_FILE`** – List of mapped files (libraries, executables).
- **`NT_PRPSINFO`** – Process status (PID, command name, etc.).

#### **4. Memory Segments (`PT_LOAD`)**

- Represent actual memory mappings of the process.
- Include stack, heap, text, and shared libraries.

### **Core Dump Configuration**

You can control core dumps using:

- `ulimit -c unlimited` (enables core dumps).
- `/proc/sys/kernel/core_pattern` (defines file naming).
- `/proc/sys/kernel/core_uses_pid` (appends PID to the core file).
- `/proc/sys/kernel/core_pipe_limit` (limits concurrent core dumps).

### **Analyzing Core Dumps**

Use `gdb`:
```sh
gdb /path/to/executable core
```

Or extract information using `readelf`:
```sh
readelf -n core
```

