FROM python:3.7

COPY . /home/app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

WORKDIR /home/app

EXPOSE 8080

CMD python main.py
