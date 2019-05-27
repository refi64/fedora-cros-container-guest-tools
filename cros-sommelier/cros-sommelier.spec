Name: cros-sommelier
Version: 0.22
Release: 0.22%{?dist}
Summary: sommelier base package

License: BSD-3-Clause
Source0: sommelier@.service
Source1: sommelier-x@.service
Source2: sommelierrc
Source3: sommelier.sh

Requires: systemd-pam
Recommends: xorg-x11-utils
Recommends: xorg-x11-server-utils
Recommends: xorg-x11-xauth
Recommends: xkeyboard-config

BuildArch: noarch

%description
This package installs unitfiles and support scripts for sommelier.

%install
install -Dm 644 sommelier@.service %{buildroot}/%{_userunitdir}/sommelier@.service
install -Dm 644 sommelier-x@.service %{buildroot}/%{_userunitdir}/sommelier-x@.service
install -Dm 644 sommelierrc %{buildroot}/%{_sysconfdir}/sommelierrc
install -Dm 644 sommelier.sh %{buildroot}/%{_sysconfdir}/profile.d/sommelier.sh

%files
%{_userunitdir}/sommelier@.service
%{_userunitdir}/sommelier-x@.service
%config %{_sysconfdir}/sommelierrc
%config %{_sysconfdir}/profile.d/sommelier.sh

%post
if [ $1 == 1 ]; then
  ln -s /opt/google/cros-containers/bin/sommelier.elf %{_bindir}/sommelier.elf
fi

%preun
if [ $1 == 0 ]; then
  rm %{_bindir}/sommelier.elf
fi
