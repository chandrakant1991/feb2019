# Database Connection
# 1) create sqlite3 database.
# 2) Database Connecton
# 3)
###########################################################
# 1) Create Database
###########################################################

import sqlite3
db =sqlite3.connect("class_11.db")
cur = db.cursor()
USERS = {
    'id': 'INTEGER PRIMARY KEY',
    'name': 'TEXT',
    'phone': 'TEXT',
    'email': 'TEXT unique',
    'password': 'TEXT',
}
command = "CREATE TABLE IF NOT EXISTS user("
command += ",".join([
    "{} {}".format(key, value) for key, value in USERS.items()
])
command += ")"
cur.execute(command)
db.close()


class DatabaseORM(object):
    """
    Database ORM
    """
    def __init__(self):
        """
        initialize class objects
        """
        self.con = None
        self.cur = None
        self.data = None
        self.database_info = dict()
        self.methods ={
            'create_table': self.create_table,
            'insert_record': self.insert_record
        }
    def main(self, **kwargs):
        """Main method of class"""
        self.create_db_connection()
        self.create_cursor()
        self.data = kwargs.get('data')
        method= kwargs.get('method')
        if method not in self.methods:
            return {
                'status':False,
                'message': 'Method does not supported.'
            }
        self.methods.get(method)()
    def create_db_connection(self):
        # """
        # create Database Connection
        # :return:
        # """"
       self.con = sqlite3.connect("class_11.db")
    def create_cursor(self):
        """create Dadtabase cursor
        """
        self.cur = self.con.cursor()
    def generate_create_table_command(self):
        """
        Generate create table command based on self.data
        :return:
        """
        statement = "CREATE TABLE IF NOT EXISTS {}(".format(
            self.data.get('table_name'))
        statement += ",".join([
            "{} {}".format(key, value)
                           for key, value in self.data.get('table_structure').items()
        ])
        statement += ")"
        return statement
    def create_table(self):
        """
        Create Table
        :return:
        """
        # print('Create table')
        command = self.generate_create_table_command()
        try:
            self.cur.execute(command)
            print("Table has been created")
        except Exception as err:
            print("Due to following error table has not created\n{err}")
    def generate_insert_statement(self):
        """
        Generate insert statement based on the provided data
        :return:
        """
        insert_data = self.data.get('insert_data')
        _fields = ", ".join([
            field for field in self.data.get('insert_data').keys()])
        place_holder = ", ".join(['?' for value in insert_data.values()])
        return F"INSERT INTO {self.data.get('table_name')}({_fields})"\
        F"VALUES({place_holder})"
        # "insert into <>"

    def insert_recor(self):
        """
        Insert record in specific record
        :return:
        """
        command = self.generate_insert_statement()
        self.cur.execute(command, tuple())
        print(command)
        # print('Insert record')

    def __del__(self):
        self.con.close()
DatabaseORM().main(**{
    'method': 'create_table',
    'data': {
        'table_name': 'user',
        'table_structure':{
            'id': 'INTEGER PRIMARY KEY',
            'name': 'TEXT',
            'phone': 'TEXT',
            'email': 'TEXT unique',
            'password': 'TEXT',
        }
    }
})
