# -*- coding: utf-8 -*-
#
# This module stores the version and changelog

# Version number
__version__ = '1.2.0'

# Change log
def changelog():
    log = """
    LSMTool Changelog.
    -----------------------------------------------

    2017/06/15 - Version 1.2.0

    2017/05/09

        Add a "pad_index" option to lsm.group() to allow the patch index to be
        padded with leading zeros

    2017/05/05

        Improve the "tessellate" grouping algorithm when negative fluxes are
        present

    2017/04/21

        Add support for LogarithmicSI column

        Add a "voronoi" option to lsm.group() to allow a previously grouped sky
        model to be regrouped using Voronoi tessellation

    2016/01/28 - Version 1.1.0

        Add support for FACTOR-formatted output

    2014/06/25 - Version 1.0.0 (initial release)
    """

    print(log)
