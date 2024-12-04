Name: clickhouse
Version:
Release: 5d124707154
Summary: Open-source distributed column-oriented DBMS
License: Apache-2.0
Group: Databases

%description
ClickHouse is an open-source column-oriented database management system that
allows generating analytical data reports in real time.

%install
mkdir -p ${RPM_BUILD_ROOT}/data/

mkdir -p ${RPM_BUILD_ROOT}/usr/lib/systemd/system/
cp -f ${RPM_BUILD_DIR}/byconity-server.service                   ${RPM_BUILD_ROOT}/etc/systemd/system/
cp -f ${RPM_BUILD_DIR}/byconity-worker.service                   ${RPM_BUILD_ROOT}/etc/systemd/system/
cp -f ${RPM_BUILD_DIR}/byconity-daemon.service                   ${RPM_BUILD_ROOT}/etc/systemd/system/
cp -f ${RPM_BUILD_DIR}/byconity-tso.service                      ${RPM_BUILD_ROOT}/etc/systemd/system/
cp -f ${RPM_BUILD_DIR}/byconity-resource.service                 ${RPM_BUILD_ROOT}/etc/systemd/system/

mkdir -p ${RPM_BUILD_ROOT}/usr/bin/
cp -f ${BYCONITY_BUILD_DIR}/programs/clickhouse                        ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-benchmark              ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-client                 ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-compressor             ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-copier                 ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-dumper                 ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-extract-from-config    ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-format                 ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-git-import             ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-keeper                 ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-keeper-converter       ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-library-bridge         ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-local                  ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-meta-inspector         ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-obfuscator             ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-odbc-bridge            ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-part-toolkit           ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-schema-advisor         ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-server                 ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-storage_tools          ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-storage-tools          ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/clickhouse-worker                 ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/daemon_manager                    ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/daemon-manager                    ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/resource_manager                  ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/resource-manager                  ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/tso_server                        ${RPM_BUILD_ROOT}/usr/bin/
cp -P ${BYCONITY_BUILD_DIR}/programs/tso-server                        ${RPM_BUILD_ROOT}/usr/bin/

mkdir -p ${RPM_BUILD_ROOT}/etc/byconity/
cp -f ${BYCONITY_BUILD_DIR}/../programs/server/byconity-daemon-manager.xml                ${RPM_BUILD_ROOT}/etc/byconity/
cp -f ${BYCONITY_BUILD_DIR}/../programs/server/byconity-resource-manager.xml              ${RPM_BUILD_ROOT}/etc/byconity/
cp -f ${BYCONITY_BUILD_DIR}/../programs/server/byconity-server.xml                        ${RPM_BUILD_ROOT}/etc/byconity/
cp -f ${BYCONITY_BUILD_DIR}/../programs/server/byconity-tso.xml                           ${RPM_BUILD_ROOT}/etc/byconity/
cp -f ${BYCONITY_BUILD_DIR}/../programs/server/byconity-worker-write.xml                  ${RPM_BUILD_ROOT}/etc/byconity/
cp -f ${BYCONITY_BUILD_DIR}/../programs/server/byconity-worker.xml                        ${RPM_BUILD_ROOT}/etc/byconity/
cp -f ${BYCONITY_BUILD_DIR}/../programs/server/cnch_config.xml                            ${RPM_BUILD_ROOT}/etc/byconity/
cp -f ${BYCONITY_BUILD_DIR}/../programs/server/config.xml                                 ${RPM_BUILD_ROOT}/etc/byconity/
cp -f ${BYCONITY_BUILD_DIR}/../programs/server/embedded.xml                               ${RPM_BUILD_ROOT}/etc/byconity/
cp -f ${BYCONITY_BUILD_DIR}/../programs/server/users.xml                                  ${RPM_BUILD_ROOT}/etc/byconity/

%pre
%_sbindir/groupadd -r -f _clickhouse 2> /dev/null ||:
%_sbindir/useradd -r -g _clickhouse -d %_localstatedir/lib/%name -s /dev/null -c "ClickHouse User" _clickhouse 2> /dev/null ||:

%post
systemctl daemon-reload

%postun
rm -rf /etc/systemd/system/byconity_server.service
rm -rf /etc/systemd/system/byconity_worker.service
rm -rf /etc/systemd/system/byconity_daemon.service
rm -rf /etc/systemd/system/byconity_resource.service
rm -rf /etc/systemd/system/byconity_tso.service
systemctl daemon-reload

%files
%_bindir/clickhouse
%_bindir/clickhouse-server
%_bindir/clickhouse-worker
%_bindir/daemon-manager
%_bindir/tso-server
%_bindir/resource-manager

%dir %_sysconfdir/clickhouse-server
%config(noreplace) %_sysconfdir/byconity/byconity-daemon-manager.xml    
%config(noreplace) %_sysconfdir/byconity/byconity-resource-manager.xml 
%config(noreplace) %_sysconfdir/byconity/byconity-server.xml           
%config(noreplace) %_sysconfdir/byconity/byconity-tso.xml              
%config(noreplace) %_sysconfdir/byconity/byconity-worker-write.xml     
%config(noreplace) %_sysconfdir/byconity/byconity-worker.xml           
%config(noreplace) %_sysconfdir/byconity/cnch_config.xml               
%config(noreplace) %_sysconfdir/byconity/config.xml                    
%config(noreplace) %_sysconfdir/byconity/embedded.xml                  
%config(noreplace) %_sysconfdir/byconity/users.xml                     
