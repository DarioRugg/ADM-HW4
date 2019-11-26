import math
import random
import numpy as np
from collections import defaultdict as dd
import itertools

def dist(v1, v2):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(v1, v2)]))  # that's just the euclidean distance
    return distance


data = [(3, 4, 1), (2, 5, 2), (5, 6, 1), (1, 4, 4), (5, 2, 3), (2, 5, 2), (3, 6, 4), (1, 6, 1), (4, 3, 2)]
data = list(map(lambda x: np.array(x), data))
k = 3


centroids = [[] for i in range(k)]

a = random.sample(range(0, len(data)), k)
for number in range(k):
    centroids[number] = data[a[number]]

i = 0
go_on = True
while go_on:

    classes = dd(list)
    for elements in data:
        distance = [dist(elements, cluster) for cluster in centroids]
        cluster = distance.index(min(distance))
        classes[cluster].append(elements)

    old_centroids = centroids.copy()
    data.append(np.array((1, 2, 3)))
    for cluster in classes.keys():
        centroids[cluster] = sum(classes[cluster]) / len(classes[cluster])

    i += 1
    print("\n----------> iteration number: ", i)
    print(centroids)
    print(old_centroids)
    if all([np.allclose(x, y) for x, y in zip(centroids, old_centroids)]):
        go_on = False

for dim1, dim2 in itertools.combinations([dim for dim in range(len(data[0]))], 2):
    print(centroids[0][dim1], centroids[0][dim2])
