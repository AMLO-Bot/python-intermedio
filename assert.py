def divisors(num):
  assert num > 0 , 'Can not be negative'
  return [i for i in range(1, num+1) if num%i == 0]


def run():
    num = int(input('Enter a number: '))
    assert num.isnumeric(), 'Debes ingresa un numero'
    print(divisors(num))
    print('\nProgram ended')

if __name__ == '__main__':
  run()