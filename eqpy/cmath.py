from sympy import (
    acos,
    acosh,
    asin,
    asinh,
    atan,
    atanh,
    cos,
    cosh,
    E as e,
    exp,
    # `isfinite` defined below
    # `isinf` defined below
    # `isnan` defined below
    log,
    # `log10` defined below
    arg as phase,
    pi,
    # `polar` defined below
    # `rect` defined below
    sin,
    sinh,
    sqrt,
    tan,
    tanh,
)
from eqpy.math import log10, isfinite as _isfinite, isinf as _isinf
from sympy import (S as _S, nan as _nan, Abs as _Abs, I as _I, re as _re,
                   im as _im)


def isfinite(x):
    """isfinite(z) -> bool
    Return True if both the real and imag parts of z are finite, else False.
    """
    x = _S(x)
    return _isfinite(_re(x)) and _isfinite(_im(x))


def isinf(x):
    """isinf(z) -> bool
    Checks if the real or imaginary part of z is infinite.
    """
    x = _S(x)
    return _isinf(_re(x)) or _isinf(_im(x))


def isnan(x):
    """isnan(z) -> bool
    Checks if the real or imaginary part of z not a number (NaN)
    """
    x = _S(x)
    return x == _nan


def polar(z):
    """polar(z) -> r: float, phi: float

    Convert a complex from rectangular coordinates to polar coordinates. r is
    the distance from 0 and phi the phase angle.
    """
    return (_Abs(z), phase(z))


def rect(r, phi):
    """rect(r, phi) -> z: complex

    Convert from polar coordinates to rectangular coordinates.
    """
    return r * cos(phi) + _I * r * sin(phi)
