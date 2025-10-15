""" 

SCScore: Synthetic Complexity Learned from a Reaction Corpus

This package provides a model for predicting the synthetic complexity of molecules
based on a neural network trained on reaction data from Reaxys.
"""

__version__ = "1.0.0"
__author__ = "SCScore Authors"

from .standalone_model_numpy import SCScorer

# Convenience function for quick scoring
def get_score(smiles, model_path=None):
    """
    Get synthetic complexity score for a SMILES string.
    
    Args:
        smiles (str): SMILES string of the molecule
        model_path (str, optional): Path to model weights. If None, uses default.
    
    Returns:
        tuple: (canonical_smiles, score) where score is between 1-5
    """
    scorer = SCScorer()
    if model_path:
        scorer.restore(model_path)
    else:
        scorer.restore()
    return scorer.get_score_from_smi(smiles)

__all__ = [
    "SCScorer",
    "get_score",
]