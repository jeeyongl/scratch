from kmean import *

a= DataPoint([[1,2,3],[2,3,4]])
b= DataPoint([[1,2,3],[2,3,4]])
c= DataPoint([[1,2,3],[3,3,4]])
d= DataPoint([[1,2,3,3],[3,3,4,5]])
e= DataPoint([[1,1,1,1],[1,1,1,1]])

print(a==b)
print(a==c)
print(a.distance(c))
print(a.distance(d))
print(a)
print(e)
print(e.distance(d))

KMeans()