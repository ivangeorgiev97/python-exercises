import numpy
import matplotlib.pyplot as pplt

# uniform
# numbers = numpy.random.uniform(6.0, 13.0, 60)

# print(numbers)

# pplt.hist(numbers, 6)


# normal
# numbers_two = numpy.random.normal(6.0, 1.0, 300)

# pplt.hist(numbers_two)


# Scatter plot
numbers_sp_one = numpy.random.normal(6.0, 1.0, 300) # [6, 9, 13, 18, 24, 3]
numbers_sp_two = numpy.random.normal(12.0, 3.0, 300) # [96, 99, 88, 124, 85, 78]

pplt.scatter(numbers_sp_one, numbers_sp_two)
pplt.show()
