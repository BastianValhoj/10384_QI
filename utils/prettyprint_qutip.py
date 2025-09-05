import qutip as qt
import numpy as np
from IPython.display import display, Math

def format_complex(number, digits=3):
    """Format a complex number into LaTeX style string with i instead of j."""
    re, im = np.real(number), np.imag(number)
    out = ""
    
    # if np.isclose(number, 0):
    #     return "0"
    
    if not np.isclose(re, 0): # real part
        out += f"{re:.{digits}f}"
    if not np.isclose(im, 0): # imag part
        sign = "-" if im < 0 else ("+" if re > 0 else "") # adds sign if non-zero
        out += f"{sign} i{abs(im):.{digits}f}"
        
    return out


def _add_parenthesis(number, digits=3):
    """Return formatted complex number, wrapped in parentheses if both parts nonzero."""
    re, im = number.real, number.imag

    if np.isclose(re, 0) and np.isclose(im, 0):
        return None, None

    formatted = format_complex(number, digits)

    if not np.isclose(re, 0) and not np.isclose(im, 0):
        return f"({formatted})", True

    return formatted, False

def prettyprint(label, state, digits=3):
    """Pretty-print a state as LaTeX."""
    if isinstance(state, qt.Qobj):
        state = state.full().ravel()
    elif isinstance(state, np.ndarray):
        state = state.ravel()
    elif isinstance(state, (int, float, complex)):
        return display(Math(label + format_complex(state, digits)))
    else:
        raise TypeError(
            f"state must be qutip.Qobj, numpy.ndarray, int, float, or complex, not {type(state)}"
        )

    if len(state) != 2:
        raise ValueError("prettyprint currently only supports 2D states.")

    zero, one = state
    ket0, ket1 = r"\ket{0}", r"\ket{1}"
    total = label

    zero_str, zero_par = _add_parenthesis(zero, digits)
    one_str, one_par = _add_parenthesis(one, digits)
    print(f"{one_str = }")
    if zero_str is not None:
        total += zero_str + ket0

    if one_str is not None:
        # If parentheses OR no explicit sign
        if one_par or (not one_str[0] in "+-"):
            total += "+" + one_str + ket1
        else:
            total += one_str + ket1

    display(Math(total))
    