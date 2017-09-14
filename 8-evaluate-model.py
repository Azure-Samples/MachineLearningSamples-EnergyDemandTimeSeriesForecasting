import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from azureml.logging import get_azureml_logger
import pickle
import os
from sklearn.metrics import mean_squared_error

model_name = sys.argv[1]
aml_dir = os.environ['AZUREML_NATIVE_SHARE_DIRECTORY']

run_logger = get_azureml_logger()
run_logger.log("Model Name", model_name)

test = pd.read_csv(aml_dir + 'nyc_demand_test.csv', parse_dates=['timeStamp'])

# Load trained model pipeline
with open(aml_dir + model_name + '.pkl', 'rb') as f:
    model = pickle.load(f)

def mean_absolute_percentage_error(y_true, y_pred):
    return ((y_pred - y_true).abs() / y_true).mean()

def evaluate_model(model, test_df):
    X_test = test_df.drop(['demand', 'timeStamp'], axis=1)
    y_pred = model.predict(X_test)
    y_true = test_df.demand
    mse = mean_squared_error(y_true, y_pred)
    rmse = mse**0.5
    mape = mean_absolute_percentage_error(y_true, y_pred)
    predictions_df = test_df.copy()
    predictions_df['predictions'] = y_pred
    return (mse, rmse, mape, predictions_df)

mse, rmse, mape, predictions = evaluate_model(model, test)

run_logger.log("MSE", mse)
run_logger.log("RMSE", rmse)
run_logger.log("MAPE", mape)

# Output the predictions dataframe
with open(aml_dir + model_name + '_predictions.pkl', 'wb') as f:
    pickle.dump(predictions, f)

# Store the trained model in the Outputs folder.
with open('./outputs/' + model_name + '.pkl', 'wb') as f:    
    pickle.dump(model, f)