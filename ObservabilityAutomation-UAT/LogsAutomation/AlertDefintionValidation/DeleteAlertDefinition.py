#!/usr/lib/python3
import requests
import yaml
import json


def DeleteLogAlertDefinition(config_and_report_directory,workdirectory, parsedreportfile, AuthToken, portal, tenantid):

    alertidfile = open(
        workdirectory + "/AlertDefintionValidation/alertinfo.yml")
    parsedalertidfile = yaml.load(alertidfile, Loader=yaml.FullLoader)
    alertcomponent = parsedalertidfile['AlertComponent']

    deleteurl = "https://"\
        + portal + \
        "/log-alert/api/v1/alerts/tenants/"\
        + tenantid +\
        "/delete"

    payload = json.dumps({
        "alertIds": [
            "" + alertcomponent + ""
        ]
    })

    headers = {
        'Authorization': AuthToken,
        'Content-Type': 'application/json'
    }

    response = requests.request(
        "POST", deleteurl, headers=headers, data=payload)
    if response.status_code == 200:
        status = "Validation Pass - Log Alert Definiton Deleted Successfully"
        parsedreportfile['LogAlertDeletion'] = status
    else:
        status = "Validation Fail - Log ALert Defintion Not Deleted Successfully"
        parsedreportfile['LogAlertDeletion'] = status

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
