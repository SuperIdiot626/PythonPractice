#!/bin/sh
#func
echo "You are now using FlowField Output."
read -p "Please input where cases in: " dir1
cd $dir1

myfunc(){
	for x in $(ls -F | grep '/$')
	do
		cd "$x";
		echo "$x"
		genplif tecplotb <tecout.inp
		surftec < tecout.inp
		cd ..
	done			
}
myfunc
