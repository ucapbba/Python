from numpy import void
from pandas import DataFrame
from Source.Base.BaseDataHelper import BaseDataHelper


class TrajDataHelper(BaseDataHelper):
    """For importing and manipulating file data in trajectory plotter"""
    def __init__(self, _path, _fname):
        BaseDataHelper.__init__(self, _path, _fname)
        self.p0 = 'p0'
        self.p0_perp = 'p0_perp'
        self.t0_re = 't0_re'
        self.t0_im = 't0_im'
        self.pf = 'p'
        self.pf_perp = 'p_perp'
        self.orbit = 'orbit'
        self.z0 = 'z0'
        self.usePoint = 'usePoint'

    def AssignColumnNames(self):
        self.myDataFrame.columns = [self.p0, self.p0_perp, self.t0_re, self.t0_im,\
                                    self.z0, self.pf, self.pf_perp, self.orbit,\
                                    'rf', 'rf_perp', 'stability', 'guoy']

    def Truncate(self, size: int) -> void:
        newArray = self.myArray[:size]
        self.myArray = newArray
        self.myDataFrame = DataFrame(self.myArray)
        self.AssignColumnNames()

    def GetAllColumns(self) -> list:
        return self.GetDataFrame().columns

    def GetColumnsToDrop(self) -> list:
        columnsToDrop = []
        columnsToDrop.append(self.orbit)
        columnsToDrop.append(self.p0)
        columnsToDrop.append(self.pf)
        return columnsToDrop

    def GetTargetColumns(self) -> list:
        targetColumns = []
        targetColumns.append(self.orbit)
        return targetColumns

    def FilterByOrbit(self, orbit):
        df = self.myDataFrame
        self.myDataFrame = df.loc[df[self.orbit] == orbit]

    def PrintAllOrbitsInfo(self):
        df = self.myDataFrame
        orbits = []
        orbits.append(df.loc[df[self.orbit] == 1])
        orbits.append(df.loc[df[self.orbit] == 2])
        orbits.append(df.loc[df[self.orbit] == 3])
        orbits.append(df.loc[df[self.orbit] == 4])
        orbitsSize = df[self.p0].size
        for orbit in range(1, 5):
            orbitSize = orbits[orbit - 1][self.p0].size
            percentage = orbitSize / orbitsSize * 100
            txt = "Orbit " + str(orbit) + " size: " + str(orbitSize) + " of " \
                + str(orbitsSize) + " total = {value:.2f} %"
            print(txt.format(value=percentage))
