#!/bin/sh
#####################################################
#@音频接口左声道测试
#@author:GUOLeiLei
#@blog:https://blog.csdn.net/rong11417
#@mail:1040446144@qq.com
#
#######################################################
externpath=$1
flags=$2 #二级标识
logname=$3 #统一存放log的log名
tablename=$4 #数据库表名
insertsql=$5 #插入数据语句
path=$(pwd) #qt运行的路径
echo "this path is "$path >> ${path}/log/${logname}.log
echo $flags  #打印的信息
echo "flags:"$flags >> ${path}/log/${logname}.log
starttime1=$(date "+%Y-%m-%d/%H-%M-%S")
starttime=$(date "+%Y-%m-%d %H:%M:%S")
echo "starttime="${starttime}
echo "starttime="${starttime} >> ${path}/log/${logname}.log
mplayer ${path}${externpath}left.mp3 -af volume=10
endtime1=$(date "+%Y-%m-%d/%H-%M-%S")
endtime=$(date "+%Y-%m-%d %H:%M:%S")
echo "endtime="${endtime}
echo "endtime="${endtime} >> ${path}/log/${logname}.log
start=`date +%s -d "${starttime}"`
end=`date +%s -d "${endtime}"`
usetime_sec=$(($end-$start))
echo "usetime_sec:"${usetime_sec}
echo "usetime_sec:"${usetime_sec} >> ${path}/log/${logname}.log
sed -i '/'${flags}'/c #:'${flags}':'${starttime1}':'${endtime1}':'${usetime_sec}':TEST:NOPASS' ${path}/configure/teststatus.ini
echo "sed ok"
echo "sed ok" >> ${path}/log/${logname}.log

chmod +x ${path}${externpath}insertaudio.py 
python ${path}${externpath}insertaudio.py 
echo "python mysql insert into "${tablename}
echo "python mysql insert into "${tablename} >> ${path}/log/${logname}.log
