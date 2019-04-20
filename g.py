from random import randint
player=input('paper(p),scisor(s),rock(r)')

chosen=randint(1,3)
#print(chosen)
if chosen ==1:
  com='p'
elif chosen ==2:
  com='s'
else:
  com='r'
#print(com)
print(player,'vs',com)

if com==player:
  print(draw)
elif com=='p' and player=='s':
  print('player wins')
elif com=='s' and player=='r':
  print('player wins')
elif com=='r' and player=='p':
  print('player wins')


elif com=='s' and player=='p':
  print('computer wins')
elif com=='r' and player=='s':
  print('computer wins')
elif com=='p' and player=='r':
  print('computer wins')

else:
  print('invalid')
