Name: cros-guest-tools
Version: 0.22
Release: 0.22%{?dist}
Summary: Metapackage for Chromium OS integration

License: BSD-3-Clause

Requires: cros-garcon
Requires: cros-notificationd
Requires: cros-sftp
Requires: cros-sommelier

Recommends: bash-completion
Recommends: bzip2
Recommends: cros-pulse-config
Recommends: cros-sommelier-config
Recommends: cros-sudo-config
Recommends: cros-systemd-overrides
Recommends: cros-ui-config
Recommends: cros-wayland
Recommends: curl
Recommends: dbus-x11
Recommends: file
Recommends: git
Recommends: gnupg
Recommends: iputils
Recommends: less
Recommends: libXScrnSaver
Recommends: man-db
Recommends: pulseaudio
Recommends: unzip
Recommends: usbutils
Recommends: vim
Recommends: wget

BuildArch: noarch

%description
This package has dependencies on all other packages necessary for Chromium OS integration.
