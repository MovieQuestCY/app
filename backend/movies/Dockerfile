FROM python:3.9

WORKDIR /code

COPY ../requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ../moviequesttypes /moviequesttypes
RUN pip install -e /moviequesttypes
COPY ./movies /code/movies

CMD ["uvicorn", "movies.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]