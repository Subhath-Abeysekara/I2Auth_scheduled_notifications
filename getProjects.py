from connect_mongo import connect_mongo_dev_project, connect_mongo_beta_project, connect_mongo_prod_project

collection_name = connect_mongo_dev_project()
collection_name_beta = connect_mongo_beta_project()
collection_name_prod = connect_mongo_prod_project()

def get_projects_dev():
    projects = collection_name.find({'scheduel_notification':True})
    projects_code_list = []
    for project in projects:
        projects_code_list.append(str(project['_id']))
    print('project_codes',projects_code_list)
    return projects_code_list

def get_projects_beta():
    projects = collection_name_beta.find({'scheduel_notification':True})
    projects_code_list = []
    for project in projects:
        projects_code_list.append(str(project['_id']))
    print('project_codes',projects_code_list)
    return projects_code_list

def get_projects_prod():
    projects = collection_name_prod.find({'scheduel_notification':True})
    projects_code_list = []
    for project in projects:
        projects_code_list.append(str(project['_id']))
    print('project_codes',projects_code_list)
    return projects_code_list