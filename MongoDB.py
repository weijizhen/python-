#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2018/5/27 20:06
#@Author    :weijizhen
#@File      :MongoDB.py
'''
mongod  启动服务器
mongo   连接客户端

sudo service mongod start   启动MongoDB
sudo service mongod stop    停止MongoDB

db 查看当前数据库名称
db.stats() 查看当前数据库信息

show dbs   列出物理机上存在的数据库
use 数据库    切换数据库，如果数据库不存在，则指向数据库，但不创建，直接插入数据或者创建集合时数据库才被创建

默认的数据库为test，如果你没有创建新的数据库，集合将存放在test数据库中

db.dropDatabase()    数据库删除，如果数据库不存在，则什么也不做

集合创建 （数据库的集合，我认为就是表格）  db.createCollection(name,options)
               name是要创建的集合的名称
               options是一个文档，用于指定集合的配置
               选项​​参数是可选的，所以只需要到指定的集合名称。以下是可以使用的选项列表：
例1：不限制集合大小
db.createCollection('stu')

                参数capped:默认值为false表示不设置上限，值为true表示设置上限
                参数size: 当capped值为true时，需要指定此参数，表示上限大小，当文档达到上限时，会将之前的数据覆盖，单位制时字节
例2：限制集合大小
db.createCollection('stu',{capped:true,size:10})

查看当前数据库的集合
show collections
删除数据库的集合（这里的集合我认为就是的表格）
db.集合名称.drop()
'''

'''
数据类型
Object ID：文档ID
String：最常用的字符串，必须是有效的UTF-8
Boolean：存储一个布尔值，true或者false
Integer：整数可以是32位或64位，这取决于服务器
Double：存储浮点值
Arrays：数组或列表，多个值存储到一个键
Object：用于嵌入式的文档，即一个值为一个文档
Null：存储Null值
Timestamp：时间戳
Date：存储当前日期或时间的UNIX时间格式

重点：object id  
        { "_id" : ObjectId("5b0aabd4a59ebfa19aa8ad42"), "name" : "weiwie", "mingzhi" : "yanyan" }
        每个文档都有一个属性，为_id，保证每个文档的唯一性
        可以自己去设置_id插入文档
        如果没有提供，那么MongoDB为每个文档提供了一个独特的_id，类型为objectID
        objectID是一个12字节的十六进制数
        前4个字节为当前时间戳
        接下来3个字节的机器ID
        接下来的2个字节中MongoDB的服务进程id
        最后3个字节是简单的增量值

插入
db.集合名称.insert()
        例子：db.stu.insert({name:'weiwie',mingzhi:'yanyan'})
db.集合名称.find()
        例子：{ "_id" : ObjectId("5b0aabd4a59ebfa19aa8ad42"), "name" : "weiwie", "mingzhi" : "yanyan" }

插入的第二种方法
s1={_id:'20160101',name:'hr'}
s1.gender=0
db.stu.insert(s1)

'''

'''
更新
db.集合名称.update(<query>,<update>,{multi: <boolean>})
        参数query:查询条件，类似sql语句update中where部分
        参数update:更新操作符，类似sql语句update中set部分
        参数multi:可选，默认是false，表示只更新找到的第一条记录，值为true表示把满足条件的文档全部更新
        1.例子：db.stu.update({},{$set:{name:'weiyan'}})
        更新效果：db.stu.find()
                      { "_id" : ObjectId("5b0aabd4a59ebfa19aa8ad42"), "name" : "weiyan", "mingzhi" : "yanyan" }
        2.指定属性更新，通过操作符$set
        db.stu.update({},{$set:{name:'weiwei11111'}})
        3.修改多条匹配到的数据
        db.stu.update({},{$set:{gender:0}},{multi:true})
        
保存
db.集合名称.save(do cument)
        如果文档的_id已经存在则修改，如果文档的_id不存在则添加
        1.例子：db.stu.save({name:'weiyan',age:22})
                   WriteResult({ "nInserted" : 1 })
           保存结果：
                db.stu.find()
                { "_id" : ObjectId("5b0abc77a59ebfa19aa8ad46"), "name" : "weiyan", "age" : 22 }
                { "_id" : ObjectId("5b0abe4ca59ebfa19aa8ad47"), "name" : "weiyan", "age" : 22 }

删除
db.集合名称.remove(<query>, { justOne: <boolean>})
            参数query:可选，删除的文档的条件
            参数justOne:可选，如果设为true或1，则只删除一条，默认false，表示删除多条
            1.例子：只删除匹配到的第一条
            db.stu.remove({gender:0},{justOne:true})
            2.例子：全部删除
            db.stu.remove({})
            删除结果：
            WriteResult({ "nRemoved" : 4 })


'''