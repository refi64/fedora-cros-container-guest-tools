#!/bin/bash
# Copyright 2019 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

set -ex

build_guest_tools() {
    local src_root="${KOKORO_ARTIFACTS_DIR}"/git/cros-container-guest-tools
    local result_dir="${src_root}"/guest_debs
    mkdir -p "${result_dir}"

    cd "${src_root}"

    # Build all targets.
    bazel build //...

    # Copy resulting debs to results directory.
    chmod 644 bazel-bin/*/*.deb
    cp bazel-bin/*/*_*.deb "${result_dir}"
}

build_mesa() {
    local base_image="buildmesa"
    local base_image_tarball="${KOKORO_GFILE_DIR}"/"${base_image}".tar.xz

    if [[ "$(docker images -q ${base_image} 2> /dev/null)" == "" ]]; then
        docker load -i "${base_image_tarball}"
    fi

    docker run \
        --rm \
        --privileged \
        -v "${KOKORO_ARTIFACTS_DIR}"/mesa_debs:/artifacts \
        "${base_image}" \
        ./sync-and-build.sh
}
