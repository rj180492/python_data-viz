import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

churn=pd.read_csv('Churn_Modelling.csv')
print(churn)
churn_age_g=churn.groupby(['Age','Gender'])[['CreditScore','EstimatedSalary']].mean().reset_index()
print(churn_age_g)

#multiplot using sns
sns.lineplot(data=churn_age_g,x='Age',y='CreditScore',hue='Gender')
plt.show()
#creating 2 separate scatterplot
sns.relplot(data=churn_age_g,x='Age',y='CreditScore',row='Gender')
plt.show()
#side by side
sns.relplot(data=churn_age_g,x='Age',y='CreditScore',col='Gender')
plt.show()
#if we want lineplot side by side
sns.relplot(data=churn_age_g,x='Age',y='CreditScore',row='Gender',kind='line')
plt.show()