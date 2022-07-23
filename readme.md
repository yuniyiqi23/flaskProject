### 使用flask-sqlacodegen生成Model
flask-sqlacodegen "mysql+pymysql://root:root@127.0.0.1:3306/seedling_dev" --tables "account" --outfile "models/account.py" --flask

### 所使用的环境全部的包的环境
pip freeze > requirements.txt
### 只生成项目依赖的包的环境
pip install pipreqs
pipreqs ./