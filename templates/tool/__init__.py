#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from entities.tool import Tool


class ToolName(Tool):
    def __init__(self):
        Tool.__init__(self, type(self).__name__)
        return

    def _run(self, input_data):
        return {}


def main(argv):
    tool = ToolName()
    tool.run(argv)
    return 0

if __name__ == "__main__":
    main()