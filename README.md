# ncov
根据上次填写，定时自动填报BUPT疫情情况



#### 部署

1. 在ncov.py中填写需要打卡的学生学号与密码，以及北邮学生登录校园网的学号与密码

2. 在服务器上使用crontab命令定时执行ncov.py文件，以下是示例：

   使用crontab -e，在文件末尾添加：

   ```
   0 8 * * * /home/user/app/miniconda3/envs/something/bin/python /home/user/ncov/ncov.py 2> /home/user/ncov/error.txt
   ```



#### 声明

项目维护者对该脚本的滥用不承担任何责任。

