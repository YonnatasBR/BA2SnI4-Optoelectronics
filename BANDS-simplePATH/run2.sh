#!/bin/bash
#PBS -N  BANDS
#PBS -e  job.err
#PBS -o  job.o
#PBS -q  workq
#PBS -l nodes=salpeter-04:ppn=32

module load vasp-5
module load vasp-pp

ulimit -s unlimited

export I_MPI_FABRICS=shm

cd $PBS_O_WORKDIR

cp INCAR2 INCAR

cp KPOINTS2 KPOINTS

mpirun -np $NCPUS vasp_ncl > scf.out
