from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn import svm
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import GridSearchCV


def calculate_slope(df, location_col, quantity_col, location_list):
    '''
        This function will loop through the location list and calculate slope of best fit of linear regression.

    Parameters:
    df: time series dataframe
    location_col: the group by location column name
    quantity_col: aggregated quantity column name by certain frequency
    location_list: Location to loop through

    '''
    location_dict = {}
    for location in location_list:
        df2 = df[df[location_col] == location].reset_index(drop=True)
        df2[quantity_col] = df2[quantity_col].replace('', 0)
        # Extract the time values and reshape them to a 2D array
        X = df2.index.values.reshape(-1, 1)

        # Extract the time series values and reshape them to a 1D array
        y = df2[quantity_col].values.reshape(-1, 1)

        # Fit a linear regression model to the data
        reg = LinearRegression().fit(X, y)

        # Get the prediction
        y_pred = reg.predict(X)

        # Get the fitting metrics
        mape = mean_absolute_error(y, y_pred)
        r2 = r2_score(y, y_pred)

        # Get the slope of the trend line
        slope = reg.coef_[0][0]

        mean = np.mean(y)

        # Store each location - gradient pairs into dictionary
        location_dict[location] = (slope, mape, mean, r2)
        lr_df = pd.DataFrame(location_dict).transpose()
        lr_df = lr_df.rename(columns={0: 'gradient', 1: 'mae', 2: 'mean', 3: 'r2_score'})
        lr_df['mape'] = lr_df['mae'] / lr_df['mean']
    return lr_df

def calculate_tau(df, location_col, quantity_col, location_list):
    '''
        This function will loop through the location list and compute tau statistics for each zone.

    Parameters:
    df: time series dataframe
    location_col: the group by location column name
    quantity_col: aggregated quantity column name by certain frequency
    location_list: Location to loop through

    '''
    location_pvalue_dict = {}
    for location in location_list:
        df2 = df[df[location_col] == location].reset_index(drop=True)
        df2[quantity_col] = df2[quantity_col].replace('', 0)
        # Extract the time values and reshape them to a 2D array
        X = df2.index.values.reshape(-1, 1)

        # Extract the time series values and reshape them to a 1D array
        y = df2[quantity_col].values.reshape(-1, 1)

        # Compute tau statistics
        tau, p_value = stats.kendalltau(X, y)

        # Store each location - gradient pairs into dictionary
        location_pvalue_dict[location] = (tau, p_value)
        tau_df = pd.DataFrame(location_pvalue_dict).transpose()
        tau_df = tau_df.rename(columns={0: 'tau', 1: 'pvalue'})
    return tau_df

def visualize_location_gradient(df):
    '''
    Take location - gradient pairs and give bar chart visualization.
    '''
    df = df.sort_values('gradient', ascending=False)
    fig = px.bar(df, x=df.index, y='gradient', title='Gradient for each location')
    fig.show()

def patterns(obj):
    miner = data_patterns.PatternMiner(obj)


def data_set(dataset):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def SVM(X_scaled, y_train):
    # Create a SVM classifier
    clf = svm.SVC(kernel='linear')
    clf.fit(X_scaled, y_train)

    return clf

def model_eval(clf, X_test, y_test):
    # Predictions
    y_pred = clf.predict(X_test)

    # Evaluation
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

def hp_tuning(X_scaled, y_train):
    param_grid = {'C': [0.1, 1, 10], 'gamma': [0.01, 0.1, 1]}
    grid = GridSearchCV(svm.SVC(), param_grid, refit=True, verbose=2)
    grid.fit(X_scaled, y_train)


def main():
    # Example of splitting data
    X_train, X_test, y_train, y_test = data_set(dataset)

    # Example of scaling data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_train)

    clf = SVM(X_scaled, y_train)
    model_eval(clf, X_test, y_test)
    hp_tuning(X_scaled, y_train)