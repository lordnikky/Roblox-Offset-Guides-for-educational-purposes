# HashLookUp

search for string "data_model_service_init_part3_begin", first xref, decompile:

```c
                  if ( v181 != 0 )
                    sub_35A2510(a1: v138);
                  v221 = a1;
                  sub_362C3D0(a1: v138 + 568, a2: v196, a3: &v221);
                  sub_74DEB0(a1: v196);
                  v140 = sub_7678F0(a1: &v184);
                  v317 = *(_OWORD *)sub_74DCE0(a1: v339, a2: "data_model_service_init_part2_end", a3: v140);
                  sub_522E260(a1: v141, a2: &v317);
                  v142 = sub_7678F0(a1: &v184);
                  v318 = *(_OWORD *)sub_74DCE0(a1: v338, a2: "data_model_service_init_part3_begin", a3: v142); // <-- you are here
                  sub_522E260(a1: v143, a2: &v318);
                  sub_362C4A0(a1: v56);
                  sub_31D3DF0(a1: v56);
                  sub_362C4B0(a1: v56);
                  sub_362C4C0(a1: v56);
                  sub_362C4D0(a1: v56);
                  sub_362C4E0(a1: v56);
                  v144 = sub_2AB0720(a1: "GamePassService"); // this is the hashlookup
                  sub_290B3A0(a1: v319, a2: v56, a3: v144);
                  sub_74E3F0(a1: v319);
                  sub_362C4F0(a1: v56);
```

so the offset is 0x2A6F370

<details>

<summary><b>verify:</b></summary>

```c
__int64 __fastcall sub_2AB0720(__int64 a1)
{
  __int64 v1; // rax

  v1 = qword_8DCFB98;
  if ( qword_8DCFB98 == 0 )
    v1 = sub_2AB0300(a1);
  return sub_2AB03C0(a1: v1, a2: a1);
}
```

that should be the whole function, takes 1 arg
  
</details>
