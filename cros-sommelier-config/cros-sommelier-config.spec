Name: cros-sommelier-config
Version: 0.13
Release: 0.13%{?dist}
Summary: sommelier config for Chromium OS integration

License: BSD-3-Clause
Source0: cros-sommelier-override.conf
Source1: cros-sommelier-x-override.conf
Source2: cros-sommelier-low-density-override.conf

Requires: systemd-pam
Requires: cros-sommelier
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

BuildArch: noarch

%description
This package installs default configuration for sommelier that is ideal for integration with
Chromium OS.

%install
install -Dm 644 cros-sommelier-override.conf %{buildroot}/%{_sysconfdir}/systemd/user/sommelier@0.service.d/cros-sommelier-override.conf
install -Dm 644 cros-sommelier-override.conf %{buildroot}/%{_sysconfdir}/systemd/user/sommelier@1.service.d/cros-sommelier-override.conf
install -Dm 644 cros-sommelier-low-density-override.conf %{buildroot}/%{_sysconfdir}/systemd/user/sommelier@1.service.d/cros-sommelier-low-density-override.conf
install -Dm 644 cros-sommelier-x-override.conf %{buildroot}/%{_sysconfdir}/systemd/user/sommelier-x@0.service.d/cros-sommelier-x-override.conf
install -Dm 644 cros-sommelier-x-override.conf %{buildroot}/%{_sysconfdir}/systemd/user/sommelier-x@1.service.d/cros-sommelier-x-override.conf
install -Dm 644 cros-sommelier-low-density-override.conf %{buildroot}/%{_sysconfdir}/systemd/user/sommelier-x@1.service.d/cros-sommelier-low-density-override.conf
touch %{_bindir}/sommelier
mkdir -p %{_libdir}/dri
touch %{_libdir}/dri/swrast_dri.so

%files
%config %{_sysconfdir}/systemd/user/sommelier@0.service.d/cros-sommelier-override.conf
%config %{_sysconfdir}/systemd/user/sommelier@1.service.d/cros-sommelier-override.conf
%config %{_sysconfdir}/systemd/user/sommelier@1.service.d/cros-sommelier-low-density-override.conf
%config %{_sysconfdir}/systemd/user/sommelier-x@0.service.d/cros-sommelier-x-override.conf
%config %{_sysconfdir}/systemd/user/sommelier-x@1.service.d/cros-sommelier-x-override.conf
%config %{_sysconfdir}/systemd/user/sommelier-x@1.service.d/cros-sommelier-low-density-override.conf
%ghost %{_bindir}/sommelier
%ghost %{_libdir}/dri/swrast_dri.so

%post
if [ $1 -eq 1 ]; then
  systemctl --no-reload enable sommelier@0.service >/dev/null 2>&1 ||:
  systemctl --no-reload enable sommelier@1.service >/dev/null 2>&1 ||:
  systemctl --no-reload enable sommelier-x@0.service >/dev/null 2>&1 ||:
  systemctl --no-reload enable sommelier-x@1.service >/dev/null 2>&1 ||:
fi

%{_sbindir}/update-alternatives --install %{_bindir}/sommelier sommelier /opt/google/cros-containers/bin/sommelier 1
%{_sbindir}/update-alternatives --install %{_libdir}/dri/swrast_dri swrast_dri /opt/google/cros-containers/lib/swrast_dri.so 1

%preun
if [ $1 -eq 0 ]; then
  systemctl --no-reload disable sommelier@0.service >/dev/null 2>&1 ||:
  systemctl --no-reload disable sommelier@1.service >/dev/null 2>&1 ||:
  systemctl --no-reload disable sommelier-x@0.service >/dev/null 2>&1 ||:
  systemctl --no-reload disable sommelier-x@1.service >/dev/null 2>&1 ||:
fi

%postun
if [ $1 -eq 0 ]; then
  %{_sbindir}/update-alternatives --remove sommelier /opt/google/cros-containers/bin/sommelier
  %{_sbindir}/update-alternatives --remove swrast_dri /opt/google/cros-containers/lib/swrast_dri.so
fi
