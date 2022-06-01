from Participle import *

if __name__ == '__main__':
    p = Participle(is_read_file=False,read_num=50).seg_result
    # 读取缓存数据
    # p = Participle(is_read_file=True).seg_result
    print("ok")