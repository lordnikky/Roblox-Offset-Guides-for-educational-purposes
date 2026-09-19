# LuaC_Step

search for string "InvalidInstance", second xref, decompile and scroll up until you see that big wall of __int:

```c
  __int64 v73; // rcx
  int v74; // [rsp+20h] [rbp-78h]
  __int64 v75; // [rsp+40h] [rbp-58h]
  __int128 v76; // [rsp+58h] [rbp-40h] BYREF
  __int64 v77; // [rsp+A8h] [rbp+10h]

  v3 = *a2;
  v4 = *(_QWORD *)(a1 + 72);
  v5 = *(_QWORD *)(v4 + 56);
  if ( *a2 != nullptr )
  {
    v19 = ((char *)v3[1] - (char *)*v3) >> 4;
    if ( *(_QWORD *)(v4 + 64) >= v5 )
      sub_2764400(a1, a2: 1); 		// <-- luaC_step
    v20 = *(_BYTE *)(a1 + 2);
    if ( (v20 & 4) != 0 )
    {
      v21 = *(_QWORD *)(a1 + 72);
      *(_BYTE *)(a1 + 2) = v20 & 0xFB;
      *(_QWORD *)(a1 + 56) = *(_QWORD *)(v21 + 40);
      *(_QWORD *)(v21 + 40) = a1;
    }
    if ( (unsigned __int64)(*(_QWORD *)(a1 + 88) + 16LL) > **(_QWORD **)(a1 + 64)
      && (unsigned int)sub_273DD50(a1, a2: 1) == 0 )
    {
LABEL_135:
      sub_2772A20(a1, a2: "stack overflow");
      sub_2740680(a1);
    }
```

so the offset is 0x2764400