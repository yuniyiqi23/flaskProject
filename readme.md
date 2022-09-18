#### 访问地址
http://120.26.4.95:5000

***
#### 使用flask-sqlacodegen生成Model
flask-sqlacodegen "mysql+pymysql://root:root@127.0.0.1:3306/seedling_dev" --tables "account" --outfile "models/account.py" --flask

***
#### 所使用的环境全部的包的环境
pip freeze > requirements.txt
#### 只生成项目依赖的包的环境
pip install pipreqs
pipreqs ./

***
### 部署
#### uwsgi命令行启动
uwsgi --http-socket :5000 --wsgi-file run.py --callable app --master --processes 4 --threads 2

#### 配置文件启动(阿里云看这里)
cd /home/adam/flaskProject
uwsgi --ini uwsgi.ini //启动
uwsgi --stop /tmp/logs/movie.pid //停止服务  
uwsgi --reload /tmp/logs/movie.pid //可以无缝重启服务

##### 通过命令行停止服务
ps -ef | grep uwsgi //kill掉一个就行了  
uWSGI 通过 xxx.ini 启动后会在相同目录下生成一个 xxx.pid 的文件，里面只有一行内容是 uWSGI 的主进程的进程号。

