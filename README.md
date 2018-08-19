# Raspberry Pi 用セルフ貸出アプリ

[![Maintainability](https://api.codeclimate.com/v1/badges/72dd97418daca5699a80/maintainability)](https://codeclimate.com/github/nakamura-akifumi/self_checkout_machine/maintainability)

## 概要

Raspberry Pi に Felicaリーダー、バーコードリーダ、液晶モニタを接続し、セルフ貸出機として利用できるようにするアプリケーションです。

サーバ側との接続方法は、
- http(s) 直接接続 （想定アプリ：Next-L Enju 1.3+)
- slack 経由 (想定アプリ：AssetManager [@tmpz84作成、非公開Railsアプリ])
となります。

開発中です。

### 外観

- 画像は以下で構成
    - Raspberry Pi 3
    - ケース
    - micro SD カード (16GB以上)
    - [Sony RC-S380](https://www.sony.co.jp/Products/felica/consumer/products/RC-S380.html)
    - 公式 7" Touchscreen Display
    - USB バーコードリーダー

### 画面   

(あとで) 

## 動作環境の構築

事前にネット上の記事などを参考に構築してください。
OS のイメージは、Raspbian Stretch (2018-04-18-raspbian-stretch.zip) で確認しています。
設定もネット上の記事を参考に設定してください。
注意点として、raspi-config にて Advanced Options -> A7 GL Drive で G1 GL (Full KMS) の設定すると、
公式７インチタッチディスプレイでの表示ができません。(2018/8/19現在)

ミドルウェアなどのインストールを行います。

```
$ sudo apt-get -y update
$ sudo apt-get -y upgrade
$ sudo apt-get -y install libfreetype6-dev libfontconfig1-dev
$ sudo apt-get -y install fonts-takao
$ python -V
Python 2.7.13
$ sudo apt-get -y install qt-sdk python-qt4
$ apt-get remove python-pip
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python get-pip.py
$ sudo pip install pyyaml requests
$ sudo pip install pyusb libusb1 pyserial
$ sudo pip install nfcpy
```

```
$ sudo pip install slackclient
```

利用するFelicaリーダーを登録します。
以下のようにlsusbコマンドでFelicaリーダーのIDを確認しておきます。
（例は、ID 054c:06c3 Sony Corp. の箇所で、ベンダーIDは、054c 、プロダクトIDは、06c3 ）

```
$ lsusb
Bus 001 Device 008: ID 046d:c534 Logitech, Inc. Unifying Receiver
Bus 001 Device 007: ID 046d:c534 Logitech, Inc. Unifying Receiver
Bus 001 Device 005: ID 1a40:0101 Terminus Technology Inc. Hub
Bus 001 Device 004: ID 248a:ff0f  
Bus 001 Device 010: ID 054c:06c3 Sony Corp. 
Bus 001 Device 003: ID 0424:ec00 Standard Microsystems Corp. SMSC9512/9514 Fast Ethernet Adapter
Bus 001 Device 002: ID 0424:9514 Standard Microsystems Corp. SMC9514 Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

一般ユーザでもアクセス出来るようにして、再起動する。

```
$ sudo sh -c 'echo SUBSYSTEM==\"usb\", ACTION==\"add\", ATTRS{idVendor}==\"054c\", ATTRS{idProduct}==\"06c3\", GROUP=\"plugdev\" >> /etc/udev/rules.d/nfcdev.rules'
$ sudo reboot
```

本アプリをダウンロードし、起動する。

```
$ git clone https://github.com/nakamura-akifumi/self_checkout_machine.git
$ cd self_checkout_machine
$ ./launch.sh
```

## 入出力仕様

(あとで)

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
$ pip install pyyaml requests
$ pip install pyusb libusb1 pyserial
$ pip install nfcpy 
````

https://launchpad.net/takao-fonts
からフォント(TakaoFonts-00303.01.zip)をダウンロードする。
https://ipafont.ipa.go.jp/node72 を参考にインストールする。

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
$ pyuic4 -o src/ui_main_window.py ui_form/main_window.ui
$ pyuic4 -o src/ui_checkout_window.py ui_form/checkout_window.ui 
$ pyuic4 -o src/ui_checkin_window.py ui_form/checkin_window.ui 
````

##  製作者・貢献者 (Authors and contributors)
- [Akifumi NAKAMURA](https://github.com/nakamura-akifumi) ([@tmpz84](https://twitter.com/tmpz84))

## License
EUPL 1.1
