class dog(object):
    def __init__(self,name,dog_type):
        self.name = name
        self.type = dog_type

    def sayhi(self):
        print('hello,I am a dog, my name is ',self.name)
        print('I am a ',self.type)

d = dog('liuliu','jingba')
d.sayhi()

