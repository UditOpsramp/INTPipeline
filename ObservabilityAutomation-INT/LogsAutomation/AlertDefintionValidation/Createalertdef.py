#!/usr/lib/python3
import requests
import json
import yaml


def CreateLogAlertDefinition(config_and_report_directory,workdirectory, parsedreportfile, AuthToken, portal, tenantid):

    createurl = "https://"\
        + portal +\
        "/log-alert/api/v1/alerts/tenants/"\
        + tenantid +\
        "/add"

    payload = json.dumps({
        "alert": {
            "name": "LogAlertTest",
            "type": "log",
            "tenantId": tenantid,
            "conditions": [
                {
                    "severity": "critical",
                    "operator": ">",
                    "value": 1,
                    "duration": {
                        "value": 30,
                        "unit": "minute"
                    }
                }
            ],
            "notification": {
                "subject": "LogAlertTest",
                "description": "LogAlertTest"
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
        status = "Validation Pass - Log Alert Definiton Created Successfully"
        parsedreportfile['LogAlertCreation'] = status
    else:
        status = "Validation Fail - Log Alert Defintion Not Created Successfully"
        parsedreportfile['LogAlertCreation'] = status
    jsonreponse = response.json()

    alertid = jsonreponse['alert']['alertId']

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)

    with open(workdirectory + "/AlertDefintionValidation/alertinfo.yml", "w") as file:
        file.write("AlertComponent" + ': ' + alertid + "\n")
