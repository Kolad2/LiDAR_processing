readme file

Обновление модулей впервые
```
git submodule update --init --recursive
```

```
sudo apt install ffmpeg
```

```
conda create --name nerfstudio -y python=3.8
conda activate nerfstudio
pip install --upgrade pip
```

```
pip install torch==2.1.2+cu118 torchvision==0.16.2+cu118 --extra-index-url https://download.pytorch.org/whl/cu118
conda install -c "nvidia/label/cuda-11.8.0" cuda-toolkit
pip install ninja
```
The most hard to execute.
```
pip install git+https://github.com/NVlabs/tiny-cuda-nn/#subdirectory=bindings/torch
```
tiny-cuda-nn supports only gcc-11 compiler use if you cant install
```
sudo apt install gcc-11 g++-11
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 60
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-11 60
```

```
pip install --upgrade pip setuptools
cd nerfstudio
pip install -e . #устанавливает пакет в ваше текущее окружение в режиме разработки.
```


git submodule update --init --recursive


# cli
## Test Data
Download Data
```
ns-download-data nerfstudio --capture-name=poster
```

Train model
```
ns-train nerfacto --data data/nerfstudio/poster
```




