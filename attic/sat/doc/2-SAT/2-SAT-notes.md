működhet a behelyettesítés változóba két formában is:

1. paritás

ha van olyan x1,x2 ami kétféle alakban is előfordul, akkor csökkenthető a változók száma:

```
(x1, x2) & (x1, ~x2) => x1 true
(x1, x2) & (~x1, ~x2) => x1 = ~x2
```

ha viszont bármely két változó csak egyféle alakban fordul elő, akkor 0,1,2 megoldás 
lehet csak a független részeken

kössük össze a behelyettesített értékeket: 

minden `(x_i, v)`-t azokon a 2-sat kikötéseken keresztül, ahol az `x_i` `v`-vel ellentétes alakban 
szerepel (azaz, amire `v` nem teljesíti az `x_i`-re eső kikötést, ergo a másik tag kell igaz legyen), 
összekötjük a másik tag értékével.

jelölés:

```
^x =  x esetén ^x^ := true
^x = ~x esetén ^x^ := false
```

`(x_i, true)` össze van kötve `(x_j, ^x_j^)`-vel, ha van `(~x_i, ^x_j)` alakú kettes (egyféle lehet)
szavakkal, 

azaz egy behelyettesítés meghatároz egy csomó értéket, egészen, amíg független részhez nem jutok

2. függetlenség

amikor behelyettesítek és következtetéseket vonok le, akkor maradhatnak kettesek, amik nem függnek
a behelyettesítéstől, mármont ezek diszjunktak a kétféle behelyettesítési ágon, vagy ha nem akkor az
ami közös, az független a két ágtól???

egy probléma, amikor így néz ki példán illusztrálva:

(x_1 = true)  not -> (x_3, x_4), (x_4, x_5) az utolsó kettő kikötésben semmi nem levezethető x_1 = true-ból
(x_1 = false) not -> (x_3, x_5), (x_4, x_5) az utolsó kettő kikötésben semmi nem levezethető x_1 = false-ból

vagyis nem üres a metszet sem, a szimmetrikus diff sem és ezek összefüggőek

példa:

(~x_1, x_5), 
	(x_3, x_5)
(x_1, x_4), 	
	(x_3, x_4)
(x_4, x_5)

ami invalid, mivel az x_4, x_5 is kiesik x_1 = true esetén
szóval, elképzelhető, hogy a fenti eset nem állhat elő