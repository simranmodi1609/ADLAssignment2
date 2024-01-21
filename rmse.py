import numpy as np

def rmse(predictions, targets):
    pred = np.array(predictions)
    tar = np.array(targets)
       # Calculate the mean squared differences
    mse = np.mean((pred - tar)**2)

    # Calculate the root mean squared error
    rmse = np.sqrt(mse)

    return rmse