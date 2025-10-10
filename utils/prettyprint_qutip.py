import numpy as np
import qutip as qt
from IPython.display import display, Math
from typing import Optional, Tuple, Union

# ------------------------- Numeric formatting -------------------------

def format_complex(number: complex, digits: int = 3) -> str:
    """Format a complex number into LaTeX with i (not j), omitting zero parts."""
    re, im = np.real(number), np.imag(number)
    out = ""
    if not np.isclose(re, 0):
        if np.isclose(abs(re), 1):
            out += "+" if re > 0 else "-"
        else:
            out += f"{re:.{digits}f}"
    if not np.isclose(im, 0):
        sign = "-" if im < 0 else ("+" if re > 0 else "")
        if np.isclose(abs(im), 1):
            out += f"{sign} i"
        else:
            out += f"{sign} i{abs(im):.{digits}f}"
    return out

def format_coeff_with_parens(number: complex, digits: int = 3) -> Tuple[Optional[str], bool]:
    """
    Return (formatted, need_parens). formatted is None if number≈0.
    need_parens=True when both real and imag are nonzero.
    """
    re, im = number.real, number.imag
    if np.isclose(re, 0) and np.isclose(im, 0):
        return None, None
    formatted = format_complex(number, digits)
    need_parens = (not np.isclose(re, 0)) and (not np.isclose(im, 0))
    if need_parens:
        return f"({formatted})", True
    else:
        return formatted, False

# ------------------------- Input normalization -------------------------

def to_vector_or_matrix(state: Union[qt.Qobj, np.ndarray, int, float, complex]
                        ) -> Tuple[str, Optional[np.ndarray], Optional[np.ndarray]]:
    """
    Normalize input into ('scalar'|'vector'|'matrix', vector, matrix).
    - vector is a 1D np.ndarray of length 2
    - matrix is a 2x2 np.ndarray
    """
    if isinstance(state, (int, float, complex)):
        return "scalar", None, None

    if isinstance(state, qt.Qobj):
        if state.isoper:
            mat = state.full()
            return "matrix", None, mat
        else:
            vec = state.full().ravel()
            return "vector", vec, None

    if isinstance(state, np.ndarray):
        if state.ndim == 1:
            return "vector", state.ravel(), None
        if state.ndim == 2:
            return "matrix", None, state

    raise TypeError("state must be qutip.Qobj, numpy.ndarray, int, float, or complex.")

def validate_qubit_vector(vec: np.ndarray):
    if vec is None or vec.size != 2:
        raise ValueError("Expected a 2D ket/bra (length-2 vector).")

def validate_qubit_matrix(mat: np.ndarray):
    if mat is None or mat.shape != (2, 2):
        raise ValueError("Expected a 2x2 operator (matrix).")

# ------------------------- LaTeX term assembly -------------------------

def append_term(total: str, coeff_str: str, need_parens: bool, basis_symbol: str, is_first: bool) -> Tuple[str, bool]:
    """
    Append a single term with correct sign handling into `total`.
    Returns updated (total, is_first).
    """
    s = coeff_str
    if is_first:
        # strip leading '+' on the first visible term
        if s.startswith("+"):
            s = s[1:]
        total += s + basis_symbol
        return total, False

    # For subsequent terms: add '+' if coeff_str lacks an explicit sign or is parenthesized
    if need_parens or (s[0] not in "+-"):
        total += "+"
    total += s + basis_symbol
    return total, False

def vector_to_ket_latex(vec: np.ndarray, digits: int = 3, label: str = "") -> str:
    """Build LaTeX for a qubit ket/bra vector: a|0> + b|1> (with signs and parentheses)."""
    validate_qubit_vector(vec)
    ket0, ket1 = r"\ket{0}", r"\ket{1}"
    total = label
    is_first = True

    for coeff, basis_symbol in [(vec[0], ket0), (vec[1], ket1)]:
        coeff_str, need_parens = format_coeff_with_parens(coeff, digits)
        if coeff_str is None:
            continue
        total, is_first = append_term(total, coeff_str, need_parens, basis_symbol, is_first)

    if is_first:  # no terms -> zero
        total += "0"
    return total

def matrix_to_ketbra_latex(mat: np.ndarray, digits: int = 3, label: str = "") -> str:
    """Build LaTeX for a 2x2 operator in the {|0><0|, |0><1|, |1><0|, |1><1|} basis."""
    validate_qubit_matrix(mat)
    a00, a01 = mat[0, 0], mat[0, 1]
    a10, a11 = mat[1, 0], mat[1, 1]

    terms = [
        (a00, r"\ket{0}\bra{0}"),
        (a01, r"\ket{0}\bra{1}"),
        (a10, r"\ket{1}\bra{0}"),
        (a11, r"\ket{1}\bra{1}"),
    ]

    total = label
    is_first = True

    for coeff, basis_op in terms:
        coeff_str, need_parens = format_coeff_with_parens(coeff, digits)
        if coeff_str is None:
            continue
        total, is_first = append_term(total, coeff_str, need_parens, basis_op, is_first)

    if is_first:
        total += "0"
    return total

# ------------------------- Public API -------------------------

def state_to_latex(state: Union[qt.Qobj, np.ndarray, int, float, complex], digits: int = 3) -> str:
    """Convert any supported state/scalar to a LaTeX string with no leading label."""
    kind, vec, mat = to_vector_or_matrix(state)
    if kind == "scalar":
        return format_complex(state, digits)
    if kind == "vector":
        return vector_to_ket_latex(vec, digits=digits)
    if kind == "matrix":
        return matrix_to_ketbra_latex(mat, digits=digits)
    # Unreachable due to to_vector_or_matrix checks
    raise RuntimeError(f"Unexpected state kind : {type(state)}.")

# ------------------------- Public API (variadic) -------------------------

def prettyprint(*items: Union[str, qt.Qobj, np.ndarray, int, float, complex], digits: int = 3):
    """
    Pretty-print a concatenation of LaTeX fragments.
    Accepts any number of positional items. Each item may be:
      - str: appended verbatim (treat as LaTeX, e.g., r"\\psi = ")
      - scalar (int/float/complex): formatted numeric
      - 2D ket/bra (vector of length 2): rendered as a|0> + b|1>
      - 2x2 operator (matrix): rendered as sum_{ij} a_ij |i><j|
    Only 'digits' is accepted as a keyword argument.
    """
    latex_total = ""
    for obj in items:
        if isinstance(obj, str):
            latex_total += obj
        else:
            latex_total += state_to_latex(obj, digits=digits)
    return display(Math(latex_total))
