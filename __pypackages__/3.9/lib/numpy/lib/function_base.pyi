from typing import List

from numpy import (
    vectorize as vectorize,
)

from numpy.core.function_base import (
    add_newdoc as add_newdoc,
)

from numpy.core.multiarray import (
    add_docstring as add_docstring,
    bincount as bincount,
)
from numpy.core.umath import _add_newdoc_ufunc

__all__: List[str]

add_newdoc_ufunc = _add_newdoc_ufunc

def rot90(m, k=..., axes = ...): ...
def flip(m, axis=...): ...
def iterable(y): ...
def average(a, axis=..., weights=..., returned=...): ...
def asarray_chkfinite(a, dtype=..., order=...): ...
def piecewise(x, condlist, funclist, *args, **kw): ...
def select(condlist, choicelist, default=...): ...
def copy(a, order=..., subok=...): ...
def gradient(f, *varargs, axis=..., edge_order=...): ...
def diff(a, n=..., axis=..., prepend = ..., append = ...): ...
def interp(x, xp, fp, left=..., right=..., period=...): ...
def angle(z, deg=...): ...
def unwrap(p, discont = ..., axis=..., *, period=...): ...
def sort_complex(a): ...
def trim_zeros(filt, trim=...): ...
def extract(condition, arr): ...
def place(arr, mask, vals): ...
def disp(mesg, device=..., linefeed=...): ...
def cov(m, y=..., rowvar=..., bias=..., ddof=..., fweights=..., aweights=..., *, dtype=...): ...
def corrcoef(x, y=..., rowvar=..., bias = ..., ddof = ..., *, dtype=...): ...
def blackman(M): ...
def bartlett(M): ...
def hanning(M): ...
def hamming(M): ...
def i0(x): ...
def kaiser(M, beta): ...
def sinc(x): ...
def msort(a): ...
def median(a, axis=..., out=..., overwrite_input=..., keepdims=...): ...
def percentile(a, q, axis=..., out=..., overwrite_input=..., interpolation=..., keepdims=...): ...
def quantile(a, q, axis=..., out=..., overwrite_input=..., interpolation=..., keepdims=...): ...
def trapz(y, x=..., dx=..., axis=...): ...
def meshgrid(*xi, copy=..., sparse=..., indexing=...): ...
def delete(arr, obj, axis=...): ...
def insert(arr, obj, values, axis=...): ...
def append(arr, values, axis=...): ...
def digitize(x, bins, right=...): ...
