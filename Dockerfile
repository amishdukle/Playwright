FROM python:3.8-slim

WORKDIR /workspace

COPY requirements.txt .
RUN pip install -r requirements.txt && playwright install

CMD ["pytest"]
