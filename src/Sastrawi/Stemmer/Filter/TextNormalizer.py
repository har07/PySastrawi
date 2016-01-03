import re

def normalizeText(text):
    result = str.lower(text)
    result = re.sub(r'/[^a-z0-9 -]/im', ' ', result)
    result = re.sub(r'/( +)/im', ' ', result)

    return result.strip()



