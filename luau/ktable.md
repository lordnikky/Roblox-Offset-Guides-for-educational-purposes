# KTable

search for string ``"Trying to call method on object of type: `%s` with incorrect arguments"``

```asm
.rdata:0000000006F70910 aTryingToCallMe db 'Trying to call method on object of type: `%s` with incorrect argu'
.rdata:0000000006F70910                                         ; DATA XREF: sub_413BD90+B9↑o
.rdata:0000000006F70910                                         ; sub_4143B70+112↑o ...
```

first xref, decompile

```c
    {
      if ( v7 < 0
        || (v12 = qword_80BBE20[v7], (v10 = (__int64 (__fastcall **)(__int64))sub_B27E20(a1: a3, a2: &v12)) == nullptr) ) // <-- the qword is the needed rva
      {
        sub_4924110(a1: "%s is not a valid member of %s", v9, a2);
      }
      return (*v10)(a1);
    }
  }
  sub_4924110(a1: "Trying to call method on object of type: `%s` with incorrect arguments.", a2); // <-- you're here
}
```

so the offset is 0x80BBE20
