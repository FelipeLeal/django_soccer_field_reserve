FROM python:3
ENV PYTHONUNBUFFERED 1
ENV WEBAPP_DIR=/code
RUN apt-get update && pip install --upgrade pip && mkdir $WEBAPP_DIR
WORKDIR $WEBAPP_DIR
ADD requirements.txt $WEBAPP_DIR/
RUN pip install -r requirements.txt
COPY . $WEBAPP_DIR/
