### 访问地址
http://120.26.4.95:5000

### 使用flask-sqlacodegen生成Model
flask-sqlacodegen "mysql+pymysql://root:root@127.0.0.1:3306/seedling_dev" --tables "account" --outfile "models/account.py" --flask

### 所使用的环境全部的包的环境
pip freeze > requirements.txt
### 只生成项目依赖的包的环境
pip install pipreqs
pipreqs ./

### uwsgi启动
uwsgi --http-socket :5000 --wsgi-file run.py --callable app --master --processes 4 --threads 2