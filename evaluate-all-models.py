import os

# Run 8-evaluate-model-py for all models.
# Only use this script after running notebooks 2-7.
# Execute this script by opening a command prompt from the Workbench and running:
# > python evaluate-all-models.py
models = ['linear_regression',
    "ridge",
    "ridge_poly2",
    "mlp",
    "dtree",
    "gbm"]

for model in models:
    os.system('az ml experiment submit -c local ./8-evaluate-model.py {}'.format(model))