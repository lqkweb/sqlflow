# coding=utf-8

import time
from dsl.nodes import NodeType

def execute_create_table(node):
    pass


def execute_show_tables(node):
    pass


def execute_insert(node):
    pass


def execute_drop_table(node):
    pass


def print_table(names, data):
    pass


def execute_print_table(node):
    pass


def execute_alert(node):
    pass


def execute_delete(node):
    pass


def set_value(data, names, set_list):
    # print "set_value() data:" + str(data)
    dict = {}
    for idx in range(len(names)): dict[names[idx]] = data[idx]
    left = set_list[0].attr_name
    a = __get_value(set_list[0], dict)
    b = __get_value(set_list[1], dict)

    if a != 'NULL' and b != 'NULL' and type(a) != type(b):
        raise Exception("Type not match")
    data[names.index(left)] = b


def execute_update(node):
    pass


def __dur(op=None, clock=[time.time()]):
    if op:
        duration = time.time() - clock[0]
        print('%s finished. Duration %.6f seconds.' % (op, duration))
    clock[0] = time.time()


def __can_use_index_select(table_name, where_node):
    pass


def __can_use_index_joint(table_name, where_node):
    pass


def execute_select(node, lexer, spark):
    data = spark.read.csv(
        "file:///Users/leiqiankun/PycharmProjects/sqlflow/data/data.csv",
        header=True)
    data.createOrReplaceTempView("A")
    if node.as_table:
        data.createOrReplaceTempView(node.as_table)
        datatem = spark.sql(lexer.lexdata.replace(";", "").split("as")[0])
        datat_response = datatem.rdd.collect()
        print(datat_response)
        return datat_response
    else:
        datatem = spark.sql(lexer.lexdata.replace(";", ""))
        datat_response = datatem.rdd.collect()
        print(datat_response)
        return datat_response


def execute_train(node, lexer, spark):
    pass


def execute_register(node, lexer, spark):
    pass


def execute_load(node, lexer, spark):
    pass


def execute_save(node, lexer, spark):
    pass


def execute_connect(node, lexer, spark):
    pass

def execute_set(node, lexer, spark):
    pass


def __get_value(node, dict):
    if node.type == NodeType.relation_attr:
        return dict[str(node)]
    else:
        return node.value


def __check_node(node, dict):
    assert (node.type == NodeType.condition)
    if node.op == "AND":
        return __check_node(node.left, dict) and __check_node(node.right, dict)
    elif node.op == "OR":
        return __check_node(node.left, dict) or __check_node(node.right, dict)
    elif node.op == ">=":
        return __get_value(node.left, dict) >= __get_value(node.right, dict)
    elif node.op == "<=":
        return __get_value(node.left, dict) <= __get_value(node.right, dict)
    elif node.op == ">":
        return __get_value(node.left, dict) > __get_value(node.right, dict)
    elif node.op == "<":
        return __get_value(node.left, dict) < __get_value(node.right, dict)
    elif node.op == "=":
        return __get_value(node.left, dict) == __get_value(node.right, dict)
    elif node.op == "!=":
        return __get_value(node.left, dict) != __get_value(node.right, dict)


def check_where(where_node, part_names, data_line, full_names=None):
    assert len(part_names) == len(data_line)
    if not where_node: return True
    dict = {}
    for idx in range(len(part_names)):
        dict[part_names[idx]] = data_line[idx]
    if full_names:
        for idx in range(len(full_names)):
            dict[full_names[idx]] = data_line[idx]
    return __check_node(where_node, dict)


def execute_create_index(node):
    pass


def execute_drop_index(node):
    pass


def __check_power(node_type, table_list):
    pass


def execute_create_user(node):
    pass


def execute_grant_user(node):
    pass


def execute_revoke_user(node):
    pass


def execute_main(command, lexer, spark):
    if command.type == NodeType.select:
        return execute_select(command, lexer, spark)
    elif command.type == NodeType.train:
        return execute_train(command, lexer, spark)
    elif command.type == NodeType.register:
        return execute_register(command, lexer, spark)
    elif command.type == NodeType.load:
        return execute_load(command, lexer, spark)
    elif command.type == NodeType.save:
        return execute_save(command, lexer, spark)
    elif command.type == NodeType.connect:
        return execute_connect(command, lexer, spark)
    elif command.type == NodeType.set:
        return execute_set(command, lexer, spark)
