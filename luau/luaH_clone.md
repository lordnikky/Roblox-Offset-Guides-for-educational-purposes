# luaH_clone

search for string `table has a protected metatable`, second xref and decompile:

```c
  if ( (unsigned int)sub_2592E80(a1, a2: 1, a3: &qword_6F7DBC8) != 0 ) // <-- hallo zir, you ar here
    sub_25905A0(a1, a2: 1, a3: "table has a protected metatable");
  *(_QWORD *)&v4 = sub_25BED00(a1, a2: *(_QWORD *)a1[5]); // luaH_clone
```

so the offset is 0x25BED00

<details>

<summary><b>verify</b></summary>

so it has 2 args, 

```c
  v2 = *(unsigned __int8 *)(a1 + 4);
  v4 = *(_QWORD *)(a1 + 24);
  if ( byte_7DEB930 < 0 ) // <-- checks if its less than 0, if it is then it calls newpage to allocate 112 byes
  {
    v11 = (_DWORD *)sub_25C9AF0(a1, a2: (int)v4 + 800, a3: 112, a4: 48, a5: 1);
    v9 = v11 + 16;
    v11[12] -= v11[9];
    ++v11[13];
  }
  else
  {
    v6 = *(_QWORD *)(v4 + 424 + 8LL * byte_7DEB930);
    v7 = (_QWORD *)(v4 + 424 + 8LL * byte_7DEB930);
    if ( v6 == 0 )
      v6 = sub_25C9C60(a1, a2: v4 + 424, a3: (int)v4 + 800, a4: byte_7DEB930, a5: 0); // calls newclasspage too
    v8 = *(int *)(v6 + 48);
    if ( (int)v8 < 0 )
    {
      v9 = *(_DWORD **)(v6 + 40);
      *(_QWORD *)(v6 + 40) = *((_QWORD *)v9 + 1);
    }
    else
    {
      v9 = (_DWORD *)(v8 + v6 + 64);
      LODWORD(v8) = v8 - *(_DWORD *)(v6 + 36);
      *(_DWORD *)(v6 + 48) = v8;
    }
```

</details>
