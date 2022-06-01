from gensim import corpora
from gensim import models
import os
import os.path

# 读取停用词
def load_stopwords():
    with open("stop_words.txt") as F:
        stopwords=F.readlines()
        F.close()
    return [word.strip() for word in stopwords]

#  读取文件内容核文件路径，存储为列表
def load_files():
    filePaths = []
    fileContents = []
    for root, dirs, files in os.walk(
        r"../../THUCNews/体育"
    ):
        for index,name in enumerate(files):
            if(index < 5000):
                filePaths.append(os.path.join(root, name))
                f = open(filePaths[index], encoding= 'utf-8')
                fileContent = f.read()
                f.close()
                fileContents.append(fileContent)
    return fileContents



stop_word = load_stopwords()
file_content = load_files()
