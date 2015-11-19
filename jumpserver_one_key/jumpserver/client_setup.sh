#!/bin/bash
# Author: LaoGuang
# Date: 2014-04-28

getSysVersion(){
    cat /etc/redhat-release  | awk '{ print $3 }' | awk -F. '{ print $1 }'
}

sys_version=`getSysVersion`
read -p "输入LDAP Server地址: " server

if [ "$sys_version" == "5" ];then
    yum -y install openldap openldap-clients nss_ldap &> /dev/null && echo "安装 LDAP Client 成功"
    grep "pam_mkhomedir.so" /etc/pam.d/system-auth &> /dev/null || echo "session required pam_mkhomedir.so skel=/etc/skel umask=0077" >> /etc/pam.d/system-auth
    authconfig --enableldap --enableldapauth --enablemkhomedir --ldapserver=$server --ldapbasedn="dc=jumpserver,dc=org" --update
    grep "Sudoers" /etc/ldap.conf &> /dev/null || echo "Sudoers_base ou=Sudoers,dc=jumpserver,dc=org" >> /etc/ldap.conf
    grep "Sudoers" /etc/nsswitch.conf || echo "Sudoers_base ou=Sudoers,dc=jumpserver,dc=org" >> /etc/ldap.conf

elif [ "$sys_version" == "6" ];then
    yum -y install openldap openldap-clients nss-pam-ldapd pam_ldap &> /dev/null && echo "安装 LDAP Client 成功"
    grep "pam_mkhomedir.so" /etc/pam.d/system-auth &> /dev/null || echo "session required pam_mkhomedir.so skel=/etc/skel umask=0077" >> /etc/pam.d/system-auth
    authconfig --savebackup=auth.bak
    authconfig --enableldap --enableldapauth --enablemkhomedir --enableforcelegacy --disablesssd --disablesssdauth --ldapserver=$server --ldapbasedn="dc=jumpserver,dc=org" --update
    grep "Sudoers" /etc/sudo-ldap.conf &> /dev/null || echo -e "uri ldap://$server\nSudoers_base ou=Sudoers,dc=jumpserver,dc=org" > /etc/sudo-ldap.conf
    grep "Sudoders" /etc/nsswitch.conf || echo "Sudoers: files ldap" >>  /etc/nsswitch.conf
else
    echo "脚本不支持该系统版本，请手工测试"
    exit 2
fi
