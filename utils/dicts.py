# файл dicts.py
def get_val(collection, key, default='git'):
    if collection == {}:
        return {}
    if collection.get(key, "NOT FIND") == "NOT FIND":
        return default


    return collection[key]



print(get_val({1:"first",2: "second", 3:"third" },333333333))