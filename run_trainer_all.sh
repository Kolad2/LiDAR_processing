#!/bin/bash


for i in {17..20}
do
  DATA_PATH="/home/ubuntu/Projects/LiDAR_processing/data/nerfstudio/Horga4_"$i
  OPTIONS="--viewer.quit-on-train-completion True"
  ns-train nerfacto --data $DATA_PATH $OPTIONS
done

#
# ns-train nerfacto --data $DATA_PATH --load-dir $CHECKPOINT_PATH $OPTIONS
