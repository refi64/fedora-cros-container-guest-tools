#!/bin/bash
# Copyright 2019 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

set -ex

. "$(dirname "$0")/common.sh" || exit 1
. "$(dirname "$0")/common_build.sh" || exit 1

main() {
    require_kokoro_artifacts

    build_guest_tools
    build_mesa
}

main "$@"
