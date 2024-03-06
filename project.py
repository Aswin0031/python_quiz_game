class questions:
    def __init__(self,q,a):
        self.quiz_question=q
        self.quiz_answer=a
football_queston=[questions('Who won the most Ballondor in football history?\n(a)Messi\n(b)C.Ronaldo\n(c)Mbappe\n(d)Neymar\n','a'),
                questions('Who won FIFA world cup in 2022?\n(a)Brazil\n(b)Portugal\n(c)France\n(d)Argentina\n','d'),
                  questions('Who won Euro cup in 2020?\n(a)Portugal\n(b)Italy\n(c)France\n(d)Netherlands\n','b'),
                  questions('Who hosted FIFA world cup in 2014?\n(a)Italy\n(b)Australia\n(c)Brazil\n(d)England\n','c')]
cricket_question=[questions('Who is the caption of india in 2011?\n(a)V.Kohli\n(b)Sachin\n(c)Dhoni\n(d)R.Sharma\n','c'),
                  questions('Who hit 6 sixes in an over?\n(a)Ricky Ponding\n(b)Chris Gayle\n(c)Sachin\n(d)Yuvraj Singh\n','d'),
                  questions('Who won cricket world cup in 2023?\n(a)Australia\n(b)India\n(c)England\n(d)Srilanka\n','a'),
                  questions('Who scored the 1st 200 in world cup?\n(a)Sachin\n(b)Chris Gayle\n(c)Sewag\n(d)B.McCullum\n','b')]

movie_question=[questions('Who won the best actor national award in 2022?\n(a)Surya\n(b)Allu Arjun\n(c)Vikram\n(d)Dhanush\n','a'),
    questions('Who directed the movie manichithrathazhu?\n(a)Sibi Malayil\n(b)Bharathan\n(c)Padmarajan\n(d)Fazil\n','d'),
                questions('Best director of 2023?\n(a)Rajamouli\n(b)Nikhil Mahajan\n(c)R.hirani\n(d)S.Sankar\n','b'),
                questions('Best  music director of 2023?\n(a)A.R Rahman\n(b)Illairaja\n(c)Devi Sri Prasad\n(d)Vidya Sagar\n', 'c')
                ]
politics_question=[questions('Who is the 1st prime minister of india?\n(a)Abdul Kalam\n(b)Nehru\n(c)Vajpayee\n(d)Manmohan Singh\n','b'),
    questions('Who is the education minister of kerala?\n(a)Veena George\n(b)G.R.Anil\n(c)V.Shivankutty\n(d)R.Bindu\n','c'),
                questions('Who is the curren president of india?\n(a)Pratibha Patil\n(b)Rajendra Prasad\n(c)Ram Nath Govind\n(d)Droupati Murmu\n','d'),
                questions('Who is the CM of kerala?\n(a)Pinaray vijayan\n(b)K.Balakrishnan\n(c)Umman Chandi\n(d)Balagopal\n', 'a')
                ]
def run_politics_questions():
    score = 0
    for questions in politics_question:
        answer = input(questions.quiz_question)
        while answer not in ['a','b','c','d']:
            answer = input("Invalid input. Try Again").lower()
        if answer != questions.quiz_answer:
            print('your answer is incorrect! the correct answer is', questions.quiz_answer)

        else:
            print('your answer is correct! you have got 5 points')
            score += 5
    print(f'you got {score // 5} correct answers')
    return (f'you got total points {score} out of {len(politics_question) * 5}')
def run_cricket_questions():
    score = 0
    for questions in cricket_question:
        answer = input(questions.quiz_question)
        while answer not in ['a','b','c','d']:
                answer = input("Invalid input. Try Again").lower()
        if answer != questions.quiz_answer:
            print('your answer is incorrect! the correct answer is', questions.quiz_answer)

        else:
            print('your answer is correct! you have got 5 points')
            score += 5
    print(f'you got {score // 5} correct answers')
    return (f'you got total points  {score} out of {len(cricket_question) * 5}')

def run_football_questions():
    score = 0
    for questions in football_queston:
        answer = input(questions.quiz_question).lower()

        while answer not in ['a','b','c','d']:
                answer = input("Invalid input. Try Again").lower()
        if answer != questions.quiz_answer:
            print('your answer is incorrect! the correct answer is', questions.quiz_answer)

        else:
            print('your answer is correct! you have got 5 points')
            score += 5
    print(f'you got {score // 5} correct answers')
    return (f'you got total points  {score} out of {len(football_queston) * 5}')


def run_movie_question():
    score=0
    for questions in movie_question:
        answer=input(questions.quiz_question).lower()
        while answer not in ['a','b','c','d']:
                answer = input("Invalid input. Try Again").lower()
        if answer!=questions.quiz_answer:
            print('your answer is incorrect! the correct answer is',questions.quiz_answer)

        else:
            print('your answer is correct! you have got 5 points')
            score+=5
    print(f'you got {score//5} correct answers')
    return  (f'you got total points {score} out of {len(movie_question)*5}')

print('Welcome to the WORLD of QUIZ GAME!')
playing=input('Do you want to play?(YES?NO) : ').lower()
while playing not in ['yes','no']:
    playing = input("Invalid input,try Again :( ").lower()
if playing=='yes':
    print('Okay Let us play :)')
else:
    print('Game Ended :(')
    quit()

type=input('Which type of questions you want?\nMovies\nSports\nPolitics\n').lower()
while type not in ['movies','sports','politics']:
    type = input("Invalid input,try Again : ").lower()
if type=='sports':
    sports_type=input('Which type of sports you want?\nFootball\nCricket\n').lower()
    while sports_type not in ['football', 'cricket']:
        sports_type = input("Invalid input,try Again : ").lower()
    if sports_type=='football':
        print('There will be 4 options in your hand!,you have to choose one option as given in the the question.\n')
        print(run_football_questions())
    if sports_type=='cricket':
        print('There will be 4 options in your hand!,you have to choose one option as given in the the question.\n')
        print(run_cricket_questions())
if type=='movies':
    print('There will be 4 options in your hand!,you have to choose one option as given in the the question.\n')
    print(run_movie_question())
if type=='politics':
    print('There will be 4 options in your hand!,you have to choose one option as given in the the question.\n')
    print(run_politics_questions())