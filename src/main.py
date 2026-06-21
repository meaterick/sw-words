from datetime import datetime


# -----------------------------
# Subject Class
# -----------------------------
class Subject:
    def __init__(self, subject_id, subject_name, exam_range):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.exam_range = exam_range

    def get_exam_range(self):
        return self.exam_range

    def set_exam_range(self, exam_range):
        self.exam_range = exam_range


# -----------------------------
# Question Class
# -----------------------------
class Question:
    def __init__(self, question_id, content, answer, explanation):
        self.question_id = question_id
        self.content = content
        self.answer = answer
        self.explanation = explanation

    def check_answer(self, user_answer):
        # 사용자가 실수로 입력한 앞뒤 공백을 제거하고 비교
        return self.answer.lower() == user_answer.strip().lower()

    def show_explanation(self):
        return self.explanation


# -----------------------------
# Answer Class
# -----------------------------
class Answer:
    def __init__(self, answer_id, user_answer):
        self.answer_id = answer_id
        self.user_answer = user_answer
        self.is_correct = False

    def submit_answer(self, question):
        self.is_correct = question.check_answer(self.user_answer)

    def get_result(self):
        return self.is_correct


# -----------------------------
# Quiz Class
# -----------------------------
class Quiz:
    def __init__(self, quiz_id, subject):
        self.quiz_id = quiz_id
        self.subject = subject
        self.created_date = datetime.now()
        self.questions = []
        self.answers = []

    def generate_quiz(self):
        """
        실제 서비스에서는 DB 또는 AI 기반 문제 생성 가능
        현재는 예시 문제 생성
        """

        if self.subject.subject_name == "Python":
            self.questions = [
        Question(
            1,
            "Python에서 리스트를 생성할 때 사용하는 기호는?",
            "[]",
            "리스트는 대괄호 [] 를 사용하여 생성한다."
        ),
        Question(
            2,
            "Python에서 함수 선언에 사용하는 키워드는?",
            "def",
            "함수는 def 키워드로 선언한다."
        ),
        Question(
            3,
            "Python에서 조건문에 사용하는 키워드는?",
            "if",
            "조건문은 if 키워드를 사용한다."
        ),
        Question(
            4,
            "Python에서 반복문에 사용하는 키워드 중 하나는?",
            "for",
            "for 문은 반복 작업에 사용된다."
        ),
        Question(
            5,
            "Python에서 값을 출력하는 함수는?",
            "print",
            "print() 함수는 값을 출력한다."
        ),
        Question(
            6,
            "Python에서 사용자 입력을 받는 함수는?",
            "input",
            "input() 함수는 사용자 입력을 받는다."
        ),
        Question(
            7,
            "Python에서 한 줄 주석에 사용하는 기호는?",
            "#",
            "# 기호 뒤의 내용은 주석 처리된다."
        ),
        Question(
            8,
            "Python에서 문자열 자료형의 이름은?",
            "str",
            "문자열 자료형은 str 이다."
        ),
        Question(
            9,
            "Python에서 정수 자료형의 이름은?",
            "int",
            "정수 자료형은 int 이다."
        ),
        Question(
            10,
            "Python에서 실수 자료형의 이름은?",
            "float",
            "실수 자료형은 float 이다."
        ),
        Question(
            11,
            "Python에서 참/거짓 자료형의 이름은?",
            "bool",
            "참/거짓 자료형은 bool 이다."
        ),
        Question(
            12,
            "Python에서 데이터의 길이를 구하는 함수는?",
            "len",
            "len() 함수는 데이터의 길이를 반환한다."
        ),
        Question(
            13,
            "Python에서 클래스를 선언할 때 사용하는 키워드는?",
            "class",
            "클래스는 class 키워드로 선언한다."
        ),
        Question(
            14,
            "Python에서 예외 처리를 시작할 때 사용하는 키워드는?",
            "try",
            "예외 처리는 try 문으로 시작한다."
        ),
        Question(
            15,
            "Python에서 반복문을 즉시 종료하는 키워드는?",
            "break",
            "break 는 반복문을 즉시 종료한다."
        ),
        Question(
            16,
            "Python에서 현재 반복을 건너뛰고 다음 반복으로 넘어가는 키워드는?",
            "continue",
            "continue 는 다음 반복으로 넘어간다."
        ),
        Question(
            17,
            "Python 파일의 기본 확장자는?",
            ".py",
            "Python 파일은 .py 확장자를 사용한다."
        ),
        Question(
            18,
            "Python에서 딕셔너리를 생성할 때 사용하는 기호는?",
            "{}",
            "딕셔너리는 중괄호 {} 를 사용한다."
        ),
        Question(
            19,
            "Python에서 튜플을 생성할 때 사용하는 기호는?",
            "()",
            "튜플은 소괄호 () 를 사용한다."
        ),
        Question(
            20,
            "Python에서 여러 줄 문자열 작성에 사용할 수 있는 기호는?",
            "\"\"\"",
            "여러 줄 문자열에는 삼중 따옴표를 사용할 수 있다."
        )
        ]

        elif self.subject.subject_name == "Math":
            self.questions = [
                Question(
                    1,
                    "2 + 3 = ?",
                    "5",
                    "2와 3을 더하면 5이다."
                ),
                Question(
                    2,
                    "10 / 2 = ?",
                    "5",
                    "10을 2로 나누면 5이다."
                ),
                Question(
                    3,
                    "5 * 6 = ?",
                    "30",
                    "5와 6을 곱하면 30이다."
                ),
                Question(
                    4,
                    "9 - 4 = ?",
                    "5",
                    "9에서 4를 빼면 5이다."
                ),
                Question(
                    5,
                    "7 + 8 = ?",
                    "15",
                    "7과 8을 더하면 15이다."
                ),
                Question(
                    6,
                    "12 / 3 = ?",
                    "4",
                    "12를 3으로 나누면 4이다."
                ),
                Question(
                    7,
                    "2 * 7 = ?",
                    "14",
                    "2와 7을 곱하면 14이다."
                ),
                Question(
                    8,
                    "15 - 9 = ?",
                    "6",
                    "15에서 9를 빼면 6이다."
                )
            ]

    def get_questions(self):
        return self.questions


# -----------------------------
# WrongAnswerNote Class
# -----------------------------
class WrongAnswerNote:
    def __init__(self):
        self.note_id = 1
        self.saved_date = datetime.now()
        self.wrong_questions = []

    def save_wrong_question(self, question):
        # 이미 동일한 문제가 오답 노트에 있으면 중복 저장 방지
        if question not in self.wrong_questions:
            self.wrong_questions.append(question)

    def retry_question(self):
        print("\n===== 오답 다시 풀기 =====")

        still_wrong_questions = []

        for question in self.wrong_questions:
            print(f"\n문제: {question.content}")
            user_answer = input("답 입력: ")

            if question.check_answer(user_answer):
                print("정답입니다! (오답 노트에서 삭제됩니다.)")
            else:
                print("오답입니다.")
                print("해설:", question.show_explanation())
                still_wrong_questions.append(question)

        self.wrong_questions = still_wrong_questions


# -----------------------------
# QuizHistory Class
# -----------------------------
class QuizHistory:
    def __init__(self):
        self.history_id = 1
        self.solve_date = datetime.now()
        self.records = []

    def save_record(self, quiz, score):
        self.records.append({
            "quiz_id": quiz.quiz_id,
            "subject": quiz.subject.subject_name,
            "score": score,
            "date": datetime.now()
        })

    def view_record(self):
        print("\n===== 퀴즈 기록 =====")

        for record in self.records:
            print(
                f"과목: {record['subject']} | "
                f"점수: {record['score']} | "
                f"날짜: {record['date']}"
            )


# -----------------------------
# User Class
# -----------------------------
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.quiz_history = QuizHistory()
        self.wrong_answer_note = WrongAnswerNote()

    def select_subject(self):
        print("과목 선택")
        print("1. Python")
        print("2. Math")

        choice = input("선택: ")

        if choice == "1":
            return Subject(1, "Python", "기초 문법")

        elif choice == "2":
            return Subject(2, "Math", "기초 계산")

        else:
            print("잘못된 선택입니다.")
            return None

    def view_quiz_history(self):
        self.quiz_history.view_record()


# -----------------------------
# Main Program
# -----------------------------
def main():

    print("===== 시험 범위 기반 퀴즈 시스템 =====")

    user = User(1, "홍길동")

    # 과목 선택
    subject = user.select_subject()

    if subject is None:
        return

    # 퀴즈 생성
    quiz = Quiz(1, subject)
    quiz.generate_quiz()

    questions = quiz.get_questions()

    score = 0

    print("\n===== 퀴즈 시작 =====")

    # 퀴즈 풀이
    for question in questions:

        print(f"\n문제 {question.question_id}")
        print(question.content)

        user_answer = input("답 입력: ")

        answer = Answer(question.question_id, user_answer)
        answer.submit_answer(question)
        quiz.answers.append(answer)

        # 정답 확인
        if answer.get_result():
            print("정답입니다!")
            score += 1
        else:
            print("오답입니다.")
            print("정답:", question.answer)
            print("해설:", question.show_explanation())

            # 오답 저장
            user.wrong_answer_note.save_wrong_question(question)

    # 결과 출력
    print("\n===== 결과 =====")
    print(f"총 점수: {score}/{len(questions)}")

    # 기록 저장
    user.quiz_history.save_record(quiz, score)

    # 기록 조회
    user.view_quiz_history()

    if user.wrong_answer_note.wrong_questions:
        retry = input("\n오답 문제를 다시 풀겠습니까? (y/n): ")
        if retry.lower() == "y":
            user.wrong_answer_note.retry_question()
            if not user.wrong_answer_note.wrong_questions:
                print("\n🎉 축하합니다! 모든 오답을 맞혀 오답 노트가 비었습니다.")
    else:
        print("\n✨ 만점입니다! 틀린 문제가 없습니다.")


# 프로그램 실행
if __name__ == "__main__":
    main()
