#!/usr/lib/python3

import requests
import yaml
import time
import subprocess as sp

def ServiceLabelValue(workdirectory, AuthToken, tenantid, portal, tracingservice, starttimemilisec, endtimemilisec, parsedreportfile):

    cmd= "sudo systemctl restart opsramp-agent"
    sp.getoutput(cmd)
    
    time.sleep(30)

    petclinicserverurl = "http://172.25.220.220:8080"

    petclinicresponse = requests.request(
        "GET", petclinicserverurl)

    time.sleep(60)

    serviceurl = "https://"\
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

    service_response = requests.request(
        "GET", serviceurl, headers=headers, data=payload)
    if service_response.status_code == 200:
        service_responsejson = service_response.json()
        servicenamelist = service_responsejson['services']

        if not servicenamelist:
            status = "Validation Fail : Value is not Coming for Tracing Service Label Attribute"
            parsedreportfile['ServiceLabelValueStatus'] = status
        else:
            status = "Validation Pass : Value is Coming for Tracing Service Label Attribute"
            parsedreportfile['ServiceLabelValueStatus'] = status

    with open(workdirectory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
