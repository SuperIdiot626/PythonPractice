import os
stringPart1=r'''#! /bin/bash
##the value of -q option can be long or verylong or priv
'''

stringPart2=r'''
#PBS -q batch
#PBS -j oe
#
ulimit -s unlimited
#
cd $PBS_O_WORKDIR
#
NPROCS=`cat $PBS_NODEFILE|wc -l`

export MPI_ROOT=/public/METACOMP/hpmpi
export PATH=$MPI_ROOT/bin:$PATH
. /public/METACOMP/mcfdenv.sh


#
cat $PBS_NODEFILE >>ma
rm mpi_init.log -rf
/public/METACOMP/mlib/mcfd.14.1/exec/tometis pmetis ${NPROCS} >>mpi_init.log
#
echo "start at  `date +'%F %k:%M:%S'`"
#
mpirun -ibv -hostfile $PBS_NODEFILE -np ${NPROCS} hpmpimcfd>output 2>&1
#
echo "finish at  `date +'%F %k:%M:%S'`"
'''
dire='H:\\0610\\0613\\'
node_num=12
node_num_flag=0
i=1
while(i<=40):
    file=open(dire+str(i)+'\\job1.cfd','w')
    print('file name is '+str(i)+'job1.cfd')
    file.write(stringPart1)
    file.write('#PBS -N '+str(i))
    file.write('\n')
    file.write('#PBS -l nodes=node'+str(node_num)+':ppn=48')
    file.write(stringPart2)
    i=i+1
    node_num_flag=node_num_flag+1
    if node_num_flag%2==0 and node_num_flag>0:
        node_num=node_num+1
    file.close()
