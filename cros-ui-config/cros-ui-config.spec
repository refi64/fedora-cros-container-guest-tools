Name: cros-ui-config
Version: 0.12
Release: 0.12%{?dist}
Summary: UI integration for Chromium OS

License: BSD-3-Clause
Source0: gtkrc
Source1: settings.ini
Source2: Trolltech.conf
Source3: 01-cros-ui
Source4: user

Requires: cros-adapta
Requires: dconf
Requires: google-croscore-fonts
Requires: google-roboto-fonts

BuildArch: noarch

%description
This package installs default configuration for GTK+ that is ideal for integration with
Chromium OS.

%install
install -Dm 644 gtkrc %{_prefix}/%{_sysconfdir}/gtk-2.0/gtkrc
install -Dm 644 settings.ini %{_prefix}/%{_sysconfdir}/gtk-3.0/settings.ini
install -Dm 644 Trolltech.conf %{_prefix}/%{_sysconfdir}/xdg/Trolltech.conf
install -Dm 644 01-cros-ui %{_prefix}/%{_sysconfdir}/dconf/db/local.d/01-cros-ui
install -Dm 644 user %{_prefix}/%{_sysconfdir}/dconf/profile/user

%files
%config %{_sysconfdir}/gtk-2.0/gtkrc
%config %{_sysconfdir}/gtk-3.0/settings.ini
%config %{_sysconfdir}/xdg/Trolltech.conf
%config %{_sysconfdir}/dconf/db/local.d/01-cros-ui
%config %{_sysconfdir}/dconf/profile/user

%post
%{_bin}/dconf update

%postun
%{_bin}/dconf update
