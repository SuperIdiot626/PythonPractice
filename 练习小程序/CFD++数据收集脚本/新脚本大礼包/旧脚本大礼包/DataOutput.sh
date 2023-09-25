#!/bin/sh
#func
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