#!/bin/bash

DATA_NAME="Horga5"

for i in {0..20}
do
  DATA_PATH="./data/nerfstudio/"$DATA_NAME"/"$DATA_NAME"_"$i
  OUTPUT_DIR="outputs/"$DATA_NAME
  OPTIONS="--viewer.quit-on-train-completion True --output-dir "$OUTPUT_DIR
  ns-train nerfacto --data $DATA_PATH $OPTIONS
done

