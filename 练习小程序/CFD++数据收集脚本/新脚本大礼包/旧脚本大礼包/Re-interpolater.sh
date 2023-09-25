#!/bin/sh
#func
myfunc(){
	for x in $(ls -F | grep '/$')
	do
		cd "$x";
		echo "$x"
		reintsom new_cellsin.bin new_nodesin.bin new_cdepsout.bin cdepsout.bin 1
		cd ..
	done
}
myfunc
