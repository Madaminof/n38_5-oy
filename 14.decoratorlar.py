# dekoratorlar
def currency(fn):
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)
    return wrapper


# map
maplist=[1,2,3,4,5,6]
maps=map(lambda x:x**2,maplist)
print(list(maps))

# filter
filterlist=[1,2,3,4,5,6]
filters=filter(lambda x:x%2!=0,filterlist)
print(list(filters))

# zip
l1=[1,2,3,4]
l2=['a','b','c','d']
zips=zip(l1,l2)
print(list(zips))
