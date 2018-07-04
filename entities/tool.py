
from jsonschema import validate
import os
import shutil
from workflow import Workflow

class Tool:
    def __init__(self,name):
        self.name = name
        return

    def _run(self, input_data):
        raise NotImplementedError("This tool hasn't been impletemented yet")

    def get_input_json(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(self.__class__.__module__.replace('.','/'))))
        return Workflow.yml_to_json_current_dir(os.path.join(__location__,"input.yml"))


    def _validate(self, validator_yml,input_json):
        if os.path.isfile(validator_yml):
            __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(self.__class__.__module__.replace('.','/'))))
            validator_json = Workflow.yml_to_json_current_dir(os.path.join(__location__,validator_yml))
            validator_json['type'] = 'object'
            validate(input_json,validator_json)

    def run(self, input_json):
        self._validate("input.yml", input_json)
        output = self._run(input_json)
        self._validate("output.yml", output)
        return output

    @staticmethod
    def create(module_name, tool_name):
        module_path = os.path.join(os.getcwd(),'tools',module_name)
        if not os.path.isdir(module_path):
            os.mkdir(module_path)
        tool_path = os.path.join(module_path,tool_name)
        if os.path.isdir(tool_path):
            raise FileExistsError("The tool already exists")
        shutil.copytree("templates/tool",tool_path)

        with open(os.path.join(tool_path,'__init__.py'),'r') as f:
            newText = f.read().replace('ToolName',Tool.to_camel_case(tool_name.title()))

        with open(os.path.join(tool_path,'__init__.py'),'w') as f:
            f.write(newText)

    @staticmethod
    def to_camel_case(snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])
