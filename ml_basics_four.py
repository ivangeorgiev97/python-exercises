import numpy
import matplotlib.pyplot as pplt
from sklearn.metrics import r2_score
numpy.random.seed(2)


# Train/Test
# x
minutes = numpy.random.normal(3, 1, 120)
# y
amount = numpy.random.normal(150, 40, 120) / minutes

# pplt.scatter(minutes, amount)
# pplt.show()

train_minutes = minutes[:80]
train_amount = amount[:80]

test_minutes = minutes[80:]
test_amount = amount[80:]

# pplt.scatter(train_minutes, train_amount)
# pplt.scatter(test_minutes, test_amount)
# pplt.show()

my_plt_model = numpy.poly1d(numpy.polyfit(train_minutes, train_amount, 4))

my_plt_line = numpy.linspace(0, 6, 120)

r2 = r2_score(train_amount, my_plt_model(train_minutes))
print(f"R2: { r2 }")
print(f"For 6 minutes: { my_plt_model(6) }")

pplt.scatter(train_minutes, train_amount)
pplt.plot(my_plt_line, my_plt_model(my_plt_line))
pplt.show()
