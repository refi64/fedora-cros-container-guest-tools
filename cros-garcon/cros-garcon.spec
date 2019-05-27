Name: cros-garcon
Version: 0.21
Release: 0.21%{?dist}
Summary: Chromium OS Garcon Bridge

License: BSD-3-Clause
Source0: skel.cros-garcon.conf
Source1: garcon_host_browser.desktop
Source2: cros-garcon.service
Source3: garcon-terminal-handler
Source4: garcon-url-handler
Source5: cros-garcon-override.conf
# Ignore garcon-synaptic.pkla because it's not useful here.
Source6: garcon-packagekit.pkla
# Custom dnf plugin to replace cros-garcon-dpkg-config:
Source7: garcon_trigger.py

BuildArch: noarch

Requires: desktop-file-utils
Requires: PackageKit
Requires: xdg-utils
Requires: dnf
Requires: dnf-plugins-core

%description
This package provides the systemd unit files for Garcon, the bridge to Chromium OS.

# XXX: Isn't this supposed to be defined by default?
%define python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

%install
install -Dm 644 %{SOURCE0} %{buildroot}/%{_sysconfdir}/skel/.config/cros-garcon.conf
install -Dm 644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/garcon_host_browser.desktop
install -Dm 644 %{SOURCE2} %{buildroot}/%{_userunitdir}/cros-garcon.service
install -Dm 755 %{SOURCE3} %{buildroot}/%{_bindir}/garcon-terminal-handler
install -Dm 755 %{SOURCE4} %{buildroot}/%{_bindir}/garcon-url-handler
install -Dm 644 %{SOURCE5} %{buildroot}/%{_sysconfdir}/systemd/user/cros-garcon.service.d/cros-garcon-override.conf
install -Dm 644 %{SOURCE6} %{buildroot}/%{_sharedstatedir}/polkit-1/localauthority/50-local.d/garcon-packagekit.pkla
install -Dm 644 %{SOURCE7} %{buildroot}/%{python3_sitelib}/dnf-plugins/garcon_trigger.py

%files
%config %{_sysconfdir}/skel/.config/cros-garcon.conf
%{_datadir}/applications/garcon_host_browser.desktop
%{_userunitdir}/cros-garcon.service
%{_bindir}/garcon-terminal-handler
%{_bindir}/garcon-url-handler
%config %{_sysconfdir}/systemd/user/cros-garcon.service.d/cros-garcon-override.conf
%{_sharedstatedir}/polkit-1/localauthority/50-local.d/garcon-packagekit.pkla
%{python3_sitelib}/dnf-plugins/garcon_trigger.py
%{python3_sitelib}/dnf-plugins/__pycache__/garcon_trigger.*

%post
[ $1 -eq 1 ] && systemctl --no-reload enable cros-garcon.service >/dev/null 2>&1 ||:

%preun
[ $1 -eq 0 ] && systemctl --no-reload disable cros-garcon.service >/dev/null 2>&1 ||:
