
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

perma_list=[3.50,3.63,4.13,4.38,4.50,4.94,4.94,5.00,5.25,5.25,
5.25,5.31,5.31,5.31,5.38,5.38,5.69,5.69,5.81,5.88,6.06,6.06,
6.25,6.25,6.31,6.31,6.31,6.38,6.38,6.44,6.50,6.50,6.56,6.63,6.63,6.75,6.75,
6.81,6.81,6.81,6.88,6.94,6.94,7.00,7.00,7.13,7.13,7.13,7.13,
7.13,7.13,7.13,7.19,7.25,7.25,7.25,7.25,7.31,7.44,7.44,7.44,
7.44,7.69,7.75,7.75,7.81,7.81,7.81,7.81,7.94,8.00,8.06,8.13,8.13,8.13,8.13,8.19,8.19,8.25,8.38,8.38,8.50,8.63,8.63,8.69,8.81,
8.88,8.88,8.94,8.94,8.94,9.00,9.13,9.44,9.44]

sa_list=[20,20,20,22,22,23,24,25,25,26,26,26,26,
26,26,26,27,27,27,29,29,29,29,29,30,30,30,30,30,30,
30,30,30,30,30,31,31,31,31,31,31,31,31,31,32,32,32,32,32,32,32,32,
33,33,33,33,33,33,33,34,34,34,34,34,
34,34,34,34,35,35,35,35,35,36,36,36,36,36,36,36,36,36,37,37,37,37,37,37,38,38,39,39,39,40,40,40]

ia_list=[14.00,14,14,15.00,16.00,16,17.00,18.00,19.00,
19.00, 21,21,22,22,23,23,23,23,23,23,24,24,25,26,26,27,
27,27,27,27,29,29,29,30,30,30,31,31,32,32,32,34,34,34,35,35,35,35,
36,36,36,36,37,39,39,41,41,41,42,42,42,43,43,44,45,45,45,
45,46,47,47,47,47,49,49,50,51,51,51,53,53,56,57,58,58,
58,58,61,62,62,63,64,65,69,70,88]
sns.set(style="ticks")

fig, ax = plt.subplots(2,3, gridspec_kw={"height_ratios": (.15, .85)})
sns.histplot(ax=ax[1,0],x=perma_list, bins=4,stat="percent")
box1=sns.boxplot(ax=ax[0,0], x=perma_list)
ax[1,1].hist(sa_list, bins=4)
box2=sns.boxplot(ax=ax[0,1], x=sa_list)
ax[1,2].hist(ia_list, bins=4)
box3=sns.boxplot(ax=ax[0,2], x=ia_list)
box1.set_xticks([])
box1.set_yticks([])
box2.set_xticks([])
box2.set_yticks([])
box3.set_xticks([])
box3.set_yticks([])
box1.spines['right'].set_visible(False)
box1.spines['top'].set_visible(False)
box1.spines['left'].set_visible(False)
box1.spines['bottom'].set_visible(False)
box2.spines['right'].set_visible(False)
box2.spines['top'].set_visible(False)
box2.spines['left'].set_visible(False)
box2.spines['bottom'].set_visible(False)
box3.spines['right'].set_visible(False)
box3.spines['top'].set_visible(False)
box3.spines['left'].set_visible(False)
box3.spines['bottom'].set_visible(False)
ax[1,0].set_xlabel('PERMA')
ax[1,1].set_xlabel('Self Efficacy')
ax[1,2].set_xlabel('Internet')
plt.show()
