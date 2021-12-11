def filter_list(l):
  return list(filter(lambda item: not type(item) == str, l))
