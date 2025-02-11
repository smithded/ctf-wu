1. dogbolt.org
2. Ghidra give this to us

```
#include "out.h"

int _init(EVP_PKEY_CTX *ctx)

{
  int iVar1;
  
  iVar1 = __gmon_start__();
  return iVar1;
}



void FUN_00401020(void)

{
  (*(code *)(undefined *)0x0)();
  return;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

char * strncpy(char *__dest,char *__src,size_t __n)

{
  char *pcVar1;
  
  pcVar1 = strncpy(__dest,__src,__n);
  return pcVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int puts(char *__s)

{
  int iVar1;
  
  iVar1 = puts(__s);
  return iVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

size_t strlen(char *__s)

{
  size_t sVar1;
  
  sVar1 = strlen(__s);
  return sVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int printf(char *__format,...)

{
  int iVar1;
  
  iVar1 = printf(__format);
  return iVar1;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int strcmp(char *__s1,char *__s2)

{
  int iVar1;
  
  iVar1 = strcmp(__s1,__s2);
  return iVar1;
}



void __isoc99_scanf(void)

{
  __isoc99_scanf();
  return;
}



void processEntry _start(undefined8 param_1,undefined8 param_2)

{
  undefined auStack_8 [8];
  
  __libc_start_main(main,param_2,&stack0x00000008,0,0,param_1,auStack_8);
  do {
                    // WARNING: Do nothing block with infinite loop
  } while( true );
}



void _dl_relocate_static_pie(void)

{
  return;
}



// WARNING: Removing unreachable block (ram,0x004010dd)
// WARNING: Removing unreachable block (ram,0x004010e7)

void deregister_tm_clones(void)

{
  return;
}



// WARNING: Removing unreachable block (ram,0x0040111f)
// WARNING: Removing unreachable block (ram,0x00401129)

void register_tm_clones(void)

{
  return;
}



void __do_global_dtors_aux(void)

{
  if (completed_0 == '\0') {
    deregister_tm_clones();
    completed_0 = 1;
    return;
  }
  return;
}



void frame_dummy(void)

{
  register_tm_clones();
  return;
}



void transform(char *param_1)

{
  size_t sVar1;
  int local_1c;
  
  local_1c = 0;
  while( true ) {
    sVar1 = strlen(param_1);
    if (sVar1 <= (ulong)(long)local_1c) break;
    param_1[local_1c] = (param_1[local_1c] ^ 0x3fU) + 5;
    local_1c = local_1c + 1;
  }
  return;
}



bool check_input(char *param_1)

{
  int iVar1;
  char local_48 [26];
  undefined local_2e;
  char local_28 [32];
  
  builtin_strncpy(local_28,"TUaP^IOMQTe\r\\\x11eV\x13\x0e\\\re\x13\x0fe`\x10RYG",0x1d);
  strncpy(local_48,param_1,0x1a);
  local_2e = 0;
  transform(local_48);
  iVar1 = strcmp(local_48,local_28);
  return iVar1 == 0;
}



void reveal_flag(void)

{
  puts("Correct!");
  return;
}



undefined8 main(void)

{
  int iVar1;
  undefined local_28 [32];
  
  printf("Enter the correct input: ");
  __isoc99_scanf(&DAT_00402027,local_28);
  iVar1 = check_input(local_28);
  if (iVar1 == 0) {
    puts("Incorrect input. Try again.");
  }
  else {
    reveal_flag();
  }
  return 0;
}



void _fini(void)

{
  return;
}
```

The provided code is a decompiled C program that checks user input against a transformed version of a hardcoded string. The `transform` function XORs each character of the input string with `0x3f` (63) and adds 5 to the result. The `check_input` function compares the transformed input string with the transformed hardcoded string. If they match, the `reveal_flag` function is called, which prints "Correct!".

To find a valid input, you can reverse the `transform` function. Here's a Python script that does that:

```
def reverse_transform(s):
    return ''.join([chr((ord(c) - 5) ^ 0x3f) for c in s])

hardcoded_string = "TUaP^IOMQTe\r\\\x11eV\x13\x0e\\\re\x13\x0fe`\x10RYG"
valid_input = reverse_transform(hardcoded_string)
print(valid_input)
```

Run this script, and it will print a valid input that you can use to reveal the flag.

**poctf{uwsp_7h3_n16h7_15_d4rk}**
 
