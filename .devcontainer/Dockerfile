FROM python:3.12.2
ENV PYTHONUNBUFFERED 1 
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# # ベースイメージを選択
# FROM python:3

# # 作業ディレクトリを設定します。
# WORKDIR /app

# # ローカルのプロジェクトディレクトリをコンテナ内にコピーします。
# COPY . /app

# # Pythonパッケージをインストールします。
# RUN pip install -r requirements.txt  

# # Djangoアプリケーションを実行します。
# CMD python manage.py runserver 0.0.0.0:8000

