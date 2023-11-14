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

    def FilterByOrbit(self, orbit):
        df = self.myDataFrame
        self.myDataFrame = df.loc[df[self.orbit] == orbit]
