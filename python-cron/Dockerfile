# Use an official Alpine Linux with Python runtime as a parent image
FROM python:3.9-alpine

RUN pip install --no-cache-dir google-cloud-bigquery

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
#RUN apk --update --no-cache add bash

COPY keyfile.json /app/keyfile.json
ENV GOOGLE_APPLICATION_CREDENTIALS /app/keyfile.json
# Copy the Python script into the container
#COPY script.py /app/script.py
COPY script2.py /app/script2.py
COPY bigquery.py /app/bigquery.py

# Add a cron job to execute the script every 5 minutes
RUN echo "*/2 * * * * /usr/local/bin/python /app/script2.py >> /var/log/cron.log 2>&1" > /etc/crontabs/root
RUN echo "*/2 * * * * /usr/local/bin/python /app/bigquery.py >> /var/log/bigquery.log 2>&1" > /etc/crontabs/root

# Run crond and keep the container running
CMD ["crond", "-f"]