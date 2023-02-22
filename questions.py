import os

import requests

api_key = os.environ.get('API_KEY')

url = "https://quizapi.io/api/v1/questions"
post_url = "https://quizgecko.com/api/v1/questions"
response = requests.get(
    url,
    headers={"X-Api-Key": api_key},
    params={'apiKey': api_key},
    data={
        "question_type": "multiple_choice",
        "difficulty": "easy"
    }
)

questions = response.json()
