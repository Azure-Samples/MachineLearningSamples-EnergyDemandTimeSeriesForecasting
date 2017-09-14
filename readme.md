# Time Series Forecasting

![Energy demand forecast](./media/scenario-time-series-forecasting/forecast_illustration.png)

## Prerequisites

1. Please ensure that you have properly installed Azure ML Workbench by following the [installation guide](https://github.com/Azure/ViennaDocs/blob/master/Documentation/Installation.md).
2. This sample assumes that you are running Azure ML Workbench on Windows 10 with [Docker engine](https://www.docker.com/) locally installed. If you are using macOS, the instruction is largely the same.
3. This sample requires that you update the Pandas installation to version 0.20.3. Run the following command in the CLI to upgrade the package.

    ```
    conda install pandas==0.20.3
    ```

Notes:

- The sample was built and tested on a Windows 10 machine with the following specification: Intel Core i7-6600U CPU @ 2.60 GHz, 16-GB RAM, 64-bit OS, x64-based processor with Docker Version 17.06.2-ce-win27 (13194).
- Model operationalization was built using this version of Azure ML CLI: azure-cli-ml==0.1.0a24.post2

## Introduction

Time series forecasting is the task of predicting future values in a time-ordered sequence of observations. It is a common problem and has applications in many industries. For example, retail companies need to forecast future products sales so they can effectively organize their supply chains to meet demand. Similarly, package delivery companies need to estimate the demand for their services so they can plan workforce requirements and delivery routes ahead of time. In many cases, the financial risks of inaccurate forecasts can be significant and forecasting is therefore often a business critical activity.

This sample shows how time series forecasting can be performed through applying machine learning techniques. You are guided through every step of the modeling process including:
- data preparation to clean and format the data;
- creating features for the machine learning models from raw time series data;
- training various machine learning models;
- evaluating the models by comparing their performance on a held-out test dataset; and,
- operationalizing the best model, making it available through a web service to generate forecasts on demand.

Azure Machine Learning Workbench aids the modeling process at every step: 
- The sample shows how the Jupyter notebook environment - available directly from through Workbench - can make developing Python code easier. The model development process can be explained to others more clearly using markdown annotations and charts. These notebooks can be viewed, edited, and executed directly from the Workbench.
- Trained models can be persisted and uploaded to blob storage. This helps the data scientist to keep track of trained model objects and ensure they are retained and retrievable when needed.
- Metrics can be logged while executing a Python script, enabling the data scientist to keep a record of model performance scores.
- The workbench produces customizable tables of logged metrics allowing the data scientist to easily compare model performance metrics. Charts are automatically displayed so the best performing model can be readily identified.
- Finally, the sample shows how a trained model can be operationalized by deploying it in a realtime web service.

## Use Case Overview

This scenario focuses on energy demand forecasting. This is the task of predicting the future load on an energy grid. It is a critical business operation for companies in the energy sector. For example, energy grid operators need to maintain the fine balance between the energy consumed on a grid and the energy supplied to it. If too much power is supplied to the grid, it can result in energy wastage or even technical faults. However, if there is not enough supply to meet demand it can lead to blackouts, leaving many people without power. Typically, grid operators can take short-term decisions to manage energy supply to the grid and keep the load in balance. An accurate short-term forecast of energy demand is therefore essential for the operator to make these decisions with confidence.

This scenario shows how the task of energy demand forecasting can be approached as a machine learning problem. Models are trained on a public dataset from the [New York Independent System Operator (NYISO)](http://www3.dps.ny.gov/W/PSCWeb.nsf/All/298372E2CE4764E885257687006F39DF?OpenDocument), which operates the power grid for New York State. The dataset includes hourly power demand data for New York City over a period of five years. An additional dataset containing hourly weather conditions in New York City over the same time period was taken from [darksky.net](https://darksky.net).

## Scenario Structure

When you open this sample for the first time, navigate to the Files pane on the left-hand side of the Workbench. Here you will see the following files:
- **1-data-preparation.ipynb** - this Jupyter notebook downloads and processes the data to prepare it for modeling. This is the first notebook you will run.
- **2-linear-regression.ipynb** - this notebook trains a linear regression model on the training data.
- **3-ridge.ipynb** - trains a ridge regression model.
- **4-ridge-poly2.ipynb** - trains a ridge regression model on polynomial feature of degree 2.
- **5-ridge-poly3.ipynb** - trains a ridge regression model on polynomial feature of degree 3.
- **6-dtree.ipynb** - trains a decision tree model.
- **7-gbm.ipynb** - trains a gradient boosted machine model.
- **8-evaluate-model .py** - this script loads a trained model and uses it to make predictions on a held-out test dataset. It produces model evaluation metrics so the performance of different models can be compared.
- **9-forecast-output-exploration.ipynb** - this notebook produces visualizations of the forecasts generated by the machine learning models.
- **10-deploy-model.ipynb** - this notebook demonstrates how a trained forecasting model can be operationalized in a realtime web service.