def divisors(num):
  return [i for i in range(1, num+1) if num%i == 0]


def run():
  num = int(input('Enter a number'))
  print(divisors(num))
  
if __name__ == '__main__':
  run()