readme file
pip install torch==2.1.2+cu118 torchvision==0.16.2+cu118 --extra-index-url https://download.pytorch.org/whl/cu118


Download Data\
ns-download-data nerfstudio --capture-name=poster

Train model
ns-train nerfacto --data data/nerfstudio/poster


pip install ninja git+https://github.com/NVlabs/tiny-cuda-nn/#subdirectory=bindings/torch
pip install --upgrade pip setuptools
pip install -e .