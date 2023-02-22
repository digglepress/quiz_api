import os
from dataclasses import dataclass

from questions import questions


# print(questions)


@dataclass
class Option:
    key: str
    value: str

    def __str__(self):
        return f"{self.key}: {self.value}"


@dataclass
class Quiz:
    id: int
    question: str
    answer: int
    options: list
    tags: list

    def is_correct(self, answer: str):
        return answer == self.answer

    @classmethod
    def get_quizzes(cls) -> list:
        quizzes = [Quiz(
            id=question['id'],
            question=question['question'],
            answer=question['correct_answer'],
            tags=[t['name'] for t in question['tags']],
            options=[Option(key=key.split('_')[1], value=value) for key, value in question['answers'].items()]
        ) for question in questions]
        return quizzes


score = 0
index = 1
if __name__ == '__main__':
    for quiz in Quiz.get_quizzes():
        print()
        print(f"question {index} of {len(Quiz.get_quizzes())}")
        print(quiz.question)

        for option in quiz.options:
            print(option)
        for tag in quiz.tags:
            print('tags: ', ''.join(tag), '\n', end='')

        guess = input('select option: ')
        if quiz.is_correct(f"answer_{guess.lower()}"):
            score += 1
        index += 1
        os.system('clear')

    print()
    print()
    mark = int(score / len(Quiz.get_quizzes()) * 100)
    print(f"you scored {mark}% out of {len(Quiz.get_quizzes())} questions")
