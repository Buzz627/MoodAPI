FROM python:3

ADD server.py /

ADD mood.py /

RUN pip install flask

RUN pip install pymongo

RUN pip install gunicorn


CMD [ "gunicorn", "--bind=0.0.0.0", "server:app"]
