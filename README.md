# Assignment 6: Making the Impossible Possible

## Setup Instructions

### 1. Clone this repository and open in VS Code

```bash
git clone <REPO_URL>
cd dp-assignment
code .
```

### 2. Generate the DNA sequences

Run the sequence generator to create test cases of varying sizes:

```bash
python sequence_generator.py
# You may need to run python3 sequence_generator.py
```

This will create:
- `sequences/dna_10.json` - 10 base pair sequences
- `sequences/dna_20.json` - 20 base pair sequences
- `sequences/dna_50.json` - 50 base pair sequences
- `sequences/dna_100.json` - 100 base pair sequences
- `sequences/dna_200.json` - 200 base pair sequences
- `sequences/dna_500.json` - 500 base pair sequences
- `sequences/dna_1000.json` - 1000 base pair sequences

### 3. Implement your LCS algorithms

Open `starter_code.py` and complete the three functions:
1. `lcs_recursive()` - Naive recursive solution (will be slow)
2. `lcs_memoization()` - Top-down dynamic programming with caching
3. `lcs_tabulation()` - Bottom-up dynamic programming with table

### 4. Test and compare

Uncomment the test functions in the `__main__` block:

```python
if __name__ == "__main__":
    test_small_cases()          # Verify correctness on small inputs
    time_recursive()            # See how slow recursive becomes
    compare_all_approaches()    # Compare all three on large inputs
```

Then run:

```bash
python starter_code.py
# or python3 starter_code.py
```

## The Problem: Longest Common Subsequence (LCS)

Given two DNA sequences, find the length of their longest common subsequence.

A **subsequence** is a sequence that appears in the same relative order but not necessarily contiguous.

**Example:**
- Sequence 1: `AGGTAB`
- Sequence 2: `GXTXAYB`
- LCS: `GTAB` (length 4)

The characters G, T, A, B appear in both sequences in that order (though not consecutively). The DNA sequences that you will analyze in this assignment will be composed of strings that have a combination of the letters G, C, T, and A (the four bases found in DNA stands).

## What to Submit

Submit two items:
1. **GitHub repository link** containing your completed code
2. **Written analysis document** (Google Doc or Word) containing:
   - Recursive Analysis section (100-150 words)
   - Dynamic Programming Comparison section (200-250 words)
   - Total: 300-400 words

Good luck! Remember: the key skill is recognizing when and how to optimize.