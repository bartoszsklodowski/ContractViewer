FROM python:3.9.6-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /ContractViewer

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --user

COPY . .

ENTRYPOINT ["/ContractViewer/docker-entrypoint.sh"]

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]