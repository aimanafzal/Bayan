import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv(
    "../dataset/emotion_final.csv"
)  # Replace 'your_dataset.csv' with your actual file path

# Assuming your CSV file has features in columns 'feature1', 'feature2', ..., 'featureN'
# You can adjust this based on your CSV file structure
features = data[["Text", "Emotion"]]

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Determine the optimal number of clusters using the elbow method
inertia = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# Plot the elbow graph to find the optimal number of clusters
plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), inertia, marker="o", linestyle="--")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

# Based on the elbow graph, choose the optimal number of clusters and train the K-means model
optimal_clusters = (
    3  # You can adjust this based on the elbow graph and your specific use case
)
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
kmeans.fit(scaled_features)

# Assign clusters to the data points
data["Cluster"] = kmeans.labels_

# Now, 'data' dataframe contains the original data with an additional 'Cluster' column indicating the cluster for each data point
# You can use this clustered data for further analysis or visualization

# Print the cluster centers
print("Cluster Centers:")
print(scaler.inverse_transform(kmeans.cluster_centers_))

# Print the count of data points in each cluster
print("Count of data points in each cluster:")
print(data["Cluster"].value_counts())
