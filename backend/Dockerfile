FROM python:3.12

RUN mkdir -p /app/src
COPY . /app/src
WORKDIR /app/src
EXPOSE 5000
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "server.py"]