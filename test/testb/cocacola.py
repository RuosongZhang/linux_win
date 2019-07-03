# -*- coding: utf-8 -*-
class cocacola:
    formula = ['caffeine', 'sugar', 'water', 'soda']

    def drink(self,how_much):
        if how_much == 'a sip':
            print('Cool~')
        elif how_much == 'whole bottle':
            print('Headache')
        print('Energy')

ice_coke = cocacola()
ice_coke.drink('a sip')

coke = cocacola()
coke.drink('whole bottle')

coke_for_china = cocacola()
print(cocacola.formula)
coke_for_china.local_logo = '可口可乐'
print(coke_for_china.local_logo)

