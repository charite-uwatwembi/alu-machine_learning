# Mean, Variance, Covariance, Correlation

## Mean
def mean(x):
    # x is a vector
    return sum(x) / len(x)

## Variance

def variance(x):
    mu = mean(x)
    return sum([(xi - mu) ** 2 for xi in x]) / len(x)



