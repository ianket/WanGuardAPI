import requests
from requests.auth import HTTPBasicAuth


class WanGuard:

    def __init__(self, url, username, password):
        self._url = url
        self._username = username
        self._password = password

    def get_anomalies(self, from_date=None):
        url = self._url + "/wanguard-api/v1/anomalies"
        if from_date:
            url += "?from_date=%s" % from_date
        return requests.get(url, auth=HTTPBasicAuth(self._username, self._password)).json()

    def get_anomaly(self, id):
        url = self._url + "/wanguard-api/v1/anomalies/%s" % (str(id))
        return requests.get(url, auth=HTTPBasicAuth(self._username, self._password)).json()

    def get_top_flow(self, from_date):
        return requests.get(
            self._url + "/wanguard-api/v1/flow_tops?"
                        "from=%s&until=now&top_type=Flow%20Records&top_order=Flows&top=50&output=JSON" % from_date,
            auth=HTTPBasicAuth(self._username, self._password)).json()
