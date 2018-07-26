from session.abstract_class import PysparkPro


class DslAdaptor(object):
    pysparkpro = PysparkPro()
    select = 'SELECT'
    insert = 'INSERT'
    delete = 'DELETE'
    update = 'UPDATE'
    alert = 'ALERT'
    create_table = 'CREATETABLE'
    drop_table = 'DROPTABLE'
    create_index = 'CREATEINDEX'
    drop_index = 'DROPTABLE'
    create_user = 'CREATEUSER'
    exit = 'EXIT'
    print_table = 'PRINT'
    show_tables = 'SHOW'
    value = 'VALUE'
    condition = 'CONDITION'
    relation_attr = 'RELATTR'
    grant_user = 'GRANTUSER'
    revoke_user = 'REVOKEUSER'
    attr_type = "ATTRTYPE"


class ConnectNode():
    def __init__(self, select_list, from_list, where_list):
        self.type = DslAdaptor.select
        self.select_list = select_list
        self.from_list = from_list
        self.where_list = where_list


class CreateNode():
    def __init__(self, select_list, from_list, where_list):
        self.type = DslAdaptor.select
        self.select_list = select_list
        self.from_list = from_list
        self.where_list = where_list


class InsertNode():
    def __init__(self, select_list, from_list, where_list):
        self.type = DslAdaptor.select
        self.select_list = select_list
        self.from_list = from_list
        self.where_list = where_list


class LoadNode():
    def __init__(self, select_list, from_list, where_list):
        self.type = DslAdaptor.select
        self.select_list = select_list
        self.from_list = from_list
        self.where_list = where_list


class RefreshNode():
    def __init__(self, select_list, from_list, where_list):
        self.type = DslAdaptor.select
        self.select_list = select_list
        self.from_list = from_list
        self.where_list = where_list


class RegisterNode():
    def __init__(self, select_list, from_list, where_list):
        self.type = DslAdaptor.select
        self.select_list = select_list
        self.from_list = from_list
        self.where_list = where_list


class SaveNode():
    def __init__(self, select_list, from_list, where_list):
        self.type = DslAdaptor.select
        self.select_list = select_list
        self.from_list = from_list
        self.where_list = where_list


class ScriptNode():
    def __init__(self, select_list, from_list, where_list):
        self.type = DslAdaptor.select
        self.select_list = select_list
        self.from_list = from_list
        self.where_list = where_list


class SelectNode():
    def __init__(self, select_list, from_list, where_list):
        self.type = DslAdaptor.select
        self.select_list = select_list
        self.from_list = from_list
        self.where_list = where_list


class SetNode():
    def __init__(self, select_list, from_list, where_list):
        self.type = DslAdaptor.select
        self.select_list = select_list
        self.from_list = from_list
        self.where_list = where_list


class TrainNode():
    def __init__(self, select_list, from_list, where_list):
        self.type = DslAdaptor.select
        self.select_list = select_list
        self.from_list = from_list
        self.where_list = where_list


class Exit:
    def __init__(self):
        self.type = DslAdaptor.exit


class PrintTable:
    def __init__(self, table_name):
        self.type = DslAdaptor.print_table
        self.table_name = table_name


class ShowTables:
    def __init__(self):
        self.type = DslAdaptor.show_tables


class Value:
    def __init__(self, value_type, value):
        self.type = DslAdaptor.value
        self.value_type = value_type
        self.value = value

    def __str__(self):
        return str(self.value) + '[' + self.value_type + ']'


class RelAttr:
    def __init__(self, attr_name, table_name=None):
        self.type = DslAdaptor.relation_attr
        self.table_name = table_name
        self.attr_name = attr_name

    def __str__(self):
        if self.table_name:
            return self.table_name + '.' + self.attr_name
        else:
            return self.attr_name


class Cond:
    def __init__(self, left, op, right):
        self.type = DslAdaptor.condition
        self.op = op.upper()
        self.left = left
        self.right = right

    def __str__(self):
        return '(' + str(self.left) + ', ' + str(self.right) + ', ' + self.op + ')'


class AttrType:
    def __init__(self, attr_name, attr_type, type_len = 1):
        self.type = DslAdaptor.attr_type
        self.attr_type = attr_type
        self.type_len = type_len
        self.attr_name = attr_name

    def __str__(self):
        return self.attr_name + " " + self.attr_type + " " + str(self.type_len)

if __name__ == '__main__':
    spark = DslAdaptor()
    print(spark)
