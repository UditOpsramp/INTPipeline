#!/usr/lib/python3

import requests
import yaml
import time


def TracingService(workdirectory, AuthToken, tenantid, portal, tracingservice, starttimemilisec, endtimemilisec, parsedreportfile):

    petclinicserverurl = "http://172.25.220.220:8080"

    petclinicresponse = requests.request(
        "GET", petclinicserverurl)

    time.sleep(60)

    traceserviceurl = "https://"\
        + portal +\
        "/tracing-query/api/v1/tenants/"\
        + tenantid +\
        '/services?start='\
        + str(starttimemilisec) +\
        "&end="\
        + str(endtimemilisec)

    payload = {}
    headers = {
        'Authorization': AuthToken,
        'Content-Type': 'application/json'
    }

    traceservice_response = requests.request(
        "GET", traceserviceurl, headers=headers, data=payload)
    if traceservice_response.status_code == 200:
        traceservice_responsejson = traceservice_response.json()
        traceservicenamelist = traceservice_responsejson['services']

        if tracingservice in traceservicenamelist:
            status = "Validation Pass : Tracing Service " + tracingservice + " is Coming"
            parsedreportfile['TracingServiceNameStatus'] = status
        else:
            status = "Validation Fail : Tracing Service " + tracingservice + " is not Coming"
            parsedreportfile['TracingServiceNameStatus'] = status

    with open(workdirectory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
