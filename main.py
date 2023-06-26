import requests
from bs4 import BeautifulSoup
import sqlite3
import time
import http.client
import mimetypes
from codecs import encode
import openai
openai.api_key = ""

def askgpt(cityname):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user",
                 "content": "give me a 5 day plan for traveling to {} in persian".format(cityname)},
            ]
        )

        result = ''
        for choice in response.choices:
            result += choice.message.content
        print(result)

    except Exception as e:
          print("beeb")


askgpt("dubai")
