"""
faker 来生成

pip install faker

https://blog.csdn.net/weixin_43499626/article/details/99670187

activate textgen
cd /d F:\Project\docpartner\core\textocr\datahelper\datagen\synthtiger\scripts
python lang_corpus_gen.py
# 多语言 https://faker.readthedocs.io/en/master/locales.html
zh_CN

"""

import os 
import random
from faker import Faker

language = "ko_KR"
print(language)
langDict = {
    "zh_CN":"chinese", # OK
    "ar_AA":"arabic", # OK
    "bn_BD":"bangla", # OK
    "ja_JP":"japanese", # OK
    "ko_KR":"korean", # OK
    "hi_IN":"hindi", # OK
    "en":"english" # 已有，暂时不用
}
# 阿拉伯语 "ar_"
# 孟加拉语 bn
# 日语 ja_JP
# 韩语 ko_KR
# 拉丁语
# 印地语 hi_IN
faker = Faker(language) 
nowPath = os.path.abspath(os.path.dirname(__file__))
synthtigerPath = os.path.dirname(nowPath)
resourcesPath = os.path.join(synthtigerPath,"resources")
dictsPath = os.path.join(resourcesPath,"dicts")


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
    if random.random()<0.2:
        randStr = randStr[0]
    return randStr


def gen_japan_word_or_sequence():
    a = random.random()
    if a<0.05:
        randStr = faker.address()
        randStr = randStr[0:-3]
    elif 0.05 < a< 0.1:
        randStr = faker.first_kana_name_female()
        if random.random()<0.2:
            randStr = randStr[0]
    elif 0.1<a<0.2:
        randStr = faker.kana_name()
        if random.random()<0.2:
            randStr = randStr[0]
    elif 0.2<a<0.25:
        randStr = faker.kana_name_female()
        if random.random()<0.2:
            randStr = randStr[0]
    elif 0.25<a<0.3:
        randStr = faker.first_kana_name_male()
        if random.random()<0.2:
            randStr = randStr[0]
    elif 0.3<a<0.35:  
        randStr = faker.kana_name_male()
        if random.random()<0.2:
            randStr = randStr[0]
    elif 0.35<a<0.4:  
        randStr = faker.last_kana_name()
        if random.random()<0.2:
            randStr = randStr[0]
    elif 0.4<a<0.5:
        randStr = faker.first_kana_name()
        if random.random()<0.2:
            randStr = randStr[0]
    elif 0.5<a<0.6:
        randStr = faker.sentence(nb_words=10,variable_nb_words=True,ext_word_list=None)
    elif 0.6<a<0.7:
        randStr = faker.sentence(nb_words=6,variable_nb_words=True,ext_word_list=None)
    elif 0.8<a<0.9:
        randStr = faker.sentence(nb_words=15,variable_nb_words=True,ext_word_list=None) # 句子
    else:
        randStr = faker.sentence(nb_words=18,variable_nb_words=True,ext_word_list=None)

    return randStr


def _gen_korean_word_or_sequence():
    a = random.random()
    b = random.random()
    if a<0.2:
        if b < 0.5:
            randStr = faker.address()
        else:
            randStr = faker.address_detail() 
    elif 0.2<a<0.4:
        if b < 0.25:
            randStr = faker.borough()
        elif 0.25 < b < 0.5:
            randStr = faker.building_dong()
        elif 0.5 < b < 0.75:
            randStr = faker.building_name()
        else:
            randStr = faker.city()
        # randStr = faker.city_name()
    elif 0.4<a<0.6:
        if b < 0.25:
            randStr = faker.province()
        elif 0.25 < b < 0.5:
            randStr = faker.name()
        elif 0.5 < b < 0.75:
            randStr = faker.first_name() 
        else:
            randStr = faker.first_name_female()

    elif 0.6<a<0.8:  
        if b < 0.25:
            randStr = faker.street_address()
        elif 0.25 < b < 0.5:
            randStr = faker.street_name()
        elif 0.5 < b < 0.75:
            randStr = faker.road()
        else:
            randStr = faker.road_name()
        
    elif 0.8<a<1:
        if b < 0.25:
            randStr = faker.company()
        elif 0.25 < b < 0.5:
            randStr = faker.company_suffix() 
        elif 0.5 < b < 0.7:
            randStr = faker.first_name_male()
        elif 0.7 < b < 0.85:
            randStr = faker.last_name()
        else:
            randStr = faker.road_address()
    
    return randStr

def gen_korean_word_or_sequence():
    a = random.random()
    if a < 0.5:
        randStr = _gen_korean_word_or_sequence()
    elif 0.5<a<0.9:
        randStr = _gen_korean_word_or_sequence() + _gen_korean_word_or_sequence() # 10
    else:
        randStr = _gen_korean_word_or_sequence() + _gen_korean_word_or_sequence() + _gen_korean_word_or_sequence()
    if random.random()<0.2:
        randStr = randStr[0]
    return randStr

#------------
def load_dict(lang):
    """Read the dictionnary file and returns all words in it.

    trdg utils.py
    """

    lang_dict = []
    with open(
        os.path.join(dictsPath, lang + ".txt"),
        "r",
        encoding="utf8",
        errors="ignore",
    ) as d:
        lang_dict = [l for l in d.read().splitlines() if len(l) > 0]
    return lang_dict


def create_strings_from_dict(length, allow_variable, count, lang_dict):
    """
    trdg string_generator.py
        Create all strings by picking X random word in the dictionnary
    """

    dict_len = len(lang_dict)
    strings = []
    for _ in range(0, count):
        current_string = ""
        for _ in range(0, random.randint(1, length) if allow_variable else length):
            current_string += lang_dict[random.randrange(dict_len)]
            current_string += " "
        strings.append(current_string[:-1])
    return strings


def gen_word_or_sequence(lang="ar",count = 10000,lengthList=[1,5,10,15,20] ):
    israndom = True
    strList = []
    lang_dict = load_dict(lang)
    for length in lengthList:
        strings = create_strings_from_dict(
            length, israndom, count, lang_dict
        )
        strList.extend(strings)
    strList = [stri+"\n" for stri in strList]
    return strList


def main_multi_language():
    if language == "ar_AA":
        strList = gen_word_or_sequence(lang="ar",count = 10000,lengthList=[1,3,5,7,9,11,13] ) # 直接生成
    elif language == "bn_BD":
        strList = gen_word_or_sequence(lang="bn",count = 10000,lengthList=[1,5,7,9,11] ) # 直接生成
    elif language == "hi_IN":
        strList = gen_word_or_sequence(lang="hi",count = 10000,lengthList=[1,5,7,9,11] ) # 直接生成
    else:
        strList = []
        n = 50000

        for i in range(n):
            if language == "zh_CN":
                iStr = gen_chinese_word_or_sequence()
            elif language == "ja_JP":
                iStr = gen_japan_word_or_sequence()
            elif language == "ko_KR":
                iStr = gen_korean_word_or_sequence()
            print(iStr)
            if iStr == "":
                continue
            if len(iStr)>50:
                continue

            if iStr.endswith("."):
                iStr = iStr.strip(".")
            if iStr.endswith("。"):
                iStr = iStr.strip("。")
            iStr += "\n"

            strList.append(iStr)

    corpusPath = os.path.join(resourcesPath,"corpus","{lang}corpus.txt".format(lang=langDict[language]))
    with open(corpusPath,"a",encoding="utf-8") as f:
        f.writelines(strList)

def __main():
    main_multi_language()

if __name__ == "__main__":
    __main()

