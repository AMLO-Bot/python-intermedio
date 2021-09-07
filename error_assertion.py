def divisors(num):
  try:
    if num < 1:
      raise ValueError('Number must be non negative')
    return [i for i in range(1, num+1) if num%i == 0]
  except ValueError as ve:
    print(ve)
    return False


def run():
  try:
    num = int(input('Enter a number: '))
    print(divisors(num))
    print('\nProgram ended')
  except ValueError:
    print('Debes ingresar un numero')

if __name__ == '__main__':
  run()