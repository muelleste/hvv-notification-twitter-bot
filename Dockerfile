FROM python:3.8.6-slim-buster

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt --trusted-host pypi.python.org

CMD ["python3", "api.py"]