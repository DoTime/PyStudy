from yarn_api_client import ApplicationMaster, HistoryServer, NodeManager, ResourceManager
from conf import config





# def get_yarn_state():
#     # 提交到rm的所有apps的信息
#     response=rm.cluster_applications(state="RUNNING").data
#     app=response['apps']['app']
#     for i in app:
#         print("i:%s,value:%s" % (app.index(i),i))

def get_state(application_id):
    rm = ResourceManager([config.yarn_url])
    response=rm.cluster_application(application_id).data
    app = response['app']
    state=app['state']
    return state


if __name__=="__main__":
    get_state('application_1584966871407_39586')







