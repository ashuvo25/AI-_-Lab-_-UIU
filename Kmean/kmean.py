import numpy as np
import matplotlib.pyplot as plt

X = np.loadtxt("Search algo in python\Kmean\jain_feats.txt")
centroid_old = np.loadtxt("Search algo in python\Kmean\jain_centers.txt")

centroid_new = np.zeros_like(centroid_old)

labels = np.zeros(X.shape[0])

plt.scatter(X[:, 0], X[:, 1], color='b', label='Data Points')
plt.scatter(centroid_old[:, 0], centroid_old[:, 1], color=['r'], marker='*',s=250, label='Initial Centroids')
plt.title('Initial State')
plt.legend()
plt.show()

def distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))

def update_centroids(X, labels, k):
    centroids = np.zeros((k, X.shape[1]))
    for i in range(k):
        centroids[i] = np.mean(X[labels == i], axis=0)
    return centroids

# Main K-means algorithm
max_iterations = 100
epsilon = 1e-7
for e in range(max_iterations):

    for i in range(len(X)):
        dist = [distance(X[i], c) for c in centroid_old]
        labels[i] = np.argmin(dist)

    centroid_new = update_centroids(X, labels, centroid_old.shape[0])

    if np.max(np.abs(centroid_new - centroid_old)) < epsilon:
        print("Converged after {} iterations".format(e+1))
        break
    else:
        centroid_old = centroid_new

cluster_colors = ['r', 'g']
for i, centroid in enumerate(centroid_old):
    plt.scatter(X[labels == i, 0], X[labels == i, 1], color=cluster_colors[i], cmap='viridis', alpha=0.5)
    plt.scatter(centroid[0], centroid[1], color=cluster_colors[i], marker='*', s=250, label='Final Centroid {}'.format(i+1))

plt.title('Final State')
plt.legend()
plt.show()
