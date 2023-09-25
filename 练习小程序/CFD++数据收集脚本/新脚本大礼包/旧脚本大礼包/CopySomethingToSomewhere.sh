#/bin/bash
read -p "Please input where files are in: " dir1
read -p "Please input where files go: " dir2
cd /$dir2
dir1=$dir1$"/*"
echo "starttime: `date +"%Y-%m-%d %H:%M:%S"`"

num=0
for x in $(ls -F | grep '/$')
do
	echo $dir2$"/"$x
	cp -r $dir1  $dir2$"/"$x
	let num=num+1
done

echo "All done, files in $dir1 has been copied $num times"