#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2015-2020 CERN.
# SPDX-License-Identifier: MIT

# Run tests with real HTTP calls to Datacite REST APIs to their test endpoint.

# Quit on errors
set -o errexit

if [ -z "${DATACITE_USER}" ] || [ -z "${DATACITE_PW}" ] || [ -z "${DATACITE_PREFIX}" ]; then
  echo "DATACITE_USER, DATACITE_PW or DATACITE_PREFIX env var not set"
  exit 1
fi

python -m pytest --runpw
