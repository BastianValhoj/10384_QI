__version__ = '0.1.1'

from .bloch_plotly import plot_bloch_plotly
from .bloch_plotly import plot_bloch_plotly as plot_bloch
from .prettyprint_qutip import prettyprint, format_complex
from .prettyprint_qutip import prettyprint as pprint

__all__ = ["prettyprint", "pprint", 
           "format_complex", 
           "plot_bloch_plotly", "plot_bloch",
           "__version__"
    ]