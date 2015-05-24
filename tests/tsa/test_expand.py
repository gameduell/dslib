import pandas as pd
from dslib.tsa import expand as x


def test_shadow():
    ts = pd.Series(range(12), pd.date_range('2014-01-31', periods=12, freq='M'))
    sh = x.Shadow(ts)

    assert sh.expansion.shape == (12, sh.depth)
    assert (sh.expansion.index == ts.index).all()
    assert (sh.expansion[1] == ts.shift(1)).iloc[1:].all()

    sh.depth = 8
    assert sh.expansion.shape == (12, 8)

    sh = x.Shadow(ts, depth=23)
    assert sh.expansion.shape == (12, 23)


def test_stack():
    ts = pd.Series(range(12), pd.date_range('20140101', periods=12, freq='d'))
    sh = x.Stacked(ts, base='3d')

    assert sh.expansion.shape == (4, 3)

    sh.base = '6d'
    assert sh.expansion.shape == (2, 6)

    sh.base = '5d'
    assert sh.expansion.shape == (3, 5)


# TODO monthly tsacks ...
