# Energy Demand Time Series Forecasting

## Link to the Microsoft DOCS site

The detailed documentation for this real world scenario includes the step-by-step walkthrough:

[https://docs.microsoft.com/azure/machine-learning/preview/scenario-time-series-forecasting](https://docs.microsoft.com/azure/machine-learning/preview/scenario-time-series-forecasting)

## Link to the Gallery GitHub repository

The public GitHub repository for this real world scenario contains all the code samples:

[https://github.com/Azure/MachineLearningSamples-EnergyDemandTimeSeriesForecasting](https://github.com/Azure/MachineLearningSamples-EnergyDemandTimeSeriesForecasting)

## Overview

Time series forecasting is the task of predicting future values in a time-ordered sequence of observations. It is a common problem and has applications in many industries. This example focuses on energy demand forecasting where the goal is to predict the future load on an energy grid. It is a critical business operation for companies in the energy sector.

In this example, machine learning methods are applied to forecast time series. Although the context is energy demand forecasting, the methods used can be applied to many other contexts and use cases. Using Azure Machine Learning Workbench, you are guided through every step of the modeling process including:
- Data preparation to clean and format the data;
- Creating features for the machine learning models from raw time series data;
- Training various machine learning models;
- Evaluating the models by comparing their performance on a held-out test dataset; and,
- Operationalizing the best model, making it available through a web service to generate forecasts on demand.

## Key components needed to run this scenario

1. An [Azure account](https://azure.microsoft.com/free/) (free trials are available).
2. An installed copy of Azure Machine Learning Workbench with a workspace created.
3. For model operationalization:
    - [Docker engine](https://www.docker.com/).
    - Azure Machine Learning Operationalization with a local deployment environment set up and a model management account created as described in this  [guide](https://github.com/Azure/Machine-Learning-Operationalization/blob/master/documentation/getting-started.md).
4. This example could be run on any compute context. However, it is recommended to run it on a multi-core machine with at least of 8-GB memory.

## Data/Telemetry
The Energy Demand Time Series Forecasting sample collects usage data and sends it to Microsoft to help improve our products and services. Read our privacy statement to learn more. 

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (for example, label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information, see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.