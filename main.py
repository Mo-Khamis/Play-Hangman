import random
def play():
  mode = input("\nPlease Type 'A' for easy mode or 'B' for hard mode: ")
  mode = mode.upper()
  if mode == "A":
    easy_mode()
  elif mode == "B":
    hard_mode()
  elif mode != "A" and mode != "B":
    print("Invalid, please try again ")
    play()

def easy_mode():
  print("\n**Easy Mode**")
  print("________________\n")
  my_dict = {}
  old_list = []
  new_list = []
  rem_lives = 8
  with open("words.txt", "r") as file:
    for line in file:
      my_dict[line.split(":")[0]] = line.split(":")[1].replace("\n", "")
    keys = my_dict.keys()
    hidden_word = random.choice(list(keys))
    print(f"your hint is: {my_dict[hidden_word]}")

    for letter in hidden_word:
      old_list.append(letter)
    for letter in hidden_word:
      if letter != " ":
        new_list.append("*")
      else:
        new_list.append(" ")
    print("\n", new_list)

  still_running = True
  while still_running:
    guess_w = input("\n**Type a letter to guess: ")
    for letter in old_list:
      if guess_w == letter:

        ind = old_list.index(guess_w)
        new_list[ind] = guess_w
        old_list[ind] = guess_w.upper()

    print("\n**Correct guess :)")
    print("*********************\n")
    print(new_list)
    if guess_w not in old_list and guess_w not in new_list:
      rem_lives = rem_lives - 1
      print("\n**wrong guess :(\n ")
      print(f"{rem_lives} remaining lives ! ")
    if rem_lives == 0:
      print(f"\nSorry you lost! The word was {hidden_word}")
      print("\nBack to menu")
      still_running = False
    if "*" not in new_list:
      print("\n************************************************************")
      print(
        f"\nYour word '{hidden_word}' was guessed correctly, You Won the game\n"
      )
      print("************************************************************")
      print("\nBack to menu")
      still_running = False
def hard_mode():
  print("\nHard Mode, no hints:")
  print("**********************")
  my_dict = {}
  old_list = []
  new_list = []
  rem_lives = 8
  with open("words.txt", "r") as file:
    for line in file:
      my_dict[line.split(":")[0]] = line.split(":")[1].replace("\n", "")
    keys = my_dict.keys()
    hidden_word = random.choice(list(keys))
    for letter in hidden_word:
      old_list.append(letter)
    for letter in hidden_word:
      if letter != " ":
        new_list.append("*")
      else:
        new_list.append(" ")
    print("\n", new_list)
  still_running = True
  while still_running:
    guess_w = input("\n**Type a letter to guess: ")
    for letter in old_list:
      if guess_w == letter:
        print("\nCorrect guess :)")
        ind = old_list.index(guess_w)
        new_list[ind] = guess_w
        old_list[ind] = guess_w.upper()
    print(new_list)
    if guess_w not in old_list and guess_w not in new_list:
      rem_lives = rem_lives - 1
      print("\nwrong guess :( ")
      print(f"\n{rem_lives} remaining lives")
    if rem_lives == 0:
      print(f"Sorry you lost! The word was {hidden_word}")
      print("\nBack to menu")
      still_running = False
    if "*" not in new_list:
      print("\n*******************")
      print("You Won the game")
      print("*******************")
      print("\nBack to menu")
      still_running = False


def list_words():
  file = open("words.txt", "r")
  read = file.readlines()
  print(read)


def add_word():
  key = input("Please enter a new word: ").lower()
  value = input("Please enter the hint: ").lower()
  with open("words.txt", "a") as f:
    f.writelines("\n")
    f.write(key)
    f.write(":")
    f.write(value)
    print(f"\n'{key}':'{value}' has been added to words.txt file")


def menu():
  print("\n-----------------------------------")
  print("1. Play Hangman\n" + "2. List Words in Dictionary\n" +
        "3. Add Word to Dictionary\n" + "4. Exit")
  print("-----------------------------------")


def main():
  name = input("Please enter your name: ")
  name = name.upper()
  print(f"\nHello {name}, welcome to the Hangman Menu")
  menu()
  number = input("Please enter your choice: ")
  while True:
    if number == '1':
      play()
    elif number == '2':
      print("Listing words...")
      list_words()
    elif number == '3':
      add_word()

    elif number == '4':
      exit()
    else:
      print("\nERROR, Please select a valid number\n")
    menu()
    number = input("Please enter your choice: ")
  else:
    print("Exited..")
main()

