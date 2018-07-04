#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from entities.tool import Tool
import json
import argparse
import sys

class PrintString(Tool):
    def __init__(self):
        Tool.__init__(self, type(self).__name__)
        return

    def _run(self, input_data):
        print(input_data.get('value'))
        return {'value':input_data.get('input_data')}


def main(argv):
    tool = PrintString()
    tool.run(argv)
    return 0

if __name__ == "__main__":
    main()