FROM python:3.11-slim

WORKDIR /app

COPY lib.txt .

RUN pip install --no-cache-dir -r lib.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]