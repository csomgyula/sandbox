# Goal oriented

## Célszerűség

### Célok
- Minden IT dolognak (pl. adat, funkció, folyamat) 
  - van eredete (itt kevésbé fontos)
  - van célja, amiért létrejött, létezik
- A goal oriented programming esetén pl. 
  - közvezlen célja a hatékony garbage collection, takarékosság, illetve:
  - vizsgált, hogy mennyire alkalmazható az alternatívák kezelésére (ugyanaz a cél többféleképpen is elérhető)

### Érdekeltség
- Minden célnak van érdekeltje, aminek az érdekében történik

### Alapvetések
- A goal oriented rendszernek vannak alapvetései, olyan célok, érdekeltek, amik a rendszeren kívül vannak

### Relációk
- Szeletelés: A cékok között ilyen rendezett (PO) relációk lehetségesek:
  - Magasabb szintű cél vs. alacsonyabb rendű
  - Alcélok: adott cél elérhető az alcélok megvalósításával
  - Alternatívák: a cél megoldható az alternativák bármelyikével
  - A fenti nem feltétlen hierarchia, hanem általában csak N:M kapcsolat, azaz részben rendezés
- Rekurzió: A cékok között ilyen numerikus relációk lehetségesek:
  - Rekurzió, ez az alcélok olyan verziója, ami rekurzív

### Fajták

- Hard: Must
- Soft: Should, Nice

### Alapvetések 2

1. Először a Must, utána a Should, utána a Nice
2. Minden IT dolog célszerűen csak addig létezhet, amíg a legmagasabb hard céljai (alapvetések) nincs kielégítve. Ez nem azt jelenti, hogy addig létezik is (vö. idő constraintek), csak azt, hogy utána már nem muszáj

Példa:
- folyamat addig fut, amig ki nem számolja amit ki kell, de amit ki akar számolni az is valamilyen célt szolgál, így nem feltétlenül kell addig futnia, ha már a magasabb cél ki van elégítve, akkor megszakítható a futása
- egy state, (tudás, információ a memóriában) addig létezik, amíg a célját be nem töltötte
  - amik van (lehet) olyan folyamat, ami használja, használni akarja
  - az őt létrehozó funkció magas szintű célja nincs betöltve
- fenti érvényes stateful funkciókra, objektumokra is, ahol a használat nem query, hanem execute v. több query valamelyike

## Megkötések
TODO

