#!/bin/bash
#PBS -N  DOS 
#PBS -e  job.err
#PBS -o  job.o
#PBS -q  workq
#PBS -l nodes=salpeter-06:ppn=64

module load vasp-5
module load vasp-pp

ulimit -s unlimited

export I_MPI_FABRICS=shm
export I_MPI_HYDRA_TOPOLIB=ipl

cd $PBS_O_WORKDIR

mpirun -np $NCPUS vasp_ncl > scf.out
