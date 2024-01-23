import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

churn=pd.read_csv('Churn_Modelling.csv')
print(churn)

#histogram using pandas #default binsize is 10
churn['EstimatedSalary'].hist(bins=100)
print(churn['EstimatedSalary'].value_counts())
plt.show()

#histogram using matplotlib
vales,x,_=plt.hist(churn['EstimatedSalary'],bins=100)
print(vales)
print(x)
plt.show()

#histogram using seaborn
sns.histplot(data=churn,x='EstimatedSalary',bins=100)
plt.show()


#3D plot using pandas
churn['gender_color']=churn['Gender'].apply(lambda x:'blue' if x=='Male' else 'red')
churn.plot.scatter(x='Age',y='CreditScore',c='gender_color')
plt.show()
#using salary for color scatterplot
churn.plot.scatter(x='Age',y='CreditScore',c='EstimatedSalary')
plt.show()


#3d plot using matplotlib is quite lengthy code

#using salary for color scatterplot
col=plt.scatter(x=churn['Age'],y=churn['CreditScore'],c=churn['EstimatedSalary'])
plt.colorbar(col)
plt.show()

#3d plot using seaborn
sns.scatterplot(data=churn,x='Age',y='CreditScore',hue='Gender')
plt.show()

#using salary for color scatterplot
sns.scatterplot(data=churn,x='Age',y='CreditScore',hue='EstimatedSalary')
plt.show()
#for continous data pandas and matplotlib are better than seaborn
#but for categorical seaborn is better than 2.