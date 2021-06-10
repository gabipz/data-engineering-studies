FROM python:3.8.5-slim-buster

WORKDIR /

USER root

ENV SHELL=/bin/bash \
    NB_USER=airflow \
    NB_UID=1000 \
    NB_GID=100 \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    SLUGIFY_USES_TEXT_UNIDECODE=yes \
    AIRFLOW_FOLDER=/usr/local/airflow \
    AGS_FOLDER=/usr/local/airflow/dags \
    PYTHONPATH=PYTHONPATH:/usr/local/airflow \
    AIRFLOW_HOME=/usr/local/airflow

RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER

RUN apt clean && \
    apt update && \
    apt install -y \
    htop

WORKDIR $AIRFLOW_HOME

COPY requirements.txt requirements.txt

RUN pip3.8 install --upgrade pip \
    && pip3.8 install -U setuptools \
    && pip3.8 install -U wheel
RUN pip3.8 install -r requirements.txt --use-feature=2020-resolver

COPY entrypoint.sh /entrypoint.sh
RUN chmod 777 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
