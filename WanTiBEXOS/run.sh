#!/bin/bash
#PBS -N  pk-wtb
#PBS -e  job-opt.err
#PBS -o  job-opt.o
#PBS -q  workq 
#PBS -l nodes=salpeter-02:ppn=56

module load wtb

ulimit -s unlimited

export OMP_NUM_THREADS=$NCPUS

export I_MPI_FABRICS=shm

export KMP_STACKSIZE=10gb

cd $PBS_O_WORKDIR

wtb.x < input_bands.dat

wtb.x < input_dos.dat

wtb.x < input_opts.dat

wtb.x < input_exc.dat

wtb.x < input_PCE.dat

