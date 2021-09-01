import random

import time
import os

from audioplayer import AudioPlayer

playornoplay = input("do you want to play cards game, yes or no? \n")

playercard1 = 0
playercard2 = 0
playercard3 = 0

comcard1 = 0
comcard2 = 0
comcard3 = 0

card1active = True
card2active = True
card3active = True
card4active = True
card5active = True
card6active = True

cardsused = 0

false = False

randomcardlist = []

wrongcard = False

playerturndone = False
comturndone = False

if playornoplay == "yes":

    time.sleep(1)
    os.system("clear")
    
    #This means the game will run 
    print("then lets play!\n")
    #Game rules
    rulessong = AudioPlayer("rules song.mp3")
    rulessong.play()

    print("Here is how to play this game:\n")
    print("there will be six cards you can only pick 3 and the com player will pick 3\n")
    print("you pick the three cards and win by luck. you might have good luck meaning you win\n")
    print("or you have bad luck and you lose!\n")
    print("press key 1 to 6 to choose a card for each turn you get and then press enter\n")
    print("when you select one card you cant use it again.\n")
    print("For example. you use 3rd card as first card, you can't use it again nor the com use it\n")

    print("Now do you understand the rules and do you want to start the game?\n")

    request = input("Yes or No>\n")

    if request == "Yes" or "yes":

     rulessong.stop()

     time.sleep(5)

     os.system("clear")

     lucksong = AudioPlayer("lucksong.mp3")

     card1 = random.randrange(1,15)
     card2 = random.randrange(1,15)
     card3 = random.randrange(1,15)
     card4 = random.randrange(1,15)
     card5 = random.randrange(1,15)
     card6 = random.randrange(1,15)
   
     while True:
          
          lucksong.play()

          print(playercard1)
          print(playercard2)
          print(playercard3)

          print(card1)
          print(card2)
          print(card3)
          print(card4)
          print(card5)
          print(card6)

          print("Choose a card:\n")
          if card1active:    
               print("1.card 1")
          
          if card2active:
               print("2.card 2")

          if card3active:
               print("3.card 3")
          
          if card4active:
               print("4.card 4")
          
          if card5active:
               print("5.card 5")

          if card6active:
               print("6.card 6")
          player = input("So what card does your gut agree with?\n")
    
          if player == '1' and card1active:
               print("Card 1 is {}".format(card1))
               card1active = False

               if playercard1 == 0:
                    playercard1 = card1

                    playerturndone = True

               if playerturndone == False and playercard2 == 0:
                    playercard2 = card1

                    playerturndone = True

               if playerturndone == False and  playercard3 == 0:
                    playercard3 = card1

               cardsused = cardsused + 1

          elif player == '1' and card1active == False:
               print("Hahahaha, card 1 is already used so you can't use it")

          elif player == '2' and card2active:
               print("Card 2 is {}".format(card2))
               card2active = False

               if playercard1 == 0:
                    playercard1 = card2

                    playerturndone = True

               if  playerturndone == False and playercard2 == 0:
                    playercard2 = card2

                    playerturndone = True

               if  playerturndone == False and playercard3 == 0:
                    playercard3 = card2

               cardsused = cardsused + 1

          elif player == '2' and card2active == False:
               print("Hahahaha, card 2 is already used so you can't use it")

          elif player == '3' and card3active:
               print("Card 3 is {}".format(card3))
               card3active = False

               if playercard1 == 0:
                    playercard1 = card3

                    playerturndone = True

               if  playerturndone == False and playercard2 == 0:
                    playercard2 = card3

                    playerturndone = True

               if playerturndone == False and playercard3 == 0:
                    playercard3 = card3

               cardsused = cardsused + 1

          elif player == '3' and card3active == False:
               print("Hahahaha, card 3 is already used so you can't use it")
               
          elif player == '4' and card4active:
               print("Card 4 is {}".format(card4))
               card4active = False

               if playercard1 == 0:
                    playercard1 = card4

                    playerturndone = True

               if  playerturndone == False and playercard2 == 0:
                    playercard2 = card4

                    playerturndone = True

               if  playerturndone == False and playercard3 == 0:
                    playercard3 = card4
                    
               cardsused = cardsused + 1

          elif player == '4' and card4active == False:
               print("Hahahaha, card 4 is already used so you can't use it")

          elif player == '5' and card5active:
               print("Card 5 is {}".format(card5))
               card5active = false

               if playercard1 == 0:
                    playercard1 = card5

                    playerturndone = True

               if  playerturndone == False and  playercard2 == 0:
                    playercard2 = card5

                    playerturndone = True

               if  playerturndone == False and playercard3 == 0:
                    playercard3 = card5

               cardsused = cardsused + 1

          elif player == '5' and card5active == False:
               print("Hahahaha, card 5 is already used so you can't use it")

          elif player == '6' and card6active:
               print("Card 6 is {}".format(card6))
               card6active = False

               if playercard1 == 0:
                    playercard1 = card6

                    playerturndone = True

               if playerturndone == False and playercard2 == 0:
                    playercard2 = card6

                    playerturndone = True
                    
               if playerturndone == False and playercard3 == 0:
                    playercard3 = card6

               cardsused = cardsused + 1

          elif player == '6' and card6active == false:
                print("Hahahaha, card 6 is already used so you can't use it")
          
          else:
               print("Invalid!")

               wrongcard = True

          
          # Ai turn

          if wrongcard == False:

               lucksong.stop()

               time.sleep(2.5)

               os.system("clear")


               aisong = AudioPlayer("ai.mp3")

               aisong.play()

               print("Hahhahaha now your turn is done, it's now Ai's turn")

               if card1active:
                    randomcardlist.append('card 1')

               if card2active:
                    randomcardlist.append('card 2')  

               if card3active:
                    randomcardlist.append('card 3')    

               if card4active:
                    randomcardlist.append('card 4')  

               if card5active:
                    randomcardlist.append('card 5')    

               if card6active:
                    randomcardlist.append('card 6')  

               aichoice = random.choice(randomcardlist)

               time.sleep(3)

               os.system('clear')
               
               print("thinking....")
               
               time.sleep(5)

               if aichoice == 'card 1':
                    card1active = false

                    print("Com picked card 1 which is {}".format(card1))

                    if comturndone == False and comcard1 == 0:
                         comcard1 = card1

                         comturndone = True

                    if comturndone == False and comcard2 == 0:
                         comcard2 = card1

                         comturndone = True

                    if comturndone == False and comcard3 == 0:
                         comcard3 = card1

               if aichoice == 'card 2':
                    card2active = false

                    print("Com picked card 2 which is {}".format(card2))

                    if comturndone == False and comcard1 == 0:
                         comcard1 = card2

                         comturndone = True

                    if comturndone == False and comcard2 == 0:
                         comcard2 = card2

                         comturndone = True

                    if  comturndone == False and comcard3 == 0:
                         comcard3 = card2

               if aichoice == 'card 3':
                    card3active = false

                    print("Com picked card 3 which is {}".format(card3))

                    if comturndone == False and comcard3 == 0:
                         comcard1 = card3

                         comturndone = True

                    if comturndone == False and comcard2 == 0:
                         comcard2 = card3

                         comturndone = True

                    if  comturndone == False and comcard3 == 0:
                         comcard3 = card3
               
               if aichoice == 'card 4':
                    card4active = false

                    print("Com picked card 4 which is {}".format(card4))

                    if comturndone == False and comcard1 == 0:
                         comcard1 = card4

                         comturndone = True

                    if comturndone == False and comcard2 == 0:
                         comcard2 = card4

                         comturndone = True

                    if comturndone == False and comcard3 == 0:
                         comcard3 = card4


               if aichoice == 'card 5':
                    card5active = false

                    print("Com picked card 5 which is {}".format(card5))

                    if comturndone == False and comcard1 == 0:
                         comcard1 = card5

                         comturndone = True

                    if comturndone == False and comcard2 == 0:
                         comcard2 = card5

                         comturndone = True

                    if comturndone == False and comcard3 == 0:
                         comcard3 = card5
               
               if aichoice == 'card 6':
                    card6active = false

                    print("Com picked card 6 which is {}".format(card6))

                    if comturndone == False and comcard1 == 0:
                         comcard1 = card6

                         comturndone = True

                    if comturndone == False and comcard2 == 0:
                         comcard2 = card6

                         comturndone = True

                    if comturndone == False and comcard3 == 0:
                         comcard3 = card6
               
               cardsused = cardsused + 1

               randomcardlist.clear()

               time.sleep(5)

               if cardsused >= 6:
                    aisong.stop()

                    os.system("clear")

                    print("Finish!")

                    print("player card 1 is " + str(playercard1) + "\n")
                    print("player card 2 is " + str(playercard2)  + "\n")
                    print("player card 3 is " + str(playercard3)  + "\n")

                    print("com card 1 is " + str(comcard1)  + "\n")
                    print("com card 2 is " + str(comcard2)  + "\n")
                    print("com card 3 is " + str(comcard3)  + "\n")

                    totalplayercards = playercard1 + playercard2 + playercard3
                    totalcomcards = comcard1 + comcard2 + comcard3

                    time.sleep(1.5)

                    print("player card 1 + player card 2 + player card 3 = {}".format(totalplayercards))

                    print("com card 1 + com card 2 + com card 3 = {}".format(totalcomcards))

                    if totalplayercards > totalcomcards:
                         print("you won, you have good luck")

                         victorysong = AudioPlayer("victory.mp3")

                         victorysong.play()

                    elif totalplayercards == totalcomcards:
                         print("well its a tie")

                    else:
                         gameover = AudioPlayer("wah wah sound.mp3")

                         gameover.play()
                         
                         print("you lost")
                         print("bad luck!")

                    input("press enter to quit?")

                    quit()
                         
               time.sleep(2)

               print("Now it's your turn")

               time.sleep(4)
               aisong.stop()

               playerturndone = False
               comturndone = False

               input("prees enter to continue")

               lucksong.play()

               os.system('clear')

          wrongcard = false
else:
    print("Goodbye...")
    quit()