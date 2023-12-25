import pandas as pd
from pprint import pprint

def entropy(probs):
    import math
    return sum([-prob * math.log(prob, 2) for prob in probs])

def entropy_of_list(a_list):
    from collections import Counter
    cnt = Counter(a_list)
    return entropy([x / len(a_list) for x in cnt.values()])

def information_gain(df, split_attr, target_attr):
    df_split = df.groupby(split_attr)
    entropies = df_split[target_attr].apply(entropy_of_list)
    weights = df_split.size() / len(df)
    return entropy_of_list(df[target_attr]) - sum(entropies * weights)

def id3(df, target_attr, attrs, default_class=None):
    from collections import Counter
    cnt = Counter(df[target_attr])
    if len(cnt) == 1:
        return next(iter(cnt))
    elif df.empty or not attrs:
        return default_class
    else:
        default_class = max(cnt.keys())
        gains = [information_gain(df, attr, target_attr) for attr in attrs]
        best_attr = attrs[gains.index(max(gains))]
        tree = {best_attr: {}}
        remaining_attrs = [attr for attr in attrs if attr != best_attr]
        for attr_val, data_subset in df.groupby(best_attr):
            subtree = id3(data_subset, target_attr, remaining_attrs, default_class)
            tree[best_attr][attr_val] = subtree
        return tree

df_tennis = pd.read_csv('ID3.csv')
attribute_names = list(df_tennis.columns)
attribute_names.remove('PlayTennis')

tree = id3(df_tennis, 'PlayTennis', attribute_names)

print("\n\nThe Resultant Decision Tree is :\n")
pprint(tree)

