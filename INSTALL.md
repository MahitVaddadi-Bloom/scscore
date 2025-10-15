# SCScore Installation Guide

## Quick Installation

The easiest way to install SCScore is using the provided setup script:

```bash
./setup.sh
```

This will create a virtual environment and install all dependencies automatically.

## Manual Installation

### Prerequisites

- Python 3.8 or later
- `uv` package manager ([installation instructions](https://docs.astral.sh/uv/getting-started/installation/))

### Step-by-step Installation

1. **Clone the repository** (if you haven't already):
```bash
git clone <repository-url>
cd scscore
```

2. **Create a virtual environment**:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install the package**:
```bash
uv pip install -e .
```

### Alternative: Install dependencies first

If you prefer to install dependencies separately:

```bash
uv pip install -r requirements.txt
uv pip install -e .
```

## Optional Dependencies

### For TensorFlow support (legacy):
```bash
uv pip install -e ".[tensorflow]"
```

### For training/development:
```bash
uv pip install -e ".[training]"
```

### For development:
```bash
uv pip install -e ".[dev]"
```

## Verification

Test your installation:

```bash
# Test Python API
python -c "from scscore import get_score; print(get_score('CCO'))"

# Test CLI
scscore 'CCO'

# Run example
python example.py
```

## Model Files

The package includes pre-trained models:
- Default: `models/full_reaxys_model_1024bool/model.ckpt-10654.as_numpy.json.gz`
- Alternative models available in other subdirectories of `models/`

## Troubleshooting

### Common Issues

1. **RDKit import errors**: Make sure RDKit is properly installed
2. **Model loading errors**: Verify model files are present in `models/` directory
3. **Permission errors**: Ensure you have write permissions in the installation directory

### Dependencies

Core requirements:
- numpy
- rdkit
- six

### Platform Compatibility

Tested on:
- macOS (Intel/Apple Silicon)
- Linux (Ubuntu, CentOS)
- Windows 10/11

## Development Setup

For contributors:

```bash
uv pip install -e ".[dev]"
pytest  # Run tests
black . # Format code
```