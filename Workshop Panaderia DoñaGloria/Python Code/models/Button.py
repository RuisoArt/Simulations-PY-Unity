
class Button():
    pulsador_marcha = False

    def __init__(self,pulsador_marcha):
        self.pulsador_marcha = pulsador_marcha
    
    @property
    def get_pulsador_marcha(self):
        return self.pulsador_marcha
    @get_pulsador_marcha.setter
    def set_pulsador_marcha(self, value):
        self.pulsador_marcha = value

    def __str__(self):
        return str(self.pulsador_marcha)