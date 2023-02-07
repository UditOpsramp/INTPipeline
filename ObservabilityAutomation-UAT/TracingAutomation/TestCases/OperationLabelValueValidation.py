#!/usr/lib/python3

import requests
import yaml
import time
import subprocess as sp


def OperationLabelValue(config_and_report_directory, AuthToken, tenantid, portal, starttimemilisec, endtimemilisec, parsedreportfile):

    cmd= "sudo systemctl restart opsramp-agent"
    sp.getoutput(cmd)
    
    time.sleep(30)

    petclinicserverurl = "http://localhost:8080"

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

    else:
        status = operation_response.reason
        parsedreportfile['OpearationLabelValueStatus'] = status
    
    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
