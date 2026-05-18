Use Cases :
1. 

요구사항 정의서
기능 요구사항 (Functional Requirements)
기능 ID	주요 기능	설명	우선순위
FR-01	퀴즈 생성 기능	사용자는 과목 및 시험 범위를 선택하여 해당 범위에 맞는 퀴즈를 생성할 수 있어야 한다.	상
FR-02	퀴즈 풀이 및 답안 제출	사용자는 생성된 퀴즈를 풀고 정답을 제출할 수 있어야 한다.	상
FR-03	정답 및 해설 확인	사용자는 퀴즈 풀이 후 정답, 오답, 해설을 확인할 수 있어야 한다.	중
FR-04	오답 저장 및 복습	시스템은 틀린 문제를 자동 저장하고 사용자가 다시 풀 수 있도록 지원해야 한다.	중
FR-05	학습 기록 확인	사용자는 점수, 정답률 등 자신의 퀴즈 풀이 기록을 확인할 수 있어야 한다.	중
비기능 요구사항 (Non-Functional Requirements)
기능 ID	주요 기능	설명	우선순위
NFR-01	성능	시스템은 퀴즈 생성 및 결과 표시를 0.5초 이내에 완료해야 한다.	중
NFR-02	보안	시스템은 사용자 학습 데이터 및 기록을 안전하게 저장하고 인증된 사용자만 접근할 수 있도록 해야 한다.	중

----

```mermaid
flowchart LR
    User([일반 사용자])

    UC1((과목 및 시험 범위 선택))
    UC2((범위 기반 퀴즈 생성))
    UC3((퀴즈 풀이))
    UC4((정답 제출))
    UC5((정답/오답/해설 확인))
    UC6((오답 문제 자동 저장))
    UC7((오답 문제 다시 풀기))
    UC8((퀴즈 풀이 기록 확인))

    INC1[<<include>>]
    INC2[<<include>>]
    INC3[<<include>>]

    EXT1[<<extend>>]
    EXT2[<<extend>>]

    User --> UC2
    User --> UC3
    User --> UC5
    User --> UC7
    User --> UC8

    %% include 관계
    UC2 -.-> INC1 -.-> UC1
    UC3 -.-> INC2 -.-> UC4
    UC5 -.-> INC3 -.-> UC4

    %% extend 관계
    UC6 -.-> EXT1 -.-> UC5
    UC7 -.-> EXT2 -.-> UC6
```
---
# 클래스 다이어그램

아래는 시험 범위 기반 퀴즈 시스템의 유스케이스를 기반으로 작성한 클래스 다이어그램이다.

## 클래스 다이어그램 (Mermaid)

```mermaid
classDiagram

class User {
    -userId: int
    -name: String
    +selectSubject() void
    +viewQuizHistory() void
}

class Subject {
    -subjectId: int
    -subjectName: String
    +getExamRange() String
    +setExamRange(range: String) void
}

class Quiz {
    -quizId: int
    -createdDate: Date
    +generateQuiz() void
    +getQuestions() List<Question>
}

class Question {
    -questionId: int
    -content: String
    -answer: String
    +checkAnswer(userAnswer: String) boolean
    +showExplanation() String
}

class Answer {
    -answerId: int
    -userAnswer: String
    -isCorrect: boolean
    +submitAnswer() void
    +getResult() boolean
}

class WrongAnswerNote {
    -noteId: int
    -savedDate: Date
    +saveWrongQuestion(q: Question) void
    +retryQuestion() void
}

class QuizHistory {
    -historyId: int
    -solveDate: Date
    +saveRecord() void
    +viewRecord() List<Quiz>
}

%% 관계 정의
User --> Quiz : solves
User --> QuizHistory : views
User --> WrongAnswerNote : manages

Quiz --> Subject : based on
Quiz "1" *-- "many" Question : contains

Question --> Answer : checked by

WrongAnswerNote --> Question : stores

QuizHistory --> Quiz : records

Answer ..> Question : depends on
WrongAnswerNote ..> Answer : uses
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
