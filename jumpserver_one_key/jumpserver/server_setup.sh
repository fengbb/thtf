#!/bin/bash
# Version: 2.0.0
# Author: LaoGuang
# Date: 2015-04-28

ldap_conf=/etc/openldap/slapd.conf

getSysVersion(){
    cat /etc/redhat-release  | awk '{ print $3 }'
}

echo
echo -e "\033[32m 开始安装Jumpserver v2.0.0 版，期间需要下载软件包，根据网络情况会持续一段时间，并不是卡死. \033[0m"

echo
rpm -q automake &> /dev/null
mini=$?
version=`getSysVersion`
if [ "$mini" != "0" -a "$version" != "6.5" ];then
    echo -n "你确定你的CentOS 6.5 且是最小化安装吗?"
    read confirm
fi
service iptables stop &> /dev/null && setenforce 0
# Install epel and dependency package
rpm -ivh epel-release-6-8.noarch.rpm &> setup.log && echo "1. 安装epel源 成功" || echo "1. epel已经安装"
yum clean all &> /dev/null 
yum install -y vim automake autoconf gcc xz ncurses-devel patch python-devel git python-pip gcc-c++  &>> setup.log && echo "2. 安装依赖包 成功" || exit 2

# Install openldap server
yum install -y openldap openldap-servers openldap-clients openldap-devel &>> setup.log && echo "3. 安装ldapserver 成功" || exit 3

# Set ldap config
rm -rf /var/lib/ldap/* && cp /usr/share/openldap-servers/DB_CONFIG.example /var/lib/ldap/DB_CONFIG 
cp /usr/share/doc/sudo-1.8.6p3/schema.OpenLDAP /etc/openldap/schema/sudo.schema
cp slapd.conf /etc/openldap/

# Start service 
service slapd restart &> /dev/null
rm -rf /etc/openldap/slapd.d/*
slaptest -f /etc/openldap/slapd.conf -F /etc/openldap/slapd.d &> /dev/null && echo "4. LDAP Server 配置 成功"
chown -R ldap:ldap /etc/openldap/slapd.d/
service slapd restart
echo 

# Import ldif
echo "5. 导入基本schema到LDAP Server"
ldapadd -x -w secret234 -D "cn=admin,dc=jumpserver,dc=org" -f base.ldif &>> setup.log && echo "	base.ldif OK"
ldapadd -x -w secret234 -D "cn=admin,dc=jumpserver,dc=org" -f group.ldif &>> setup.log  && echo "	group.ldif OK"
ldapadd -x -w secret234 -D "cn=admin,dc=jumpserver,dc=org" -f passwd.ldif &>> setup.log && echo "	passwd.ldif OK"
ldapadd -x -w secret234 -D "cn=admin,dc=jumpserver,dc=org" -f sudo.ldif &>> setup.log && echo "	sudo.ldif OK"
echo 

echo -n "6. 在客户端(另一台测试机)上执行 client_setup.sh ，完成后 回车继续"
read confirm

echo -n "7. 另开一个session执行 ssh testuser@客户端地址 , 密码是 testuser123, 并测试 sudo su(不应该提示输密码), 如果没有问题,回车继续"
read confirm 
ldapdelete -x -D "cn=admin,dc=jumpserver,dc=org" -w secret234 "uid=testuser,ou=People,dc=jumpserver,dc=org"
ldapdelete -x -D "cn=admin,dc=jumpserver,dc=org" -w secret234 "cn=testuser,ou=Sudoers,dc=jumpserver,dc=org"

# Install mysql
yum -y install mysql mysql-server mysql-devel &> /dev/null
service mysqld start &> /dev/null
mysql -e "drop database if exists jumpserver;create database jumpserver charset='utf8';" || echo "MySQL 密码不对 退出"
mysql -e "grant all on jumpserver.* to 'jumpserver'@'127.0.0.1' identified by 'mysql234';" || exit 2
echo "8. 安装MySQL 成功"

# Clone jumpserver project
tar xf jumpserver.tar.bz2 -C /opt
tar xf node_modules.tar.bz2 -C /opt/jumpserver/websocket/
tar xf pip-build-root.tar.bz2 -C /tmp/
cd /opt/jumpserver
git pull origin master:master && echo "9. 更新代码 成功"
cd /opt/jumpserver/docs
rm -rf /usr/lib64/python2.6/site-packages/Crypto && echo y | pip uninstall pycrypto
pip install -r requirements.txt &>> setup.log && echo "10. 安装pypi依赖库 成功"

# Config jumpserver conf
cd /opt/jumpserver
read -p "输入本机IP地址：" host
read -p "输入smtp server地址: （如 smtp.qq.com）" smtp_server
read -p "输入smtp server端口: （如 25）" smtp_port
read -p "输入邮件地址: （如 446465001@qq.com) " email
read -p "输入邮箱密码: （如 dfkelfasdf) " password

cf="jumpserver.conf" 
sed -i "s@ip =.*@ip = $host@g" $cf
sed -i "s@web_socket.*@web_socket_host = $host:3000@g" $cf
sed -i "s@email_host = .*@email_host = $smtp_server@g" $cf
sed -i "s@email_port.*@email_port = $smtp_port@g" $cf
sed -i "s/email_host_user.*/email_host_user = $email/g" $cf
sed -i "s@email_host_password.*@email_host_password = $password@g" $cf

echo "11. 修改jumpserver.conf 配置文件 成功"

mkdir -p logs/{connect,exec_cmds} && chmod -R 777 logs
chmod +x *.py *.sh
echo no | python manage.py syncdb
echo

# config websocket
yum -y install nodejs npm &>> setup.log
cd /opt/jumpserver/websocket
npm install &>> setup.log
echo "12. Nodejs 安装并设置完成"
echo "13. 启动服务"
cd /opt/jumpserver
sh service.sh start

cd docs
cp zzjumpserver.sh /etc/profile.d/ 
echo "14. 设置登录运行 成功"
echo "15. 浏览器访问 http://$host/install 初始化 然后登陆，默认账号密码 admin admin 访问http://laoguang.blog.51cto.com/获得帮助"

