# Question class oluştur
# Quiz class'i oluştur
# Quiz class'i Question class'indan soruları alacak
# aldığı soruları sırayla kullanıcıya gösterecek
# bu sorulara cevaplar verilecek verilen cevaplara göre bir skor bilgisi tutulacak
# sorduğunuz 5 sorunun 3 tanesini bildi şeklinde cevap göstersin.

# Class

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        return self.answer == answer

# Quiz

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0 # gönderilecek sorunun sırası
    
    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-' + q)

        answer = input ('Cevap: ')
        self.guess(answer)
        self.loadQuestion()
    
    def guess(self, answer):
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    
    def showScore(self):
        print('Score : ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        
        if questionNumber > totalQuestion:
            print('Quiz ends')
        else:
            print(f'You are in {questionNumber}/{totalQuestion}'.center(100, "*"))



# print(question.checkAnswer(answer))
# self.questionIndex += 1 # Bir sonraki soruya geçiş

q1 = Question('En iyi programlama dili hangisidir? ', ['C#', 'python', 'javascript', 'java'], 'python')
q2 = Question('En popüler programlama dili hangisidir? ', ['javascript', 'python', 'C#', 'java'], 'python')
q3 = Question('En çok kazandıran programlama dili hangisidir? ', ['C#', 'java', 'javascript', 'python'], 'python')
q4 = Question('En çok sevilen programlama dili hangisidir? ', ['C#', 'java', 'javascript', 'python'], 'python')
q5 = Question('En kolay  programlama dili hangisidir? ', ['C#', 'java', 'javascript', 'python'], 'python')

questions = [q1, q2, q3, q4, q5]
# print(q1.checkAnswer('python'))# True döndürür


quiz = Quiz(questions)

# question = quiz.questions[quiz.questionIndex]
# print(question.text)

quiz.loadQuestion()