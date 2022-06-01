from gensim import corpora
from gensim import models
import os
import os.path
import codecs
import pandas

def load_content():
    with open("../THUCNews/财经/798977.txt",encoding="utf-8") as F:
        content=F.readlines()
        F.close()
    return content


def load_stopwords():
    with open("stop_words.txt") as F:
        stopwords=F.readlines()
        F.close()
    return [word.strip() for word in stopwords]


filePaths = []
fileContents = []

for root, dirs, files in os.walk(
    r"../THUCNews/体育"
):
    for index,name in enumerate(files):
        filePaths.append(os.path.join(root, name))
        f = open(filePaths[index], encoding= 'utf-8')
        fileContent = f.read()
        f.close()
        fileContents.append(fileContent)


content = load_content()
stop_word = load_stopwords()
dictionary = corpora.Dictionary([content])
texts = [dictionary.doc2bow(text) for text in [content]]
num_topics=5
lda = models.ldamodel.LdaModel(corpus=texts, id2word=dictionary, num_topics=num_topics)

for index,topic in lda.print_topics(5):
    print(topic)

print(content)