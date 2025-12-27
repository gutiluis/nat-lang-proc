## How it works: 

# build image
docker-compose build
# run interactively the input inside the unix terminal
docker-compose run -rm nlp-app


## Features:

Get the grammar, parts of speech, and split into words from a different input sentence everytime.

some grammar:
- NNP -> proper noun
- VBZ -> verb 3rd person singular present
- PRP -> pronoun
- RBR -> adverb comparative

------

###

------

# run it with python
python3 -m venv .venv
source .venv/bin/activate
pip install requirements.txt
chmod +x nlp.py
python3 nlp.py

-----

## Technologies Used

- Python

------

##

clone Repo:
