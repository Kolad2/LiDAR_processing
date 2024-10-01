#!/bin/bash


DATA_NAME="Horga5"

for i in {0..20}
do
  POLYCAM_ZIP="./data/polycam/"$DATA_NAME"/"$DATA_NAME"_"$i".zip"
  OUTPUT_PATH="./data/nerfstudio/"$DATA_NAME"/"$DATA_NAME"_"$i
  ns-process-data polycam --data $POLYCAM_ZIP --output-dir $OUTPUT_PATH
done


