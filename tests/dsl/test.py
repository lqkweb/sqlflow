# coding=utf-8
from dsl.lexer import lexer
from dsl.parser import parser
from abstract_class import PysparkPro

create_table_test = """
create table A (
  id int,
  name char(10),
  age int,
  grade int
);
"""

select_test = "select * from A where x>5 as b;"

insert_test = "insert into A values(5, 'c', 33, 24), (6, 'd', 33, 11);"

delete_test = "delete from A where id = 1;"

update_test = "update A set age = 1 where id = 2;"

print_test = "print A;"

alert_add_test = "alert table A add num char(20);"

alert_drop_test = "alert table A drop num;"

drop_table_test = "drop table mumu;"


def test_big():
    f = open("test.txt", 'w')
    for i in range(10000):
        f.write(str(i) + " " + str(i) + "\n")
    f.close()


def exec_sql(sql, spark):
    res = parser.parse(sql, lexer=lexer)
    from main import execute_main
    execute_main(res, lexer, spark)


if __name__ == '__main__':
    spark = PysparkPro().pysparkpro
    # sql = input("请输入>")
    exec_sql(select_test, spark)
# exec_sql("drop user tyh password 'tyh';")
# exec_sql("insert into big values(1, 1), (2 ,2);")

# exec_sql("print B;")
# exec_sql("select B.id, A.id from B, A where B.id > 2 and B.id > A.id;")
