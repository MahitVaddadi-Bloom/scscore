"""Command line interface for SCScore."""

import argparse
import sys
from .standalone_model_numpy import SCScorer


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description='Calculate synthetic complexity scores for molecules')
    parser.add_argument('smiles', nargs='*', help='SMILES strings to score')
    parser.add_argument('-f', '--file', help='File containing SMILES strings (one per line)')
    parser.add_argument('-m', '--model', help='Path to model weights file')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    if not args.smiles and not args.file:
        parser.error("Must provide either SMILES strings or a file containing SMILES")
    
    # Initialize scorer
    scorer = SCScorer()
    if args.model:
        scorer.restore(args.model)
    else:
        scorer.restore()
    
    # Collect SMILES
    smiles_list = []
    if args.smiles:
        smiles_list.extend(args.smiles)
    
    if args.file:
        try:
            with open(args.file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        smiles_list.append(line)
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found")
            sys.exit(1)
    
    # Score molecules
    for smi in smiles_list:
        canonical_smi, score = scorer.get_score_from_smi(smi, v=args.verbose)
        if canonical_smi:
            print(f"{score:.4f}\t{canonical_smi}")
        else:
            print(f"ERROR\t{smi}")


if __name__ == '__main__':
    main()