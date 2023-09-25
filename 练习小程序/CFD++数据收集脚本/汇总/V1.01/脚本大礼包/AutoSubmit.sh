#!/bin/sh
#func
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
