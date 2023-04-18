FROM alpine:latest
RUN apk update
RUN apk add py-pip
RUN apk add --no-cache python3-dev 
RUN pip install --upgrade pip
COPY requirements.txt /app/
WORKDIR /app
COPY . /asyncapi
RUN pip --no-cache-dir install -r requirements.txt
COPY . .
EXPOSE 3080

# ENV port = 3000
# Pass environment variables to the container
# ARG DEVELOPER_NAME
ENV DEVELOPER_NAME=DEVELOPER_NAME

CMD ["python3", "asyncapi.py"]