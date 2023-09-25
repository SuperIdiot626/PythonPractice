#/bin/bash
read -p "Please input where  file in: " dir1
read -p "Please input your file name: " name
read -p "Please input times you want: " num
cd $dir1

echo "starttime: `date +"%Y-%m-%d %H:%M:%S"`"
for i in  $(seq 1 1 $num)
do
   cp -r $name $i
   echo "$i done `date +"%Y-%m-%d %H:%M:%S"`"
   ((i=i+1))
done
echo "All done, $name has been copied $num times"