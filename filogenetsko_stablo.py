import os
from Bio import SeqIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import Phylo
import matplotlib.pyplot as plt

SEQUENCE_DIR = "sequences"

sequences = list(SeqIO.parse(os.path.join(SEQUENCE_DIR, "all_sequences.fasta"), "fasta"))

calculator = DistanceCalculator('identity')
dm = calculator.get_distance(sequences)

constructor = DistanceTreeConstructor()
tree = constructor.nj(dm)

Phylo.draw(tree)
plt.show()

Phylo.draw(tree, do_show=False)
plt.savefig("filogenetsko_stablo.png")
print("Stablo je spremljeno kao filogenetsko_stablo.png")
