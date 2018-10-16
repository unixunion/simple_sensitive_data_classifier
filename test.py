from rasa_nlu.model import Interpreter
import json

interpreter = Interpreter.load("./models/current/nlu")
messages = ["the password could be bananas", "username foo, password: Zzzsa23", "the weather is just fine"]

for message in messages:
    result = interpreter.parse(message)
    print(result['intent'])
    print(json.dumps(result, indent=2))