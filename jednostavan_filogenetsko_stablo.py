import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as mpatches

def create_phylogenetic_tree():
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    
    nodes = {
        'root': (0, 2),
        'branch1': (2, 3),
        'branch2': (2, 1),
        'hemoglobin': (4, 3.5),
        'myoglobin': (4, 2.5),
        'insulin': (4, 1.5),
        'cytochrome': (4, 0.5)
    }
    
    branches = [
        ('root', 'branch1'),
        ('root', 'branch2'),
        ('branch1', 'hemoglobin'),
        ('branch1', 'myoglobin'),
        ('branch2', 'insulin'),
        ('branch2', 'cytochrome')
    ]
    
    for start, end in branches:
        x1, y1 = nodes[start]
        x2, y2 = nodes[end]
        
        ax.plot([x1, x2], [y1, y1], 'k-', linewidth=2)
        ax.plot([x2, x2], [y1, y2], 'k-', linewidth=2)
    
    protein_labels = ['Hemoglobin', 'Myoglobin', 'Insulin', 'Cytochrome C']
    protein_positions = [(4, 3.5), (4, 2.5), (4, 1.5), (4, 0.5)]
    
    for i, (label, pos) in enumerate(zip(protein_labels, protein_positions)):
        ax.text(pos[0] + 0.1, pos[1], label, fontsize=12, 
                verticalalignment='center', fontweight='bold')
        
        bbox = FancyBboxPatch((pos[0] + 0.05, pos[1] - 0.15), 
                             len(label) * 0.08, 0.3,
                             boxstyle="round,pad=0.02", 
                             facecolor='lightblue', 
                             edgecolor='navy', linewidth=1)
        ax.add_patch(bbox)
    
    ax.set_xlim(-0.5, 6)
    ax.set_ylim(0, 4)
    ax.set_title('Filogenetsko stablo proteinskih sekvenci', fontsize=16, fontweight='bold')
    ax.set_xlabel('Evolucijska udaljenost', fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    
    ax.set_yticks([])
    
    legend_elements = [
        mpatches.Patch(color='lightblue', label='Proteinske sekvence'),
        mpatches.Patch(color='black', label='Evolucijski odnosi')
    ]
    ax.legend(handles=legend_elements, loc='upper left')
    
    plt.tight_layout()
    plt.savefig('filogenetsko_stablo.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Filogenetsko stablo je uspješno generirano i spremljeno kao 'filogenetsko_stablo.png'")
    print("\nObjašnjenje:")
    print("- Hemoglobin i Myoglobin su srodnije (oba su proteini koji vežu kisik)")
    print("- Insulin i Cytochrome C su na zasebnoj grani")
    print("- Duljina grana predstavlja evolucijsku udaljenost između proteina")

if __name__ == "__main__":
    create_phylogenetic_tree()
