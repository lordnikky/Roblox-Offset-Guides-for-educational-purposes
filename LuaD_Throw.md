# LuaD_Throw

search for string "Unexpected trailing character: '{}'", first xref, decompile and scroll to the very end:

```c
            *(_QWORD *)(a2 + 88) += 16LL;
            goto LABEL_78;
          }
        }
      }
      sub_2750300(a1: a2, a2: 4u); // <-- luad_throw
    }
LABEL_90:
    sub_2772A20(a1: a2, a2: "stack overflow");
    sub_2740680(a1: a2, a2: v44, a3: v45);
  }
LABEL_78:
  if ( v64 != 0 )
  {
    *(_QWORD *)&v55 = v63;
    *((_QWORD *)&v55 + 1) = v64;
    v62 = v55;
    sub_41FC6F0(a1: a2, a2: 0xFFFFFFFFLL, a3: &v62, a4: &v51);
  }
  v42 = *((_QWORD *)&v52 + 1);
  if ( *((_QWORD *)&v52 + 1) != 0
    && _InterlockedExchangeAdd((volatile signed __int32 *)(*((_QWORD *)&v52 + 1) + 12LL), 0xFFFFFFFF) == 1 )
  {
    (*(void (__fastcall **)(__int64))(*(_QWORD *)v42 + 8LL))(a1: v42);
  }
  if ( v63 != v66 )
    sub_49701B0(a1: (unsigned __int64)v63, a2: (__int64)v66, a3: v16);
  return 1;
}
```

so the offset is 0x2750300
