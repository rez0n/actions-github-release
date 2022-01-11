# Container image that runs your code
FROM python:alpine

RUN apk --update add build-base libffi-dev
RUN pip install --no-cache-dir pygithub
COPY entrypoint.py /entrypoint.py

RUN chmod +x /entrypoint.py
ENTRYPOINT ["/entrypoint.py"]