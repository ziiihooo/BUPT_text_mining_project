import os
import os.path
from unicodedata import east_asian_width
import jieba

split_word = [' ',"\u3000","\n"]

# 读取停用词
def load_stopwords():
    with open("stop_words.txt") as F:
        stopwords=F.readlines()
        F.close()
    return [word.strip() for word in stopwords]

#  读取文件内容核文件路径，存储为字典
def load_files():
    fileContents = {}
    for root, dirs, files in os.walk(
        r"../../THUCNews/"
    ):
        filePaths = []
        fileContent_eachdir = {}
        for index,name in enumerate(files):
            if(index < 50):
                filePaths.append(os.path.join(root, name))
                f = open(filePaths[index], encoding= 'utf-8')
                fileContent = f.read()
                f.close()
                fileContent_eachdir[name] = fileContent
        if fileContent_eachdir:
            fileContents[root] = fileContent_eachdir
    return fileContents


# 分词函数
def divide_delete_words(file_contents,stop_word):
    result = {}
    # 遍历文件夹
    for file_eachdir in file_contents:
        file_seg_list = {}
        # 遍历文件
        for file_name in file_contents[file_eachdir]:
            none_stop_list = []
            # print(file_contents[file_eachdir][file_name])
            # 分词函数
            seg_list = jieba.cut(file_contents[file_eachdir][file_name])
            #筛选停用词和特殊换行空格词
            for item in seg_list:
                if(item not in stop_word and item not in split_word):
                   none_stop_list.append(item)
            # 添加该文件所有分词结果
            file_seg_list[file_name] = none_stop_list
        # 添加该文件夹所有文件
        result[file_eachdir] = file_seg_list
    return result




stop_word = load_stopwords()
file_content = load_files()
seg_result = divide_delete_words(file_content,stop_word)

print(seg_result)