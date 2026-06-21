# 유스케이스 다이어그램 

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#E8E5FF', 'primaryTextColor': '#2D2D3A', 'lineColor': '#555555', 'nodeBorder': '#B3A9FF'}}}%%
flowchart LR
    %% 사용자
    User([일반 사용자])

    %% 유스케이스들
    UC1((과목 및 시험 범위 선택))
    UC2((범위 기반 퀴즈 생성))
    UC3((퀴즈 풀이))
    UC4((정답 제출))
    UC5((정답/오답/해설 확인))
    UC6((오답 문제 자동 저장))
    UC7((오답 문제 다시 풀기))
    UC8((퀴즈 풀이 기록 확인))

    %% 사용자 연결
    User --> UC2
    User --> UC3
    User --> UC5
    User --> UC7
    User --> UC8

    %% include 관계
    UC2 -. «include» .-> UC1
    UC3 -. «include» .-> UC4

    %% extend 관계
    UC6 -. «extend» .-> UC5
```
---
# 클래스 다이어그램

아래는 시험 범위 기반 퀴즈 시스템의 유스케이스를 기반으로 작성한 클래스 다이어그램이다.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#F0EDFF', 'primaryTextColor': '#2D2D3A', 'lineColor': '#666666', 'nodeBorder': '#C0B5FF'}}}%%
classDiagram
class User {
    -userId: int
    -name: String
    +selectSubject() Subject
    +viewQuizHistory() void
}

class Subject {
    -subjectId: int
    -subjectName: String
    -examRange: String
    +getExamRange() String
    +setExamRange(range: String) void
}

class Quiz {
    -quizId: int
    -createdDate: Date
    -questions: List~Question~
    -answers: List~Answer~
    +generateQuiz() void
    +getQuestions() List~Question~
}

class Question {
    -questionId: int
    -content: String
    -answer: String
    -explanation: String
    +checkAnswer(userAnswer: String) boolean
    +showExplanation() String
}

class Answer {
    -answerId: int
    -userAnswer: String
    -isCorrect: boolean
    +submitAnswer(q: Question) void
    +getResult() boolean
}

class WrongAnswerNote {
    -noteId: int
    -savedDate: Date
    -wrongQuestions: List~Question~
    +saveWrongQuestion(q: Question) void
    +retryQuestion() void
}

class QuizHistory {
    -historyId: int
    -solveDate: Date
    -records: List
    +saveRecord(quiz: Quiz, score: int) void
    +viewRecord() void
}

User --> Quiz : solves
User --> QuizHistory : views
User --> WrongAnswerNote : manages
Quiz --> Subject : based on
Quiz "1" *-- "many" Question : contains
Quiz "1" --> "many" Answer : manages
Answer --> Question : targets
WrongAnswerNote --> "many" Question : stores
QuizHistory --> "many" Quiz : records
```

---

## 클래스 설명

| 클래스 | 설명 |
|---|---|
| User | 퀴즈를 생성하고 풀이하는 일반 사용자 |
| Subject | 과목 및 시험 범위 정보를 관리 |
| Quiz | 범위 기반으로 생성된 퀴즈 |
| Question | 퀴즈에 포함되는 개별 문제 |
| Answer | 사용자의 답안 제출 및 채점 결과 |
| WrongAnswerNote | 오답 문제 저장 및 재풀이 기능 |
| QuizHistory | 사용자의 퀴즈 풀이 기록 관리 |

---

## 주요 기능

- 과목 및 시험 범위 선택
- 범위 기반 퀴즈 자동 생성
- 문제 풀이 및 정답 제출
- 정답/오답/해설 확인
- 오답 자동 저장
- 오답 다시 풀기
- 퀴즈 풀이 기록 조회
