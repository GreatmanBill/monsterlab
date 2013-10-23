monsterlab
==========

This is a organizational website for tongpao. 
数据库:
========
数据库用mysql
密码为123456,不是这个的,重新安装

安装git:
========
1.在ubuntu或win7下自己安装好git
2.配置用户名和邮箱
    git config --global user.email "me@here.com"
    git config --global user.name "me"

    如我的配置:
    git config --global user.email "xiaobingzhang29@gmail.com"
    git config --global user.name "xiaobing"


git 使用规则:
=========
1.生成SSH key
    若是ubuntu,打开终端
    使用:ssh-keygen -t rsa
    若是windows,打开git bash
    使用:ssh-keygen -t rsa

    输入后,直接按三个回车就ok了,不要输入文件,密码
2.获得SSH key的公钥
    若是ubuntu,
        cd ~/.ssh
        打开id_rsa.pub,全部复制,然后将这个用gmail邮箱发给我
    若是windows,
        在你的自己的目录下,找到同样的目录,这个应该是隐藏文件,
        打开后,也是用你的gmail发给我
3.发给我后,我把你们的key加入到我的信息里面去,你们就可以推送和拉取我的文件了

4.在本地见一个目录,名为tongpao
    如:mkdir ~/workspace/tongpao
5.将项目拉到本地
    cd ~/workspace/tongpao
    git pull git@github.com:GreatmanBill/monsterlab.git
6.添加远程库的引用
    git remote add tongpao git@github.com:GreatmanBill/monsterlab.git

    查看效果:
    git remote -v
    出现这样的就成功了
    tongpao git@github.com:GreatmanBill/monsterlab.git (fetch)
    tongpao git@github.com:GreatmanBill/monsterlab.git (push)
7.之后,就可以使用简单的缩写来拉取代码了,如:
    拉数据回本地:
        git pull tongpao master
    推数据到远端:
        git push tongpao master

git 修改数据简单命令:
===========
1.添加需要提交的文件
    git add filename
    该命令为:添加指定的文件进入提交状态, 点号 '.' 为当前目录,及其所有子目录
    文件都加入到提交状态
2.提交修改的文件
    git commit -m 'commit messge'
    该命令用于提交修改的文件到本地的库中,commit message为你对这些文件修改的
    简短的描述信息
3.将远端数据拉回本地,与本地数据合并
    git pull tongpao master
4.将本地的修改推送到远端
    git push tongpao master

5.查看当前文件的状态
    git status

    这个可以在任何时候使用,可以查看当前的所有文件所处于的什么版本

    git status -s
    显示简短的说明


