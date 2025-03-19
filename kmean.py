from __future__ import annotations
import numpy
from typing import Iterable, Generic
import sys


class DataPoint:
    def __init__(self, data: Iterable[float]):
        self._raw_data = numpy.array(data, dtype= numpy.float32).flatten()
        self.data = self._zscore()
        self.shape = self.data.shape

    def __repr__(self):
        return f'data: {self.shape}:\n{self.data}' 
    
    def __eq__(self, other: DataPoint):
        if not isinstance(other, DataPoint) or self.shape != other.shape:
            return NotImplemented
        return numpy.allclose(self.data, other.data)
    
    def distance(self, other: DataPoint):
        if not isinstance(other, DataPoint) or self.shape != other.shape:
            print('DataPoint not matched, returning infinity', file=sys.stderr)
            return numpy.inf
        return numpy.linalg.norm(self.data - other.data)
    
    def _zscore(self):
        if numpy.std(self._raw_data) == 0: # all data points are same
            return numpy.zeros(self._raw_data.shape)
        else:
            return (self._raw_data - numpy.mean(self._raw_data) / numpy.std(self._raw_data))
        

    

# # Algorithm for kmeans # #
# 1. initialize data points and k
# 2. normalize data points
# 3. create random centeroids for each cluster
# 4. assign data points to clusters
# 5. recalculate centeroids with new cluster data points
# 6. repeat 4 and 5
# 7. stop with maximum iterations or centeroids no move

class KMeans(Generic[DataPoint]):
    pass
