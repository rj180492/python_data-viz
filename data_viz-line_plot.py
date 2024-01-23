import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

churn=pd.read_csv('Churn_Modelling.csv')
print(churn)

#line plot using pandas
churn_age_cs=churn.groupby('Age')[['CreditScore','EstimatedSalary']].mean().reset_index()
print(churn_age_cs)
churn_age_cs.plot.line(x='Age',y='CreditScore')
plt.show()

#line plot using matplotlib
plt.plot(churn_age_cs['Age'],churn_age_cs['CreditScore'])
plt.show()

#line plot using seaborn
sns.lineplot(data=churn_age_cs,x='Age',y='CreditScore')
plt.show()

#bar plot
print(churn['Gender'].unique())
churn_sal_g=churn.groupby('Gender')[['EstimatedSalary','CreditScore']].mean().reset_index()
print(churn_sal_g)

#bar plot using pandas
churn_sal_g.plot.bar(x='Gender',y='EstimatedSalary')
plt.show()
#horizontal bar plot
churn_sal_g.plot.barh(x='Gender',y='EstimatedSalary')
plt.show()



#bar plot using matplotlib
plt.bar(churn_sal_g['Gender'],churn_sal_g['EstimatedSalary'])
plt.show()
#horizontal bar plot
plt.barh(churn_sal_g['Gender'],churn_sal_g['EstimatedSalary'])
plt.show()


#bar plot using seaborn
sns.barplot(data=churn_sal_g,x='Gender',y='EstimatedSalary')
plt.show()

#horizontal bar plot
sns.barplot(data=churn_sal_g,y='Gender',x='EstimatedSalary',orient='h')
plt.show()