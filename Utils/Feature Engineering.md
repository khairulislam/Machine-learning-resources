# StandardScaler

```
def standardize(df):
    return (df-df.min())/(df.max()-df.min())
```
   
# Normalize
```
def normalize(df):
    return (df-df.mean())/df.std()
```   

# Discretizer
encode{‘onehot’, ‘onehot-dense’, ‘ordinal’}, (default=’onehot’)
strategy{‘uniform’, ‘quantile’, ‘kmeans’}, (default=’quantile’)
```
from sklearn imporn preprocessing
selected = ['col1', 'col2']
kbins = preprocessing.KBinsDiscretizer(n_bins=[20, 20], encode='ordinal', strategy='kmeans')
temp = pd.DataFrame(kbins.fit_transform(total[selected]), columns=selected)
```
ref : [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer)


# References
* [sklearn preprocessing library](https://scikit-learn.org/stable/modules/preprocessing.html)
* [Preprocessing with sklearn: a complete and comprehensive guide](https://towardsdatascience.com/preprocessing-with-sklearn-a-complete-and-comprehensive-guide-670cb98fcfb9)
* [Continuous Numeric Data](https://towardsdatascience.com/understanding-feature-engineering-part-1-continuous-numeric-data-da4e47099a7b)
