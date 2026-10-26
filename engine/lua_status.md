# LuaStatus

apparently it's an offset and idk if its any useful but i'll add it because i can

string "FrameRateManager", LAST xref, last well actual xref, not rdata

scroll till the end, search for 0.0000009536743f, or well, v__ * 0.________ or something

```c
LABEL_51:
        *(_DWORD *)(a1 + 76) = 0;
LABEL_52:
        *(_DWORD *)(a1 + 80) = LODWORD(v35);
        if ( byte_8758218 != 0 )
        {
          v47 = sub_2AB5DC0();
          if ( v47 < 0 )
            v48 = (float)(v47 & 1 | ((unsigned __int64)v47 >> 1)) + (float)(v47 & 1 | ((unsigned __int64)v47 >> 1));
          else
            v48 = (float)v47;
          *(float *)(a1 + 84) = v48 * 0.0000009536743f; // let this be your achor idk
        }
        v49 = (_DWORD *)sub_31EFFF0(a1: v12);
        if ( v49 != nullptr )
        {
          sub_425F880(a1: v49, a2: &v55); // <-- Lua Status
          *(_DWORD *)(a1 + 96) = v55;
        }
LABEL_59:
        if ( byte_8755C68 != 0 && byte_8A19BC0 != 0 && byte_86D0A58 != 0 )
        {
          v50 = *(_QWORD *)(a2 + 264);
          if ( v50 != 0
            && ((*(__int64 (__fastcall **)(__int64))(*(_QWORD *)v50 + 64LL))(a1: v50) & 0x2000000000000LL) != 0
            && *(_DWORD *)(a2 + 252) == 1
            && *(_BYTE *)(a1 + 92) == 0 )
          {
            if ( qword_8E45160 != 0 )
              v7 = *(_QWORD *)(qword_8E45160 + 24);
            sub_3B2C680(a1: v7, a2: &v53);
            LOBYTE(v51) = (*(_DWORD *)(*(_QWORD *)(a2 + 264) + 1728LL) == 1) + 1;
            sub_3B2E9A0(a1: v54, a2: v51, a3: 0);
            *(_QWORD *)(a1 + 56) = v53;
          }
        }
        return a1;
      }
      v37 = sub_7C9840();
    }
    else
    {
      v37 = a2;
    }
    if ( v37 == 0 )
      goto LABEL_51;
    goto LABEL_40;
  }
  __unwind
  {
    sub_46F67F0(a1: v56);
  }
```

so the offset is 0x425F880, i do NOT know if this is useful, and this is not getluastate its something else
