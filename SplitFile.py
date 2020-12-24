#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName :Test.py
# @Software PyCharm

from  datetime import  datetime


def Main():
    #目标路径
    target_dir = ''
    #资源路径
    source_dir = ''

    flag =0
    #文件名
    name =1
    #存放数据
    dataList =[]
    print("开始。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    with open(source_dir, 'r') as f_source:
        for line in f_source:
            flag += 1
            dataList.append(line)
            if flag == 1993:
                with open(target_dir + "sql_list_" + str(name) + ".sql", 'w+') as f_target:
                    for data in dataList:
                        f_target.write(data)
                name += 1
                flag = 0
                dataList = []
    # 处理最后一批行数少于指定行数
    with open(target_dir + "sql_" + str(name) + ".sql", 'w+') as f_target:
        for data in dataList:
            f_target.write(data)

    print("完成。。。。。")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":
    Main()