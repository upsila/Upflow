
import jsonschema
from entities.tool import Tool

class Step:
    def __init__(self,workflow, tool, input, previous_step=None, next_step=None):
        self._previous_step = previous_step
        self._next_step = next_step
        self._tool = tool
        self._input = input
        self._status = "queued"
        self._output = None
        self._errors = []
        return

    def get_input(self):
        return self._input

    def get_output(self):
        return self._output

    def set_output(self, output):
        self._output = output

    def set_status(self, status):
        self._status = status
        return

    def get_status(self):
        return self._status

    def run(self):
        self._on_before_running()
        self.set_status('running')
        self.set_output(self._tool.run(self._input))
        self.set_status('completed')
        self._on_after_running()
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

    def set_previous_step(self, previous_step):
        self._previous_step = previous_step
        return

    def set_next_step(self, next_step):
        self._next_step = next_step
        return

    def get_previous_step(self):
        return self._previous_step

    def get_next_step(self):
        return self._next_step

