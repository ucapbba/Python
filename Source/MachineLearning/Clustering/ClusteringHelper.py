import string

from numpy import ndarray
from Source.Plotters.TrajDataHelper import TrajDataHelper
from sklearn.cluster import DBSCAN


class ClusteringHelper(TrajDataHelper):
    eps : float
    samples : int
    def __init__(self, _path : string, _fname : string):
        TrajDataHelper.__init__(self, _path, _fname)

    def DropColumns(self):
        # Here we decide which columns NOT to use
        self.myDataFrame = self.myDataFrame.drop([self.t0_re, self.t0_im, self.orbit, 'rf', 'rf_perp', 'stability', 'guoy'], axis=1)

    def RunClustering(self, _eps : float, _samples : int) -> int:
        self.eps = _eps
        self.samples = _samples
        X = self.myDataFrame
        dbscan = DBSCAN(eps=_eps, min_samples = _samples)  # OPTICS performs well too
        y_pred = dbscan.fit_predict(X)
        X[self.orbit] = y_pred
        uniqueElements = self.uniqueElements(y_pred)
        self.myDataFrame = X
        return uniqueElements
    
    def uniqueElements(self, y_pred : ndarray) -> int:
        unique = []
        for element in y_pred:
            if(element not in unique):
                unique.append(element)
        return len(unique)
         