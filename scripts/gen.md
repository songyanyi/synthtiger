export PYTHONPATH=$PYTHONPATH:/opt/synthtiger
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

# 复制到宿主机
docker cp -a cf8056fa736a:/opt/synthtiger/results F:\Project\docpartner\core\textocr\dataset\synthtiger
docker cp -a cf8056fa736a:/opt/synthtiger/results/en/images F:\Project\docpartner\core\textocr\dataset\synthtiger\en\images