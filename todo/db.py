import os
import json
import sqlite3

# From: https://goo.gl/YzypOI
def singleton(cls):
  instances = {}
  def getinstance():
    if cls not in instances:
      instances[cls] = cls()
    return instances[cls]
  return getinstance

class DB(object):
  """
  DB driver for the Todo app - deals with writing entities
  to the DB and reading entities from the DB
  """

# To use the sqlite3 module, you must first create a Connection object that represents the database.
# Here the data will be stored in the todo.db file:
  def __init__(self):
    self.conn = sqlite3.connect("todo.db", check_same_thread=False)
    # self.example_create_table() # Delete this line when implementing
    self.create_task_table()

  def create_task_table(self):
    try:
      self.conn.execute("""
        CREATE TABLE task (
        ID INT PRIMARY KEY NOT NULL,
        NAME VARCHAR(255) NOT NULL,
        CREATED_AT DATETIME NOT NULL,
        DESCRIPTION TEXT NOT NULL,
        DUE_DATE DATETIME NOT NULL,
        TAGS CHAR(50) NOT NULL)
      """)
    except Exception as e: print e


  def insert_task(self, id, name, created_at, description, due_date, tags):
    self.conn.execute("""
      INSERT INTO task (ID,NAME,CREATED_AT,DESCRIPTION,DUE_DATE,TAGS)
      VALUES (?, ?, ?, ?, ?, ?)
    """, (id, name, created_at, description, due_date, tags))
    # commit = save the change
    self.conn.commit()

  def delete_task_table(self):
    try:
      self.conn.execute("""
        DROP TABLE task
      """)
    except Exception as e: print e

  def query(self):
      # creating a cursor object and calling its execute method to perform SQL commands
      # a cursor can be thought of as a pointer to a specific row within a query result
      # The reason you may need to use a database cursor is that
      # you need to perform actions on individual rows.
    cursor = self.conn.execute("""
      SELECT * FROM task;
    """)
    alltasks = []
    for row in cursor:
        mydict = {}
        mydict["id"]= row[0]
        mydict["name"]=row[1]
        mydict["created_at"]=row[2]
        mydict["description"]=row[3]
        mydict["due_date"]=row[4]
        mydict["tags"]=row[5]
        alltasks.append(mydict)
    return alltasks

  def query_id(self,id):
      # The SELECT clause specifies the table columns that are retrieved.
      # The FROM clause specifies the tables accessed.
      # The WHERE clause specifies which table rows are used.
      # The WHERE clause is optional; if missing, all table rows are used.
    cursor = self.conn.execute("""
      SELECT * FROM task WHERE ID = (?)
    """,(id,))
    alltasks = []
    for row in cursor:
        mydict = {}
        mydict["id"]= row[0]
        mydict["name"]=row[1]
        mydict["created_at"]=row[2]
        mydict["description"]=row[3]
        mydict["due_date"]=row[4]
        mydict["tags"]=row[5]
        alltasks.append(mydict)
    return alltasks

  def delete_all_tasks(self):
    self.conn.execute("""
      DELETE FROM task
    """)
    self.conn.commit()

  def delete_task_id(self, id):
    self.conn.execute("""
      DELETE FROM task WHERE ID = ?
    """, (id,))
    self.conn.commit()



# Only <=1 instance of the DB driver
# exists within the app at all times
DB = singleton(DB)
