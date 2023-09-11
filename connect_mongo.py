from pymongo import MongoClient

def connect_mongo_dev_project():
    CONNECTION_STRING = "mongodb+srv://icodeinnovahostingservice:root@cluster0.grjviix.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db_Name = client['authentication']
    collection_name = db_Name["project"]
    return collection_name

def connect_mongo_dev_user():
    CONNECTION_STRING = "mongodb+srv://icodeinnovahostingservice:root@cluster0.grjviix.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db_Name = client['authentication']
    collection_name = db_Name["user"]
    return collection_name

def connect_mongo_dev_admin():
    CONNECTION_STRING = "mongodb+srv://icodeinnovahostingservice:root@cluster0.grjviix.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db_Name = client['authentication']
    collection_name = db_Name["admin"]
    return collection_name

def connect_mongo_dev_scheduel_notification():
    CONNECTION_STRING = "mongodb+srv://icodeinnovahostingservice:root@cluster0.grjviix.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db_Name = client['authentication']
    collection_name = db_Name["scheduel_notifications"]
    return collection_name

# *********** BETA ****************

def connect_mongo_beta_project():
    CONNECTION_STRING = "mongodb+srv://icodeinnovahostingservice:Zoj6QtEQAnoeC9yy@i2auth.phgrf0g.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db_Name = client['authentication']
    collection_name = db_Name["project"]
    return collection_name

def connect_mongo_beta_user():
    CONNECTION_STRING = "mongodb+srv://icodeinnovahostingservice:Zoj6QtEQAnoeC9yy@i2auth.phgrf0g.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db_Name = client['authentication']
    collection_name = db_Name["user"]
    return collection_name

def connect_mongo_beta_admin():
    CONNECTION_STRING = "mongodb+srv://icodeinnovahostingservice:Zoj6QtEQAnoeC9yy@i2auth.phgrf0g.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db_Name = client['authentication']
    collection_name = db_Name["admin"]
    return collection_name

def connect_mongo_beta_scheduel_notification():
    CONNECTION_STRING = "mongodb+srv://icodeinnovahostingservice:Zoj6QtEQAnoeC9yy@i2auth.phgrf0g.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db_Name = client['authentication']
    collection_name = db_Name["scheduel_notifications"]
    return collection_name

# *************** PROD ******************

def connect_mongo_prod_project():
    CONNECTION_STRING = "mongodb+srv://icodeinnovahostingservice:eNZgEomXNOwBNztW@i2auth.nfdhtlq.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db_Name = client['authentication']
    collection_name = db_Name["project"]
    return collection_name

def connect_mongo_prod_user():
    CONNECTION_STRING = "mongodb+srv://icodeinnovahostingservice:eNZgEomXNOwBNztW@i2auth.nfdhtlq.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db_Name = client['authentication']
    collection_name = db_Name["user"]
    return collection_name

def connect_mongo_prod_admin():
    CONNECTION_STRING = "mongodb+srv://icodeinnovahostingservice:eNZgEomXNOwBNztW@i2auth.nfdhtlq.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db_Name = client['authentication']
    collection_name = db_Name["admin"]
    return collection_name

def connect_mongo_prod_scheduel_notification():
    CONNECTION_STRING = "mongodb+srv://icodeinnovahostingservice:eNZgEomXNOwBNztW@i2auth.nfdhtlq.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db_Name = client['authentication']
    collection_name = db_Name["scheduel_notifications"]
    return collection_name