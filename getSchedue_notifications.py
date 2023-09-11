from connect_mongo import connect_mongo_dev_scheduel_notification , connect_mongo_prod_scheduel_notification , connect_mongo_beta_scheduel_notification
collection_name_dev = connect_mongo_dev_scheduel_notification()
collection_name_beta = connect_mongo_beta_scheduel_notification()
collection_name_prod = connect_mongo_prod_scheduel_notification()

def get_all_projects(project_codes , time):
    projects = collection_name_dev.find({'project_code':{ '$in': project_codes },'time_count':time},{'_id':0})
    print('projects',projects)
    return projects

def get_all_projects_beta(project_codes , time):
    projects = collection_name_beta.find({'project_code':{ '$in': project_codes },'time_count':time},{'_id':0})
    print('projects',projects)
    return projects

def get_all_projects_prod(project_codes , time):
    projects = collection_name_prod.find({'project_code':{ '$in': project_codes },'time_count':time},{'_id':0})
    print('projects',projects)
    return projects