FROM python:3.10
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# set work directory 
WORKDIR /code
# install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system && pipenv install psycopg2
# Copy project 
COPY . /code/