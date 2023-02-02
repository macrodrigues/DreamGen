import openai
openai.organization = "org-2P7RBkMj286pwFp2tBL0Pdbe"
openai.api_key = "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"

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
    