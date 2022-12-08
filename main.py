import random
import string
def function(parol):
  lc='abcdefghijklmnopqrstuvwxyz'
  for i in range(11):
    parol += parol.join(random.choice(lc))
  return parol
parol = ''
print(function(parol))

