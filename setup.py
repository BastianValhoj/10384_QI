
from setuptools import setup, find_packages

setup(
    name="qi-utils",            # Package name on PyPI or local
    version="0.1",
    packages=find_packages(),   # Automatically finds `utils`
    install_requires=[          # Optional: list dependencies here
        "qutip",
        "numpy",
        "plotly"
    ],
)