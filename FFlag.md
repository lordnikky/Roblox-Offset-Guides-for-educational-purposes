# GetFFlag

search for string "not declared!", second xref, decompile, and scroll up a bit:

```c
LABEL_136:
        v87 = qword_887CA40;
        v88 = qword_887CA40 + 64;
        v135.m128_u64[0] = qword_887CA40 + 64;
        v89 = sub_5A2B400(a1: qword_887CA40 + 64);
        if ( v89 != 0 )
          sub_5A2B9D0(a1: v89);
        v90 = sub_493AF20(a1: v87, a2: v152, a3: (__int64)&v155, a4: 1); <-- getfflag
        sub_5A2B460(a1: v88);
        if ( v90 != 0 )
        {
          if ( v51 < 4 )
          {
            v94 = false;
          }
          else
          {
            v91 = 0;
            while ( 1 )
            {
              v92 = *(_BYTE *)(*(_QWORD *)v137 + v91++);
              if ( v92 != aUser_0[v91 - 1] )
                break;
              if ( v91 == 4 )
              {
                v93 = 0;
                goto LABEL_144;
              }
            }
            v93 = v92 < (unsigned __int8)aUser_0[v91 - 1] ? -1 : 1;
LABEL_144:
            v94 = v93 == 0;
          }
          v82 = "not declared!";	<-- you're here
          if ( v94 )
            v82 = "UserFlag";
        }
        else
```

so the offset is 0x493AF20


# SetFFlag

search for string "[FLog::FastLogValueChanged] Setting variable {}" or "[FLog::FastLogValueChanged] ...(previously unknown)...", first xref will be the setfflag

```asm
.rdata:0000000006FD61A8 aFlogFastlogval db '[FLog::FastLogValueChanged] Setting variable {}',0
.rdata:0000000006FD61A8                                         ; DATA XREF: sub_493A3A0+261↑o
.rdata:0000000006FD61D8 aFlogFastlogval_0 db '[FLog::FastLogValueChanged] ...(previously unknown)...',0
.rdata:0000000006FD61D8                                         ; DATA XREF: sub_493A3A0+328↑o
```

so the offset is 0x493A3A0