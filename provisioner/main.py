#!/usr/bin/env python3
"""
opennms-provisioner main module

This is the main module of opennms-provisioner

:license: MIT, see LICENSE for more details
:copyright: (c) 2018 by Michael Batz, see AUTHORS for more details
"""

import sys
import opennms

def main():
    """main function"""
    print("Sample Project")

    # testing
    testnode = opennms.Node("testnode.example.net", "1")
    testnode.add_interface("127.0.0.1")
    testnode.add_asset("city", "Fulda")
    testnode.add_asset("zip", "36041")
    testnode.add_category("Test")
    print(testnode.get_xml_string())
    testrequisition = opennms.Requisition("test")
    testrequisition.add_node(testnode)
    print(testrequisition.get_xml_string())


if __name__ == "__main__":
    main()