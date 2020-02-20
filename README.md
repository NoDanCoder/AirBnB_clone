# AirBnB clone project

![holberton](./hbnb.png)

---

## Description

For a make a clone for Airbnb product, you first make a console that is a first step for manupulate a storage system.

---

### Command interpreter Description

* The console runs in interactive mode as well.

    <code>$ ./console.py</code>

* The console runs in non-interactive mode as well.

    <code>$ echo "help" | ./console.py</code>

### Commands

Commands mostly use this form:

    (hbnb) <instance> <id> <...> <...>

## Create
Each instance is treated as an object within the console.

To create an instance you just have to write a command like the following:

    (hbnb) create BaseModel
    e4f9efcf-22cd-461f-8f7a-491ee70d8190
    (hbnb)

## Show
To see an instance you must use:

    (hbnb) show BaseModel e4f9efcf-22cd-461f-8f7a-491ee70d8190
    [BaseModel] (e4f9efcf-22cd-461f-8f7a-491ee70d8190) {'id': 'e4f9efcf-22cd-461f-8f7a-491ee70d8190', 'created_at': datetime.datetime(2020, 2, 19, 18, 46, 26, 448621), 'updated_at': datetime.datetime(2020, 2, 19, 18, 46, 26, 448670)}
    (hbnb)

## All
To list all instances created:

    (hbnb) all
    ["[BaseModel] (e4f9efcf-22cd-461f-8f7a-491ee70d8190) {'id': 'e4f9efcf-22cd-461f-8f7a-491ee70d8190', 'created_at': datetime.datetime(2020, 2, 19, 18, 46, 26, 448621), 'updated_at': datetime.datetime(2020, 2, 19, 18, 46, 26, 448670)}"]
    (hbtn) 

## Update
When you need update any atribute of you instance:

    (hbnb) update BaseModel e4f9efcf-22cd-461f-8f7a-491ee70d8190 first_name "Daniel"
    (hbnb) show BaseModel e4f9efcf-22cd-461f-8f7a-491ee70d8190
    [BaseModel] (e4f9efcf-22cd-461f-8f7a-491ee70d8190) {'id': 'e4f9efcf-22cd-461f-8f7a-491ee70d8190', 'created_at': datetime.datetime(2020, 2, 19, 18, 46, 26, 448621), 'updated_at': datetime.datetime(2020, 2, 19, 18, 55, 10, 376964), 'first_name': 'Daniel'}
    (hbnb)

## Destroy
To destroy an instance:

    (hbtn) destroy BaseModel e4f9efcf-22cd-461f-8f7a-491ee70d8190
    (hbtn) show BaseModel e4f9efcf-22cd-461f-8f7a-491ee70d8190
    ** no instance found **
    (hbtn) 

## Help && quit
If you have no idea what to do try using help, and to exit is quit.

    (hbtn) help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  create  destroy  help  quit  show  update

    (hbtn) quit
    $
