#!/usr/lib/python3

import requests
import yaml
import json
import time
import subprocess as sp

def TracingData(config_and_report_directory, AuthToken, tenantid, portal, starttimenanosec, endtimenanosec, parsedreportfile):

    cmd= "sudo systemctl restart opsramp-agent"
    sp.getoutput(cmd)
    
    time.sleep(30)

    petclinicserverurl = "http://localhost:8082"

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
        "query": "",
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

        if not tracesdatalist:
            status = "Validation Fail : Traces are not Coming"
            parsedreportfile['TracesComingStatus'] = status
        else:
            status = "Validation Pass : Traces are Coming"
            parsedreportfile['TracesComingStatus'] = status

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
