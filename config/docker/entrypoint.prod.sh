#!/bin/sh

echo "📌 엔트리포인트 스크립트 시작"

python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py collectstatic --no-input

exec "$@"