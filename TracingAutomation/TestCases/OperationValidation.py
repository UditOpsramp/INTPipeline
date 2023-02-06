#!/usr/lib/python3

import requests
import yaml
import time


def TracingOperation(workdirectory, AuthToken, tenantid, portal, tracingoperation, starttimemilisec, endtimemilisec, parsedreportfile):

    petclinicserverurl = "http://172.25.220.220:8080" + tracingoperation

    petclinicresponse = requests.request(
        "GET", petclinicserverurl)

    time.sleep(60)

    traceoperationurl = "https://"\
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

    traceoperation_response = requests.request(
        "GET", traceoperationurl, headers=headers, data=payload)

    if traceoperation_response.status_code == 200:
        traceoperation_responsejson = traceoperation_response.json()
        traceoperationslist = traceoperation_responsejson['operations']

        if tracingoperation in traceoperationslist:
            status = "Validation Pass : Tracing Operation " + tracingoperation + " is Coming"
            parsedreportfile['TracingOperationStatus'] = status
        else:
            status = "Validation Fail : Tracing Operation " + \
                tracingoperation + " is not Coming"
            parsedreportfile['TracingOperationStatus'] = status

    with open(workdirectory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
