# %% [markdown]
# **Importing Libraries**

# %%
from ucimlrepo import fetch_ucirepo 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
breast_cancer_wisconsin_diagnostic = fetch_ucirepo(id=17) 

# %% [markdown]
# **Load the dataset**

# %%
X = breast_cancer_wisconsin_diagnostic.data.features 
y = breast_cancer_wisconsin_diagnostic.data.targets

# %% [markdown]
# **Preprocess the data**

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# %% [markdown]
# **Build the model**

# %%
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train_scaled, y_train)

# %% [markdown]
# **Predict and Evaluate the model**

# %%
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


