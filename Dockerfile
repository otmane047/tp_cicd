FROM python:3.10-slim

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "unittest", "test_simple_math.py"]