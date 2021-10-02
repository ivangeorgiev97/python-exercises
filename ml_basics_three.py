import matplotlib.pyplot as pplt
import numpy
from scipy import stats
from sklearn.metrics import r2_score
from sklearn import linear_model
import pandas


# Linear Regression
numbers_sc_one = [24, 19, 38, 18, 24, 21, 21]
numbers_sc_two = [100, 30, 180, 40, 90, 55, 56]

slope, intercept, r, p, std_err = stats.linregress(numbers_sc_one, numbers_sc_two)

print(f"Coefficient of correlation: { r }")
print(r)

def calc(x):
    return slope * x + intercept

my_cool_model = list(map(calc, numbers_sc_one))

fifty_year_old = calc(50)
print(fifty_year_old)

# pplt.scatter(numbers_sc_one,numbers_sc_two)
# pplt.plot(numbers_sc_one, my_cool_model)
# pplt.show()


# Polynomial Regression

numbers_sc_pone = [1, 4, 8, 12, 16, 20, 23]
numbers_sc_ptwo = [80, 80, 100, 90, 85, 55, 56]

my_second_model = numpy.poly1d(numpy.polyfit(numbers_sc_pone, numbers_sc_ptwo, 3))

print(f"R2 score: { r2_score(numbers_sc_ptwo, my_second_model(numbers_sc_pone)) }")

example_speed = my_second_model(15)
print(example_speed)

my_line = numpy.linspace(1, 23, 100)

# pplt.scatter(numbers_sc_pone, numbers_sc_ptwo)
# pplt.plot(my_line, my_second_model(my_line))
# pplt.show()


# Multiple Regression
# The file is not uploaded to the repository

dfo = pandas.read_csv("random_cars.csv")

# independentValues
X = dfo[['Weight', 'Horse Power']]
# dependentValues
y = dfo['CO2']

rgr = linear_model.LinearRegression()
rgr.fit(X, y)

# Predict CO2 value of a car
predictCO2 = rgr.predict([[1400, 185]])
print(predictCO2)

# Coefficient
print(rgr.coef_)


# Scale - TODO
