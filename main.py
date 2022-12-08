import random
import string
def function(parol):
  lc='abcdefghijklmnopqrstuvwxyz'
  uc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  num='1234567890'
  for i in range(11):
    parol += parol.join(random.choice(lc+uc+num))
  return parol
parol = ''
print(function(parol))

