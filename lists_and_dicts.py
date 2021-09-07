
def separator(sep='-'):
    print(sep*40)

def run():
    # Repaso
    my_list = [1,'hello', True, 4.5]
    my_dict = {'firstname': 'Aldair', 'lastname': 'Avalos'}

    # Lista de dictionarios y dictionarios de listas
    super_list = [
        {'firstname': 'Aldair', 'lastname': 'Avalos'},
        {'firstname': 'Fernanda', 'lastname': 'Albino'},
        {'firstname': 'Jesus', 'lastname': 'Alvarado'},
        {'firstname': 'Violeta', 'lastname': 'Martinez'},
    ]

    super_dict = {
        'natural_nums': [1,2,3,4,5,6,7],
        'integer_nums': [1,2,-3,-4,5,6,-7],
        'floating_nums': [1.2,3.8,6.56]
    }

    for key, value in super_dict.items():
        print(key, '-', value)
    separator()
    for student in super_list:
        print(student['firstname'], '-', student['lastname'])
    separator()


    # Lista con los 10 primeros numeros naturales al cuadrado
    squared = [num**2  for num in range(1,101) if num%3 != 0]
    print (squared)
    separator()
    multiples = [num for num in range(1,10) if num%36 == 0]
    print(multiples)
    separator()

    # Dictionary comprehension
    cubed = {num: num**3 for num in range(1,101) if num%3 != 0}
    print(cubed)
    separator()
    sqrt = {num: round(num**0.5, 2) for num in range(1,1000)}
    print(sqrt)
    separator()
    
if __name__ == '__main__':
    run();