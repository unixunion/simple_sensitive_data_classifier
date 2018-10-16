## Installing Deps

```
pip install rasa_nlu[spacy]
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
```

## Review the training data

see train.md

## Train the model

```sh
python -m rasa_nlu.train -c nlu_config.yml --data train.md -o models --fixed_model_name nlu --project current--verbose
```

## Run the test

```sh
python test.py
```

## Output "per-sentence"

```json
all data: {
  "intent": {
    "name": "containspassword",
    "confidence": 0.882201147940561
  },
  "entities": [
    {
      "start": 24,
      "end": 31,
      "value": "zzzsa23",
      "entity": "password",
      "confidence": 0.49750060337243646,
      "extractor": "ner_crf"
    }
  ],
  "intent_ranking": [
    {
      "name": "containspassword",
      "confidence": 0.882201147940561
    },
    {
      "name": "nopassword",
      "confidence": 0.11779885205943894
    }
  ],
  "text": "username foo, password: Zzzsa23"
}
```