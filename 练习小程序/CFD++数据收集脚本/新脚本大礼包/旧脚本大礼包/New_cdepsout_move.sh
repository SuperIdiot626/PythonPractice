#/bin/bash
read -p "Please input where files from: " dir1
read -p "Please input where files go: " dir2

cd /$dir1
dir1=$dir1$"/"
echo "starttime: `date +"%Y-%m-%d %H:%M:%S"`"

num=0

for x in $(ls -F | grep '/$')
do
	echo $"from  "$dir1$x$"  to  "$dir2$"/"$x
	cp -r $dir1$x$"new_cdepsout.bin"  $dir2$"/"$x$"cdepsout.bin"
	let num=num+1
done

echo "All done, files in $dir1 has been copied $num times"