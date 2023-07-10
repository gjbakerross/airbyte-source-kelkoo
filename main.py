#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_kelkoo_statistics import SourceKelkooStatistics

if __name__ == "__main__":
    source = SourceKelkooStatistics()
    launch(source, sys.argv[1:])
