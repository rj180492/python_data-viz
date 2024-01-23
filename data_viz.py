import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

churn=pd.read_csv('Churn_Modelling.csv')
print(churn)
print(churn.shape)
print(churn.info)

#plot graph using pandas
# print(churn.sample(1000).plot.scatter(x='Age',y='CreditScore'))
# plt.show()

#plot graph using pyplot
plt.scatter(x=churn['Age'],y=churn['CreditScore'])
plt.xlabel('Age')
plt.ylabel('Credit Score')
plt.show()

#plot using seaborn
sns.scatterplot(data=churn,x='Age',y='CreditScore')
plt.show()