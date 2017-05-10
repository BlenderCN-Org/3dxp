#!/bin/bash

# Starting from step 0
export WORKING_DIR="/n/coxfs01/thejohnhoffer/2017/3dxp/getmesh"
ROOT_IN="/n/coxfs01/thejohnhoffer/R0/2017_05_10_844z/pngs/"
IDS_JSON="/n/coxfs01/leek/results/2017-05-05_R0/boss/boss.json"
RAW_JSON="/n/coxfs01/leek/dropbox/25k_201610_dataset_em.json"
IDS_PNG=$ROOT_IN"/3200_3200_ids"
RAW_PNG=$ROOT_IN"/1600_1600_raw"
export IDS_DOWNSAMPLE_XY=3
export IDS_DOWNSAMPLE_Z=2
export RAW_DOWNSAMPLE_XY=4
export RAW_DOWNSAMPLE_Z=2
export PNG_RUNS=80

# Starting from step 1
IDS_H5=$ROOT_IN"/3200_3200_ids.h5"
RAW_H5=$ROOT_IN"/1600_1600_raw.h5"

# Starting from step 2
export BLOCK_COUNTS="8"
BLOCK_RUNS=$((BLOCK_COUNTS**3))
ROOT_OUT="/n/coxfs01/thejohnhoffer/R0/2017_05_10_844z/meshes/"

# Starting from step 3
export NUMBER_TOP="20"
export RANK_Z="1"

# Starting from step 4
WWW_IN="/n/coxfs01/thejohnhoffer/2017/3dxp/X3DOM/www"

# Load the virtual environment
source new-modules.sh
module load python/2.7.11-fasrc01
conda create -n h5_tile --clone="$PYTHON_HOME"
source activate h5_tile
# Build the virtual environment
conda remove scikit-image
pip install scikit-image
pip install --upgrade h5py
pip install --upgrade numpy
pip install --upgrade scipy
pip install --upgrade mahotas
pip install --upgrade tifffile
pip install --upgrade numpy-stl
pip install --upgrade opencv-python

# Make important directories
mkdir -p $ROOT_IN
mkdir -p $ROOT_OUT

# Run one of the steps
case "$1" in

0) sbatch -o /n/coxfs01/thejohnhoffer/tiff_lists/ids_%a.out -e /n/coxfs01/thejohnhoffer/tiff_lists/ids_%a.err --export=WORKING_DIR=$WORKING_DIR,N_DOWNSAMPLE_XY=$IDS_DOWNSAMPLE_XY,N_DOWNSAMPLE_Z=$IDS_DOWNSAMPLE_Z,PNG_RUNS=$PNG_RUNS,IN_JSON=$IDS_JSON,OUT_PNG=$IDS_PNG --array=0-$((PNG_RUNS - 1)) scale_png.sbatch
   sbatch -o /n/coxfs01/thejohnhoffer/tiff_lists/raw_%a.out -e /n/coxfs01/thejohnhoffer/tiff_lists/raw_%a.err --export=WORKING_DIR=$WORKING_DIR,N_DOWNSAMPLE_XY=$RAW_DOWNSAMPLE_XY,N_DOWNSAMPLE_Z=$RAW_DOWNSAMPLE_Z,PNG_RUNS=$PNG_RUNS,IN_JSON=$RAW_JSON,OUT_PNG=$RAW_PNG --array=0-$((PNG_RUNS - 1)) scale_png.sbatch
   ;;

1) python png2hd.py $RAW_PNG $RAW_H5
   python png2hd.py -c $IDS_PNG $IDS_H5
   ;;

2) python all_counts.py -b $BLOCK_COUNTS $IDS_H5 $ROOT_OUT
   ;;

3) sbatch --export=WORKING_DIR=$WORKING_DIR,RANK_Z=$RANK_Z,NUMBER_TOP=$NUMBER_TOP,BLOCK_COUNTS=$BLOCK_COUNTS,IDS_H5=$IDS_H5,ROOT_OUT=$ROOT_OUT --array=0-$((BLOCK_RUNS - 1)) all_stl.sbatch
   ;;

4) sbatch --export=WORKING_DIR=$WORKING_DIR,RANK_Z=$RANK_Z,NUMBER_TOP=$NUMBER_TOP,WWW_IN=$WWW_IN,RAW_H5=$RAW_H5,RAW_PNG=$RAW_PNG,ROOT_OUT=$ROOT_OUT --array=0-$((NUMBER_TOP - 1)) all_x3d.sbatch
   ;;

*) python all_index.py $ROOT_OUT
   ;;

esac
