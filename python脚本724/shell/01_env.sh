#!/bin/bash
set -x
function _install_JDK () {
		mkdir -p /root/soft/JDK
		cd /root/soft/JDK
		wget http://file-server.toppay.com/soft/JDK/jdk-6u45-linux-x64-rpm.bin
		wget http://file-server.toppay.com/soft/JDK/jdk.sh
		cp /root/soft/JDK/jdk.sh /etc/profile.d/
		source /etc/profile
		bash jdk-6u45-linux-x64-rpm.bin
}
function _install_koan () {
		rpm -ivh http://file-server.toppay.com/soft/Oracle/koan-2.4.0-1.el6.noarch.rpm
}
_install_JDK
_install_koan
