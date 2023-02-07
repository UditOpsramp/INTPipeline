#!/usr/lib/python3

import requests
import yaml
import time
import subprocess as sp


def TracingOperation(config_and_report_directory, AuthToken, tenantid, portal, tracingoperation, starttimemilisec, endtimemilisec, parsedreportfile):

    cmd= "sudo systemctl restart opsramp-agent"
    sp.getoutput(cmd)
    
    time.sleep(30)

    petclinicserverurl = "http://localhost:8080" + tracingoperation

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

        if traceoperationslist :
            if tracingoperation in traceoperationslist:
                status = "Validation Pass : Tracing Operation " + tracingoperation + " is Coming"
                parsedreportfile['TracingOperationStatus'] = status
            else:
                status = "Validation Fail : Tracing Operation " + \
                    tracingoperation + " is not Coming"
                parsedreportfile['TracingOperationStatus'] = status

        else:
            status = "Validation Fail : Tracing Operations are not Coming"
            parsedreportfile['TracingOperationStatus'] = status

    else:
        status = traceoperation_response.reason
        parsedreportfile['TracingOperationStatus'] = status

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
