from kmean import *
from subprocess import getoutput
getoutput('python3 -m pip install icecream')
from icecream import ic

a= DataPoint([[1,2,3],[2,3,4]])
b= DataPoint([[1,2,3],[2,3,4]])
c= DataPoint([[1,2,3],[3,3,4]])
d= DataPoint([[1,2,3,3],[3,3,4,5]])
e= DataPoint([[1,1,1,1],[1,1,1,1]])

# ic(a==b)
# ic(a==c)
# ic(a.distance(c))
# ic(a.distance(d))
# ic(a)
# ic(e)
# ic(e.distance(d))

k= KMeans(2,[a,b,c])
ic(k)
ic(k.random_centeroids())
ic(k.random_centeroids())
ic(k.assign_clusters())
ic(k.clusters[0])
ic(k.clusters[1])
ic(k.run())