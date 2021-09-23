import matplotlib.pyplot as pplt
from scipy import stats

numbers_sc_one = [24, 19, 38, 18, 24, 21, 21]
numbers_sc_two = [100, 30, 180, 40, 90, 55, 56]

slope, intercept, r, p, std_err = stats.linregress(numbers_sc_one, numbers_sc_two)

print("Coefficient of correlation")
print(r)

def calc(x):
    return slope * x + intercept

my_cool_model = list(map(calc, numbers_sc_one))

fifty_year_old = calc(18)
print(fifty_year_old)

pplt.scatter(numbers_sc_one,numbers_sc_two)
pplt.plot(numbers_sc_one, my_cool_model)
pplt.show()
