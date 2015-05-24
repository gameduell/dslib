__author__ = 'dwae'

import pandas as pd

from supplies import param, depend, Params


class Shadow(Params):
    def __init__(self, data, **kws):
        super().__init__(**kws)
        self.data = data

    @depend
    def data(self):
        """ data the shadow is based on """

    @param
    def depth(self, val=12):
        return val

    @depend
    def expansion(self):
        sh = pd.concat((self.data.shift(i) for i in range(self.depth)), axis=1)
        sh.columns = range(self.depth)
        return sh


class Stacked(Params):
    def __init__(self, data, **kws):
        super().__init__(**kws)
        self.data = data

    @depend
    def data(self):
        """ data the stack is based on """

    @param
    def base(self, val='1d'):
        return pd.datetools.to_offset(val)

    @depend
    def expansion(self):
        return (self.data
                .groupby(pd.TimeGrouper(self.base))
                .apply(lambda x:
                       pd.Series(x.values, index=x.index - x.name, copy=False))
                .unstack())
