import requests


def next():
    response = requests.get("https://olcf-ci-service.herokuapp.com/github-push-events/pop").json()
    if 'data' in response:
        return PushEvent.fromGithubEvent(response['data'])
    

class PushEvent(object):
    def __init__(self, clone_url, commit):
        self.clone_url = clone_url
        self.commit = commit

    @classmethod
    def fromGithubEvent(cls, event):
        clone_url = event['repository']['clone_url']
        commit = event['head_commit']['id']
        return cls(clone_url, commit)
