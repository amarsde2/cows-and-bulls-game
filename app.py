# Cows and bulls Game Implementation using Python 

# Author Details 

# Name  :  Er. Amar kumar 
# Email :  amarkumar9685079691@gmail.com 

## Start of a Game ##

import random

class CowsAndBullGame:
    _secret_code = None 
    _cows = 0
    _bulls = 0
    _allowed_trials = 0
    _guess_code = None
    
    def _noDuplicate(self):
        '''
        This function check weather a given number is contains unqiue digits or not
        '''
        digits = []
        
        for x in self._secret_code:
            digits.append(x)

        return len(self._secret_code) == len(set(digits))
    
    def _generateSecretCode(self):
        
        '''
        This is a  function generate secret code for guess
        '''
        self._secret_code = str(random.randint(1000,9999))
        
        while not self._noDuplicate():
            self._secret_code = str(random.randint(1000,9999))
         
    
    def _resetGameState(self):
        '''   
        This is function to reset game state
        '''
        self._generateSecretCode()
        self._cows = 0
        self._bulls = 0
        self._allowed_trials = 5
        self._guess_code = None
        print(f"secret code  {self._secret_code} ")


    def _getUserCode(self):
        
        print(f"You are only {self._allowed_trials} attempts left! ")
        self._guess_code = str(input("Enter a unique 4 digit number! "))
        
        while not self._noDuplicate() or len(self._guess_code) != 4:
            print("Please enter a 4 digit number where digit should be unique! ")
            self._guess_code = str(input("Enter a unique 4 digit number! "))
       

    def _welcomeMessage(self):
        
        '''   
        This is a just function to show welcome message and hit about guess number
        '''
        
        print("Welcome! ")
        print("You are playing cows and bulls game! ")
        print("You have 5 attempts in which you have to guess 4 unique digit number ")
        print("Best of Luck! ")
      

    def _validateCode(self):
      
        '''
        This is a function to calculate cows and bulls 
        '''
        self._cows = 0
        self._bulls = 0

        for i in range(4):
            if self._secret_code[i] == self._guess_code[i]:
                self._cows += 1
            else:
                if self._guess_code[i] in self._secret_code:
                   self._bulls += 1


    def _playAction(self):
       
        '''   
        This is a function to handle play again case or exit
        '''
       
        choice = int(input("You want to play again? Type 1 for yes or 2 for exit! ")) 

        if choice == 1:
            self.play()
        else:
            print("Bye, See you again! ")
            exit(0)  
    
    def _handleWinner(self):
       
        '''   
        This is a function to handle winning case
        '''
       
        print("Congratulations! ")    
        print(f"You won the game. You have guessed number in {5 - self._allowed_trials} ")  
        self._playAction()
        

    def _handleLose(self):  
        '''   
        This is a function to handle lose case
        '''
        print("Oops! You lost the game ")    
        self._playAction()   

    def play(self):
       
        self._welcomeMessage()
        self._resetGameState()
       
        try:
            while self._allowed_trials > 0:
       
                self._getUserCode()
                self._validateCode()

                if  self._cows == 4:
                    self._handleWinner()
                    break
                else:
                    self._allowed_trials -= 1
                    print(f"You have {self._cows} cows and {self._bulls} bulls ")
                    print("Try, Next best guess! ")
                    if  self._allowed_trials == 0:
                        self._handleLose()
           
        except  KeyboardInterrupt:
            print("Bye, See you again! ")
            exit(0)


if __name__ == "__main__":
    app = CowsAndBullGame()
    app.play()

   