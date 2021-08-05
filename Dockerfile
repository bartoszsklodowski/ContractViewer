FROM python:3.9.6-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /ContractViewer

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]