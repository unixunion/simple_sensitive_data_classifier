from rasa_nlu.model import Interpreter
import json

interpreter = Interpreter.load("./models/current/nlu")
messages = ["the password could be bananas", "username foo, password: Zzzsa23"]

for message in messages:
    result = interpreter.parse(message)
    print(json.dumps(result, indent=2))