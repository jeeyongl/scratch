from __future__ import annotations
import numpy
from typing import Iterable, Generic, TypeVar
from dataclasses import dataclass
import sys
import random
from functools import reduce


class DataPoint:
    self._raw_data: numpy.array
    self.data: numpy.array
    self.shape: tuple[int,...]
    
    def __init__(self, data: Iterable[float]):
        self._raw_data = numpy.array(data, dtype= numpy.float32).flatten()
        self.data = numpy.array(data, dtype= numpy.float32).flatten() #self._zscore()
        self.shape = self.data.shape

    def __repr__(self):
        return f'DataPoint: shape({self.shape}): {self.data}' 
    
    def __eq__(self, other: DataPoint):
        if not isinstance(other, DataPoint) or self.shape != other.shape:
            return NotImplemented
        return numpy.allclose(self.data, other.data)
    
    def distance(self, other: DataPoint):
        if not isinstance(other, DataPoint) or self.shape != other.shape:
            print('DataPoint not matched, returning infinity', file=sys.stderr)
            return numpy.inf
        return numpy.linalg.norm(self.data - other.data)

# # Algorithm for kmeans # #
# 1. initialize data points and k
# 2. normalize data points
# 3. create random centeroids for each cluster
# 4. assign data points to clusters
# 5. recalculate centeroids with new cluster data points
# 6. repeat 4 and 5
# 7. stop with maximum iterations or centeroids no move
P = TypeVar('P', bound= DataPoint)
class KMeans(Generic[P]):
    @dataclass
    class Clust:
        centeroid: P
        members: list[P]

    def __init__(self, k:int, data_points: list(P)):
        if k < 1:
            raise ValueError('k must be positive integer')
        self.k= k
        self.data_points = data_points
        self.zscore_normalize()
        self.clusters: list(self.Clust) = []
        for _ in range(self.k):
            self.clusters.append(self.Clust(self.random_centeroids(), []))

    def __repr__(self) -> str:
        return f'{self.memberss}'
    
    def random_centeroids(self) -> P:
        data= reduce(lambda x,y: numpy.vstack([x.data, y.data]), self.data_points)
        low, high = (numpy.min(data, axis= 0), numpy.max(data, axis= 0))
        cent= numpy.zeros(low.shape[0])
        for i in range(low.shape[0]):
            cent[i] = random.uniform(low[i], high[i])
        return DataPoint(cent)
    
    def zscore_normalize(self):
        # combine DataPoints.data
        data= reduce(lambda x,y: numpy.vstack([x.data, y.data]), self.data_points)
        # calc z-score
        for i in range(data.shape[1]):
            if numpy.std(data[:,i]) == 0: # all data points are same
                data[:,i] = numpy.zeros(data.shape[0])
            else:
                data[:,i] = (data[:,i] - numpy.mean(data[:,i]) / numpy.std(data[:,i]))
        # put back to DataPoints
        for i in range(data.shape[0]):
            self.data_points[i].data = data[i,:]
        
    def assign_clusters(self):
        centeroids= [clust.centeroid.data for clust in self.clusters]
        for point in self.data_points:
            dist = numpy.linalg.norm(centeroids - point.data, axis = 1)
            idx = numpy.argmin(dist)
            self.clusters[idx].members.append(point)

    def calculate_centeroids(self):
        for clust in self.clusters:
            data= reduce(lambda x,y: numpy.vstack([x.data, y.data]), clust.cluster)
            clust.centeroid = DataPoint(data.mean(axis= 0))

    def run(self, max_iterations: int = 100) -> List[KMeans.Clust]:
        for iters in range(max_iterations):
            for clust in self.clusters:
                clust.members.clear()

            self.assign_clusters()
            previous_centeroids: List[Point] = deepcopy(self._centeroids)
            self.calculate_centeroids()

            centroid_shift = sum([previous_centeroid.distance(current_centeroid)
                           for previous_centeroid, current_centeroid in zip(previous_centeroids, self._centeroids)])
            if centroid_shift < 1e-18:
                print(f'Converged after {iters} iterations')
                return self._clusters

        print('Did not converged in 100 iterations')
        return self._clusters
        pass

