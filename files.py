import os

def read():
  numbers = []
  with open('./archives/numbers.txt', 'r', encoding='utf-8') as f:
    foo = [int(line) for line in f.readlines() ]
    print(foo)

def write():
  names = ['Facundo','Chrostioan','Miguel', 'Rocío']
  with open('./archives/names.txt', 'w') as f:
    for name in names:
      f.write(name)
      f.write('\n')
  

def run():
  print('working')
  read()
  write()

if __name__ == "__main__":
  run()