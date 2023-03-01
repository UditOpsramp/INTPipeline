#!/usr/lib/python3
import requests
import json
import yaml


def CreateAlertDefinitionGroupBY(config_and_report_directory, workdirectory, parsedreportfile, AuthToken, portal, tenantid):

    alertidfile = open(
        workdirectory + "/AlertDefintionValidation/alertinfo.yml")
    parsedalertfile = yaml.load(alertidfile, Loader=yaml.FullLoader)

    createurl = "https://"\
        + portal +\
        "/log-alert/api/v1/alerts/tenants/"\
        + tenantid +\
        "/add"

    payload = json.dumps({
        "alert": {
            "name": "LogAlertTest_GroupBY",
            "type": "log",
            "tenantId": tenantid,
            "conditions": [
                {
                    "severity": "critical",
                    "operator": ">",
                    "value": 1,
                    "grouping": ["resourceUUID"],
                    "duration": {
                        "value": 60,
                        "unit": "minute"
                    }
                }
            ],
            "notification": {
                "subject": "LogAlertTest_GroupBY",
                "description": "LogAlertTest_GroupBY"
            },
            "query": "{level=\"Debug\"}"
        },
        "tenantId": tenantid
    })

    headers = {
        'Authorization': AuthToken,
        'Content-Type': 'text/plain'
    }

    response = requests.request(
        "POST", createurl, headers=headers, data=payload)
    if response.status_code == 200:
        status = "Validation Pass - Log Alert Definiton with GroupBY Created Successfully"
        parsedreportfile['LogAlertCreation_GroupBy'] = status
        jsonreponse = response.json()
        alertid = jsonreponse['alert']['alertId']
        parsedalertfile['AlertComponent_GroupBY'] = alertid
    else:
        status = "Validation Fail - Log Alert Defintion with GroupBY Not Created Successfully " + response.reason
        parsedreportfile['LogAlertCreation_GroupBy'] = status

    with open(workdirectory + "/AlertDefintionValidation/alertinfo.yml", "w") as file:
        yaml.dump(parsedalertfile, file)

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
