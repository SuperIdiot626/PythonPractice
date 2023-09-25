#!/bin/sh
#func
echo "You are now using 3 in 1 output."
read -p "Please input where cases in: " dir1
cd $dir1

myfunc() {
	for x in $(ls -F | grep '/$')
		do
			cd "$x";
			echo "$x"
			genplif tecplotb <tecout.inp
			surftec < tecout.inp
			infout1r
			cd ..
		done
}
myfunc