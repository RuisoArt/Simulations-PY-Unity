class Machines():
    A1 = False
    A2 = False

    def __init__(self,A1, A2):
        self.A1 = A1
        self.A2 = A2
    
    @property
    def get_A1(self):
        return self.A1
    @get_A1.setter
    def set_A1(self, value):
        self.A1 = value
    
    @property
    def get_A2(self):
        return self.A2
    @get_A2.setter
    def set_A2(self, value):
        self.A2 = value

    