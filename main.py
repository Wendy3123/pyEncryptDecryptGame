from art import logo
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def crypt(textInput, shiftInput, directionInput):
  completeWord = ''
  for letter in textInput:
    if letter in alphabet:
      if direction == 'encode':
        newLetter = alphabet.index(letter) + shiftInput
      elif direction == 'decode':
        newLetter = alphabet.index(letter) - shiftInput
      completeWord += alphabet[newLetter]
    else:
      completeWord += letter
  print(completeWord)

print(logo)
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26 #makes it so if the number is too large it will give the remainder
  crypt(text,shift,direction)
  result=input("Type 'yes' if you want to continue with another text. Otherwise type 'no': ")
  if result == 'no':
    should_continue = False
    print('Goodbye!')