#!/bin/bash


OUTPUT_PATH="/home/ubuntu/Projects/LiDAR_processing/data/nerfstudio/Horga4_2"
POLYCAM_ZIP="/home/ubuntu/Projects/LiDAR_processing/data/polycam/Horga4/Horga4_2.zip"

ns-process-data polycam --data $POLYCAM_ZIP --output-dir $OUTPUT_PATH
