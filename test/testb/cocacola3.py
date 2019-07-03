# -*- coding: utf-8 -*-

class Cocacola:
    formula = ['caffeine', 'sugar', 'water', 'soda']
    def __init__(self,logo_name):
        self.logo_name = logo_name

    def drink(self):
        print('Energy')

coke = Cocacola('可口可乐')
coke.logo_name