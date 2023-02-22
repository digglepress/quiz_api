FROM python:3.9-slim
WORKDIR /app
ENV TERM=xterm-color
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "/app/main.py"]