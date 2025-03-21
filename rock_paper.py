class Game:
  def __init__(self):
    
    self.computer_pick=self.get_computer_pick()
    
    self.player_pick=self.get_player_pick()
    
    self.result=self.result()
  
  def get_computer_pick(self):
    import random
    
    ran=random.randint(0,2)
    
    choices = ['rock', 'paper', 'scissor']

    return choices[ran]
  
  def get_player_pick(self):
    while True:
      user=input("Enter your choice among rock/paper/scissor :")
      user=user.lower()
      if user in ('rock','paper','scissor'):
        return user
      else:
        print("invalid choice")
        
  def result(self):
    if self.computer_pick == self.player_pick:
      return "It's a tie!"
    elif self.computer_pick=='rock' and self.player_pick=='paper':
      return "You Win!!!"
    elif self.computer_pick=='paper' and self.player_pick=='scissor':
      return "You Win!!!"
    elif self.computer_pick=='scissor' and self.player_pick=='rock':
      return "You Win!!!🥳🥳"
    else:
      return "You lose😔😔"
  
  def print(self):
    print(f'computer choice:{self.computer_pick}')
    print(f'your choice:{self.player_pick}')
    print(f'{self.result}')
      
while True:
  game=Game()
  game.print()
  a=input("Enter y to play again: ")
  
  if a=='y':
    continue
  else:
    break













