class Cookie:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

cookieOne = Cookie("red")
cookieTwo = Cookie("green")

print("Cookie One is", cookieOne.getColor())
print("Cookie two is", cookieTwo.getColor())

cookieOne.setColor("blue")

print("Cookie One is", cookieOne.getColor())
print("Cookie two is", cookieTwo.getColor())

