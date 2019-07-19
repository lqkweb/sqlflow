# coding=utf-8

import ply.yacc as yacc
from dsl.nodes import *
from dsl import lexer

# Get the token map.
tokens = lexer.tokens

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'LE', 'LE', 'GE', 'GT', 'EQ', 'NE'),
    # Nonassociative operators
)


def p_start(p):
    """ start : command
              | command ';' """
    p[0] = p[1]


def p_command(p):
    """ command : ddl
                | dml
                | utility
                | nothing """
    p[0] = p[1]


def p_ddl(p):
    """ ddl : createtable
            | createindex
            | droptable
            | dropindex
            | showtables
            | alerttable
            | createuser
            | grantuser
            | revokeuser """
    p[0] = p[1]


def p_dml(p):
    """ dml : query
            | insert
            | delete
            | update
            | train
            | register
            | load
            | save
            | connect
            | set """
    p[0] = p[1]


def p_utility(p):
    """ utility : exit
                | print """
    p[0] = p[1]



def p_nothing(p):
    """ nothing : """
    p[0] = None



def p_createtable(p):
    """ createtable : CREATE TABLE ID '(' non_mattrtype_list ')' """
    p[0] = CreateTableNode(p[3], p[5])


def p_createindex(p):
    """ createindex : CREATE INDEX ID '(' ID ')' """
    p[0] = CreateIndexNode(p[3], p[5])


def p_droptable(p):
    """ droptable : DROP TABLE ID """
    p[0] = DropTableNode(p[3])


def p_dropindex(p):
    """ dropindex : DROP INDEX ID '(' ID ')' """
    p[0] = DropIndexNode(p[3], p[5])


def p_showtables(p):
    """ showtables : SHOW TABLES """
    p[0] = ShowTables()


def p_alerttable(p):
    """ alerttable : ALERT TABLE ID ADD attrtype
                   | ALERT TABLE ID DROP non_mrelation_list """
    if p[4].upper() == 'ADD':
        p[0] = AlertNode(p[3], 'ADD', p[5])
    else:
        p[0] = AlertNode(p[3], 'DROP', p[5])


def p_createuser(p):
    """ createuser : CREATE USER ID PASSWORD STRING"""
    p[0] = CreateUserNode(p[3], p[5])


def p_grantuser(p):
    """ grantuser : GRANT power_list ON non_mrelation_list TO non_mrelation_list """
    p[0] = GrantUserNode(p[2], p[4], p[6])


def p_revokeuser(p):
    """ revokeuser : REVOKE power_list ON non_mrelation_list FROM non_mrelation_list """
    p[0] = RevokeUserNode(p[2], p[4], p[6])


def p_query(p):
    """ query : SELECT non_mselect_clause FROM non_mrelation_list opwhere_clause oplimit_clause opas_clause """
    p[0] = QueryNode(p[2], p[4], p[5], p[6], p[7])


def p_insert(p):
    """ insert : INSERT INTO ID VALUES inservalue_list """
    p[0] = InsertNode(p[3], p[5])


def p_delete(p):
    """ delete : DELETE FROM ID opwhere_clause """
    p[0] = DeleteNode(p[3], p[4])


def p_update(p):
    """ update : UPDATE ID SET relattr EQ relattr_or_value opwhere_clause """
    p[0] = UpdateNode(p[2], (p[4], p[6]), p[7])


def p_train(p):
    """ train : TRAIN non_mselect_clause opas_clause """
    p[0] = TrainNode(p[2], p[3])


def p_register(p):
    """ register : REGISTER non_mselect_clause opas_clause """
    p[0] = RegisterNode(p[2], p[3])


def p_load(p):
    """ load : LOAD non_mselect_clause opas_clause """
    p[0] = LoadNode(p[2], p[3])


def p_save(p):
    """ save : SAVE OVERWRITE TABLE opas_clause """
    p[0] = SaveNode(p[4])


def p_connect(p):
    """ connect : CONNECT JDBC opwhere_clause """
    p[0] = ConnectNode(p[3])


def p_set(p):
    """ set : SET non_mselect_clause opas_clause """
    p[0] = SetNode(p[2], p[3])

def p_power_list(p):
    """ power_list : power_list ',' power_type
                   | power_type """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_power_type(p):
    """  power_type : SELECT
                    | UPDATE
                    | INSERT
                    | DELETE
                    | PRINT
                    | ALL
    """
    p[0] = p[1].upper()



def p_print(p):
    """ print : PRINT ID """
    p[0] = PrintTable(p[2])


def p_exit(p):
    """ exit : EXIT """
    p[0] = Exit()





def p_inservalue_list(p):
    """ inservalue_list : '(' non_mvalue_list ')' ',' inservalue_list
                        | '(' non_mvalue_list ')' """
    if len(p) > 4:
        p[0] = [p[2]] + p[5]
    else:
        p[0] = [p[2]]





def p_non_mattrtype_list(p):
    """ non_mattrtype_list : attrtype ',' non_mattrtype_list
                           | attrtype """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_attrtype(p):
    """ attrtype : ID type
                 | ID type '(' NUMBER ')'
                 | PRIMARY KEY '(' ID ')' """
    if len(p) == 3:
        p[0] = AttrType(p[1], p[2])
    elif p[1].upper() == "PRIMARY":
        p[0] = AttrType(p[4], 'PK')
    else:
        p[0] = AttrType(p[1], p[2], p[4])


def p_type(p):
    """ type : INT
             | CHAR """
    p[0] = p[1].upper()


def p_non_mselect_clause(p):
    """ non_mselect_clause : non_mrelattr_list
                           | '*' """
    p[0] = p[1]


def p_non_mrelattr_list(p):
    """ non_mrelattr_list : relattr ',' non_mrelattr_list
                          | relattr """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_relattr(p):
    """ relattr : ID '.' ID
                | ID """
    if len(p) == 2:
        p[0] = RelAttr(p[1])
    else:
        p[0] = RelAttr(p[3], p[1])


def p_non_mrelation_list(p):
    """ non_mrelation_list : relation ',' non_mrelation_list
                           | relation """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_relation(p):
    """ relation : ID """
    p[0] = p[1]


def p_opwhere_clause(p):
    """ opwhere_clause : WHERE non_mcond_list
                       | nothing """
    if len(p) == 3:
        p[0] = p[2]


def p_oplimit_clause(p):
    """ oplimit_clause : LIMIT value
                        | nothing """
    if len(p) == 3:
        p[0] = p[2]


def p_opas_clause(p):
    """ opas_clause : AS ID
                    | nothing """
    if len(p) == 3:
        p[0] = p[2]


def p_non_mcond_list(p):
    """ non_mcond_list : non_mcond_list AND non_mcond_list
                       | non_mcond_list OR  non_mcond_list
                       | '(' non_mcond_list ')'
                       | condition """
    if len(p) == 2:
        p[0] = p[1]
    elif p[1] == '(':
        p[0] = p[2]
    else:
        p[0] = Cond(p[1], p[2], p[3])


def p_condition(p):
    """ condition : relattr op relattr_or_value
                  | relattr EQ null_value
                  | relattr NE null_value """
    p[0] = Cond(p[1], p[2], p[3])


def p_relattr_or_value(p):
    """ relattr_or_value : relattr
                         | value """
    p[0] = p[1]


def p_non_mvalue_list(p):
    """ non_mvalue_list : value ',' non_mvalue_list
                        | value
                        | null_value ',' non_mvalue_list
                        | null_value """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_value_string(p):
    """ value : STRING """
    p[0] = Value('STRING', p[1])


def p_value_number(p):
    """ value : NUMBER """
    p[0] = Value('NUMBER', p[1])


def p_null_value(p):
    """ null_value : NULL """
    p[0] = Value('NULL', None)


def p_op(p):
    """ op : LT
           | LE
           | GT
           | GE
           | EQ
           | NE """
    p[0] = p[1]



# Error rule for syntax errors
def p_error(p):
    if not p:
        print("Syntax error, missing something (maybe ';').")
    else:
        print("Syntax error at token '%s'(%s)" % (p.value, p.type))


# Build the parser
from dsl.lexer import lexer as lex

parser = yacc.yacc(debug=True)

if __name__ == '__main__':
    while True:
        try:
            s = input('Parser > ')
        except EOFError:
            break
        if not s: continue
        try:
            result = parser.parse(s, lexer=lex)
        except Exception as e:
            print(e)
