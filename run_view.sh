#!/bin/bash



DATA_NAME="Horga5"
number=0

MODEL_PATH="outputs/"$DATA_NAME"/"$DATA_NAME"_"$number
#MODEL_PATH="./outputs/poster/nerfacto/2024-10-07_162639/nerfstudio_models"


config_path=$(find $MODEL_PATH -type f -name "*.yml" -print -quit)
ns-viewer --load-config $config_path


