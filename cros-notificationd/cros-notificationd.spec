Name: cros-notificationd
Version: 0.1
Release: 0.1%{?dist}
Summary: Chromium OS Notification Bridge

License: BSD-3-Clause
Source0: org.freedesktop.Notifications.service

BuildArch: noarch

%description
This package installs D-Bus on-demand service specification for notificationd.

%install
install -Dm 644 org.freedesktop.Notifications.service %{buildroot}/%{_datadir}/dbus-1/services/org.freedesktop.Notifications.service

%files
%{_datadir}/dbus-1/services/org.freedesktop.Notifications.service
