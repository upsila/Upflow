
from entities.tool import Tool

class Step:
    def __init__(self,workflow, tool, input):
        self._workflow = workflow
        self._tool = tool
        self._input = input
        self._status = "queued"
        self._output = None
        return

    def get_input(self):
        return self._input

    def get_output(self):
        return self._output

    def set_output(self, output):
        self._output = output
        return

    def set_status(self, status):
        self._status = status
        return

    def get_status(self):
        return self._status

    def set_workflow(self, workflow):
        self._workflow = workflow
        return

    def get_workflow(self):
        return self._workflow

    def run(self):
        self.set_status('running')
        self.set_output(self._tool.run(self._input))
        self.set_status('completed')
        return self

    def set_tool(self, tool):
        """
        :return: The message
        :rtype: Tool
        """
        self._tool = tool
        return

    def get_tool(self):
        return self._tool
