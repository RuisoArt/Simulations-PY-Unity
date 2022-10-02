class Tasks():
    W1 = False
    W2 = False
    W3 = False
    W4 = False
    W5 = False

    def __init__(self, W1, W2, W3, W4, W5):
        self.W1 = W1
        self.W2 = W2
        self.W3 = W3
        self.W4 = W4
        self.W5 = W5
    
    @property
    def get_W1(self):
        return self.W1
    @get_W1.setter
    def set_W1(self, value):
        self.W1 = value

    @property
    def get_W2(self):
        return self.W2
    @get_W2.setter
    def set_W2(self, value):
        self.W2 = value
    
    @property
    def get_W3(self):
        return self.W3
    @get_W3.setter
    def set_W3(self, value):
        self.W3 = value
    
    @property
    def get_W4(self):
        return self.W4
    @get_W4.setter
    def set_W4(self, value):
        self.W4 = value
    
    @property
    def get_W5(self):
        return self.W5
    @get_W5.setter
    def set_W5(self, value):
        self.W5 = value
    
    

