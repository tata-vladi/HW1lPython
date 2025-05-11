import requests


class YouGileAPI:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get_project(self, id_project):
        resp = requests.get(self.url + '/api-v2/projects/' + id_project, headers=self.headers)
        return resp

    def create_project(self, title, users):
        body = {
            "title": title,
            "users": users
        }
        resp = requests.post(self.url + '/api-v2/projects', headers=self.headers, json=body)
        return resp

    def delete_project(self, project_id):
        body = {
            "deleted": True
        }
        resp = requests.put(self.url + '/api-v2/projects/' + project_id, headers=self.headers, json=body)
        return resp.status_code

    def update_project(self, project_id, new_title):
        body = {"title": new_title}
        resp = requests.put(f"{self.url}/api-v2/projects/{project_id}", headers=self.headers, json=body)
        return resp