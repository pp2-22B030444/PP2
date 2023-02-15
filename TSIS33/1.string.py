class cString:

    def __init__(self):
        print ('inside __init__(self):')
        self.x = 'Default String'

    def getString(self):  # input from console
        self.x =input('Enter String : ')
        return self.x

    def printString(self):
        print ('in upper: ', self.x.upper())
        return self.x.upper()


def test():
    ac = cString()
    ac.getString()
    ac.printString()
    print ('TEST Class Methods')


def main():
    # start from here
    test()

if __name__ == '__main__':
    main()