import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as pplt
import matplotlib.image as pltimg

# TODO: Add table


# Decision Tree
df = pandas.read_csv("random_ppl.csv")

d = { "Asenovgrad": 0, "Cherven": 1, "Plovdiv": 2 }
df['CityTownVillage'] = df['CityTownVillage'].map(d)
d = { 'YES': 1, 'NO': 0 }
df['Visit'] = df['Visit'].map(d)

predict_from = ['Age', 'Exp', 'Rank', 'CityTownVillage']

X = df[predict_from]
y = df['Visit']

# print(df)
# print(X)
# print(y)

decision_tree = DecisionTreeClassifier()
decision_tree = decision_tree.fit(X, y)
data = tree.export_graphviz(decision_tree, out_file=None, feature_names=predict_from)
graph_from_dot = pydotplus.graph_from_dot_data(data)
graph_from_dot.write_png('finaldecisiontree.png')

print(f"30 years old artist with 9 years experience, rank 9 and from Asenovgrad: { decision_tree.predict([[30, 9, 9, 0]]) }")

img = pltimg.imread('finaldecisiontree.png')
img_plot = pplt.imshow(img)
pplt.show()
