# BytecodeVerificationTableA

search string "/dev/urandom", first xref decompile, go to the very top 

```c
_QWORD *__fastcall sub_1CCA3E0(_QWORD *a1)
```

press x on that sub_ and go to first xref

```c
__int64 sub_5E1B80()
{
  sub_1CCA3E0(a1: &unk_844ED90);
  return sub_5A29610(a1: sub_6004F80);
}
```

that unk is the bytecodeverificationtablea, so the offset is 0x844ED90
