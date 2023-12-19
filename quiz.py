# a ductuibart tgat stores the questions and answers
# have a variable that tracks score of the player
# loop through dictionary using the key values pair
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
    "question1" : {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2" : {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3" : {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4" : {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5" : {
        "question": "What is the capital of Portugal?",
        "answer": "Libson"
    },
    "question6" : {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question7" : {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer: ")
    
    if answer.lower() == value['answer'].lower():
        print("Correct!")
        score = score +1
        
    else:
        print("Wrong")
        print("The Answer is:", value['answer'])
        
    print("Your Score is:", str(score))
    print("==============")

quiz_length = len(quiz)
percentage = int((score/quiz_length)*100)
print("You got " +str(score) + " ("+str(percentage)+"%) out of " + str(quiz_length))
