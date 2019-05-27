Name: cros-pulse-config
Version: 0.1
Release: 0.1%{?dist}
Summary: PulseAudio helper for Chromium OS integration

License: BSD-3-Clause
Source0: cros-pulse-config.service

Requires: pulseaudio

BuildArch: noarch

%description
This package installs a helper systemd unit for PulseAudio support. This is
required as a workaround for the lack of udev in unprivileged containers.

%install
install -Dm 644 cros-pulse-config.service %{buildroot}/%{_userunitdir}/cros-pulse-config.service

%files
%{_userunitdir}/cros-pulse-config.service

%post
[ $1 -eq 1 ] && systemctl --no-reload enable cros-pulse-config.service >/dev/null 2>&1 ||:

%preun
[ $1 -eq 0 ] && systemctl --no-reload disable cros-pulse-config.service >/dev/null 2>&1 ||:
