from dsl.nodesbak import DslAdaptor


def execute_select(command):
    pass


def execute_main(command):
    if command.type == DslAdaptor.select:
        execute_select(command)