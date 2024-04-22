import json


def get_articles() -> dict[str: str]:
    with open('articles.json', 'r', encoding='utf-8') as articles_file:
        articles = json.load(articles_file)
        return articles


def save_article(name: str, text: str):
    with open('articles.json', 'r', encoding='utf-8') as articles_file:
        file = json.load(articles_file)
        file[name] = text

    with open('articles.json', 'w', encoding='utf-8') as articles_file:
        json.dump(file, articles_file, ensure_ascii=False)


def delete_article(name):
    with open('articles.json', 'r', encoding='utf-8') as articles_file:
        file = json.load(articles_file)
        del file[name]

    with open('articles.json', 'w', encoding='utf-8') as articles_file:
        json.dump(file, articles_file, ensure_ascii=False)





