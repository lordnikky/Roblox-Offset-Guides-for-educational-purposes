# dumpgco

search for string `{\"type\":\"string\",\"cat\":%d,\"size\":%d,\"data\":\`, first xref is it 

```c
.rdata:0000000007141A58 aTypeStringCatD db '{"type":"string","cat":%d,"size":%d,"data":"',0
.rdata:0000000007141A58                                         ; DATA XREF: sub_2659700+50↑o
.rdata:0000000007141A85                 align 8
.rdata:0000000007141A88 asc_7141A88     db '"}',0               ; DATA XREF: sub_2659700+6C↑o
.rdata:0000000007141A88                                         ; sub_37B3610+440↑o ...
```

so the offset is sub_27261C0

sig: 48 89 5C 24 ? 57 48 83 EC 20 48 8D 15

<details>

<summary><b>verify</b></summary>


2 args

```c
      sub_71D250(a1: Stream, a2: "{\"type\":\"function\",\"cat\":%d,\"size\":%d", a2[1], v5 + 16 * a2[5]);
      sub_71D250(a1: Stream, a2: ",\"env\":");
      sub_71D250(a1: Stream, a2: "\"%p\"", *(a2 + 2));
      if ( a2[3] != 0 )
      {
        v6 = *(a2 + 4);
        if ( v6 != 0 )
          sub_71D250(a1: Stream, a2: ",\"name\":\"%s\"", (v6 + 24));
        if ( a2[5] != 0 )
        {
LABEL_15:
          sub_71D250(a1: Stream, a2: ",\"upvalues\":[");
          sub_2658E50(Stream);
          sub_71D250(a1: Stream, a2: "]");
        }
      }
      else
      {
        v7 = *(a2 + 3) + 16LL;
        if ( v7 != *v7 )
          sub_71D250(a1: Stream, a2: ",\"name\":\"%s\"", ((v7 ^ *v7) + 24));
        sub_71D250(a1: Stream, a2: ",\"proto\":");
        sub_71D250(a1: Stream, a2: "\"%p\"", *(a2 + 3));
        if ( a2[5] != 0 )
          goto LABEL_15;
      }
      return sub_71D250(a1: Stream, a2: "}");
    case 9u:
      v8 = *(a2 + 1);
      if ( v8 > 16 )
        v8 = (v8 + 15) & 0xFFFFFFF0;
      sub_71D250(a1: Stream, a2: "{\"type\":\"userdata\",\"cat\":%d,\"size\":%d,\"tag\":%d", a2[1], v8 + 16, a2[3]);
      v9 = a2 + 8;
      if ( *v9 == v9 )
        return sub_71D250(a1: Stream, a2: "}");
      sub_71D250(a1: Stream, a2: ",\"metatable\":");
```

can be verified by the fact that it prints what it dumps
  
</details>
