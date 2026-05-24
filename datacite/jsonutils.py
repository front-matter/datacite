# SPDX-FileCopyrightText: 2016 CERN.
# SPDX-FileCopyrightText: 2025 Graz University of Technology.
# SPDX-License-Identifier: BSD-3-Clause

"""JSON utilities."""

import json

from jsonresolver.contrib.jsonschema import RefResolverBase
from jsonschema.validators import validator_for


def validator_factory(schema_filename):
    """Provide a JSON schema validator for a given schema file."""
    with open(schema_filename, "r") as fp:
        schema = json.load(fp)

    validator_cls = validator_for(schema)
    validator_cls.check_schema(schema)

    return validator_cls(
        schema, resolver=RefResolverBase("file:{}".format(schema_filename), schema)
    )
