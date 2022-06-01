from msilib.schema import Directory
import os
import os.path
import jieba
import json

split_word = [' ',"\u3000","\n"]

class Participle:
    # 读取停用词
    def load_stopwords(self):
        with open("stop_words.txt") as F:
            stopwords=F.readlines()
            F.close()
        return [word.strip() for word in stopwords]

    #  读取文件内容核文件路径，存储为字典
    def load_files(self,read_num=12000):
        fileContents = {}
        for root, dirs, files in os.walk(
            r"../../THUCNews/"
        ):
            filePaths = []
            fileContent_eachdir = {}
            for index,name in enumerate(files):
                if(index < read_num):
                    filePaths.append(os.path.join(root, name))
                    f = open(filePaths[index], encoding= 'utf-8')
                    fileContent = f.read()
                    f.close()
                    fileContent_eachdir[name] = fileContent
                else :
                    break
            if fileContent_eachdir:
                fileContents[root] = fileContent_eachdir
        return fileContents

    def write2json(self):
        result2file = json.dumps(self.seg_result,ensure_ascii=False)
        f = open('seg_result_json.json',encoding="utf-8", mode='w')
        f.write(result2file)
        f.close()
        return

    def read_json2directory(self):
        f = open('seg_result_json.json',encoding="utf-8", mode='r')
        content = f.read()
        self.seg_result = json.loads(content)
        f.close()
        return

    # 分词函数
    def divide_delete_words(self,file_contents,stop_word):
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

    def __init__(self, read_num = 12000,is_read_file = False) -> Directory:
        if not is_read_file:
            stop_word = self.load_stopwords()
            file_content = self.load_files(read_num)
            self.seg_result = self.divide_delete_words(file_content,stop_word) 
            self.write2json()
        elif is_read_file:
            self.read_json2directory()
        return 