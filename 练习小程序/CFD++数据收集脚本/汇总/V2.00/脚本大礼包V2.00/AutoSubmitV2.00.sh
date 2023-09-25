#!/bin/sh
#func
echo "You are now using Asuto Subimt Script."
read -p "Please input where cases in: " dir1
cd $dir1

myfunc(){
	for x in $(ls -F | grep '/$')
	do
		cd "$x";
		echo "$x"
		qsub job1.cfd		
		cd ..
	done			
}
myfunc
