from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# 1. Load a sample dataset (Iris dataset is the standard for labs)
data = load_iris()
X = data.data
y = data.target

# 2. Split the dataset into Training and Testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Initialize the Decision Tree Classifier
clf = DecisionTreeClassifier(criterion='entropy', max_depth=3)

# 4. Train the model
clf.fit(X_train, y_train)

# 5. Make predictions
predictions = clf.predict(X_test)

# 6. Check accuracy
accuracy = clf.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# 7. Visualize the Decision Tree
plt.figure(figsize=(12,8))
tree.plot_tree(clf, feature_names=data.feature_names, class_names=data.target_names, filled=True)
plt.show()
