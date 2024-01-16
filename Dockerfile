FROM python:3.11.0a1-slim
ENV PYTHONUNBUFFERED=1 \
    TZ=Asia/Calcutta
WORKDIR /app
RUN apt-get update \
  && apt-get install -y build-essential curl libpq-dev  --no-install-recommends \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && useradd --create-home python \
  && chown python:python -R /app  \
  && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime  \
  && echo $TZ > /etc/timezone
USER python
COPY --chown=python:python . .
RUN pip3 install --no-warn-script-location --user -r requirements.txt
ENV PATH="/home/python/.local/bin:${PATH}"
EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0", "-p", "8000", "run:application"]
