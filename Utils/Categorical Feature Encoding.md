# One hot encoding
Using pandas. This returns a dataframe object.
```
import pandas as pd
df = pd.get_dummies(df).astype(np.int8)
```
Using sklearn's OneHotEncoder. It returns a sparse matrix, so more 
memory efficient.
```
from sklearn.preprocessing import OneHotEncoder
one=OneHotEncoder()
one.fit(df)
df = one.transform(df)
print(df.shape)
```

# Label encoder
```
from sklearn.preprocessing import LabelEncoder
label=LabelEncoder()
for col in train.columns:
    if(train[col].dtype=='object'):
        train[col]=label.fit_transform(train[col])
```
Reference : [an-overview-of-encoding-techniques](https://www.kaggle.com/shahules/an-overview-of-encoding-techniques)