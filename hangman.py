# MANDATORY
# error handling

# TIPS
# enumerate function

# OPTIONAL BUT GREAT
# score system
# list of used characters

from os import system
from time import sleep
from random import randint
from operator import itemgetter
import sprites


def randword():
  with open('./archives/data.txt', 'r', encoding='utf-8') as f:
    options = [line.rstrip('\n') for line in f.readlines()]
  return options[randint(0,170)]

def draw_ui(game_status):
  mistakes, board, win_word, used_chars = \
  itemgetter('mistakes', 'board', 'win_word', 'used_chars')(game_status)
  splitted_word = list(win_word)

  print(sprites.OTHERS['title_banner'])
  print(sprites.HANGMAN[mistakes])
  print(win_word)
  print(board)
  print('You have enterd this letters \n', ','.join(used_chars))
  try:
    user_char = input('Try to guess the word. \n Enter a letter: ')
    game_status['used_chars'] = used_chars.append(user_char)
  except ValueError:
    pass
  iserror = True   #flag to decide wether to add a mistake or not

  for index in range(len(splitted_word)):
    if user_char == splitted_word[index]:
      game_status['board'][index] = user_char
      iserror = False
      
  sleep(0.02)
  if iserror:
    game_status['mistakes'] = mistakes + 1
  else:
    game_status['iswinner'] = win_word == ''.join(board)
  print(game_status)
  sleep(0.5)

  return game_status

def gameend_ui(game_status):
  game_status['gameover'] = True
  sleep(1)
  system('clear')
  print(sprites.OTHERS['win_game'] 
    if game_status.get('iswinner') 
    else sprites.OTHERS['lose_game']
  )
  sleep(3)
  system('clear')

def game(win_word):
  game_status = {
    'win_word': win_word,
    'gameover': False,
    'mistakes': 0,
    'board': ['_' for letter in list(win_word)],
    'iswinner': False,
    'used_chars': []
  }

  while not game_status['gameover']:
    game_status = draw_ui(game_status) #update pairs in game_status

    if game_status.get('iswinner'):
      gameend_ui(game_status)
    else:
      system('clear')
      if game_status['mistakes'] >= len(sprites.HANGMAN):
        gameend_ui(game_status)
      

def run():
  win_word = randword()
  game(win_word)

if __name__ == "__main__":
  run()