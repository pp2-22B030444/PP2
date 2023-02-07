
words = input().split() 
f = 'I have {} in my shopping cart.'
results = ', '.join(words)
print(f.format(results))