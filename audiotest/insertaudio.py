#!/usr/bin/python
# -*- coding: UTF-8 -*-
#####################################################
#@导入MYSQL数据库
#@author:GUOLeiLei
#@blog:https://blog.csdn.net/rong11417
#@mail:1040446144@qq.com
#
#######################################################
import MySQLdb
import sys,commands,time
path=commands.getoutput(('pwd'))
tablename=sys.argv[1]
read_goodsid=open(path+"/src/items/python_mysql/ini/goodsid.m","r")
goodsid_line = read_goodsid.readlines()
goodsid= goodsid_line[0]
goodsid=goodsid.strip()
read_goodsid.close()
print("goodsid:"+str(goodsid))
read_txt = open(path + "/configure/teststatus.ini","r")
read_line = read_txt.readlines()
read_frontL= read_line[0]
start_datetime=read_frontL.split(':')[2]
read_frontR=read_line[1]
read_frontM=read_line[2]
read_frontIN=read_line[3]
read_rearL=read_line[4]
read_rearR=read_line[5]
read_rearM=read_line[6]
read_rearIN=read_line[7]
end_datetime=read_rearIN.split(':')[3]
result=[read_frontL,read_frontR,read_frontM,read_frontIN,read_rearL,read_rearR,read_rearM,read_rearIN]
read_txt.close()
i=0
description=" "
res=''
for n in range(0,8):
  result[n]=result[n].split(':')[6]
  print("result["+ str(n)+"]:"+ str(result[n]))
  if result[n] == 'PASS':
    i+=1
if i == 8:
  res="PASS"
else:
  res="NOPASS"
sql1="insert into sys_items_audio values(0,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" %  (str(goodsid),str(result[0]),str(result[1]),str(result[2]),str(result[3]),str(result[4]),str(result[5]),str(result[6]),str(result[7]),str(res),str(description),str(start_datetime),str(end_datetime)) 
print("sql1:"+sql1)
db = MySQLdb.connect("localhost","root","100trust","computer_test",charset='utf8')

cursor=db.cursor()

try:
  cursor.execute(sql1)
  db.commit()
except:
  print "Error: unable to insert data"
  db.rollback()
db.close()
print("db.close()")
