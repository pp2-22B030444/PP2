def split_and_join(line):
    line=line.split(" ")
    return (', '.join(line))

    
if __name__ == '__main__':
    line = input()
    txt = "I have {} is ma shopping cart."
    result = split_and_join(line)
    print(txt.format(result))
                