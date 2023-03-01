#!/usr/lib/python3
import requests
import yaml
import time


def GetAlertDetailsGroupBY(config_and_report_directory, workdirectory, parsedreportfile, AuthToken, portal, tenantid):

    alertinfofile = open(
        workdirectory + "/AlertDefintionValidation/alertinfo.yml")
    parsedalertinfofile = yaml.load(alertinfofile, Loader=yaml.FullLoader)
    AlertComponent_GroupBY = parsedalertinfofile['AlertComponent_GroupBY']

    time.sleep(420)

    url = "https://"\
        + portal + \
        "/api/v2/tenants/"\
        + tenantid + \
        "/alerts/search"\

    payload = {'queryString': 'metrics:'+"LogAlertTest_GroupBY"}

    headers = {
        'Authorization': 'Bearer' + AuthToken,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, params=payload)
    if response.status_code == 200:
        json = response.json()
        results = json['results']
        for i in results:
            alertcomponent = i['component']
            if alertcomponent == AlertComponent_GroupBY:
                if "dnsName" in i['resource']:
                    status = "Validation Pass - Alert is Successfully Mapped with Resource"
                    parsedreportfile['LogAlertGeneration_GroupBy'] = status
                else:
                    status = "Validation Fail - Alert is not Successfully Mapped with Resource"
                    parsedreportfile['LogAlertGeneration_GroupBy'] = status
    else:
        status = response.reason
        parsedreportfile['LogAlertGeneration_GroupBy'] = status

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
