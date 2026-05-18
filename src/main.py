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
        return self.answer.lower() == user_answer.lower()

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

    def generate_quiz(self):
        """
        실제 서비스에서는 DB 또는 AI 기반 문제 생성 가능
        현재는 예시 문제 생성
        """

        if self.subject.subject_name == "Python":
            self.questions = [
                Question(
                    1,
                    "Python에서 리스트를 생성하는 기호는?",
                    "[]",
                    "리스트는 대괄호 [] 를 사용하여 생성한다."
                ),
                Question(
                    2,
                    "Python에서 함수 선언 키워드는?",
                    "def",
                    "함수는 def 키워드를 사용한다."
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
        self.wrong_questions.append(question)

    def retry_question(self):
        print("\n===== 오답 다시 풀기 =====")

        for question in self.wrong_questions:
            print(f"\n문제: {question.content}")
            user_answer = input("답 입력: ")

            if question.check_answer(user_answer):
                print("정답입니다!")
            else:
                print("오답입니다.")
                print("해설:", question.show_explanation())


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

    # 오답 다시 풀기
    retry = input("\n오답 문제를 다시 풀겠습니까? (y/n): ")

    if retry.lower() == "y":
        user.wrong_answer_note.retry_question()


# 프로그램 실행
if __name__ == "__main__":
    main()
