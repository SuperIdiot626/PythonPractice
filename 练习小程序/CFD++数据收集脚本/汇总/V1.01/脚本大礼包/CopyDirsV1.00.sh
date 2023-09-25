#/bin/bash
read -p "Please input your file name: " name
read -p "Please input times you want: " num

echo "starttime: `date +"%Y-%m-%d %H:%M:%S"`"
for((i=1;i<=num;i++))
do
   cp -r $name $i
   echo "$i done `date +"%Y-%m-%d %H:%M:%S"`"
done
echo "All done, $name has been copied $num times"
