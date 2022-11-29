import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

age_hist_df=pd.read_csv('age_histogram.csv')
sns.barplot(x = 'Age',y = 'Count',data = age_hist_df).set(title='Age Distribution of Respondents')
plt.show()

education_df=pd.read_csv('education.csv')
fig, ax = plt.subplots(1, 1, figsize = (2,3))
sns.barplot(x = 'Academic Discipline',y = 'Count',
data = education_df).set(title='Distribution of Respondents by Academic Discipline')
plt.xticks(rotation=10)
ax.set_xlabel('')
plt.show()

colors = [["white","white"],["blue","blue"],["blue","blue"], ["white","white"],["green",'green'],["green",'green'],
["white","white"],["yellow","yellow"],["yellow","yellow"],["yellow","yellow"], ["white","white"],["red","red"],["red","red"],["red","red"]]
demographics_df=pd.read_csv('demographics.csv')

demographics_df = demographics_df.replace('\t','', regex=True)
print(demographics_df.head())
fig, ax = plt.subplots()
table = ax.table( cellText=demographics_df.values,colLabels=demographics_df.columns,cellColours=colors, loc='center')
table.scale(.6,1.5)
table.auto_set_font_size(False)
table.set_fontsize(16)
ax.axis('off')
plt.show()

big3df=pd.read_csv('big3_correlations.csv')
big3df=big3df.set_index("CATEGORY")
sns.heatmap(big3df,annot = True,cmap="YlGnBu").set_title("Primary Category Correlation Coefficients (Pearson)\nYellow-Significant at Alpha=.05\nSky Blue-Significant at alpha=.01")
plt.show()

se_df=pd.read_csv('se_corr.csv')
se_df=se_df.set_index("CATEGORY")
sns.heatmap(se_df,annot = True,cmap="YlGnBu").set_title("Self Efficacy\nPositive Emotions Significant at Alpha=.05\nPerma & Engagement Significant at Alpha=.01")
plt.show()

ia_df=pd.read_csv('ia_corr.csv')
ia_df=ia_df.set_index("CATEGORY")
sns.heatmap(ia_df,annot = True,cmap="YlGnBu").set_title("Internet Addiction\nPerma : Significant at Alpha=.05")
plt.show()

ia_oi_df=pd.read_csv('ia_oi.csv')
ia_oi_df=ia_oi_df.set_index("CATEGORY")
sns.heatmap(ia_oi_df,annot = True,cmap="YlGnBu").set_title("Internet Addiction vs.OI Category")
plt.show()

se_oi_df=pd.read_csv('se_oi.csv')
se_oi_df=se_oi_df.set_index("CATEGORY")
sns.heatmap(se_oi_df,annot = True,cmap="YlGnBu").set_title("Self Efficacy vs.OI Category\nOL12 : Significant at Alpha=.01")
plt.show()

perma_list=[3.50,3.63,4.13,4.38,4.50,4.94,4.94,5.00,5.25,5.25,5.25,5.31,5.31,5.31,5.38,5.38,5.69,5.69,5.81,5.88,6.06,6.06,6.25,6.25,6.31,6.31,6.31,6.38,6.38,6.44,6.50,6.50,6.56,6.63,6.63,6.75,6.75,
6.81,6.81,6.81,6.88,6.94,6.94,7.00,7.00,7.13,7.13,7.13,7.13,7.13,7.13,7.13,7.19,7.25,7.25,7.25,7.25,7.31,7.44,7.44,7.44,7.44,7.69,7.75,7.75,7.81,7.81,7.81,7.81,7.94,8.00,8.06,8.13,8.13,8.13,8.13,8.19,8.19,8.25,8.38,8.38,8.50,8.63,8.63,8.69,8.81,
8.88,8.88,8.94,8.94,8.94,9.00,9.13,9.44,9.44]
sns.histplot(x=perma_list, kde=True, bins=4,stat="density")
plt.xlabel('Perma Score', fontsize=16)
plt.ylabel('Proportion', fontsize=16)
plt.show()
sns.boxplot(x=perma_list)
plt.xlabel('Perma Score', fontsize=16)
plt.show()

ia_list=[14.00,14,14,15.00,16.00,16,17.00,18.00,19.00,19.00, 21,21,22,22,23,23,23,23,23,23,24,24,25,26,26,27,27,27,27,27,29,29,29,30,30,30,31,31,32,32,32,34,34,34,35,35,35,35,
36,36,36,36,37,39,39,41,41,41,42,42,42,43,43,44,45,45,45,45,46,47,47,47,47,49,49,50,51,51,51,53,53,56,57,58,58,58,58,61,62,62,63,64,65,69,70,88]
sns.histplot(x=ia_list, kde=True, bins=4,stat="density")
plt.xlabel('Internet Addiction Score', fontsize=16)
plt.ylabel('Proportion', fontsize=16)
plt.show()
sns.boxplot(x=ia_list)
plt.xlabel('Internet Addiction Score', fontsize=16)
plt.show()

sa_list=[20,20,20,22,22,23,24,25,25,26,26,26,26,26,26,26,27,27,27,29,29,29,29,29,30,30,30,30,30,30,30,30,30,30,30,31,31,31,31,31,31,31,31,31,32,32,32,32,32,32,32,32,
33,33,33,33,33,33,33,34,34,34,34,34,34,34,34,34,35,35,35,35,35,36,36,36,36,36,36,36,36,36,37,37,37,37,37,37,38,38,39,39,39,40,40,40]
ia_list=[14.00,14,14,15.00,16.00,16,17.00,18.00,19.00,19.00, 21,21,22,22,23,23,23,23,23,23,24,24,25,26,26,27,27,27,27,27,29,29,29,30,30,30,31,31,32,32,32,34,34,34,35,35,35,35,
36,36,36,36,37,39,39,41,41,41,42,42,42,43,43,44,45,45,45,45,46,47,47,47,47,49,49,50,51,51,51,53,53,56,57,58,58,58,58,61,62,62,63,64,65,69,70,88]
sns.histplot(x=sa_list, kde=True, bins=4,stat="density")
plt.xlabel('Self Efficacy Score', fontsize=16)
plt.ylabel('Proportion', fontsize=16)
plt.show()
sns.boxplot(x=sa_list)
plt.xlabel('Self Efficacy Score', fontsize=16)
plt.show()
