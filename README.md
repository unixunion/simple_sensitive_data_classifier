## Installing Deps

pip install rasa_nlu[spacy]
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en

## Review the training data

see train.md

## Train the model

python -m rasa_nlu.train -c nlu_config.yml --data train.md -o models --fixed_model_name nlu --project current--verbose

## Run the test

python test.py