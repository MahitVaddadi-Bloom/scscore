"""Example usage of SCScore package."""

from scscore import SCScorer, get_score

# Example molecules with varying complexity
molecules = [
    'CCO',                          # Ethanol (simple)
    'CCC',                          # Propane (simple) 
    'c1ccccc1',                     # Benzene (moderate)
    'CCCNc1ccccc1',                 # N-propylaniline (moderate)
    'CC(C)(C)OC(=O)NC1CC1C(=O)O',   # More complex structure
]

print("=== Quick Scoring with get_score() ===")
for smi in molecules[:3]:
    canonical_smi, score = get_score(smi)
    print(f"Score: {score:.4f} for {canonical_smi}")

print("\n=== Advanced Usage with SCScorer Class ===")
scorer = SCScorer()
scorer.restore()  # Load default model

for smi in molecules:
    canonical_smi, score = scorer.get_score_from_smi(smi, v=False)
    if canonical_smi:
        print(f"Score: {score:.4f} for {canonical_smi}")
    else:
        print(f"ERROR: Could not parse {smi}")

print(f"\nModel uses {scorer.FP_len}-bit fingerprints with radius {scorer.FP_rad}")
print("Score range: 1.0 (simple) to 5.0 (complex)")