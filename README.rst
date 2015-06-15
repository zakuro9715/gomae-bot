============
ごまえー♪bot
============

Install
=======

#. 事前にtwitterアプリケーションを登録していることを前提とします。

#. 依存ライブラリのインストール::
  
    pip install -r requirements.txt

#. 設定のコピー::

    cp settings.py.default settings.py

#. 設定ファイルを適宜書き換える。

Usage
=====

簡単な使い方::

  python3 gomae.py

デフォルトでは、起動してすぐに時刻修正し、2分後にツイートされます。
