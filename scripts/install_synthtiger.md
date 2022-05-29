# docker
docker pull fnndsc/ubuntu-python3:18.04

apt install git -y

cd /opt

git clone https://github.com/songyanyi/synthtiger.git

下载 whl opencv
https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/opencv-python/

libraqm 安装
set -euxo pipefail
apt install -y \
    libtiff5-dev \
    libjpeg8-dev \
    libopenjp2-7-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    tcl8.6-dev \
    tk8.6-dev \
    python3-tk \
    libharfbuzz-dev \
    libfribidi-dev \
    libxcb1-dev

pip install opencv_python..


pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/



synthtiger 添加到搜索路径
export PYTHONPATH=$PYTHONPATH:/opt/synthtiger


运行 script_corpus_gen.py 在 resource/corpus 中生成 chinesecorpus.txt

trdg 中的中文字体移动到 font 




