import numpy as np
# Test if everything is OK!
print('Hello, world!')

# Create a function to calculate
# Mean Squared Error

def MSE(slope, interceptor, Xs, Ys):

    y_hats = [(slope * x) + interceptor for x in Xs]
    result = 0.5 * (np.mean(np.power((np.array(Ys) - np.array(y_hats)), 2)))
    return y_hats, result


vals = [1.2, 2, [2, 5, -4, -7, 8], [-2, 6, -4, 1, 14]]
y_hats, result = MSE(vals[0], vals[1], vals[2], vals[3])
print('Results {:.2f}'.format(result))
