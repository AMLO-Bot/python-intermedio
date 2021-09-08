# TIPS
# enumerate function

# OPTIONAL BUT GREAT
# score system

from os import system
from random import randint
from operator import itemgetter
import sprites


def randword():
  with open('./archives/data.txt', 'r', encoding='utf-8') as f:
    options = [line.rstrip('\n') for line in f.readlines()]
  return options[randint(0,170)]

def repaint_window(game_status):
  mistakes, board, win_word, used_chars = \
  itemgetter('mistakes', 'board', 'win_word', 'used_chars')(game_status)
  splitted_word = list(win_word)

  print(sprites.OTHERS['title_banner'])
  print(sprites.HANGMAN[mistakes])
  print('[',' '.join(board),']')
  print('\nEstas son las letras que has usado \n', '-'.join(used_chars))

  try:
    user_char = input("""
      Trata de adivinar la palabra
      IMPORTANTE: Algunas palabras llevan acentos
      Introduce una letra:
      """).lower()
    if not user_char.isalpha():
      raise ValueError('Debes introducir letras, no se aceptan numeros u otros caracteres')
    if len(user_char) != 1:
      raise ValueError('Solo puedes introducir una letra a la vez')
  except ValueError as ve:
    print(ve)
    input('\n press any key...')
    return game_status
  
  used_chars = used_chars.append(user_char)
  iserror = True   #flag to decide wether to add a mistake or not

  for index in range(len(splitted_word)):
    if user_char == splitted_word[index]:
      game_status['board'][index] = user_char
      iserror = False

  if iserror:
    game_status['mistakes'] = mistakes + 1
  else:
    game_status['iswinner'] = win_word == ''.join(board)
  
  return game_status

def gameend_ui(game_status):
  game_status['gameover'] = True
  system('clear')
  print(sprites.OTHERS['win_game'] 
    if game_status.get('iswinner') 
    else sprites.OTHERS['lose_game']
  )
  input('Press any key to end the game...')
  system('clear')

def game(game_status):
  win_word = randword()
  game_status['win_word'] = win_word
  game_status['board'] = ['_' for letter in list(win_word)]
  
  while not game_status['gameover']:
    game_status = repaint_window(game_status) #update pairs in game_status

    if game_status.get('iswinner'):
      gameend_ui(game_status)
    else:
      system('clear')
      if game_status['mistakes'] >= len(sprites.HANGMAN):
        gameend_ui(game_status)
      

def run():
  game_status = {
    'win_word': '',
    'gameover': False,
    'mistakes': 0,
    'board': '',
    'iswinner': False,
    'used_chars': ['']
  }

  game(game_status)

if __name__ == "__main__":
  run()