import numpy
from scipy import stats


numbers = [13, 6, 24, 9, 24]

# Mean
x = numpy.mean(numbers)

print("Mean:")
print(x)
print('------')

# Median
y = numpy.median(numbers)

print("Median:")
print(y)
print('------')

# Mode
z = stats.mode(numbers)

print("Mode:")
print(z)
print('------')

# Standard deviation
sd = numpy.std(numbers)

print("Standard deviation:")
print(sd)
print('------')

# Variance
v = numpy.var(numbers)

print("Variance:")
print(v)
print('------')

# Percentile
p = numpy.percentile(numbers, 72)

print("Percentile:")
print(p)
print('------')
