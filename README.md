# Raspberry Pi 用セルフ貸出アプリ

[![Maintainability](https://api.codeclimate.com/v1/badges/72dd97418daca5699a80/maintainability)](https://codeclimate.com/github/nakamura-akifumi/self_checkout_machine/maintainability)

## 概要

Raspberry Pi に Felicaリーダー、バーコードリーダ、液晶モニタを接続し、セルフ貸出機として利用できるようにするアプリケーションです。

まだ開発中です。

### 外観

### 画面    

## 動作環境の構築

## 開発環境の構築

### Mac OS X 向け

2018.6.15 HighSierraで確認しました。

````
$ brew install libyaml
$ brew install libusb libusb-compat
$ python -V
Python 2.7.15 :: Anaconda, Inc.
$ brew install sip
$ wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.1/PyQt4_gpl_mac-4.12.1.tar.gz
$ tar zxvf PyQt4_gpl_mac-4.12.1.tar.gz
$ cd 
$ python configure-ng.py
$ make
$ make install
$ pip install pyyaml
$ pip install pyusb libusb1 pyserial
````

### Raspberry Pi 3 向け

(記載中)

### 開発メモ

Qt Designer の開き方

````
$ open -a Designer
````

uiファイルからの変換方法

````
$ export PYTHONPATH=/anaconda3/envs/self_checkout_machine/lib/python2.7/site-packages
$ pyuic4 -o main_window.py main_window.ui
````

##  製作者・貢献者 (Authors and contributors)
- [Akifumi NAKAMURA](https://github.com/nakamura-akifumi) ([@tmpz84](https://twitter.com/tmpz84))

## License
The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).