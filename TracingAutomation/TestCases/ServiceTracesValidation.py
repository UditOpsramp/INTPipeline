#!/usr/lib/python3

import requests
import yaml
import json
import time


def ServiceTracingData(workdirectory, AuthToken, tenantid, portal, tracingservice, starttimenanosec, endtimenanosec, parsedreportfile):

    petclinicserverurl = "http://172.25.220.220:8080"

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
        "query": "service IN (\"" + tracingservice + "\")",
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
            tracingservicedata = j['service']

        if tracingservicedata == tracingservice:
            status = "Validation Pass : Traces for Service Name " + \
                tracingservice + " are Coming"
            parsedreportfile['TracingServiceDataStatus'] = status
        else:
            status = "Validation Fail : Traces for Service Name " + \
                tracingservice + " are not Coming"
            parsedreportfile['TracingServiceDataStatus'] = status

    with open(workdirectory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
