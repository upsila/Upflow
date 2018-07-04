import os
from collections import OrderedDict
import jsonschema
import yaml


class Workflow:
    def __init__(self):
        self.steps = OrderedDict()
        return

    def _run(self, job):
        raise NotImplementedError("This tool hasn't been impletemented yet")

    def run(self, job_json):
        self._validate_input(job_json)
        output = self._run(job_json)
        self._validate_output(output)
        return

    def _validate_input(self, job_json):
        __location__ = os.path.realpath(os.path.join(os.getcwd(),self.__class__.__module__))
        validator = Workflow.yml_to_json_current_dir(os.path.join(__location__,"input.yml"))
        jsonschema.validate(job_json,validator)
        return

    def _validate_output(self, job_json):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(self.__class__.__module__.replace('.','/'))))
        validator = Workflow.yml_to_json_current_dir(os.path.join(__location__,"output.yml"))
        jsonschema.validate(job_json,validator)

    @staticmethod
    def yml_to_json_current_dir(yml_file):
        with open(os.path.join(yml_file), 'r') as stream:
            validator_json = yaml.load(stream)
        return validator_json
