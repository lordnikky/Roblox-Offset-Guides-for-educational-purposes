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

has been removed cuz it was wrong ill find it later

0xFFFFFFFFFFFFFF00uLL is capability mask
