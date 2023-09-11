from connect_mongo import connect_mongo_dev_admin, connect_mongo_dev_user, connect_mongo_beta_user, \
    connect_mongo_beta_admin, connect_mongo_prod_user, connect_mongo_prod_admin

collection_name_user_dev = connect_mongo_dev_user()
collection_name_admin_dev = connect_mongo_dev_admin()
collection_name_user_beta = connect_mongo_beta_user()
collection_name_admin_beta = connect_mongo_beta_admin()
collection_name_user_prod = connect_mongo_prod_user()
collection_name_admin_prod = connect_mongo_prod_admin()

def get_users_dev(project_code , types):
    admins = collection_name_user_dev.aggregate([
        {
            "$search": {
                "index": 'getByEmail',
                "compound": {
                    "should": [
                        {
                            "text": {
                                "query": types,
                                "path": "type"
                            }
                        },
                        {
                            "text": {
                                "query": project_code,
                                "path": "project_code"
                            }
                        }
                    ],
                    "minimumShouldMatch": 2
                }
            }
        },
        {"$project": {"device_token": 1, '_id': 0}}
    ])
    admin_list = list(admins)
    print('user_list',admin_list)
    return admin_list

def get_all_projects_users_dev(project_list):
    send_objects = []
    for project in project_list:
        print('project',project)
        users = get_users_dev(project['project_code'] , project['user_types'])
        send_object = {
            "users":users,
            "message":project['message'],
            "title":project['project_name']
        }
        send_objects.append(send_object)
    return send_objects

# ********** BETA ***************

def get_users_beta(project_code , types):
    admins = collection_name_user_beta.aggregate([
        {
            "$search": {
                "index": 'getByEmail',
                "compound": {
                    "should": [
                        {
                            "text": {
                                "query": types,
                                "path": "type"
                            }
                        },
                        {
                            "text": {
                                "query": project_code,
                                "path": "project_code"
                            }
                        }
                    ],
                    "minimumShouldMatch": 2
                }
            }
        },
        {"$project": {"device_token": 1, '_id': 0}}
    ])
    admin_list = list(admins)
    print('user_list',admin_list)
    return admin_list

def get_all_projects_users_beta(project_list):
    send_objects = []
    for project in project_list:
        print('project',project)
        users = get_users_beta(project['project_code'] , project['user_types'])
        send_object = {
            "users":users,
            "message":project['message'],
            "title":project['project_name']
        }
        send_objects.append(send_object)
    return send_objects

# *************** PROD ****************

def get_users_prod(project_code , types):
    admins = collection_name_user_prod.aggregate([
        {
            "$search": {
                "index": 'getByEmail',
                "compound": {
                    "should": [
                        {
                            "text": {
                                "query": types,
                                "path": "type"
                            }
                        },
                        {
                            "text": {
                                "query": project_code,
                                "path": "project_code"
                            }
                        }
                    ],
                    "minimumShouldMatch": 2
                }
            }
        },
        {"$project": {"device_token": 1, '_id': 0}}
    ])
    admin_list = list(admins)
    print('user_list',admin_list)
    return admin_list

def get_all_projects_users_prod(project_list):
    send_objects = []
    for project in project_list:
        print('project',project)
        users = get_users_prod(project['project_code'] , project['user_types'])
        send_object = {
            "users":users,
            "message":project['message'],
            "title":project['project_name']
        }
        send_objects.append(send_object)
    return send_objects

