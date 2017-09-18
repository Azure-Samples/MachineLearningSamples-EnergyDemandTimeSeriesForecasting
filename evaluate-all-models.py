import os

# Run 8-evaluate-model-py for all models.
# NOTE: Execute this script by running the following in the AML cli:
# > python evaluate-all-models.py
models = ['linear_regression',
    "ridge",
    "ridge_poly2",
    "mlp",
    "dtree",
    "gbm"]

for model in models:
    os.system('az ml experiment submit -c local ./8-evaluate-model.py {}'.format(model))