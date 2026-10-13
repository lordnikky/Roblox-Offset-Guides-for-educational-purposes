# FireMouseClick

string "FLog::DragDetectorLog] DragDetector::updateMouseState LeftMouseUp", first xref and decompile, from here scroll up till line ~250

```c
          && (*(unsigned __int8 (__fastcall **)(__int64))(*(_QWORD *)a1 + 712LL))(a1) == 0 )
        {
          if ( __eh34_unwind(4) )
            goto unwind_state_4;
          __eh34_exit_wind_state(4, 3);
          if ( *((_QWORD *)&v68 + 1) != 0 )
            sub_71D380(a1: *((_QWORD *)&v68 + 1));
          if ( *((_QWORD *)&v67 + 1) != 0 )
            sub_71D380(a1: *((_QWORD *)&v67 + 1));
          v60 = 0;
        }
        else
        {
          if ( a3 != 0 )
          {
            if ( a3 == 1 )
            {
              if ( *(_BYTE *)(a1 + 312) != 0 )
                sub_3BCF940(a1, a2, a3: a4); <-- firemouselick
              *(_BYTE *)(a1 + 312) = 0;
              v28 = v65;
              if ( v65 != 0 )
              {
                *(_QWORD *)v65 = 0;
                v29 = *(_QWORD *)(v28 + 8);
                *(_QWORD *)(v28 + 8) = 0;
                if ( v29 != 0 )
                  sub_71D380(a1: v29);
              }
            }
            else if ( a3 == 2 )
            {
              *(_BYTE *)(a1 + 313) = 1;
            }
            else if ( a3 == 3 && *(_BYTE *)(a1 + 313) != 0 )
            {
              sub_3BCFAE0(a1, a2: v27, a3: a4);
            }
          }
          else
```

scroll till you see byte check + number != 0 and after that there should be call of an rva, and after call there will be byte a1+number = 0, not a good guide not the best one but it'll work
offset is 0x3BCF940

# FireRightMouseClick

right after FireMouseClick, like 10 lines down from it there will be

```c
                if ( v28 != 0 )
                  sub_71D380(a1: v28);
              }
            }
            else if ( a3 == 2 )
            {
              *(_BYTE *)(a1 + 313) = 1;
            }
            else if ( a3 == 3 && *(_BYTE *)(a1 + 313) != 0 )
            {
              sub_3BCFAE0(a1, a2, a3: a4);
            }
          }
          else
          {
            *(_BYTE *)(a1 + 312) = 1;
          }
          if ( __eh34_unwind(4) )
          {
```

find this block, notice something familiar?             else if ( a3 == 3 && *(_BYTE *)(a1 + 313) != 0 ) yes, right after it the called rva will be firerightmouseclick

so the offset is 0x3BCFAE0

# FireProximityPrompt

"ProximityPrompt_Triggered", first xref will be it

```asm
.rdata:00000000071E8C00 xmmword_71E8C00 xmmword 5F74706D6F72507974696D69786F7250h
.rdata:00000000071E8C00                                         ; DATA XREF: sub_30CFF60+2B4↑r
.rdata:00000000071E8C10 qword_71E8C10   dq 6572656767697254h    ; DATA XREF: sub_30CFF60+2BE↑r
.rdata:00000000071E8C18 byte_71E8C18    db 64h                  ; DATA XREF: sub_30CFF60+2CB↑r
```

offset is 0x30CFF6


rest (such as FireMouseHoverEnter, FireMouseHoverLeave) will be found later since I'm lazy shit
