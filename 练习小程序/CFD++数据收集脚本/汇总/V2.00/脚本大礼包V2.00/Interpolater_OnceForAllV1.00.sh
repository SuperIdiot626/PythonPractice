#/bin/bash
read -p "Please input where CAE Files in: " dir1
read -p "Please input the CAE  Dir  Name: " dir_cae
read -p "Please input where Old Cases in: " dir2
cd $dir2

echo "starttime: `date +"%Y-%m-%d %H:%M:%S"`"


for x in $(ls -F | grep '/$')
do
	#复制过去并命名为new_**
	cp -r $dir1"/""cellsin.bin"  $dir2"/"$x"new_cellsin.bin"
	cp -r $dir1"/""nodesin.bin"  $dir2"/"$x"new_nodesin.bin"
	
	cd $dir2"/"$x
	#进行插值
	reintsom new_cellsin.bin new_nodesin.bin new_cdepsout.bin cdepsout.bin 1
	
	
	#将插值结果复制回某指定更目录，并新建一个文件夹，与x保持一致
	#复制回的文件也去掉new_的前缀
	cd $dir1
	cd ".."
	dir3=$(pwd)
	
	#复制原本的CAE文件，并将插值结果复制进去
	cp -r $dir3"/"$dir_cae  $dir3"/"$x
	
	
	cp -r $dir2"/"$x"new_cdepsout.bin"  $dir3"/"$x"cdepsout.bin"
	echo "time: `date +"%Y-%m-%d %H:%M:%S"`"
	echo $dir2"/"$x

done

echo "All done, files in $dir1 has been copied  times"