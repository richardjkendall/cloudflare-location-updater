FROM python:alpine3.16

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY update.py .

CMD [ "python", "./update.py" ]