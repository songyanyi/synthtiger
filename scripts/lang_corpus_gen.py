"""
faker 来生成

pip install faker

https://blog.csdn.net/weixin_43499626/article/details/99670187

activate textgen
cd /d F:\Project\docpartner\core\textocr\datahelper\datagen\synthtiger\scripts
python lang_corpus_gen.py
"""

import os 
import random
from faker import Faker

faker = Faker('zh_CN')

def gen_chinese_word_or_sequence():
    a = random.random()
    if a<0.1:
        randStr = faker.address()
        randStr = randStr[0:-7]
    elif 0.1<a<0.2:
        randStr = faker.city()
        # randStr = faker.city_name()
    elif 0.2<a<0.3:
        randStr = faker.province()
    elif 0.3<a<0.4:  
        randStr = faker.street_address()
    elif 0.4<a<0.5:
        randStr = faker.company()
        # randStr = faker.company_prefix()
        # randStr = faker.company_suffix() 
    elif 0.5<a<0.6:
        randStr = faker.sentence(nb_words=10,variable_nb_words=True,ext_word_list=None)
        # randStr = faker.day_of_week()
    elif 0.6<a<0.7:
        # randStr = faker.iso8601() # 时间
        randStr = faker.sentence(nb_words=6,variable_nb_words=True,ext_word_list=None)
    elif 0.7<a<0.8:
        randStr = faker.job()
        randStr = randStr.split("/")[0]
    # randStr = faker.ascii_free_email()
    #
    # randStr = faker.paragraph(nb_sentence=3, variable_nb_sentences=True,ext_word_list=None) # 段落
    # randStr = faker.paragraphs(nb=3,ext_word_list=None)
    elif 0.8<a<0.9:
        randStr = faker.sentence(nb_words=15,variable_nb_words=True,ext_word_list=None) # 句子
    # randStr = faker.sentences(nb=3,ext_word_list=None)
    else:
        randStr = faker.word(ext_word_list=None)
    # randStr = faker.words(nb=3,ext_word_list=None,unique=False)
    # randStr = faker.text(max_nb_chars=200,ext_word_list=None)
    # randStr = faker.texts(nb_texts=3)

    return randStr


strList = []
n = 50000

for i in range(n):
    
    iStr = gen_chinese_word_or_sequence()
    print(iStr)
    if iStr == "":
        continue
    if len(iStr)>50:
        continue
    if random.random()<0.2:
        iStr = iStr[0]
    if iStr.endswith("."):
        iStr = iStr.strip(".")
    
    iStr += "\n"

    strList.append(iStr)

nowPath = os.path.abspath(os.path.dirname(__file__))
synthtigerPath = os.path.dirname(nowPath)

corpusPath = os.path.join(synthtigerPath,"resources","corpus","chinesecorpus.txt")
with open(corpusPath,"a",encoding="utf-8") as f:
    f.writelines(strList)





