#!/bin/sh
#func
echo "You are now using ProbeFilters Script."
read -p "Please input where cases in: " dir1
cd $dir1

myfunc(){
	for x in $(ls -F | grep '/$')
	do
		cd "$x";
		echo "$x"
		infout1r		
		cd ..
	done			
}
myfunc
