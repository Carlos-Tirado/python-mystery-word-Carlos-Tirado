#import random module
import random
import string


def play_game():

    with open("words.txt") as open_file: 
        #porque no puedo manipular las palabras del archivo necesito crear una lista y poder hacer uso de ellas#
        word_list = []
        words = open_file.readlines()
        for word in words:  
            # word_list.append(word.strip) #short way, adding word*1 to the empty list and removing spaces*2#
            clean_word = word.strip() #*2#
            #print(clean_word) print all words for the text without the numbers
            word_list.append(clean_word) #*1#
        # my_list = [0, 1, 2, 3]#
        # my_list_len = len(my_list) --> 0 ----> 4 - 1 (3)#
        # my_list[my_list_len]#
        # get random word#
        word_list_len = len(word_list)-1
        #print(word_list_len)#

        random_index = random.randint(0, word_list_len)
        
        random_word = word_list[random_index].upper()

        # random_word = 'bike'
        print(random_word)

        print(f"The secret word contains   {len(random_word)} letters  ")

        #ya que tengo las random words(arriba)
        #defining Variables (seguimiento a tres conjunto de letras)
        alphabet = set(string.ascii_uppercase) #uso de mayusculas
        letters_to_guess = set(word) #para adivinar la palabra debo adivinar cada letra debo crear este conjunto datos especificos sin repetirse cool word {'C', 'O', 'L'}
        guessed_letters = set()
        
        opportunities = 8

        #implementar ciclo loop(proceso repetitivo), mientras queden letras por adivinar y oportunidades
        while len(letters_to_guess) > 0 and opportunities > 0:
            #'/'.join(['A', 'B', 'C']) --> 'A/B/C' this method put together all the elements in that secuence with the character inside the quotes
            #print(f"You have {opportunities} opportunities and you have used already: {'/'.join(guessed_letters)}")
            print(f"You have {opportunities} more opportunities")

            #showing Current progress of the word (like DREAM_R)
            word_item = [letter if letter in guessed_letters else '_' for letter in random_word] #this is a list comprehension
            print(f"Word: {' '.join(word_item)}") # mostrar la separacion de las letras por un espacio ademas de Underscore (R _ I _ V _ E _ R)
            print(f"You have used already: {'/'.join(guessed_letters)}")

            #El usuario escoge una letra nueva/user pick another letter
            user_letter = input('Pick a letter: ').upper()


            if  user_letter in alphabet - guessed_letters:
                guessed_letters.add(user_letter)
                #Si la letra ya está en la palabra, remover la letra 
                #del conjunto de letras pendientes por adivinar. 
                if user_letter in letters_to_guess:
                        letters_to_guess.remove(user_letter)
                        print('')
                    #Si la letra no está en la palabra, quitar una opportunity
                else:
                        opportunities = opportunities - 1
                        print(f"\nYour letter, {user_letter}.")
                #if the choose letter it was already used .
            elif user_letter in guessed_letters:
                    print("\nYou picked that one already, Use another one.")
            else:
                    print("\nThat is not a valid letter.")

                    # the game ends when there are not more remaining opportunities or when you get all the letters
            if opportunities == 0:
                print(f"You have lost. The word was: {random_word}")
            else:
                print(f'Great! You got the word {random_word}!')




if __name__ == "__main__":
    play_game()
