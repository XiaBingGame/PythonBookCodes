# 08_randomQuiz_Generator.py - Creates quizzes with  questions and answers in
# random oider, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

if __name__ == '__main__':
    for quizNum in range(35):
        quizFile = open('captialsquiz%s.txt' % (quizNum+1), 'w')
        answerKeyFile = open('captialsquiz_answers%s.txt' % (quizNum + 1), 'w')

        quizFile.write('Name:\n\nData:\n\nPeriod:\n\n')
        quizFile.write(' ' * 20 + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
        quizFile.write('\n\n')

        states = list(capitals.keys())
        random.shuffle(states)

        for questionNum in range(50):
            correctAnswer = capitals[states[questionNum]]
            wrongAnswer = list(capitals.values())
            del wrongAnswer[wrongAnswer.index(correctAnswer)]
            wrongAnswer = random.sample(wrongAnswer, 3)
            answerOptions = wrongAnswer + [correctAnswer]

            quizFile.write('%s. What is the captial of %s?\n' % (questionNum + 1, states[questionNum]))
            for i in range(4):
                quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')

            answerKeyFile.write('%s. %s\n' %(questionNum+1, 'ABCD'[answerOptions.index(correctAnswer)]))

        answerKeyFile.close()
        quizFile.close()
    print('Done.')