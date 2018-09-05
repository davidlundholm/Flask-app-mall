from app import Question, Answer, Exam

def add_data(db):
    new_exam = Exam(name = 'systemvetenskap1', university = 'ORU', semester = 'VT11')
    questions1 = Question(exam = new_exam.id, text ='Vem är tyngst')
    questions2 = Question(exam = new_exam.id, text ='Vem är längst')
    questions3 = Question(exam = new_exam.id, text ='Vem mår bäst')

    answer11 = Answer(question = questions1, text ='Sean', correct = True)
    answer12 = Answer(question = questions1, text ='Benny')

    answer21 = Answer(question = questions2, text ='Johan')
    answer22 = Answer(question = questions2, text ='Malin', correct = True)

    answer31 = Answer(question = questions3, text ='Donald', correct = True)
    answer32 = Answer(question = questions3, text ='Jimmie')

    db.session.add(new_exam)

    db.session.add(questions1)
    db.session.add(questions2)
    db.session.add(questions3)

    db.session.add(answer11)
    db.session.add(answer12)
    db.session.add(answer21)

    db.session.add(answer22)
    db.session.add(answer31)
    db.session.add(answer32)

    db.session.commit()





