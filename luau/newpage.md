# newpage

search for string `ipairs`, first  xref:

```c
  sub_260D690(a1, a2: v70, a3: &v254, a4: v78);
  *(_QWORD *)(a1 + 72) -= 16LL;
  sub_26426C0(a1, a2: "ipairs", a3: sub_26413D0, a4: sub_2641170);
  sub_26426C0(a1, a2: "pairs", a3: sub_2641010, a4: sub_2640A50);
  if ( *(_QWORD *)(*(_QWORD *)(a1 + 56) + 80LL) >= *(_QWORD *)(*(_QWORD *)(a1 + 56) + 72LL) )
    sub_2615BD0(a1, a2: 1);
  if ( (*(_BYTE *)a1 & 4) != 0 )
  {
    v79 = *(_QWORD *)(a1 + 56);
    *(_BYTE *)a1 &= ~4u;
    *(_QWORD *)(a1 + 40) = *(_QWORD *)(v79 + 32);
    *(_QWORD *)(v79 + 32) = a1;
  }
  if ( (unsigned __int64)(*(_QWORD *)(a1 + 72) + 16LL) > *(_QWORD *)(*(_QWORD *)(a1 + 48) + 24LL)
    && (unsigned int)sub_25F0900((_QWORD *)a1, a2: 1) == 0 )
  {
    goto LABEL_380;
  }
  v80 = *(_QWORD *)(a1 + 48);
  if ( v80 == *(_QWORD *)(a1 + 24) )
    v81 = *(_QWORD *)(a1 + 128);
  else
    v81 = *(_QWORD *)(**(_QWORD **)(v80 + 8) + 16LL);
  v103 = *(unsigned __int8 *)(a1 + 4);
  v104 = *(_QWORD *)(a1 + 56);
  if ( byte_8043340 < 0 )
  {
    v110 = sub_2645BD0(a1, a2: (_QWORD **)(v104 + 88), a3: 112, a4: 48, a5: 1); // <-- newpage
    v108 = v110 + 16;
    v110[12] -= v110[9];
    ++v110[13];
  }
  else
  {
    v105 = *(_QWORD *)(v104 + 480 + 8LL * byte_8043340);
    v106 = (_QWORD *)(v104 + 480 + 8LL * byte_8043340);
    if ( v105 == 0 )
```

so basically, at that string look down and look for byte_ < =, after it newpage will be called

so the offset is 0x2645BD0
