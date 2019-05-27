Name: cros-sftp
Version: 0.14
Release: 0.14%{?dist}
Summary: SFTP service files for CrOS integration

License: BSD-3-Clause
Source0: cros-sftp.service

Requires: openssh-server

BuildArch: noarch

%description
This package installs unitfiles and support scripts for enabling SFTP integration with
Chromium OS.

%install
install -Dm 644 cros-sftp.service %{buildroot}/%{_unitdir}/cros-sftp.service

%files
%{_userunitdir}/cros-sftp.service

%post
[ $1 -eq 1 ] && systemctl --no-reload enable cros-sftp.service >/dev/null 2>&1 ||:

%preun
[ $1 -eq 0 ] && systemctl --no-reload disable cros-sftp.service >/dev/null 2>&1 ||:
