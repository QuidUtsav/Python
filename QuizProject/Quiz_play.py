from  main import question_bank
class Play:
    def __init__(self):
        i=1
        correct=0
        for question in question_bank:
            if i==len(question_bank):
                print("Last Question: ")
            print(f'Q{i}. {question.que} (True/False): ')
            ans=input()
            if self.check(ans.lower(),question):
                correct+=1
                print("You Got it!!!!")
                print(f'Your score:{correct}/{i}')
            else:
                print("Try the next Question!!!!")
                print(f'Your score:{correct}/{i}')
            i+=1

    def check(self,ans,question):
        if ans==question.ans:
            return True
        else:
            return False


Play()