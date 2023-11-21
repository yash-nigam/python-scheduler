# Use an official Alpine Linux with Python runtime as a parent image
FROM python:3.9-alpine

RUN pip install --no-cache-dir google-cloud-bigquery apscheduler

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
#RUN apk --update --no-cache add bash

COPY keyfile.json /app/keyfile.json
ENV GOOGLE_APPLICATION_CREDENTIALS /app/keyfile.json
COPY bigquery.py /app/bigquery.py

# Run crond and keep the container running
CMD ["python", "bigquery.py"]