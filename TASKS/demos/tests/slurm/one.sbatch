#!/bin/bash
#
# add all other SBATCH directives here...
#
#SBATCH -p general
#SBATCH -n 1 # Number of cores
#SBATCH -N 1 # Ensure that all cores are on one machine
#SBATCH --mem=1000
#SBATCH -t 1:00

# we are working
RUNNING="echo $args"
echo $RUNNING
time $RUNNING

# end of program
exit 0;
