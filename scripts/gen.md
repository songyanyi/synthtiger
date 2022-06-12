# 
先用 lang_corpus_gen.py 生成某种语言的语料。（如果需要，添加 dicts，copy自trdg）

再在 resources / font 中添加该语言的字体。copy 自 trdg

# 打开 docker

# 打开 容器

# 打开 vscode ssh
# 

export PYTHONPATH=$PYTHONPATH:/opt/synthtiger

# 
修改 config.yaml 中的 language
corpus
max_length
font

base_font.py

# gen chinese

cd /opt/synthtiger
5w 横向，要设置字符长度 config_horizontal.yaml 

python synthtiger/main.py -o results/cn -c 50000 -w 30 -v examples/chinese/template.py SynthTiger examples/chinese/config_horizontal.yaml


1w 竖向，要设置字符长度
python synthtiger/main.py -o results/cn -c 10000 -w 30 -v examples/chinese/template.py SynthTiger examples/chinese/config_vertical.yaml


# gen english
5w 横向，要设置字符长度
设置fonts

python synthtiger/main.py -o results/en -c 50000 -w 30 -v examples/english/template.py SynthTiger examples/english/config_horizontal.yaml

1w 竖向，要设置字符长度
python synthtiger/main.py -o results/en -c 10000 -w 30 -v examples/english/template.py SynthTiger examples/english/config_vertical.yaml


# gen arabic

cd /opt/synthtiger
5w 横向，要设置字符长度 config_horizontal.yaml 

python synthtiger/main.py -o results/ar -c 50000 -w 30 -v examples/arabic/template.py SynthTiger examples/arabic/config_horizontal.yaml


1w 竖向，要设置字符长度
python synthtiger/main.py -o results/ar -c 10000 -w 30 -v examples/arabic/template.py SynthTiger examples/arabic/config_vertical.yaml

# gen bangla

cd /opt/synthtiger
5w 横向，要设置字符长度 config_horizontal.yaml 

python synthtiger/main.py -o results/bn -c 50000 -w 30 -v examples/bangla/template.py SynthTiger examples/bangla/config_horizontal.yaml


1w 竖向，要设置字符长度
python synthtiger/main.py -o results/bn -c 10000 -w 30 -v examples/bangla/template.py SynthTiger examples/bangla/config_vertical.yaml

# gen hindi

cd /opt/synthtiger
5w 横向，要设置字符长度 config_horizontal.yaml 

python synthtiger/main.py -o results/hi -c 50000 -w 30 -v examples/hindi/template.py SynthTiger examples/hindi/config_horizontal.yaml


1w 竖向，要设置字符长度
python synthtiger/main.py -o results/hi -c 10000 -w 30 -v examples/hindi/template.py SynthTiger examples/hindi/config_vertical.yaml


# gen japanese

cd /opt/synthtiger
5w 横向，要设置字符长度 config_horizontal.yaml 

python synthtiger/main.py -o results/ja -c 50000 -w 30 -v examples/japanese/template.py SynthTiger examples/japanese/config_horizontal.yaml


1w 竖向，要设置字符长度
python synthtiger/main.py -o results/ja -c 10000 -w 30 -v examples/japanese/template.py SynthTiger examples/japanese/config_vertical.yaml

# gen korean

cd /opt/synthtiger
5w 横向，要设置字符长度 config_horizontal.yaml 

python synthtiger/main.py -o results/ko -c 50000 -w 30 -v examples/korean/template.py SynthTiger examples/korean/config_horizontal.yaml


1w 竖向，要设置字符长度
python synthtiger/main.py -o results/ko -c 10000 -w 30 -v examples/korean/template.py SynthTiger examples/korean/config_vertical.yaml



# 复制到宿主机
docker cp -a cf8056fa736a:/opt/synthtiger/results F:\Project\docpartner\core\textocr\dataset\synthtiger
docker cp -a cf8056fa736a:/opt/synthtiger/results/en/images F:\Project\docpartner\core\textocr\dataset\synthtiger\en\images

docker cp -a cf8056fa736a:/opt/synthtiger/results/ja F:\Project\docpartner\core\textocr\dataset\synthtiger\ja
docker cp -a cf8056fa736a:/opt/synthtiger/results/ko F:\Project\docpartner\core\textocr\dataset\synthtiger\ko
docker cp -a cf8056fa736a:/opt/synthtiger/results/ar F:\Project\docpartner\core\textocr\dataset\synthtiger\ar
docker cp -a cf8056fa736a:/opt/synthtiger/results/bn F:\Project\docpartner\core\textocr\dataset\synthtiger\bn
docker cp -a cf8056fa736a:/opt/synthtiger/results/hi F:\Project\docpartner\core\textocr\dataset\synthtiger\hi