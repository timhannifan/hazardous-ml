#!/bin/bash          
if [ -n "$1" ]; 
then
  LOAD="--load_file $1"
  echo "Load file $1"
else
  LOAD=""
  echo "Using default load file"
fi

echo "removing log"
rm runtime.log

# Data Loading
echo  "Limit 100"
python3 driver.py --load 100
echo  "Limit 1000"
python3 driver.py --load 1000
echo "Limit 10K"
python3 driver.py --load 10000