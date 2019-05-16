#!/bin/bash
# Copyright 2018 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

set -ex

. "$(dirname "$0")/common.sh" || exit 1

main() {
    require_kokoro_artifacts
    require_cros_milestone

    local src_root="${KOKORO_ARTIFACTS_DIR}"/git/cros-container-guest-tools
    local result_dir="${src_root}"/apt
    mkdir -p "${result_dir}"

    cp -r "${KOKORO_GFILE_DIR}"/apt_signed/* "${result_dir}"
}

main "$@"
