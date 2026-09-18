# Identity Bitmasks

search for string "Cannot require a non-RobloxScript module from a RobloxScript", first xref, decompile:

```c
    qmemcpy(v155, (const void *)(*(_QWORD *)(a1 + 40) + 48LL), sizeof(v155));
    if ( (sub_1D14D50(a1: v155) & 8) != 0 ) // <-- identity im opsec
    {
      if ( (*(_BYTE *)(v127 + 360) & 1) == 0 )
        sub_498DEC0(a1: "Cannot require a non-RobloxScript module from a RobloxScript", v26, v27); // <-- you're here
```

so the offset is 0x1D14D50

# Identity struct :freezing:, press x on that rva u found in previous guide and go to first xref and look here :shocked:

```c
  *(_QWORD *)a1 = a2;
  *(_OWORD *)(a1 + 8) = *(_OWORD *)a2;
  *(_OWORD *)(a1 + 24) = *(_OWORD *)(a2 + 16);
  *(_QWORD *)(a1 + 40) = *(_QWORD *)(a2 + 48);
  *(_QWORD *)(a1 + 48) = *(_QWORD *)(a2 + 32); <-- struct
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