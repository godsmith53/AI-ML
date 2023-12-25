import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def kernel(point, xmat, k):
    weights = np.exp(np.sum((point - xmat)**2, axis=1) / (-2.0 * k**2))
    return np.diag(weights)

def localWeight(point, xmat, ymat, k):
    wei = kernel(point, xmat, k)
    W = np.linalg.inv(xmat.T @ wei @ xmat) @ (xmat.T @ wei @ ymat.T)
    return W

def localWeightRegression(xmat, ymat, k):
    ypred = np.array([x @ localWeight(x, xmat, ymat, k) for x in xmat])
    return ypred

# Load data points
data = pd.read_csv('bill.csv')
bill, tip = np.array(data.total_bill), np.array(data.tip)

# Preparing and add 1 in bill
X = np.column_stack((np.ones_like(bill), bill))

# Set k here
ypred = localWeightRegression(X, np.mat(tip), 0.5)
ypred = ypred.flatten()  # Flatten ypred to ensure correct dimensions

SortIndex = np.argsort(X[:, 1])
xsort = X[SortIndex][:, 1]

# Plotting
fig, ax = plt.subplots()
ax.scatter(bill, tip, color='green')
ax.plot(xsort, ypred[SortIndex], color='red', linewidth=5)
plt.xlabel('Total bill')
plt.ylabel('Tip')
plt.show()
