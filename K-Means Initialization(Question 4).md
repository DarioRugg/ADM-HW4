
# K-Means Initialization Problem

The K-Means algorithm converges to local optimum of the cost function. The initialization is very 
important for this type of clustering. Cost of the solution can be larger than the cost of optimal solution.

Below is an example: Supposing that the data consists of n points in five clusters (of some tiny radius
δ) arranged in a line, with some large distance B between them:

![image.png](attachment:image.png)

The optimal 5-clustering has cost roughly δ
2n. If we initialize k-means by choosing five centers at random
from the data, there is some chance that we’d end up with no centers from cluster 1, two centers from cluster
3, and one center each from clusters 2, 4, and 5:

![image.png](attachment:image.png)

In the first round of k-means, all points in clusters 1 and 2 will be assigned to the leftmost center. The
two centers in cluster 3 will end up sharing that cluster. And the centers in clusters 4 and 5 will move
roughly to the centers of those clusters.

![image.png](attachment:image.png)

Thereafter, no further changes will occur. This local optimum has cost Ω(B2n). We can make this
arbitrarily far away from the optimum cost by setting B large enough. Thus, good initialization is crucial.

Reference

https://cseweb.ucsd.edu/~dasgupta/291-unsup/lec2.pdf
