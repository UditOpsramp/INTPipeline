#!/usr/lib/python3

import requests
import yaml
import time
import json
import subprocess as sp


def OperationTracingData(config_and_report_directory, AuthToken, tenantid, portal, tracingoperation, starttimenanosec, endtimenanosec, parsedreportfile):

    global operationdata

    cmd= "sudo systemctl restart opsramp-agent"
    sp.getoutput(cmd)
    
    time.sleep(30)

    petclinicserverurl = "http://172.25.220.220:8080" + tracingoperation

    petclinicresponse = requests.request(
        "GET", petclinicserverurl)

    time.sleep(60)

    tracedataurl = "https://"\
        + portal +\
        "/tracing-query/api/v1/tenants/"\
        + tenantid +\
        '/search/traces'

    payload = json.dumps({
        "end": str(endtimenanosec),
        "limit": 51,
        "query": "operation IN (\"" + tracingoperation + "\")",
        "start": str(starttimenanosec)
    })

    headers = {
        'Authorization': AuthToken,
        'Content-Type': 'application/json'
    }

    tracedata_response = requests.request(
        "POST", tracedataurl, headers=headers, data=payload)
    if tracedata_response.status_code == 200:
        tracedata_responsejson = tracedata_response.json()
        tracesdatalist = tracedata_responsejson['traces']

        for j in tracesdatalist:
            operationdata = j['operation']

        if operationdata == tracingoperation:
            status = "Validation Pass : Traces for Operation Name " + \
                tracingoperation + " are Coming"
            parsedreportfile['TracingOperationDataStatus'] = status
        else:
            status = "Validation Fail : Traces for Operation Name " + \
                tracingoperation + " are not Coming"
            parsedreportfile['TracingOperationDataStatus'] = status

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
