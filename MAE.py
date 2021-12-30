import numpy as np
# Test if everything is OK!
print('Hello, world!')

# Create a function to calculate
# Mean Absolute Error

def MAE(slope, interceptor, Xs, Ys):

    y_hats = [(slope * x) + interceptor for x in Xs]
    result = np.mean(np.abs(np.array(Ys) - np.array(y_hats)))
    return y_hats, result


vals = [1.2, 2, [2, 5, -4, -7, 8], [-2, 6, -4, 1, 14]]
y_hats, result = MAE(vals[0], vals[1], vals[2], vals[3])
print('Results {:.2f}'.format(result))
