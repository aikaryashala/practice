# How a C Program is Loaded and Run on Linux

A comprehensive guide to understanding the journey from source code to execution for C programs compiled with Clang on x86-64 Linux.

## 1. Compilation Process

When you compile a C program:

```bash
clang -g -o max_sum max_sum.c
```

Clang produces an **ELF (Executable and Linkable Format)** binary containing:

- Machine code (.text section)
- Initialized data (.data section)
- Uninitialized data placeholder (.bss section)
- Read-only constants (.rodata section)
- Symbol tables and debugging info
- Dynamic linking information

## 2. ELF File Structure

The ELF binary contains sections grouped into segments (PT_LOAD):

| Segment | Permission | Contains |
|---------|------------|----------|
| PT_LOAD[0] | `r--` | ELF headers, symbol tables, relocation info |
| PT_LOAD[1] | `r-x` | .text, .init, .plt (executable code) |
| PT_LOAD[2] | `r--` | .rodata (string literals, constants) |
| PT_LOAD[3] | `rw-` | .data, .bss, .got (variables) |

## 3. ELF Header Contents

The ELF header is at the very start of the binary and tells the OS how to load and run the program.

### View ELF Header

```bash
readelf -h max_sum
```

### Key Fields

| Field | Purpose |
|-------|---------|
| Magic Number | `7f 45 4c 46` (`.ELF`) — identifies file as ELF |
| Class | 32-bit or 64-bit |
| Endianness | Little or big endian |
| OS/ABI | Target OS (Linux, FreeBSD, etc.) |
| Type | Executable, shared library, or relocatable |
| Machine | Architecture (x86-64, i386, ARM, etc.) |
| Entry Point | Address where execution starts (`_start`) |
| Program Header Offset | Where segment table begins |
| Section Header Offset | Where section table begins |
| Flags | Architecture-specific flags |

### Example Output

```
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00
  Class:                             ELF64
  Data:                              2's complement, little endian
  OS/ABI:                            UNIX - System V
  Type:                              DYN (Position-Independent Executable)
  Machine:                           Advanced Micro Devices X86-64
  Entry point address:               0x1050
  Start of program headers:          64 (bytes into file)
  Start of section headers:          14256 (bytes into file)
  Number of program headers:         13
  Number of section headers:         31
```

### Entry Point and `_start`

The `Entry point address` points to `_start`, **not** `main()`. The startup sequence is:

```
_start (entry point)
   ↓
__libc_start_main (C runtime setup)
   ↓
main() (your code)
   ↓
exit()
```

`_start` is provided by the C runtime and:
1. Sets up the stack
2. Initializes libc
3. Calls your `main(argc, argv)`
4. Passes return value to `exit()`

## 4. Program Loading

When you execute the program, the kernel performs these steps:

### 4.1 Kernel Creates Process

1. Allocates virtual address space
2. Sets up page tables
3. Creates process control block

### 4.2 Dynamic Linker (ld-linux-x86-64.so.2)

The kernel loads the dynamic linker first, which then:

1. Loads the main executable into memory
2. Loads required shared libraries (libc.so.6, etc.)
3. Resolves symbols (printf, malloc, etc.)
4. Sets up the PLT (Procedure Linkage Table) and GOT (Global Offset Table)

### 4.3 Memory Map After Loading

```
Virtual Address Space (48-bit addressing)
──────────────────────────────────────────

0xFFFFFFFFFFFFFFFF ┌─────────────────────┐
                   │   Kernel Space      │  (inaccessible to user)
0x7FFFFFFFFFFF     ├─────────────────────┤
                   │   Stack             │  ← grows downward
                   │   0x7ffffffde000    │
                   ├─────────────────────┤
                   │                     │
                   │   (unmapped)        │
                   │                     │
                   ├─────────────────────┤
                   │   Shared Libraries  │
                   │   libc.so.6         │  0x7ffff7d8a000
                   │   ld-linux.so.2     │  0x7ffff7fc3000
                   ├─────────────────────┤
                   │                     │
                   │   (unmapped)        │
                   │                     │
                   ├─────────────────────┤
                   │   Heap              │  ← grows upward
                   │   0x555555559000    │
                   ├─────────────────────┤
                   │   .bss   (rw-)      │  0x555555558030
                   │   .data  (rw-)      │  0x555555558020
                   ├─────────────────────┤
                   │   .rodata (r--)     │  0x555555556000
                   ├─────────────────────┤
                   │   .text  (r-x)      │  0x555555555050
                   ├─────────────────────┤
                   │   ELF headers       │  0x555555554000
                   ├─────────────────────┤
                   │   (unmapped)        │  NULL pointer trap
0x0000000000000000 └─────────────────────┘
```

## 5. Stack Frame Setup

When a function is called, the CPU sets up a stack frame:

### 5.1 Function Prologue

```asm
pushq  %rbp           # Save caller's base pointer
movq   %rsp, %rbp     # Establish new frame base
subq   $0x10, %rsp    # Allocate space for local variables (16 bytes)
```

### 5.2 Stack Frame Layout

```
Higher Address
┌─────────────────┐
│  Return Address │  ← pushed by callq
├─────────────────┤
│  Old RBP        │  ← rbp points here
├─────────────────┤
│  Local Var 1    │  -0x4(%rbp)
│  Local Var 2    │  -0x8(%rbp)
│  Local Var 3    │  -0xc(%rbp)
│  (padding)      │  -0x10(%rbp)
├─────────────────┤
│                 │  ← rsp points here
Lower Address
```

### 5.3 Function Epilogue

```asm
addq   $0x10, %rsp    # Deallocate local variables
popq   %rbp           # Restore caller's base pointer
retq                  # Return to caller
```

## 6. The Red Zone

On x86-64 Linux, leaf functions (functions that don't call other functions) can use the **red zone** — 128 bytes below `%rsp` without explicit allocation.

```
┌─────────────────┐
│                 │  ← rsp
├─────────────────┤
│                 │
│   RED ZONE      │  128 bytes
│   (safe to use) │
│                 │
└─────────────────┘
```

**Rules:**
- Only for leaf functions
- Only on Linux/macOS (not Windows)
- Destroyed by `call` instructions

## 7. Function Calls

### 7.1 The `callq` Instruction

```asm
callq  function_address
```

Internally does:
1. `rsp = rsp - 8`
2. `memory[rsp] = rip + sizeof(callq)` (push return address)
3. `rip = function_address` (jump to function)

### 7.2 The `retq` Instruction

```asm
retq
```

Internally does:
1. `rip = memory[rsp]` (pop return address)
2. `rsp = rsp + 8`

## 8. Calling Convention (System V AMD64 ABI)

### 8.1 Parameter Passing

| Parameter | Register |
|-----------|----------|
| 1st integer/pointer | `%rdi` |
| 2nd integer/pointer | `%rsi` |
| 3rd integer/pointer | `%rdx` |
| 4th integer/pointer | `%rcx` |
| 5th integer/pointer | `%r8` |
| 6th integer/pointer | `%r9` |
| Additional | Stack |

### 8.2 Return Value

| Type | Register |
|------|----------|
| Integer/pointer | `%rax` |
| Floating point | `%xmm0` |

## 9. Memory Permissions (Security)

Each memory region has specific permissions:

| Permission | Meaning | Sections |
|------------|---------|----------|
| `r--` | Read only | .rodata |
| `r-x` | Read + Execute | .text |
| `rw-` | Read + Write | .data, .bss, stack, heap |

This implements **W^X (Write XOR Execute)** — memory is either writable or executable, never both. This prevents code injection attacks.

## 10. Stack Alignment

The x86-64 ABI requires the stack to be **16-byte aligned** before any `call` instruction.

### How Alignment is Maintained

```
Before callq:     rsp = 0x7fff0010  (16-aligned ✓)

callq pushes return address (8 bytes):
                  rsp = 0x7fff0008  (misaligned!)

pushq %rbp:       rsp = 0x7fff0000  (16-aligned ✓)

subq $0x10:       rsp = 0x7ffefff0  (16-aligned ✓)
```

```asm
# At function entry: rsp is misaligned (callq pushed 8-byte return address)
pushq  %rbp           # rsp -= 8 → restores 16-byte alignment
movq   %rsp, %rbp
subq   $0x10, %rsp    # rsp -= 16 → maintains alignment (multiple of 16)
```

**Key insight:** The `callq` instruction breaks alignment by pushing 8 bytes. The first `pushq %rbp` restores it. After that, `subq` must always use a multiple of 16.

**Why alignment matters?** SSE/AVX instructions (used for floating-point and SIMD operations) require 16-byte aligned memory addresses. Misaligned access causes crashes.

## 11. Viewing Memory Maps

To see the actual memory layout of a running process:

```bash
# From LLDB
(lldb) platform shell cat /proc/<pid>/maps

# From terminal
cat /proc/<pid>/maps
```

Sample output:
```
555555554000-555555555000 r--p  max_sum        # ELF headers
555555555000-555555556000 r-xp  max_sum        # .text
555555556000-555555557000 r--p  max_sum        # .rodata
555555558000-555555559000 rw-p  max_sum        # .data, .bss
555555559000-55555557a000 rw-p  [heap]
7ffff7d8a000-7ffff7fa6000 r-xp  libc.so.6
7ffffffde000-7ffffffff000 rw-p  [stack]
```

## 12. Debugging with LLDB

### View Sections
```bash
(lldb) image dump sections
```

### View Stack Frame
```bash
(lldb) frame variable -L    # Show variables with addresses
```

### View Registers
```bash
(lldb) register read
```

### View Memory
```bash
(lldb) memory read -c 32 $rsp    # Read 32 bytes from stack pointer
```

### Disassemble Options
```bash
# Disassemble a function by name
(lldb) disassemble -n main

# Disassemble from specific address
(lldb) disassemble -s 0x555555555140

# Disassemble N instructions from address
(lldb) disassemble -s 0x555555555140 -c 10

# Disassemble address range
(lldb) disassemble -s 0x555555555140 -e 0x555555555180

# Disassemble at current program counter
(lldb) disassemble -p

# Shorthand
(lldb) di -s 0x555555555140 -c 5
```

## Summary

1. Clang compiles C source to ELF binary with distinct sections
2. Kernel creates process and loads dynamic linker
3. Dynamic linker loads executable and shared libraries
4. Memory is mapped with appropriate permissions (r/w/x)
5. Functions use stack frames for local variables and return addresses
6. `callq`/`retq` handle function call mechanics
7. Registers pass first 6 arguments, stack for additional
8. Stack must be 16-byte aligned for ABI compliance
