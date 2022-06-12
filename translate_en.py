# coding=utf-8

import numpy
import json
import sys

# Grabs the query
args = sys.argv[1]
out = args

if len(args) > 2:
    
    from googletrans import Translator
    translator = Translator()
    translation = translator.translate(args, dest='en', src = "hu")
    out = translation.text

    # The json that Alfred requires is below
result = {"items": [
    {
    "type": "file",
    "title": out,
    "subtitle": "Copy to Clipboard",
    "arg": out
    }
]}

finalResult = json.dumps(result)

print(finalResult)