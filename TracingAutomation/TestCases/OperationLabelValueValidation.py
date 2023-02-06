#!/usr/lib/python3

import requests
import yaml
import time


def OperationLabelValue(workdirectory, AuthToken, tenantid, portal, tracingoperation, starttimemilisec, endtimemilisec, parsedreportfile):

    petclinicserverurl = "http://172.25.220.220:8080"

    petclinicresponse = requests.request(
        "GET", petclinicserverurl)

    time.sleep(60)

    operationurl = "https://"\
        + portal +\
        "/tracing-query/api/v1/tenants/"\
        + tenantid +\
        '/operations?start='\
        + str(starttimemilisec) +\
        "&end="\
        + str(endtimemilisec)

    payload = {}
    headers = {
        'Authorization': AuthToken,
        'Content-Type': 'application/json'
    }

    operation_response = requests.request(
        "GET", operationurl, headers=headers, data=payload)

    if operation_response.status_code == 200:
        operation_responsejson = operation_response.json()
        operationslist = operation_responsejson['operations']

        if not operationslist:
            status = "Validation Fail : Value is not Coming for Tracing Operation Label Attribute"
            parsedreportfile['OpearationLabelValueStatus'] = status
        else:
            status = "Validation Pass : Value is Coming for Tracing Operation Label Attribute"
            parsedreportfile['OpearationLabelValueStatus'] = status

    with open(workdirectory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
