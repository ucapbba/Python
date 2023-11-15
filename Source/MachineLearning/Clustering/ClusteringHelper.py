from Source.Plotters.TrajDataHelper import TrajDataHelper
from sklearn.cluster import DBSCAN


class ClusteringHelper(TrajDataHelper):
    def __init__(self, _path, _fname):
        TrajDataHelper.__init__(self, _path, _fname)

    def DropColumns(self):
        # Here we decide which columns NOT to use
        self.myDataFrame = self.myDataFrame.drop([self.t0_re, self.t0_im, self.orbit, 'rf', 'rf_perp', 'stability', 'guoy'], axis=1)

    def RunClustering(self, _eps, _min_samples):
        X = self.myDataFrame
        dbscan = DBSCAN(eps=_eps, min_samples=_min_samples)  # OPTICS performs well too
        y_pred = dbscan.fit_predict(X)
        X[self.orbit] = y_pred
        self.myDataFrame = X
