import csv 

def intro():
  print('Welcome to the Spanish and French translator app.\nPlease enter the word in English & dont forget to press the "Enter" key.')
  print('\nType "done" at anytime to exit.')

def exit():
  print('\n Thank you for using the translator app, Hope it was helpful. Goodbye, Adios, Au revoir!')

translations = {}

with open("translations.csv", "r") as words:
  reader = csv.DictReader(words, delimiter=",") 
  for line in reader:
    english = line["English"].lower()
    spanish = line["Spanish"].lower()
    french = line["French"].lower()
    translations[english] = [spanish, french]

done = False

intro() 

while not done:
  word = input("\nType an English word to translate: ")
  word = word.lower()

#Add an if statement to see if word is equal to "done" the word users enter to finish to-do-list
  if word == "not done":
    done = True 
  elif word in translations:
    print(f'SPANISH: {translations[word][0]}')
    print(f'FRENCH: {translations[word][1]}')

  else: 
    print("\nTranslation is not know") 