# Capability

search for string "Cannot require a non-RobloxScript module from a RobloxScript", first xref, decompile:

```c
    qmemcpy(v155, (const void *)(*(_QWORD *)(a1 + 40) + 48LL), sizeof(v155));
    if ( (sub_1D14D50(a1: v155) & 8) != 0 ) // <-- identity im opsec
    {
      if ( (*(_BYTE *)(v127 + 360) & 1) == 0 )
        sub_498DEC0(a1: "Cannot require a non-RobloxScript module from a RobloxScript", v26, v27); // <-- you're here
```

so the offset is 0x1D14D50

<details>

<summary><b>verify that its correct: </b></summary>

```c
__int64 __fastcall sub_1CA23E0(_DWORD *a1)
{
  __int64 result; // rax

  switch ( *a1 )
  {
    case 1:
    case 4:
      result = 0x2000000000000003LL;
      break;
    case 3:
      result = 0x300000000000000BLL;
      break;
    case 5:
      result = 0x2000000000000001LL;
      break;
    case 6:
      result = 0x700000000000000BLL;
      break;
    case 7:
    case 8:
      result = 0x200000000000003FLL;
      break;
    case 9:
    case 0xD:
      result = 12;
      break;
    case 0xA:
      result = 0x6000000000000003LL;
      break;
    case 0xB:
      result = 0x2000000000000000LL;
      break;
    case 0xC:
      result = 0x1000000000000000LL;
      break;
    default:
      result = 0;
      break;
  }
  return result;
}
```

</details>

# Capability struct :freezing:

press x on that rva u found in previous guide and go to first xref and look here :shocked:

```c
  *(_QWORD *)a1 = a2;
  *(_OWORD *)(a1 + 8) = *(_OWORD *)a2;
  *(_OWORD *)(a1 + 24) = *(_OWORD *)(a2 + 16);
  *(_QWORD *)(a1 + 40) = *(_QWORD *)(a2 + 48);
  *(_QWORD *)(a1 + 48) = *(_QWORD *)(a2 + 32); // <-- struct
  *(_BYTE *)(a1 + 56) = *(_BYTE *)(a2 + 40);
  v5 = sub_1D14D50(a1: a3); // <-- you're here 
  v10 = v9 & 0xFFFFFFFFFFFFFF00uLL | v5;
  if ( byte_81DDC48 != 0 )
  {
    *(_QWORD *)&v15 = a5;
LABEL_3:
    BYTE8(v15) = *(_BYTE *)(v7 + 40);
```

so to get the 0x__ thingy just press x on 48, ida will show u 0x30 or whatever value you'll have in future version

0xFFFFFFFFFFFFFF00uLL is capability mask
