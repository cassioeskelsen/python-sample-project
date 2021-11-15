FROM python:3.9-slim
ARG SOURCE_FOLDER
WORKDIR /src

RUN apt-get update && apt-get install -y git tzdata gcc
ENV TZ America/Sao_Paulo
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --force

COPY ./src/xpto/common ./src/xpto/common
COPY ./src/xpto/$SOURCE_FOLDER ./src/xpto/$SOURCE_FOLDER

#CMD python -m src.xpto.${SOURCE_FOLDER}.main
CMD ./src/xpto/$SOURCE_FOLDER/run.sh