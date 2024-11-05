import random
import string

from words import words
print("Spiele Hangman mit mir!")

def hangman():
    word = random.choice(words).upper() # Das zu erratende Wort
    word_letters = set(word) #Buchstaben im Wort
    alphabet = set(string.ascii_uppercase) #benutzt das "normale" Alphabet
    used_letters = set() #vom User geratene Buchstaben

    while len(word_letters) > 0:
    #benutze Buchstaben anzeigen
        print("Du hast diese Buchstaben bereits getestet: ", " ".join(used_letters))

   # Aktueller Stand des Wortes
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Derzeitiges Wort: ", " ".join(word_list))

    #User Input
        user_letter = input ("Welcher Buchstabe könnte im Wort sein?").upper()

    # Überprüfen, ob der Buchstabe gültig ist
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Super, {user_letter} ist im Wort!")
            else:
                print(f"{user_letter} ist nicht im Wort.")

        elif user_letter in used_letters:
            print("Diesen Buchstaben hast du schon genommen")

        else:
            print ("Ungültiges Zeichen, bitte probiere es nochmal.")

    print(f"Glückwunsch, du hast das Wort '{word}' erraten!")

# Funktion aufrufen, um das Spiel zu starten
hangman()