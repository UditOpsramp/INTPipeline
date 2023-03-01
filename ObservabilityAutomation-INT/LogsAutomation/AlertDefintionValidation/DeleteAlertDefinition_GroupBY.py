#!/usr/lib/python3
import requests
import yaml
import json


def DeleteLogAlertDefinitionGroupBY(config_and_report_directory, workdirectory, parsedreportfile, AuthToken, portal, tenantid):

    alertidfile = open(
        workdirectory + "/AlertDefintionValidation/alertinfo.yml")
    parsedalertidfile = yaml.load(alertidfile, Loader=yaml.FullLoader)
    alertcomponent_groupby = parsedalertidfile['AlertComponent_GroupBY']

    deleteurl = "https://"\
        + portal + \
        "/log-alert/api/v1/alerts/tenants/"\
        + tenantid +\
        "/delete"

    payload = json.dumps({
        "alertIds": [
            "" + alertcomponent_groupby + ""
        ]
    })

    headers = {
        'Authorization': AuthToken,
        'Content-Type': 'application/json'
    }

    response = requests.request(
        "POST", deleteurl, headers=headers, data=payload)
    if response.status_code == 200:
        status = "Validation Pass - Log Alert Definiton with GroupBY Deleted Successfully"
        parsedreportfile['LogAlertDeletion_GroupBy'] = status
    else:
        status = "Validation Fail - Log Alert Definiton with GroupBY Not Deleted Successfully"
        parsedreportfile['LogAlertDeletion_GroupBy'] = status

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
