#!/bin/sh
#func
myfunc() {
	for x in $(ls -F | grep '/$')
		do
			cd "$x";
			echo "$x"
			infout1r
			cd ..
		done
}
myfunc