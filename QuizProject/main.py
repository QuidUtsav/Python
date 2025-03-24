from question import Question
from data import questions_data
question_bank=[]
for question in questions_data:
    question_text=question["question"]
    question_ans=question["answer"]
    question_bank.append(Question(question_text,question_ans))



