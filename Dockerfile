FROM python:3.11.8-bullseye

ENV POETRY_VERSION=1.7.1
ENV WORKDIR=/srv
ENV APPDIR=${WORKDIR}/resume_filter_frontend

WORKDIR ${WORKDIR}

COPY . .

RUN pip install --no-cache-dir poetry==${POETRY_VERSION}
RUN poetry install --only main

EXPOSE 80
ENTRYPOINT poetry run streamlit run --server.address 0.0.0.0 --server.port 80 ${APPDIR}/resume_filter.py
