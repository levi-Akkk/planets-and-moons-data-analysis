import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import cross_val_score

#1. Load the dataset
housing = pd.read_csv("housing.csv")

#2. create a stratifeid test set
housing["income_cat"] = pd.cut(housing["median_income"],
                                bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf], 
                                labels=[1, 2, 3, 4, 5])

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index].drop("income_cat", axis=1) # we will work on this data
    strat_test_set = housing.loc[test_index].drop("income_cat", axis=1) #set aside the test data

# we will work on the copy of training data
housing = strat_train_set.copy()


#3. separate features and labels
housing_labels = housing["median_house_value"].copy()
housing = housing.drop("median_house_value", axis=1)


#print(housing_labels)

#4. List the numerical and categorical columns
num_attribs = housing.drop("ocean_proximity", axis=1).columns.tolist()
cat_attribs = ["ocean_proximity"]

#5. lets make the piprline for numerical columns
# for numerical column
num_pipeline = Pipeline([
     ("imputer", SimpleImputer(strategy="median")), 
     ("scalar", StandardScaler())
])
# for categorical column
cat_pipeline = Pipeline([
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])
# construct the full pipeline 
full_pipeline = ColumnTransformer([
    ("num", num_pipeline, num_attribs),
    ("cat", cat_pipeline, cat_attribs)
])

#6. transform the data 
housing_prepared = full_pipeline.fit_transform(housing)
print(housing_prepared.shape)

# 7. Train the model
# Linear regression model
lin_reg = LinearRegression()
lin_reg.fit(housing_prepared, housing_labels)
lin_preds = lin_reg.predict(housing_prepared)
#lin_rmse = root_mean_squared_error(lin_preds, housing_labels)
lin_rmses = -cross_val_score(lin_reg, housing_prepared, housing_labels, scoring="neg_root_mean_squared_error", cv=10
                              )
#print("Linear Regression RMSE:" ,lin_rmse)
print(pd.Series(lin_rmses).describe())

# Decision tree 

tree_reg = DecisionTreeRegressor()
tree_reg.fit(housing_prepared, housing_labels)
tree_preds = tree_reg.predict(housing_prepared)
#tree_rmse = root_mean_squared_error(tree_preds, housing_labels)
tree_rmses = -cross_val_score(tree_reg, housing_prepared, housing_labels, scoring="neg_root_mean_squared_error", cv=10
                              )
#print("Decision tree RMSE:" ,tree_rmse)
print(pd.Series(tree_rmses).describe())

# Random forest
forest_reg = RandomForestRegressor()
forest_reg.fit(housing_prepared, housing_labels)
forest_preds = forest_reg.predict(housing_prepared)
#forest_rmse = root_mean_squared_error(forest_preds, housing_labels)
forest_rmses = -cross_val_score(forest_reg, housing_prepared, housing_labels, scoring="neg_root_mean_squared_error", cv=10
                              )
#print("Random forest RMSE:" ,forest_rmse)
print(pd.Series(forest_rmses).describe())
