import os
from os import walk
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.impute import SimpleImputer # Used for missing data
from sklearn.compose import ColumnTransformer # Used for categorical data
from sklearn.preprocessing import OneHotEncoder # Used for categorical data
from sklearn.preprocessing import LabelEncoder # Used for dependent variable
from sklearn.model_selection import train_test_split # Used to split dataset
from sklearn.preprocessing import StandardScaler # Used in feature scaling

import ml_regression as mlr

def read_file(read_path):
    print("read_files()")
    print(read_path)
    key_obj = pd.read_csv(read_path, index_col=0)

    dataset(key_obj)

def dataset(dataset):
    print("dataset")
    # print(dataset)
    # IMPORTING dataset
    X, y = mlr.data(dataset)

    print(X)
    print(y)

    input("Press enter to continue...")

    # MISSING DATA
    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputer.fit(X[:, 1:3])
    X[:, 1:3] = imputer.transform(X[:, 1:3])

    # ENCODING CATEGORICAL DATA
    # X = mlr.cat_data(X)

    # ENCODING DEPENDENT VARIABLE
    # y = mlr.dep_var(y)

    # SPLITTING DATASET INTO TRAINING AND TESTING SET
    X_train, X_test, y_train, y_test = mlr.training(X, y)

    # FEATURE SCALING
    X_train, X_test = mlr.scaling(X_train, X_test)

    # FEATURE SELECTION
    sc_X, sc_y, X, y = mlr.features(X, y)
    regressor_lr = mlr.linear_regression(X_train, X_test, y_train)
    regressor_svr = mlr.support_vector_regression(X, y)

    mlr.graph_training(X_train, y_train, regressor_lr)

    mlr.graph_svr(X, y, sc_X, sc_y, regressor_svr)

def main():
    print("main()")
    read_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data_Analysis\\weeks.csv'))

    read_file(read_path)


main()