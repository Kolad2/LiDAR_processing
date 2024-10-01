#!/bin/bash

#MODEL_PATH="./outputs/Horga4/Horga4_0/nerfacto/2024-09-30_181704/config.yml"
MODEL_PATH="./outputs/Horga4/Horga4_0/nerfacto/2024-09-30_181704/config.yml"
CHECKPOINT_PATH="./outputs/Horga4/Horga4_0/nerfacto/2024-09-30_181704/nerfstudio_models"

DATA_NAME="Horga5"
number=0

MODEL_PATH="outputs/"$DATA_NAME"/"$DATA_NAME"_"$number

config_path=$(find $MODEL_PATH -type f -name "*.yml" -print -quit)
ns-viewer --load-config $config_path


