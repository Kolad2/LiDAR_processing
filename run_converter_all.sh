#!/bin/bash




for i in {3..20}
do
  OUTPUT_PATH="/home/ubuntu/Projects/LiDAR_processing/data/nerfstudio/Horga4_"$i
  POLYCAM_ZIP="/home/ubuntu/Projects/LiDAR_processing/data/polycam/Horga4/Horga4_"$i".zip"
  ns-process-data polycam --data $POLYCAM_ZIP --output-dir $OUTPUT_PATH
done


