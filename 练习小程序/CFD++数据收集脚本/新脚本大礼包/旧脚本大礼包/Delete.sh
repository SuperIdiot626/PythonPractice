#/bin/bash
read -p "Please input the start jobID:" num1
read -p "Please input the end   jobID:" num2


for x in $(seq $num1 $num2)
do
	qdel $x
	echo "jobID "$x" deleted "
done

