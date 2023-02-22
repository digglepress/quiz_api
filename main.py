import os
import sys
from dataclasses import dataclass

from quiz_api import quiz_factory


# print(quiz_factory())


@dataclass
class Option:
    key: str
    value: str

    def __str__(self):
        return f"{self.key}: {self.value}"


@dataclass
class Quiz:
    question: str
    answer: int
    options: list
    tags: list

    def is_correct(self, answer: str) -> bool:
        return answer == self.answer

    @classmethod
    def get_quizzes(cls, question_set: list) -> list:
        quizzes = [Quiz(
            question=question['question'],
            answer=question['correct_answer'],
            tags=[t['name'] for t in question['tags']],
            options=[Option(key=key.split('_')[1], value=value) for key, value in question['answers'].items()]
        ) for question in question_set]
        return quizzes


def main(questions: list) -> int:
    """
    Quiz Builder
    :param questions:
    :return: int
    """
    score_count = 0
    index = 1
    quizzes = Quiz.get_quizzes(questions)
    for quiz in quizzes:
        print()
        print(f"question {index} of {len(quizzes)}")
        print(quiz.question)

        for option in quiz.options:
            print(option)

        print('tags: ', ', '.join(tag for tag in quiz.tags), '\n', end='')

        guess = input('select option: ')
        if quiz.is_correct(f"answer_{guess.lower()}"):
            score_count += 1
        index += 1
        os.system('clear')
    return score_count


start_quiz = ""

if __name__ == '__main__':
    quit_keys = ["n", 'N', "q", 'Q']
    while start_quiz not in quit_keys:
        question_data = quiz_factory()
        result = main(question_data)
        print()
        score = int(result / len(question_data) * 100)
        print(f"you scored {score}% out of {len(question_data)} questions")
        print()
        print(f'to quit, type any of the following: ', ", ".join(i for i in quit_keys))
        start_quiz = input('start quiz? ')
    print("thank you for your time, see you soon.")
    sys.exit(0)
