import urllib2
class testConnection:
    def __init__(self):
        self.__url = "http://www.google.com/" #Private variable
        

    def test(self):
        try:
            con = urllib2.urlopen(self.__url)
            print con
            #print data
            return True
        except:
            print "Connection failed"
            return False

test=testConnection() # Object Creation
print test.test() # method calling
