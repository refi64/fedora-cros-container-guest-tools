Name: cros-sudo-config
Version: 0.10
Release: 0.10%{?dist}
Summary: sudo config for Chromium OS integration

License: BSD-3-Clause
Source0: 10-cros-nopasswd

Requires: sudo

BuildArch: noarch

%description
This package installs default configuration for sudo to allow passwordless sudo access for the
sudo group

%install
install -Dm 440 10-cros-nopasswd %{buildroot}/%{_sysconfdir}/sudoers.d/10-cros-nopasswd

%files
%config %{_sysconfdir}/sudoers.d/10-cros-nopasswd
