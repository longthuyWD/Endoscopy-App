import math

def state(self, name):
    self.state = name

def statex4(self, name):
    self.statex4 = name
        
def changeStateClicked(self):
    if self.state == 'aspect':
        w = toNum(self, self.w.text())
        self.h.setText(str(math.ceil(w / self.ratio)))
    if self.state == 'cyclegan':
        self.method = 'cyclegan'
    if self.state == 'fice':
        self.method = 'fice'
    if self.state == 'lci':
        self.method = 'lci'
    if self.state == 'albumentation':
        self.method = 'albumentation'
    if self.state == 'vae':
        self.method = 'vae'

def toNum(self, text):
    if text == '':
        text = '0'
    num = int(text)
    return num