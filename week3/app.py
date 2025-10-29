# Complete Iris Classifier in One Colab Cell
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

print("🌸 Iris Species Classifier - Google Colab Version")

# 1. Load and prepare data
iris = load_iris()
X, y = iris.data, iris.target
feature_names = iris.feature_names
target_names = iris.target_names

print(f"Dataset: {X.shape[0]} samples, {X.shape[1]} features")
print(f"Species: {list(target_names)}")

# 2. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train model
clf = DecisionTreeClassifier(random_state=42, max_depth=3)
clf.fit(X_train, y_train)

# 4. Evaluate
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\n📊 Model Performance:")
print(f"Accuracy: {accuracy:.2%}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=target_names))

# 5. Save model
model_data = {
    'model': clf,
    'feature_names': feature_names,
    'target_names': target_names
}
with open('iris_model.pkl', 'wb') as f:
    pickle.dump(model_data, f)

print("\n✅ Model saved as 'iris_model.pkl'")

# 6. Interactive prediction demo
print("\n🎯 Interactive Prediction Demo:")
print("Enter flower measurements to predict species:")

# Sample predictions
test_cases = [
    [5.1, 3.5, 1.4, 0.2],  # Setosa
    [6.0, 2.7, 5.1, 1.6],  # Virginica
    [5.5, 2.4, 3.8, 1.1]   # Versicolor
]

for i, features in enumerate(test_cases):
    prediction = clf.predict([features])[0]
    probabilities = clf.predict_proba([features])[0]
    species = target_names[prediction]
    
    print(f"\nTest Case {i+1}: {features}")
    print(f"Predicted: {species}")
    print("Probabilities:")
    for j, prob in enumerate(probabilities):
        print(f"  {target_names[j]}: {prob:.2%}")

# 7. Visualization
print("\n📈 Creating visualizations...")

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

# Feature importance
importance = clf.feature_importances_
ax1.barh(feature_names, importance)
ax1.set_title('Feature Importance')
ax1.set_xlabel('Importance Score')

# Sample data distribution
df = pd.DataFrame(X, columns=feature_names)
df['species'] = y
df['species'] = df['species'].map({i: name for i, name in enumerate(target_names)})

# Sepal dimensions
for species in target_names:
    species_data = df[df['species'] == species]
    ax2.scatter(species_data['sepal length (cm)'], species_data['sepal width (cm)'], 
               label=species, alpha=0.7)
ax2.set_xlabel('Sepal Length (cm)')
ax2.set_ylabel('Sepal Width (cm)')
ax2.set_title('Sepal Dimensions')
ax2.legend()

# Petal dimensions
for species in target_names:
    species_data = df[df['species'] == species]
    ax3.scatter(species_data['petal length (cm)'], species_data['petal width (cm)'], 
               label=species, alpha=0.7)
ax3.set_xlabel('Petal Length (cm)')
ax3.set_ylabel('Petal Width (cm)')
ax3.set_title('Petal Dimensions')
ax3.legend()

# Species distribution
species_counts = df['species'].value_counts()
ax4.pie(species_counts.values, labels=species_counts.index, autopct='%1.1f%%',
       colors=['#ff9999', '#66b3ff', '#99ff99'])
ax4.set_title('Species Distribution')

plt.tight_layout()
plt.show()

print("\n🎉 Demo completed! You can now deploy the Streamlit app if needed.")