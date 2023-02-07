#!/usr/lib/python3

import requests
import yaml
import time
import subprocess as sp

def ServiceLabelValue(config_and_report_directory, AuthToken, tenantid, portal, starttimemilisec, endtimemilisec, parsedreportfile):

    cmd= "sudo systemctl restart opsramp-agent"
    sp.getoutput(cmd)
    
    time.sleep(30)

    petclinicserverurl = "http://localhost:8080"

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

        if servicenamelist:
            if not servicenamelist:
                status = "Validation Fail : Value is not Coming for Tracing Service Label Attribute"
                parsedreportfile['ServiceLabelValueStatus'] = status
            else:
                status = "Validation Pass : Value is Coming for Tracing Service Label Attribute"
                parsedreportfile['ServiceLabelValueStatus'] = status
    
    else:
        status = service_response.reason
        parsedreportfile['ServiceLabelValueStatus'] = status

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
