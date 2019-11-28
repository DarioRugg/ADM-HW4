import random
import numpy as np
from collections import defaultdict as dd
import itertools
import matplotlib.pyplot as plt
import math
import pandas as pd

def dist(v1, v2):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(v1, v2)]))  # that's just the euclidean distance
    return distance


data = pd.read_csv("wine.csv")
data = data.values.tolist()
data = list(map(lambda x: np.array(list(map(int, x))), data))
print(data, type(data), type(data[0]))

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
        print(elements)
        distance = [dist(elements, cluster) for cluster in centroids]
        cluster = distance.index(min(distance))
        classes[cluster].append(elements)

    old_centroids = centroids.copy()
    for cluster in classes.keys():
        centroids[cluster] = sum(classes[cluster]) / len(classes[cluster])

    i += 1
    print("\n----------> iteration number: ", i)
    print(centroids)
    print(old_centroids)
    if all([np.allclose(x, y) for x, y in zip(centroids, old_centroids)]):
        go_on = False


#---------------------------------------- plotting --------------------------------------------------------------
fig = plt.figure()
i = 1
for dim1, dim2 in set(itertools.combinations([dim for dim in range(len(data[0]))], 2)): #per ogni dimenzione
    ax = fig.add_subplot(4, 4, i)
    print(centroids[0][dim1], centroids[0][dim2])
    #creating one of the plots
    all_centroids = dd(list)
    for cluster in classes.keys(): #per ogni cluster
        #adding one of the clusters ------------------------------------------------------------------------------
        all_centroids["dim1"].append(centroids[cluster][dim1]) #trovo il punto del cluster
        all_centroids["dim2"].append(centroids[cluster][dim2])

        points = dd(list) #ed i punti appartenenti a quel cluster
        points["dim1"] = [point[dim1] for point in classes[cluster]]
        points["dim2"] = [point[dim2] for point in classes[cluster]]

        plt.scatter(points["dim1"], points["dim2"])

    plt.scatter(all_centroids["dim1"], all_centroids["dim2"], marker='x')
    if i == 4*4:
        break
    i += 1

#now we have all the plots
plt.show()
