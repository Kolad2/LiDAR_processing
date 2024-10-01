#!/bin/bash


DATA_PATH="/home/ubuntu/Projects/LiDAR_processing/data/nerfstudio/Horga4_2"
CHECKPOINT_PATH="outputs/Horga4_0/nerfacto/2024-09-30_181704/nerfstudio_models"
OPTIONS="--viewer.quit-on-train-completion True"



# ns-train nerfacto --data $DATA_PATH $OPTIONS
# ns-train nerfacto --data $DATA_PATH --load-dir $CHECKPOINT_PATH $OPTIONS
