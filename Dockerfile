FROM python:3.8

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt && playwright install

CMD ["pytest"]
