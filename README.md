 Filogenetsko stablo

 Metode izrade filogenetskog stabla

1.Distance-based metode
   - UPGMA
   - Neighbor-Joining

2.Character-based metode
   - Parsimony
   - Maximum Likelihood

Usporedba algoritama

- UPGMA - jednostavan, pretpostavlja molekularni sat
- Neighbor-Joining - ne pretpostavlja molekularni sat, efikasniji
- Maximum Likelihood - statistički najprecizniji

 Python skripte

1. `filogenetsko_stablo.py` - koristi Biopython
2. `jednostavan_filogenetsko_stablo.py` - koristi matplotlib

## Kako radi

1. Učitava proteinske sekvence iz FASTA fajla
2. Izračunava udaljenosti između sekvenci
3. Gradi stablo pomoću Neighbor-Joining algoritma
4. Prikazuje grafički prikaz stabla
5. Sprema sliku stabla kao PNG fajl