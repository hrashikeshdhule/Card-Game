'''WAP to build card game between comuter and user consider the following list of cards
Create a two methods card value and play game,card value should returns a score of card name
Play a game method should start the game between user and computer,They need to play total rounds 
of total number of cards in each round find the score of card played by user and computer at last 
compare the score of user and computer and display the winner'''

import random 
class CARD_GAME:
    def __init__(self,cards,username):
        self.cards=cards
        self.username=username
        self.computer_score=0
        self.user_score=0

    def card_value(self,card):
        card_score={v:k for k,v in enumerate(self.cards,2)}
        return card_score[card]
    
    def play_game(self):
        print('Game started')
        for i in range(len(self.cards)):
            uc=input('Enter the card:')
            if uc in self.cards:
                print(f'{self.username} played:',uc)
                self.user_score+=self.card_value(uc)

            cs_card=random.choice(self.cards)
            print('comuter played:',cs_card)
            self.computer_score+=self.card_value(cs_card)

        print()
        print("computer score:",self.computer_score)
        print(f'{self.username} score:',self.user_score)

        if self.computer_score == self.user_score:
            print("It's a tie math")
        elif self.computer_score > self.user_score:
            print('Computer win')
        else:
            print(f'{self.username} Won the game')  

cards=['2','3','4','5','6','7','8','9','10','K','Q','J','A']
print(random.choice(cards))

username=input('Enter user name:')
cg=CARD_GAME(cards,username)
cg.play_game()