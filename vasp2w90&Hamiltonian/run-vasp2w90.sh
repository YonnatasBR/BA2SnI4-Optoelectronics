#!/bin/bash
#PBS -N  mhp-w90
#PBS -e  job-opt.err
#PBS -o  job-opt.o
#PBS -q  workq 
#PBS -l nodes=salpeter-08:ppn=32

module load vasp-5
module load vasp-pp

ulimit -s unlimited

export I_MPI_FABRICS=shm

cd $PBS_O_WORKDIR

mpirun -np $NCPUS vasp_ncl > scf.out
