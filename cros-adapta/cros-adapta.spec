Name: cros-adapta
Version: 3.0
Release: 3.0%{?dist}
Summary: Chromium OS GTK Theme

License: BSD-3-Clause

BuildArch: noarch

%description
This package provides symlinks which link the bind-mounted theme into the
correct location in the container.

%post
if [ $1 == 1 ]; then
  ln -s /opt/google/cros-containers/cros-adapta %{_datadir}/themes/CrosAdapta
fi

%preun
if [ $1 == 0 ]; then
  rm %{_datadir}/themes/CrosAdapta
fi
