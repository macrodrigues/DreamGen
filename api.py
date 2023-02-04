import openai
import os
from dotenv import load_dotenv

load_dotenv('api_key.env')

openai.organization = os.getenv("ORG")
openai.api_key = os.getenv("API_KEY")

def gen_5_images(prompt):
    list_of_urls = []
    for i in range(2):
        response = openai.Image.create(
            prompt = prompt,
            n=1,
            size="1024x1024")
        image_url = response['data'][0]['url']
        list_of_urls.append(image_url)
    return list_of_urls
    