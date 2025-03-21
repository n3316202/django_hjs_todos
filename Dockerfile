# pull official base image
FROM python:3.12.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
# Python이 .pyc 캐시 파일을 생성하지 않도록 설정
# PYTHONUNBUFFERED=1: 출력을 즉시 볼 수 있도록 버퍼링 비활성화
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev  build-base python3-dev libc-dev libpcap-dev  linux-headers

COPY . /usr/src/app/
# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]
EXPOSE 8888