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
    return '\n'.join(str(i) for i in list_of_urls)
    