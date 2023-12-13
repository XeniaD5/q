#import random
#lst = ['robot'] * 10
#lst += ['human'] * 10
#random.shuffle(lst)
#data = pd.DataFrame({'whoAmI':lst})
#data.head()

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
categories = list(set(lst))
one_hot_dict = {category: [1 if val == category else 0 for val in lst] for category in categories}
    for category in categories:
     data[category] = one_hot_dict[category]
data.drop('whoAmI', axis=1, inplace=True)
print(data.head())
