import numpy as np
import pandas as pd
df = pd.read_csv('../data/ch2_scores_em.csv',index_col='student number')
df.head()

scores=np.array(df['english'])[:10]
scores
array([42, 69, 56, 41, 57, 48, 65, 49, 65, 58])
scores_df = pd.DataFrame({'score':scores}, index=pd.Index(['A','B', 'C', 'D', 'E',
                                                           'F','G','H','I','J']
                                                          ,name='student'))
scores_df
score
student	
A	42
B	69
C	56
D	41
E	57
F	48
G	65
H	49
I	65
J	58
sum(scores) / len(scores)
55.000
np.mean(scores)
55.000
scores_df.mean()
score    55.0
dtype: float64
sorted_scores = np.sort(scores)
sorted_scores
array([41, 42, 48, 49, 56, 57, 58, 65, 65, 69])
n = len(sorted_scores)
if n%2==0:
    m0=sorted_scores[n//2-1]
    m1=sorted_scores[n//2]
    median=(m0+m1)/2
else:
    median=sorted_scores[(n+1)//2-1]
median
56.500
np.median(scores)
56.500
scores_df.median()
score    56.5
dtype: float64
pd.Series([1,1,1,2,2,3]).mode()
0    1
dtype: int64
pd.Series([1,2,3,4,5]).mode()
0    1
1    2
2    3
3    4
4    5
dtype: int64
