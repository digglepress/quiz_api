FROM python:3.9-alpine
WORKDIR /app
ENV TERM=xterm-color
ARG API_KEY_ARG
ENV API_KEY=$API_KEY_ARG
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "/app/main.py"]