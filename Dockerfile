FROM python:3.11-slim-buster
LABEL maintainer="Mounir Abbas"
WORKDIR /app
COPY . .
COPY requirements.txt .
RUN apt-get upgrade -y
RUN pip install --upgrade pip
RUN pip3 install psycopg2-binary
RUN pip3 install --upgrade setuptools wheel
RUN pip3 install --no-cache-dir -r requirements.txt

# RUN pip install uwsgi
EXPOSE 8000
CMD uvicorn main:app --reload --port 8000 --host 0.0.0.0
