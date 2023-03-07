FROM python:3.11
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN mkdir /app
WORKDIR /app
COPY proiect .
ENTRYPOINT [ "python", "manage.py", "runserver" ]