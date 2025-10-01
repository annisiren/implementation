import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.impute import SimpleImputer # Used for missing data
from sklearn.compose import ColumnTransformer # Used for categorical data
from sklearn.preprocessing import OneHotEncoder # Used for categorical data
from sklearn.preprocessing import LabelEncoder # Used for dependent variable
from sklearn.model_selection import train_test_split # Used to split dataset
from sklearn.preprocessing import StandardScaler # Used in feature scaling

from sklearn.linear_model import LinearRegression # Used in linear regression
from sklearn.preprocessing import PolynomialFeatures # Used in polynomial linear regression
from sklearn.svm import SVR # Used in SVM regression
from sklearn.tree import DecisionTreeRegressor # Used in Decision Tree regression
from sklearn.ensemble import RandomForestRegressor # Used in Random Forest regression

from sklearn.metrics import r2_score # Evauluating model performance

def data(dataset):
    # dataset = pd.read_csv(dataset)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    return X, y

def missing_values(X, interval_s, interval_e):
    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputer.fit(X[:, interval_s:interval_e])
    X[:, interval_s:interval_e] = imputer.transform(X[:, interval_s:interval_e])

    return X

# ENCODING CATEGORICAL DATA
# Expand dataset by adding new columns for a category without numerical values
# i indicates which column will be used to create the new columns from org dataset
# can be multiple columns using e.g. [0,1]
def cat_data(X, i = [0]):
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [i])], remainder='passthrough')
    X = np.array(ct.fit_transform(X))

    return X

# ENCODING DEPENDENT VARIABLE
def dep_var(y):
    le = LabelEncoder()
    y = le.fit_transform(y)

    return y

# SPLITTING DATASET INTO TRAINING AND TESTING SET
def training(X, y, testSize = 0.2, randomState = 1):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = testSize, random_state = randomState)

    return X_train, X_test, y_train, y_test

# FEATURE SCALING
def scaling(X_train, X_test, i = 0):
    sc = StandardScaler()
    X_train[:, i:] = sc.fit_transform(X_train[:, i:])
    X_test[:, i:] = sc.transform(X_test[:, i:])

    return X_train, X_test

# FEATURE SELECTION
def features(X, y):
    y = y.reshape(len(y),1)
    sc_X = StandardScaler()
    sc_y = StandardScaler()
    X = sc_X.fit_transform(X)
    y = sc_y.fit_transform(y)

    return sc_X, sc_y, X, y

############################
# TRAINING REGRESSION MODEL (SIMPLE LINEAR) & (MULTIPLE LINEAR)
def linear_regression(X_train, X_test, y_train):
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    return regressor

# TRAINING POLYNOMIAL REGRESSION MODEL ON WHOLE DATASET
def polynomial_regression(X, y, deg = 4):
    poly_reg = PolynomialFeatures(degree = deg)
    X_poly = poly_reg.fit_transform(X)
    lin_reg_2 = LinearRegression()
    lin_reg_2.fit(X_poly, y)

    return poly_reg, lin_reg_2

# TRAINING SVR MODEL ON WHOLE DATASET
def support_vector_regression(X, y):
    regressor = SVR(kernel = 'rbf')
    regressor.fit(X, y)

    return regressor

def decision_tree_regression(X, y, RandomState = 0):
    regressor = DecisionTreeRegressor(random_state = RandomState)
    regressor.fit(X, y)

    return regressor

def random_forest_regression(X, y, estimators = 10, RandomState = 0):
    regressor = RandomForestRegressor(n_estimators = estimators, random_state = RandomState)
    regressor.fit(X, y)

    return regressor

############################
# PREDICT LINEAR REGRESSION
# vector = [DATA POINTS e.g. 1, 0, 0, 160000, 130000, 300000 ]
def predict_lr(regressor, vector, y_test = 0):
    y_pred = regressor.predict([vector])

    # PRINT RESULTS vs PREDICTION
    # np.set_printoptions(precision=2)
    # print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

    return y_pred

# PREDICT POLYNOMIAL REGRESSION
def predict_pr(lin_reg_2, poly_reg, vector, y_test = 0):
    y_pred = lin_reg_2.predict(poly_reg.fit_transform([vector]))

    # PRINT RESULTS vs PREDICTION
    # np.set_printoptions(precision=2)
    # print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

    return y_pred

# PREDICT SVR
def predict_svr(sc_y, sc_X, regressor, vector, y_test = 0):
    y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform([vector])))

    # PRINT RESULTS vs PREDICTION
    # np.set_printoptions(precision=2)
    # print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

    return y_pred

# PREDICT DECISION TREE, RANDOM FOREST REGRESSION
def predict_dtr(regressor, vector, y_test = 0):
    y_pred = regressor.predict([vector])

    # PRINT RESULTS vs PREDICTION
    # np.set_printoptions(precision=2)
    # print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))
    return y_pred

###########################
# EVALUATING MODEL PERFORMANCE
def r2_score_(y_test, y_pred):
    return r2_score(y_test, y_pred)

############################
# VISUALIZATION
def graph_training(X_train, y_train, regressor, title = 'Title', xlabel = 'xLabel', ylabel = 'yLabel', color_s = 'red', color_l = 'blue'):
    plt.scatter(X_train, y_train, color = color_s)
    plt.plot(X_train, regressor.predict(X_train), color = color_l)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def graph_testing(X_train, X_test, y_test, regressor, title = 'Title', xlabel = 'xLabel', ylabel = 'yLabel', color_s = 'red', color_l = 'blue'):
    plt.scatter(X_test, y_test, color = color_s)
    plt.plot(X_train, regressor.predict(X_train), color = color_l)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def graph_polynomial_r(X, y, poly_reg, lin_reg_2, title = 'Title', xlabel = 'xLabel', ylabel = 'yLabel', color_s = 'red', color_l = 'blue'):
    X_grid = np.arange(min(X), max(X), 0.1)
    X_grid = X_grid.reshape((len(X_grid), 1))
    plt.scatter(X, y, color = color_s)
    plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = color_l)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def graph_svr(X, y, sc_X, sc_y, regressor, title = 'Title', xlabel = 'xLabel', ylabel = 'yLabel', color_s = 'red', color_l = 'blue'):
    X_grid = np.arange(min(sc_X.inverse_transform(X)), max(sc_X.inverse_transform(X)), 0.1)
    X_grid = X_grid.reshape((len(X_grid), 1))
    plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color = color_s)
    plt.plot(X_grid, sc_y.inverse_transform(regressor.predict(sc_X.transform(X_grid))), color = color_l)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# DTR and RFR
def graph_dtr(X, y, regressor, title = 'Title', xlabel = 'xLabel', ylabel = 'yLabel', color_s = 'red', color_l = 'blue'):
    X_grid = np.arange(min(X), max(X), 0.01)
    X_grid = X_grid.reshape((len(X_grid), 1))
    plt.scatter(X, y, color = color_s)
    plt.plot(X_grid, regressor.predict(X_grid), color = color_l)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
