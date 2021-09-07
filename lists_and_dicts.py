# NEEDS union/pipe operator (|) available from python >= 3.9
# https://www.python.org/dev/peps/pep-0584/#specification
from functools import reduce

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

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
    nums = [1,2,3,4,5]
    sq = list(map(lambda num: num**2, nums ))
    print(sq)
    separator()
    power = reduce(lambda num, next: num*next, [2,2,2,2,2])
    print(power)

def project_filter():
    # Una con list comprehension en otra con high order functions
    separator('5')
    pythoners1 = list(filter(lambda person: person['language'] == 'python', DATA))
    pythoners2 = [person['name'] for person in DATA if person['language'] == 'python']
    separator()
    all_Platzi_workers1 = [person['name'] for person in DATA if person['organization'] == 'Platzi']
    all_Platzi_workers2 = list(map(lambda worker: worker['name'],list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))))
    separator()
    adults = list(filter(lambda person: person['age'] > 17, DATA))
    adult_names1 = list(map(lambda adult: adult['name'],adults))
    adult_names2 = [worker['name'] for worker in DATA if worker['age'] > 17]
    separator()
    old_people1 = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
    old_people2 = [(worker | {'old': worker['age'] > 70}) for worker in DATA]
    
if __name__ == '__main__':
    run();
    project_filter();