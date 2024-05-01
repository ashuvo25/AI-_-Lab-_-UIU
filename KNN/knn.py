import numpy as np
import pandas as pd

def normalize_features(X):
    min_vals = np.min(X, axis=0)
    max_vals = np.max(X, axis=0)
    X_normalized = (X - min_vals) / (max_vals - min_vals)
    return X_normalized

def predict_class(X_train, y_train, X_test, k):
    y_pred = []
    for x_test in X_test:
        distances = np.sqrt(np.sum((X_train - x_test) ** 2, axis=1))
        nearest_neighbors = np.argsort(distances)[:k]
        neighbor_classes = y_train[nearest_neighbors]
        pred_class = np.argmax(np.bincount(neighbor_classes))
        y_pred.append(pred_class)
    return np.array(y_pred)

# Load dataset
iris_df = pd.read_csv('Search algo in python\KNN\iris.csv')

# Convert labels to numeric
label_mapping = {'Setosa': 0, 'Versicolor': 1, 'Virginica': 2}
iris_df['variety'] = iris_df['variety.classnames'].map(label_mapping)

# Shuffle dataset
iris_df = iris_df.sample(frac=1).reset_index(drop=True)

# Extract features and labels
X = iris_df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
y = iris_df['variety'].values

# Train-test split
split_index = int(0.8 * len(X))
X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

# Normalize data
X_train_normalized = normalize_features(X_train)
X_test_normalized = normalize_features(X_test)

# Predict classes for test data
k = 5
y_pred = predict_class(X_train_normalized, y_train, X_test_normalized, k)

# Calculate accuracy
accuracy = np.mean(y_pred == y_test)
print("Accuracy:", accuracy)