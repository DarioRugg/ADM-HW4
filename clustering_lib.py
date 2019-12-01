import random #for taking random sample
import numpy as np #for making arrays
from collections import defaultdict as dd #for creating default dictionary
import itertools
import matplotlib.pyplot as plt #for plotting
import math #for using mathematical eqn
import pandas as pd #for reading data


#creating a function for euclidean distance, has two vector inputs and returns the euclidean distance between the vectors
def dist(v1, v2):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(v1, v2)])) 
    return distance



def plotting(centroids, classes, dimensions_number):
    # ---------------------------------------- plotting --------------------------------------------------------------
    # naming the features, so we can add them to the plots
    features = ["Alcohol",
                "Malic acid",
                "Ash",
                "Alcalinity",
                "Magnesium",
                "Total phenols",
                "Flavanoids",
                "Nonflavanoid",
                "Proanthocyanins",
                "Color",
                "Hue",
                "diluted wines",
                "Proline"]

    # findingout all the possible cupples of dimensions
    combinations_of_dimension = list(itertools.combinations([dim for dim in range(dimensions_number)], 2))

    for i in range(len(combinations_of_dimension)):  # building a subplot for each cupple of dimensions

        if i % 4 == 0:  # create a new figure for each 4 plot
            fig, axes = plt.subplots(nrows=1, ncols=4)
            fig.set_size_inches(18.5, 4, forward=True)

        #definging the dimensions
        dim1, dim2 = combinations_of_dimension[i]

        # creating one of the plots
        all_centroids = dd(list)
        for cluster in classes.keys():  # iterating on each cluster
            # saving the cluster cordinates
            all_centroids["dim1"].append(centroids[cluster][dim1])
            all_centroids["dim2"].append(centroids[cluster][dim2])

            # get the codinates of all the cluster points
            points = {"dim1": [point[dim1] for point in classes[cluster]],
                      "dim2": [point[dim2] for point in classes[cluster]]}

            axes[i % 4].scatter(points["dim1"], points["dim2"])  # adding the cluster points

        # add the centroids to the plot
        axes[i % 4].scatter(all_centroids["dim1"], all_centroids["dim2"], marker='x')

        # adding lables to the plots
        axes[i % 4].set_xlabel(features[dim1])
        axes[i % 4].set_ylabel(features[dim2])
        # removing axis
        axes[i % 4].set_xticklabels([])
        axes[i % 4].set_yticklabels([])

    #ploting everithing.
    plt.show()

def kmeansOnWines(k):

    #getting the data set with pandas
    data = pd.read_csv("wine.data")
    data.drop(data.columns[0], axis=1, inplace=True)

    data = data.values.tolist() #converting the values of dataset to lists
    data = list(map(lambda x: np.array(list(map(int, x))), data)) #converting to NumPy array

    centroids = [[] for i in range(k)] #creating empty lists for k centroids

    a = random.sample(range(0, len(data)), k) #taking k random samples from the dataset
    for number in range(k):
        centroids[number] = data[a[number]] #assigning them as initial clusters

    i = 0 #counter for iteration
    go_on = True #fixing for the while loop
    while go_on: #while go_on is true,

        classes = dd(list) #creating a default dictionary for each cluster
        for elements in data: #for every element of dataset
            distance = [dist(elements, cluster) for cluster in centroids] #calculate the distance between the centroid and element
            cluster = distance.index(min(distance)) #take the index of the cluster
            classes[cluster].append(elements) #and assign the element to cluster with that index

        old_centroids = centroids.copy() #for keeping the previous centroids
        for cluster in classes.keys():
            centroids[cluster] = sum(classes[cluster]) / len(classes[cluster]) #arrange new centroids by calculating the new mean

        i += 1 #increase the counter by 1
        if all([np.allclose(x, y) for x, y in zip(centroids, old_centroids)]): #if the previous centroids are equal to the new ones
            go_on = False #break the loop

    plotting(centroids, classes, len(data[0])) #ploting the clusters