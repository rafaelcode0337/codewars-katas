def filter_list(l):
    return list(filter(lambda item: not type(item) == str, l))

def filter_list2(l):
    return [item for item in l if not isinstance(item, str)]
