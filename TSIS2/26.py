def even_fn(x):
  if x %2!=0 and x%3!=0:
    return True
  return False

print(list(filter(even_fn, [1, 3, 2,7, 5, 20,19, 21,61])))