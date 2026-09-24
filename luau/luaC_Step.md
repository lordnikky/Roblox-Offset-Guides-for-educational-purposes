# LuaC_Step

search for string "InvalidInstance", second xref, decompile and scroll up until you see that big wall of __int:

```c
  v4 = *(_QWORD *)(a1 + 24);
  v5 = *(_QWORD *)(v4 + 80);
  if ( *a2 != nullptr )
  {
    v19 = ((char *)v3[1] - (char *)*v3) >> 4;
    if ( *(_QWORD *)(v4 + 88) >= v5 )
    {
      LOBYTE(a2) = 1;
      sub_26838F0(a1, a2); // <-- luaC_Step
    }
    v20 = *(_BYTE *)(a1 + 1);
    if ( (v20 & 4) != 0 )
    {
      v21 = *(_QWORD *)(a1 + 24);
      *(_BYTE *)(a1 + 1) = v20 & 0xFB;
      *(_QWORD *)(a1 + 80) = *(_QWORD *)(v21 + 56);
      *(_QWORD *)(v21 + 56) = a1;
    }
    if ( (unsigned __int64)(*(_QWORD *)(a1 + 40) + 16LL) > **(_QWORD **)(a1 + 8)
      && (unsigned int)sub_265C4D0(a1, a2: 1) == 0 )
    {
LABEL_134:
      sub_26968A0(a1, a2: "stack overflow");
      sub_265EE60(a1);
    }
    v86 = *(_QWORD *)(a1 + 40);
    v22 = *(unsigned __int8 *)(a1 + 4);
    v23 = *(_QWORD *)(a1 + 24);
    if ( byte_7D64A70 < 0 )
    {
```

so the offset is 0x26838F0
