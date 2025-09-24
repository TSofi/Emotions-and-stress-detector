FROM python:3.10-slim

RUN apt-get update && apt-get install -y python3-opencv
RUN python -m pip install --upgrade pip

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

WORKDIR /app
COPY . /app
CMD ["python", "src/main.py"]