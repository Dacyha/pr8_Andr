import random
import string
def function(parol):
  lc='abcdefghijklmnopqrstuvwxyz'
  uc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  for i in range(11):
    parol += parol.join(random.choice(lc+uc))
  return parol
parol = ''
print(function(parol))

