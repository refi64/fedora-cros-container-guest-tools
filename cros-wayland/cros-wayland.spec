Name: cros-wayland
Version: 0.10
Release: 0.10%{?dist}
Summary: Wayland extras for virtwl in Chromium OS

License: BSD-3-Clause
Source0: skel.weston.ini
Source1: 10-cros-virtwl.rules

BuildArch: noarch

%description
This package provides config files and udev rules to improve the Wayland experience under CrOS.

%install
install -Dm 644 skel.weston.ini %{_prefix}/%{_sysconfdir}/skel/.config/weston.ini
install -Dm 644 10-cros-virtwl.rules %{_prefix}/%{_udevrulesdir}/10-cros-virtwl.rules

%files
%config %{_sysconfdir}/skel/.config/weston.ini
%{_udevrulesdir}/10-cros-virtwl.rules
