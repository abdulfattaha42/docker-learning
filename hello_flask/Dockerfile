#Using the official Python Image, version 3.8(minimal python environment)
FROM python:3.8-slim 

#Setting working directory to "/app"
WORKDIR /app 

#Copying all the apps from the current directory and putting them in our container(we can say . . or . /app)
COPY . /app

#Addition RUN section needed for mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config

#Installing flask in our container just like how we had to install it locally
RUN pip install flask mysqlclient

#Exposing port 5002; we're making this port available so we can access it from our localhost - this makes the app accessible from outside our container
EXPOSE 5002

#Telling Docker to run our python app
CMD ["python", "app.py"]




# Stage 1: Build Stage
FROM python:3.8-slim as Build

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config

COPY . .

RUN pip install flask mysqlclient

#Stage 2: Production stage
FROM python:3.8-slim

WORKDIR /app

COPY --from=Build /usr/local /usr/local

COPY --from=Build /app /app

EXPOSE 5002

CMD ["python", "app.py"]



