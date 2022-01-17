FROM python:3.10-slim

WORKDIR /src/exercise

COPY . .
RUN pip install .[test] && pip cache purge
RUN pytest tests

ENTRYPOINT ["getlinks"]