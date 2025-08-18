FROM python:3.11-slim

WORKDIR /nlp


COPY requirements.txt /nlp/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


COPY . /nlp/


RUN python -m nltk.downloader punkt punkt_tab averaged_perceptron_tagger averaged_perceptron_tagger_eng


CMD ["python", "nlp.py"]
