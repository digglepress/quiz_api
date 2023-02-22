import os

import requests


def quiz_factory():
    api_key = os.environ.get('API_KEY')

    url = "https://quizapi.io/api/v1/questions"
    response = requests.get(
        url,
        headers={"X-Api-Key": api_key},
        params={'apiKey': api_key},
        data={
            "question_type": "multiple_choice",
            "difficulty": "easy"
        }
    )

    return response.json()
