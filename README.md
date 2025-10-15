# SCScore

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### Description
The SCScore model assigns a synthetic complexity score between 1 and 5 to a molecule. The score is based on the premise that published reactions, overall, should exhibit an increase in synthetic complexity. The model has been trained on 12M reactions from Reaxys.

## Installation

### Quick Setup (New Environment)

Run the setup script to create a new virtual environment and install:

```bash
./setup.sh
```

### Install into Existing Environment

#### Using uv (Recommended)

If you have an existing uv environment:
```bash
# Activate your existing environment
source /path/to/your/.venv/bin/activate
# Install the package
uv pip install -e .
```

#### Using conda/mamba

If you have an existing conda or mamba environment:
```bash
# Activate your conda environment
conda activate your_env_name
# or: mamba activate your_env_name

# Install dependencies
conda install numpy rdkit six
# or: mamba install numpy rdkit six

# Install this package
pip install -e .
```

#### Using regular pip

For any Python environment:
```bash
# Activate your environment
source your_env/bin/activate

# Install this package (dependencies will be installed automatically)
pip install -e .
```

### Manual Installation (New Environment)

1. Create a virtual environment:
```bash
uv venv
source .venv/bin/activate
```

2. Install the package:
```bash
uv pip install -e .
```

### Alternative: Install from requirements

```bash
uv pip install -r requirements.txt
uv pip install -e .
```

## Usage

### Python API

```python
from scscore import SCScorer, get_score

# Quick scoring (uses default model)
smiles, score = get_score('CCO')
print(f"Score for {smiles}: {score:.2f}")

# Advanced usage with custom model
scorer = SCScorer()
scorer.restore()  # Load default model
canonical_smiles, score = scorer.get_score_from_smi('CCCNc1ccccc1')
print(f"Score: {score:.4f} for {canonical_smiles}")

# Batch scoring
smiles_list = ['CCO', 'CCC', 'CCCNc1ccccc1']
for smi in smiles_list:
    canonical_smi, score = scorer.get_score_from_smi(smi)
    print(f"{score:.4f} <--- {canonical_smi}")
```

### Command Line Interface

```bash
# Score individual molecules
scscore 'CCO' 'CCC'

# Score molecules from a file
scscore -f molecules.smi

# Use custom model
scscore -m path/to/model.json.gz 'CCO'

# Verbose output
scscore -v 'CCO'
```

### Usage with the standalone numpy model
The standalone numpy model is defined in ```scscore/standalone_model_numpy.py```

```python
from scscore.standalone_model_numpy import SCScorer
import os

model = SCScorer()
model.restore()
smiles = 'CCCOCCC'
canonical_smiles, score = model.get_score_from_smi(smiles)
print(f'Score: {score:.4f} for {canonical_smiles}')
```

## Dependencies

### Core Dependencies (for using the final model)
- Python 3.8+
- RDKit
- numpy
- six

### Optional Dependencies

#### For TensorFlow model (legacy)
```bash
uv pip install -e ".[tensorflow]"
```

#### For training/development
```bash
uv pip install -e ".[training]"
```

#### For development
```bash
uv pip install -e ".[dev]"
```

## Model Files

The package includes pre-trained models in the `models/` directory:
- `full_reaxys_model_1024bool/`: Boolean fingerprint model (1024 bits)
- `full_reaxys_model_2048bool/`: Boolean fingerprint model (2048 bits)  
- `full_reaxys_model_1024uint8/`: Count fingerprint model (1024 bits)

## Performance

The numpy-based model provides fast CPU-based inference suitable for deployment scenarios where GPU acceleration is not necessary.

## Citation

If you use SCScore in your research, please cite the original paper describing the synthetic complexity scoring methodology.
