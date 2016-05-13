## 1. Clustering NBA Players ##

import pandas as pd
import numpy as np

nba = pd.read_csv("nba_2013.csv")
nba.head(3)

## 2. Point Guards ##

# Enter code here.

point_guards = nba[nba['pos'] == 'PG']
print(point_guards.head())

## 3. Points Per Game ##

point_guards['ppg'] = point_guards['pts'] / point_guards['g']

# Sanity check, make sure ppg = pts/g
point_guards[['pts', 'g', 'ppg']].head(5)

## 4. Assist Turnover Ratio ##

point_guards = point_guards[point_guards['tov'] != 0]

point_guards['atr'] = point_guards['ast'] / point_guards['tov']
print(point_guards.head())

## 7. The Algorithm ##

num_clusters = 5
# Use numpy's random function to generate a list, length: num_clusters, of indices
random_initial_points = np.random.choice(point_guards.index, size=num_clusters)
# Use the random indices to create the centroids
centroids = point_guards.ix[random_initial_points]

print(random_initial_points, centroids)

## 8. Visualize Centroids ##

plt.scatter(point_guards['ppg'], point_guards['atr'], c='yellow')
plt.scatter(centroids['ppg'], centroids['atr'], c='red')
plt.title("Centroids")
plt.xlabel('Points Per Game', fontsize=13)
plt.ylabel('Assist Turnover Ratio', fontsize=13)
plt.show()

## 9. Setup (continued) ##

def centroids_to_dict(centroids):
    dictionary = dict()
    # iterating counter we use to generate a cluster_id
    counter = 0

    # iterate a pandas data frame row-wise using .iterrows()
    for index, row in centroids.iterrows():
        coordinates = [row['ppg'], row['atr']]
        dictionary[counter] = coordinates
        counter += 1

    return dictionary

centroids_dict = centroids_to_dict(centroids)

print(centroids_dict)

## 10. Step 1 (Euclidean Distance) ##

import math

def calculate_distance(centroid, player_values):
    root_distance = 0
    
    for x in range(0, len(centroid)):
        difference = centroid[x] - player_values[x]
        squared_difference = difference**2
        root_distance += squared_difference

    euclid_distance = math.sqrt(root_distance)
    return euclid_distance

q = [5, 2]
p = [3,1]

# Sqrt(5) = ~2.24
print(calculate_distance(q, p))

## 11. Step 1 (Continued) ##

# Add the function, `assign_to_cluster`
# This creates the column, `cluster`, by applying assign_to_cluster row-by-row
# Uncomment when ready

# point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)

import math

def calculate_distance(centroid, player_values):
    root_distance = 0
    
    for x in range(0, len(centroid)):
        difference = centroid[x] - player_values[x]
        squared_difference = difference**2
        root_distance += squared_difference

    euclid_distance = math.sqrt(root_distance)
    return euclid_distance

def assign_to_cluster(row):
    ppg = row['ppg']
    atr = row['atr']
    
    distances = [calculate_distance(e, [ppg, atr]) for i, e in centroids_dict.items()]
    
    return(distances.index(min(distances)))

point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)

print(point_guards.head())

## 12. Visualizing Clusters ##

# Visualizing clusters
def visualize_clusters(df, num_clusters):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    for n in range(num_clusters):
        clustered_df = df[df['cluster'] == n]
        plt.scatter(clustered_df['ppg'], clustered_df['atr'], c=colors[n-1])
        plt.xlabel('Points Per Game', fontsize=13)
        plt.ylabel('Assist Turnover Ratio', fontsize=13)

visualize_clusters(point_guards, 5)
plt.show()

## 13. Step 2 ##

# def recalculate_centroids(df):
#     new_centroids_dict = dict()
#     # 0..1...2...3...4
#     for cluster_id in range(0, num_clusters):
#         # Finish the logic
#         return new_centroids_dict

# centroids_dict = recalculate_centroids(point_guards)

import numpy as np

def recalculate_centroids(df):
    new_centroids_dict = dict()
    # 0..1...2...3...4
    for cluster_id in range(0, num_clusters):
        # Finish the logic
        clusters = point_guards[point_guards['cluster'] == cluster_id]
        ppg_atr = np.array([np.array([e['ppg'], e['atr']]) for i, e in clusters.iterrows()])
        new_centroids_dict[cluster_id] = [ppg_atr[:,0].mean(), ppg_atr[:,1].mean()]

    return new_centroids_dict

centroids_dict = recalculate_centroids(point_guards)

print(centroids_dict)

## 14. Repeat Step 1 ##

# point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)
# visualize_clusters(point_guards, num_clusters)

# plt.show()

import math
import numpy as np

def recalculate_centroids(df):
    new_centroids_dict = dict()
    # 0..1...2...3...4
    for cluster_id in range(0, num_clusters):
        # Finish the logic
        clusters = point_guards[point_guards['cluster'] == cluster_id]
        ppg_atr = np.array([np.array([e['ppg'], e['atr']]) for i, e in clusters.iterrows()])
        new_centroids_dict[cluster_id] = [ppg_atr[:,0].mean(), ppg_atr[:,1].mean()]

    return new_centroids_dict

def calculate_distance(centroid, player_values):
    root_distance = 0
    
    for x in range(0, len(centroid)):
        difference = centroid[x] - player_values[x]
        squared_difference = difference**2
        root_distance += squared_difference

    euclid_distance = math.sqrt(root_distance)
    return euclid_distance

def assign_to_cluster(row):
    ppg = row['ppg']
    atr = row['atr']
    
    distances = [calculate_distance(e, [ppg, atr]) for i, e in centroids_dict.items()]
    
    return(distances.index(min(distances)))

def visualize_clusters(df, num_clusters):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    for n in range(num_clusters):
        clustered_df = df[df['cluster'] == n]
        plt.scatter(clustered_df['ppg'], clustered_df['atr'], c=colors[n-1])
        plt.xlabel('Points Per Game', fontsize=13)
        plt.ylabel('Assist Turnover Ratio', fontsize=13)

centroids_dict = recalculate_centroids(point_guards)

point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)
visualize_clusters(point_guards, num_clusters)

plt.show()

## 15. Repeat Step 2 and Step 1 ##

centroids_dict = recalculate_centroids(point_guards)
point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)
visualize_clusters(point_guards, num_clusters)

## 16. Challenges of K-Means ##

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(point_guards[['ppg', 'atr']])
point_guards['cluster'] = kmeans.labels_

visualize_clusters(point_guards, num_clusters)