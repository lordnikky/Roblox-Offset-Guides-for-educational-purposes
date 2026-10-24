# FireMouseClick

string `FLog::DragDetectorLog] DragDetector::updateMouseState LeftMouseUp`, first xref and decompile, from here scroll up till line ~250

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

`proximityPromptOnHeartbeat`, first xref, scroll down till line like 450 idk

```c
                  sub_893A70(a1: &v82, a2: i, a3: v49);
                  i = (__int64 **)v82.m128i_i64[1];
                }
                __unwind
                {
                  sub_74E3F0(a1: &v104);
                }
              }
              else
              {
                *i = nullptr;
                v57 = i + 1;
                i[1] = nullptr;
                v58 = v49[1];
                if ( v58 != nullptr )
                {
                  _InterlockedIncrement((volatile signed __int32 *)v58 + 2);
                  i = (__int64 **)v82.m128i_i64[1];
                  v56 = v105;
                }
                *i = *v49;
                v59 = v49[1];
                *v57 = v59;
                i += 2;
                v82.m128i_i64[1] = (__int64)i;
              }
            }
            if ( v55 != 0 )
              sub_74CFF0(a1: v56);
          }
        }
        v60 = v82.m128i_i64[0];
        for ( j = v82.m128i_i64[0]; (__int64 **)j != i; j += 16 )
        {
          v62 = *(_QWORD ***)j;
          *((_DWORD *)v62 + 4) = 0;
          *(_DWORD *)(*(_QWORD *)j + 20LL) = 2;
          sub_312C650(a1: (__int64)*v62);
          sub_312C010(a1: *v62); // <-- FireProximityPrompt
        }
      }
      __unwind
      {
        sub_76A810(a1: &v82);
      }
      if ( v60 != 0 )
      {
        if ( (__int64 **)v60 != i )
        {
          do
          {
            v63 = *(volatile signed __int32 **)(v60 + 8);
            if ( v63 != nullptr )
            {
              if ( _InterlockedExchangeAdd(v63 + 2, 0xFFFFFFFF) == 1 )
              {
                (**(void (__fastcall ***)(volatile signed __int32 *))v63)(a1: v63);
                if ( _InterlockedExchangeAdd(v63 + 3, 0xFFFFFFFF) == 1 )
                  (*(void (__fastcall **)(volatile signed __int32 *))(*(_QWORD *)v63 + 8LL))(a1: v63);
              }
              i = (__int64 **)v82.m128i_i64[1];
            }
            v60 += 16LL;
          }
          while ( (__int64 **)v60 != i );
          v60 = v82.m128i_i64[0];
```

Basically. look for something that has 1 arg after something + 4) = 0, that 4 will prob change, just saying, not proud of that guide but it'll do

offset is 0x312C010


rest (such as FireMouseHoverEnter, FireMouseHoverLeave) will be found later since I'm lazy shit
