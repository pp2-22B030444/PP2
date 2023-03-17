import os

if os.path.exists('Database.txt' and 'Word.txt'):
    os.remove('Database.txt' and 'Word.txt')
    print('file deleted')
else:
    print("file does not exists")