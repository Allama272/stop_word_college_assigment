FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY main.py .
COPY paragraphs.txt .
RUN apt-get update && apt-get install -y \
    && python3 -m nltk.downloader stopwords
CMD [ "python", "main.py" ]