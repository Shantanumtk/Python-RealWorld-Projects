import requests

def get_word_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Word Not Found or API error")
        return None
    
    data = response.json()[0]
    word_data = data['word']
    audio = data['phonetics'][0]['audio']
    license_name = data['phonetics'][0]['license']['name']
    partofSpeech = data['meanings'][0]['partOfSpeech']
    definitions = data['meanings'][0]['definitions'][1]['definition']
    meanings = data['meanings']

    for meaning in data["meanings"]:
        part = meaning['partOfSpeech']
        definition = meaning['definitions'][0]['definition']
        example = meaning['definitions'][0].get('example', 'No example available.')

        print(part)
        print(definition)
        print(example)
    print(word_data)
    print(audio)
    print(license_name)
    print(partofSpeech)
    print(definitions)

if __name__ == "__main__":
    word = input("Enter a word ")
    get_word_meaning(word)
