#!/bin/bash
#utf-8
# Author: xxx
# Version: 0.2.1
# Date  : 2012.12.12
# Usage : log delete
##############################################################################################
#获取当天日期
DATE=` date +"%Y-%m-%d %H:%M:%S"`
DAY=`date +%Y%m%d`
echo $DATE
echo $DAY

#清理以下目录的所有的7天之前文件的所有文件（不能删除的文件请不要放在logs目录，有专门的/export/Data/存放数据）
#新应用log
PATHS1=/export/Logs/
#老应用log
PATHS2=/export/home/tomcat/logs/
#新实例log
PATHS3=/export/Domains/*/logs/
PATHS8=/export/Domains/*/*/logs/
#老实例log
PATHS4=/export/home/tomcat/domains/*/logs/
PATHS9=/export/home/tomcat/domains/*/*/logs/
#apache log
PATHS5=/export/servers/apache2/logs/
#nginx log
PATHS6=/export/servers/nginx/logs/
#回收站
PATHS7=/export/.trash/
#删除脚本log
LOG_SELF=/export/Logs/logdelete/del.log
#检查log目录及文件是否存在
if [ -e ${LOG_SELF} ]
    then
    echo  "file exsit,pass" 

else
    echo "${LOG_SELF} dose not exsit.and touch it"
    mkdir -p  /export/Logs/logdelete  && touch /export/Logs/logdelete/del.log
fi

#reassgin stdout,stderr
exec 6>&1
exec >>${LOG_SELF} 2>&1

#时间戳分割线
echo $DATE ==============================================================

#删除规则：保留七天内的log文件，如果7天内的文件单个大小超过2G大小将被重定向为空

OTHER_LOG="$PATHS1 $PATHS2  $PATHS5 $PATHS6"
CATALINA_LOG="$PATHS3 $PATHS4 $PATHS8 $PATHS9"
ALL_LOG="$PATHS1 $PATHS2 $PATHS3 $PATHS4 $PATHS5 $PATHS6 $PATHS7 $PATHS8 $PATHS9"
#回收站清理
#find $PATHS7 -mtime +3 -print -exec ls -l
find PATHS7 -mtime +3 -print -exec /bin/rm -fr {} \;


#应用log和nginx apache log清理
for i in $OTHER_LOG
do
echo $DATE -------------------------------------------------
echo $i

#找到7天之前的文件除去目录
#检查用删除将换成下一行
#find $i \( -path '*deploy*' -o -path '*loghub*' -o -path '*ump*' -o -path '*UMP*' \) -a -prune -o -mtime +7 ! -type d ! -type l ! -name *.pid ! -name access.log ! -name error.log -print -exec ls -l {} \;
find $i \( -path '*deploy*' -o -path '*loghub*' -o -path '*ump*' -o -path '*UMP*' \) -a -prune -o -mtime +7 ! -type d ! -type l ! -name *.pid ! -name access.log ! -name error.log -print -exec /bin/rm -f {} \;

echo $DATE -------------------------------------------------
#找到大于2G的文件,除去当天和前一天生成的（考虑刚过凌晨前一天文件只是几小时前执行）
#检查用清空需换成下一行
#find $i \( -path '*deploy*' -o -path '*loghub*' -o -path '*ump*' -o -path '*UMP*' \) -a -prune -o ! -type d ! -type l -mtime +1 -size +2G -print -exec ls -l {} \;
find $i \( -path '*deploy*' -o -path '*loghub*' -o -path '*ump*' -o -path '*UMP*' \) -a -prune -o ! -type d ! -type l -mtime +1 -size +2G -print -exec  sh -c "> {}" \;
done



#应用log和nginx apache log清理
#tomcat log目录过滤掉软连接，因为过滤其他配置文件，只删除大于1MB的log
for j in $CATALINA_LOG
do
echo $DATE -------------------------------------------------
echo $j
#找到7天之前的文件除去目录
#检查用删除将换成下一行
#find $j -mtime +7 ! -type d ! -type l -size +1M -print -exec ls -l {} \;
find $j -mtime +7 ! -type d ! -type l -size +1M -print -exec /bin/rm -f {} \;

echo $DATE -------------------------------------------------
#找到大于2G的文件,除去当天和前一天生成的（考虑刚过凌晨前一天文件只是几小时前）
#检查用清空需换成下一行
#find $j ! -type d ! -type l -mtime +1 -size +2G -print -exec ls -l {} \;
find $j ! -type d ! -type l -mtime +1 -size +500M -print -exec  sh -c "> {}" \;
done


#清理单个文件大于50G
for k in $ALL_LOG
do
echo $DATE ================================
echo $k

#找到大于20G的文件指空,包括当天（20G了留着也没用了，拿出来也没法看）
#find $k ! -type d ! -type l -size +20G -print -exec ls -l {} \;
find $k ! -type d ! -type l -size +5G -print -exec  sh -c "> {}" \;
done

exec 1>&6 6>&-
