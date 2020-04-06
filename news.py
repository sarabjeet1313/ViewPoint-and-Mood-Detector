from pymongo import MongoClient
import re
import os


client = MongoClient()
db = client.Assignment3Database
newsCollection = db.backupNewsCollection


def clean(uncleanText):
    cleanNews = re.sub(r'http\S+', '', uncleanText)
    cleanNews = ''.join([char if ord(char) < 128 else '' for char in cleanNews])
    cleanNews = re.sub('[_()\"*#/@<>{}`+=~|]', "", str(cleanNews))
    cleanNews = ' '.join([word for word in uncleanText.split(" ") if word != "&amp"])
    cleanNews = re.sub(r'([^\s\w]|_)+', '', cleanNews)
    cleanNews = re.sub(r'(\[.*\])', '', cleanNews)
    cleanNews = cleanNews.lower()

    # print("Data cleaned for the given line")
    return cleanNews


if not os.path.exists("news"):
    os.mkdir("news")

counter = 1
for news in newsCollection.find():
    lst = news['articles']

    for l in lst:
        f = open("news/News_" + str(counter) + ".txt", "a")

        author = clean(str(l['author']))
        f.write("author : " + author)
        f.write("\n")

        title = clean(str(l['title']))
        f.write("title : " + title)
        f.write("\n")

        description = clean(str(l['description']))
        f.write("description : " + description)
        f.write("\n")

        content = clean(str(l['content']))
        f.write("content : " + content)
        f.write("\n")

        counter += 1
        f.close()