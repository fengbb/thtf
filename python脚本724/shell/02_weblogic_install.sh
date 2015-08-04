#!/bin/bash
set -x
#安装weblogic
#Oracle_Weblogic安装目录
export HOSTNAME=`hostname`
export CREATE_HOME=/resource/weblogic/Oracle/Middleware
export UC_WEBLOGIC=weblogic
export UC_GROUP=weblogic
export UC_HOME=/home/weblogic
export UC_LOG=${UC_HOME}/${UC_WEBLOGIC}_install.log
#创建域目录
export UC_BASE=${CREATE_HOME}/wlserver_10.3/common/bin

function create_weblogic () { 
cd ${UC_HOME}
cat >> wls.rsp << EOF
[ENGINE]
#DO NOT CHANGE THIS
Response File Version=1.0.0.0.0
[GENERIC]
ORACLE_HOME=/resource/weblogic/Oracle/Middleware/wls/12.1.3.0
INSTALL_TYPE=WebLogic Server
DECLINE_SECURITY_UPDATES=true
EOF
cat >> oralnst.loc << EOF
inventory_loc=/home/weblogic/oraInventory1
inst_group=weblogic
EOF
#wget http://file-server.toppay.com/soft/Weblogic/shell/silent.xml
wget http://file-server.toppay.com/soft/Weblogic/wls_121200.jar
chown -R weblogic.weblogic ${UC_HOME}
su - ${UC_WEBLOGIC} -c "cd ${UC_HOME}; java -jar wls_121200.jar -silent -response ${UC_HOME}/wls.rsp -invPtrloc ${UC_HOME}/oraInst.loc > ${ICS_LOG} 2>&1"
}
function create_weblogic_domain_server () {
cd ${UC_BASE}
cat >> silent.xml << EOF
read template from "/resource/weblogic/Oracle/Middleware/wls/12.1.3.0/wlserver/common/templates/wls/wls.jar";

find Server "AdminServer" as s1;
//set s1.ListenAddress "10.2.128.1";
set s1.ListenPort "7001";
set s1.SSL.Enabled "true";
set s1.SSL.ListenPort "7002";

create JMSServer "myJMSServer" as jmsserver;
create JMSQueue "myJMSQueue" as myq;
set myq.JNDIName "jms/myjmsqueue";
set myq.JMSServer "myJMSServer";
assign JMSServer "myJMSServer" to target "AdminServer";

find User "weblogic" as u1;
set u1.password "weblogic123";
set OverwriteDomain "true";
write domain to "/resource/user_projects/domains/wls";

close template;
EOF
#wget http://file-server.toppay.com/soft/Weblogic/shell/raadmin/wl_create_domain-user_ra.rsp
chown ${UC_WEBLOGIC}.${UC_WEBLOGIC} ${UC_HOME}/silent.xml
su - ${UC_WEBLOGIC} -c "cd ${UC_BASE}; ./config.sh -mode=silent -silent_script=${UC_HOME}/silent.xml >> ${UC_LOG} 2>&1"
}

echo "127.0.0.1 ${HOSTNAME}" >> /etc/hosts
mkdir -p ${CREATE_HOME}
chown -R ${UC_WEBLOGIC}:${UC_GROUP} ${CREATE_HOME}
create_weblogic
create_weblogic_domain_server