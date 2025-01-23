#!/bin/bash
#PBS -N  mhp-w90
#PBS -e  job-opt.err
#PBS -o  job-opt.o
#PBS -q  workq 
#PBS -l nodes=salpeter-08:ppn=1

module load wannier90

ulimit -s unlimited

export I_MPI_FABRICS=shm

cd $PBS_O_WORKDIR

wannier90.x wannier90
