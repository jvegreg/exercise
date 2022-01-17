FROM python:3.9-slim

WORKDIR /src/exercise

COPY . .
RUN pip install .[test] && pip cache purge
RUN pytest tests && getlinks --help

ENTRYPOINT ["getlinks"]