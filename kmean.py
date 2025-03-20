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
            self.clusters.append(self.Clust(centeroid=self.random_centeroids(), members=[]))

    def __repr__(self) -> str:
        return f'{self.clusters}'
    
    def random_centeroids(self) -> P:
        temp_array= reduce(lambda x,y: numpy.vstack([x.data, y.data]), self.data_points)
        low, high = (numpy.min(temp_array, axis= 0), numpy.max(temp_array, axis= 0))
        return_array= numpy.zeros(low.shape[0])
        for i in range(low.shape[0]):
            return_array[i] = random.uniform(low[i], high[i])
        return DataPoint(return_array)
    
    def zscore_normalize(self):
        # combine DataPoints.data
        temp_array= reduce(lambda x,y: numpy.vstack([x.data, y.data]), self.data_points)
        # calc z-score
        for i in range(temp_array.shape[1]): # each col should be normalized for comparison
            calculated_std = numpy.std(temp_array[:,i])
            if numpy.allclose(calculated_std, 0): # all data points are same
                temp_array[:,i] = numpy.zeros(temp_array.shape[0])
            else:
                temp_array[:,i] = (temp_array[:,i] - numpy.mean(temp_array[:,i]) / calculated_std
        # put back to DataPoints
        for i in range(temp_array.shape[0]): # each row is one data_point
            self.data_points[i].data = temp_array[i,:]
        
    def assign_clusters(self):
        centeroids= [clust.centeroid.data for clust in self.clusters]
        for point in self.data_points:
            dist = numpy.linalg.norm(centeroids - point.data, axis = 1)
            idx = numpy.argmin(dist) # which centeroid is closest?
            self.clusters[idx].members.append(point)

    def calculate_centeroids(self):
        for clust in self.clusters:
            temp_array= reduce(lambda x,y: numpy.vstack([x.data, y.data]), clust.cluster)
            clust.centeroid = DataPoint(temp_array.mean(axis= 0))

    def run(self, max_iterations: int = 100) -> list[KMeans.Clust]:
        for iters in range(max_iterations):
            for clust in self.clusters:
                clust.members.clear()

            self.assign_clusters()
            previous_centeroids: list[P] = [clust.centeroid for clust in self.clusters]
            self.calculate_centeroids()
            current_centeroids: list[P] = [clust.centeroid for clust in self.clusters]
            centroid_shift = sum([previous_centeroid.distance(current_centeroid)
                           for previous_centeroid, current_centeroid in zip(previous_centeroids, current_centeroids)])
            if centroid_shift < 1e-18:
                print(f'Converged after {iters} iterations')
                return self._clusters

        print('Did not converged in 100 iterations')
        return self._clusters
