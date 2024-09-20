import os
import json
import termplotlib as tpl

def read_text(text: str, format='json'):
    text = text.lower()
    words_number = count_words(text)
    characters_number = count_characters(text)
    words_density = get_words_density(text)
    return format_response(
        {
            "words":words_number,
            "characters":characters_number,
            "kwd_density":words_density
            },format)
    
def read_file(file_path: str, format='json'):
    _, file_extension = os.path.splitext(file_path)
    if file_extension != ".txt":
        raise ValueError("Invalid File Type")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return read_text(content,format)
    except FileNotFoundError:
        raise FileNotFoundError("File not found")


def count_words(text: str):
    return text.split().__len__()

def count_characters(text: str):
    text = text.replace("\n","")
    return list(text).__len__()

def get_differents_words(text: str):
    txt_list = text.split()
    txt_set = set(txt_list)
    return list(txt_set)

def get_words_density(text: str):
    list_words = get_differents_words(text)
    words_density = []
    for word in list_words:
        words_density.append([word,text.count(word)])
    words_density.sort(key=sort_density_words, reverse=True)
    return words_density

def sort_density_words(element):
    return element[1]

def format_response(response,format='json'):
    if (format == 'json'):
        return json.dumps(response)
    elif (format == 'plain'):
        density_plain = ''
        for word in response['kwd_density']:
            density_plain += f"{word[0]}: {word[1]}\n"
        return f"""{response['words']} words\n{response['characters']} characters\n\n{density_plain}"""
    elif (format == 'histogram'):
        strings = [word[0] for word in response['kwd_density']]  # Extrae las cadenas
        numbers = [word[1] for word in response['kwd_density']]  # Extrae los números
        fig = tpl.figure()
        fig.barh(numbers, strings, force_ascii=True)
        return f"{response['words']} words\n{response['characters']} characters\n\n{fig.get_string()}"