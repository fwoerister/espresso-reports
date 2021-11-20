FROM python:3.10-alpine

RUN apk update
RUN pip install pipenv

WORKDIR /usr/src/espresso-api
COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY espresso ./espresso

RUN pipenv install

EXPOSE 5000
ENTRYPOINT ["/usr/src/espresso-api/bootstrap.sh"]