# Quantum Information (DTU 10384)

This repository contains materials and exercises for the Quantum Information course (DTU course 10384). It includes:

- Jupyter notebooks with exercises (exercises/)
- Utility scripts for quantum state visualization and LaTeX-style pretty printing (utils/)
- Example scripts (main.py)  

---

## 📂 Repository Structure
QI/
├── README.md                  # Project overview
├── exercises/                 # Jupyter notebooks for weekly exercises
├── main.py                    # Example script to test utils
├── pyproject.toml             # Project metadata and dependencies
├── setup.py                   # For installing utils as a package
└── utils/
    ├── bloch_plotly.py        # Plotly-based Bloch sphere plotting
    └── prettyprint_qutip.py   # Pretty printing for QuTiP states


---
# Quick start

## ⚡ Setup Instructions

This project uses **`uv`** to manage the virtual environment. To set up your environment:

1. Clone the repository:

```bash
git clone https://github.com/BastianValhoj/10384_QI.git
cd QI
```

2. Create and activate a virtual environment:
```bash
uv sync
```

3. Install dependencies and make the utils package available:
```bash
uv install -e .
```

4. Verify installation:
```bash
uv run main.py
```

You should now be able to use all utilities and run the notebooks.


## 🧰 Usage

* exercises/: Open Jupyter notebooks in VS Code or JupyterLab to follow weekly exercises.

* utils/:
    * prettyprint_qutip.py: LaTeX-style display of quantum states in notebooks.
    * bloch_plotly.py: Plot qubits and quantum states on an interactive Bloch sphere using Plotly.

* main.py: Example scripts checking utils installation.

## 📦 Dependencies

* Python ≥ 3.13

* `qutip`
* `numpy`
* `plotly`
* `matplotlib`
* `ipykernel`
* `ipympl`
* `nbformat`

All dependencies are specified in pyproject.toml and will be installed automatically with uv install.

