# Dockerfile, Image, Container


FROM python:3.8

ADD main.py .

RUN pip install emoji

CMD ["python", "main.py"]