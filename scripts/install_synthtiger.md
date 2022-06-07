# docker
docker pull fnndsc/ubuntu-python3:18.04


# 
activate textgen
cd /d F:\Project\docpartner\core\textocr\datahelper\datagen\synthtiger

下载 whl opencv and pillow
https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/opencv-python/

pip install opencv_python..



python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/


libraqm 安装


synthtiger 添加到搜索路径
export PYTHONPATH=$PYTHONPATH:/opt/synthtiger


运行corpus.py 在 resource corpus 中生成 chinesecorpus.txt

trdg中的中文字体移动到 font 


# 
activate textgen
cd /d F:\Project\docpartner\core\textocr\datahelper\datagen\synthtiger

python synthtiger/main.py -o results/cn -c 100 -w 10 -v examples/my/template.py SynthTiger examples/my/config_horizontal.yaml

python synthtiger/main.py -o results/en -c 100 -w 10 -v examples/synthtiger/template.py SynthTiger examples/synthtiger/config_horizontal.yaml


