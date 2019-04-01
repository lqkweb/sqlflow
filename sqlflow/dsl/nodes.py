# coding=utf-8


class NodeType:
    sparksql = 'SPARKSQL'
    select = 'SELECT'
    insert = 'INSERT'
    delete = 'DELETE'
    update = 'UPDATE'
    train = 'TRAIN'
    register = 'REGISTER'
    load = 'LOAD'
    save = 'SAVE'
    connect = 'CONNECT'
    set = 'SET'
    alert = 'ALERT'
    create_table = 'CREATETABLE'
    drop_table = 'DROPTABLE'
    create_index = 'CREATEINDEX'
    drop_index = 'DROPINDEX'
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


class QueryNode:
    def __init__(self, select_list, from_list, where_list, limit_num, as_table):
        self.type = NodeType.select
        self.select_list = select_list
        self.from_list = from_list
        self.where_list = where_list
        self.limit_num = limit_num
        self.as_table = as_table


class SPARKSQLNode:
    def __init__(self, select_list):
        self.type = NodeType.select
        self.select_list = select_list


class LoadNode:
    def __init__(self, where_list, table_id):
        self.type = NodeType.load
        self.where_list = where_list
        self.table_id = table_id


class SaveNode:
    def __init__(self, table_id):
        self.type = NodeType.save
        self.table_id = table_id


class ConnectNode:
    def __init__(self, table_id):
        self.type = NodeType.connect
        self.table_id = table_id


class SetNode:
    def __init__(self, where_list, table_id):
        self.type = NodeType.set
        self.where_list = where_list
        self.table_id = table_id


class InsertNode:
    def __init__(self, table_name, value_list):
        self.type = NodeType.insert
        self.table_name = table_name
        self.value_list = value_list


class DeleteNode:
    def __init__(self, table_name, where_list):
        self.type = NodeType.delete
        self.table_name = table_name
        self.where_list = where_list


class UpdateNode:
    def __init__(self, table_name, set_list, where_list):
        self.type = NodeType.update
        self.table_name = table_name
        self.set_list = set_list
        self.where_list = where_list


class TrainNode:
    def __init__(self, set_list, where_list):
        self.type = NodeType.train
        self.set_list = set_list
        self.where_list = where_list


class RegisterNode:
    def __init__(self, set_list, where_list):
        self.type = NodeType.register
        self.set_list = set_list
        self.where_list = where_list


class AlertNode:
    def __init__(self, table_name, op, attr_list):
        self.type = NodeType.alert
        self.table_name = table_name
        self.op = op
        self.attr_list = attr_list


class CreateTableNode:
    def __init__(self, table_name, attr_list):
        self.type = NodeType.create_table
        self.table_name = table_name
        self.attr_list = attr_list


class DropTableNode:
    def __init__(self, table_name):
        self.type = NodeType.drop_table
        self.table_name = table_name


class CreateIndexNode:
    def __init__(self, table_name, attr_name):
        self.type = NodeType.create_index
        self.table_name = table_name
        self.attr_name = attr_name


class DropIndexNode:
    def __init__(self, table_name, attr_name):
        self.type = NodeType.drop_index
        self.table_name = table_name
        self.attr_name = attr_name


class CreateUserNode:
    def __init__(self, user_id, password):
        self.type = NodeType.create_user
        self.user_id = user_id
        self.password = password


class GrantUserNode:
    def __init__(self, power_list, table_list, user_list):
        self.type = NodeType.grant_user
        self.power_list = power_list
        self.table_list = table_list
        self.user_list = user_list


class RevokeUserNode:
    def __init__(self, power_list, table_list, user_list):
        self.type = NodeType.revoke_user
        self.power_list = power_list
        self.table_list = table_list
        self.user_list = user_list


class Exit:
    def __init__(self):
        self.type = NodeType.exit


class PrintTable:
    def __init__(self, table_name):
        self.type = NodeType.print_table
        self.table_name = table_name


class ShowTables:
    def __init__(self):
        self.type = NodeType.show_tables


class Value:
    def __init__(self, value_type, value):
        self.type = NodeType.value
        self.value_type = value_type
        self.value = value

    def __str__(self):
        return str(self.value) + '[' + self.value_type + ']'


class RelAttr:
    def __init__(self, attr_name, table_name=None):
        self.type = NodeType.relation_attr
        self.table_name = table_name
        self.attr_name = attr_name

    def __str__(self):
        if self.table_name:
            return self.table_name + '.' + self.attr_name
        else:
            return self.attr_name


class Cond:
    def __init__(self, left, op, right):
        self.type = NodeType.condition
        self.op = op.upper()
        self.left = left
        self.right = right

    def __str__(self):
        return '(' + str(self.left) + ', ' + str(
            self.right) + ', ' + self.op + ')'


class AttrType:
    def __init__(self, attr_name, attr_type, type_len=1):
        self.type = NodeType.attr_type
        self.attr_type = attr_type
        self.type_len = type_len
        self.attr_name = attr_name

    def __str__(self):
        return self.attr_name + " " + self.attr_type + " " + str(self.type_len)
