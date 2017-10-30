from collections import Counter


class Statis(list):
    def __init__(self, *args):
        list.__init__(self, *args)

    def value_counts(self):
        from pyexcel import get_sheet
        c = Counter(self)
        sheet = get_sheet(adict=c)
        sheet.rownames = ['N/A', 'counts']
        return sheet

    def plot(self):
        from pyexcel import get_sheet
        sheet = get_sheet(array=[self])
        return sheet.plot()
