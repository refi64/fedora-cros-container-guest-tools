Name: cros-systemd-overrides
Version: 0.10
Release: 0.10%{?dist}
Summary: systemd overrides for running under Chromium OS

License: BSD-3-Clause
Source0: 10-cros-nopasswd

Requires: systemd

BuildArch: noarch

%description
This package overrides the default behavior of some core systemd units.

%post
if [ $1 == 1 ]; then
  systemctl mask systemd-journald-audit.socket
fi

%preun
if [ $1 == 0 ]; then
  systemctl unmask systemd-journald-audit.socket
fi
