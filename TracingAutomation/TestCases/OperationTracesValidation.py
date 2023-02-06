#!/usr/lib/python3

import requests
import yaml
import time
import json


def OperationTracingData(workdirectory, AuthToken, tenantid, portal, tracingoperation, starttimenanosec, endtimenanosec, parsedreportfile):

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
            tracingoperationdata = j['operation']

        if tracingoperationdata == tracingoperation:
            status = "Validation Pass : Traces for Operation Name " + \
                tracingoperation + " are Coming"
            parsedreportfile['TracingOperationDataStatus'] = status
        else:
            status = "Validation Fail : Traces for Operation Name " + \
                tracingoperation + " are not Coming"
            parsedreportfile['TracingOperationDataStatus'] = status

    with open(workdirectory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
