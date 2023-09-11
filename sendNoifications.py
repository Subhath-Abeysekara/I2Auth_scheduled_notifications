import requests
import getProjects
import getSchedue_notifications
import getUsers

def sendNotification(device_token , project_name , message):
    # expo_push_token = "ExponentPushToken[oE0LGTEDMOXHPnGdxydA3Y]"
    print(device_token)
    expo_push_url = "https://exp.host/--/api/v2/push/send"
    headers = {
        "Host": "exp.host",
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/json",
        "Accept-Language": "en-US",
        "expo-sdk-version": "YOUR_EXPO_SDK_VERSION",
        "Authorization": None,
    }
    data = {
        "to": device_token,
        "title": project_name,
        "body": message,
        "sound": "default",
    }
    response = requests.post(expo_push_url, json=data, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False

def send_notifications_dev(time):
    project_codes = getProjects.get_projects_dev()
    projects = getSchedue_notifications.get_all_projects(project_codes=project_codes,time=time)
    users = getUsers.get_all_projects_users_dev(projects)
    for user in users:
        for user1 in user['users']:
            if user1 != "":
                sendNotification(user1['device_token'],user['title'],user['message'])
    return

def send_notifications_beta(time):
    project_codes = getProjects.get_projects_beta()
    projects = getSchedue_notifications.get_all_projects_beta(project_codes=project_codes,time=time)
    users = getUsers.get_all_projects_users_beta(projects)
    for user in users:
        for user1 in user['users']:
            if user1 != "":
                sendNotification(user1['device_token'],user['title'],user['message'])
    return

def send_notifications_prod(time):
    project_codes = getProjects.get_projects_prod()
    projects = getSchedue_notifications.get_all_projects_prod(project_codes=project_codes,time=time)
    users = getUsers.get_all_projects_users_prod(projects)
    for user in users:
        for user1 in user['users']:
            if user1 != "":
                sendNotification(user1['device_token'],user['title'],user['message'])
    return

# sendNotification('ExponentPushToken[I2Z2ULAfPWkr0pDda4Q5J8]','lunchbucket','test')