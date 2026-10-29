"""
Sequence Generator for Dynamic Programming Assignment
Generates DNA sequences of varying sizes for testing LCS algorithms.
"""

import random
import json
import os

def generate_sequences():
    """Generate DNA sequence test cases of varying sizes."""
    
    # Create sequences directory
    if not os.path.exists("sequences"):
        os.makedirs("sequences")
    
    print("Generating DNA sequences...\n")
    
    bases = ['A', 'C', 'G', 'T']
    sizes = [10, 20, 50, 100, 200, 500, 1000]
    
    for size in sizes:
        print(f"Generating sequences of length {size}")
        
        # Generate two random DNA sequences
        seq1 = ''.join(random.choice(bases) for _ in range(size))
        seq2 = ''.join(random.choice(bases) for _ in range(size))
        
        # Save to file
        data = {
            "size": size,
            "sequence1": seq1,
            "sequence2": seq2
        }
        
        with open(f"sequences/dna_{size}.json", "w") as f:
            json.dump(data, f, indent=2)
        
        print(f"  ✓ Generated: sequences/dna_{size}.json")
    
    print("\n" + "="*70)
    print("Sequence generation complete!")
    print("\nYou can now implement your LCS algorithms in starter_code.py")
    print("and test performance on sequences of increasing size.\n")

if __name__ == "__main__":
    generate_sequences()