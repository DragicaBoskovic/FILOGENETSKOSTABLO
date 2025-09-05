 Filogenetsko stablo

 Metode izrade filogenetskog stabla

1.Distance-based metode
   - UPGMA
   - Neighbor-Joining

2.Character-based metode
   - Parsimony
   - Maximum Likelihood

Usporedba algoritma

- UPGMA - jednostavan, pretpostavlja molekularni sat
- Neighbor-Joining - ne pretpostavlja molekularni sat, efikasniji
- Maximum Likelihood - statistički najprecizniji

 Python skripte

1. `filogenetsko_stablo.py` - koristi Biopython
2. `jednostavan_filogenetsko_stablo.py` - koristi matplotlib
3. `cytochrome_c_analysis.py` - kompletan workflow citokroma c

## Kako radi

1. Učitava proteinske sekvence iz FASTA fajla
2. Izračunava udaljenosti između sekvenci
3. Gradi stablo pomoću Neighbor-Joining algoritma
4. Prikazuje grafički prikaz stabla
5. Sprema sliku stabla kao PNG fajl

## Studija slučaja: Citokrom c

### 9.1 Odabir i preuzimanje sekvenci
- Sekvence citokroma c iz 6 vrsta (čovjek, konj, tuna, kvasac, kokoš, pšenica)
- FASTA format iz RCSB PDB baze

### 9.2 Višestruko poravnanje  
- Poravnanje sekvenci za identifikaciju homolognih pozicija
- Analiza konzerviranh i varijabilnih regija

### 9.3 Konstrukcija stabala
- UPGMA metoda (pretpostavlja molekularni sat)
- Neighbor-Joining metoda (realniji rezultati)

### 9.4 Bootstrap analiza
- 100 ponavljanja za procjenu pouzdanosti
- Grane >80% smatraju se pouzdanima

### 9.5 Interpretacija rezultata
- Usporedba UPGMA vs NJ metoda
- Evolucijski odnosi između vrsta
- Pouzdanost filogenetskih zaključaka