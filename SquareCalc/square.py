class Square:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def CalcArea(self):
        area= self.a * self.b
        return area

    def CalcHekef(self):
        hekef= 2 * (self.a + self.b)
        return hekef