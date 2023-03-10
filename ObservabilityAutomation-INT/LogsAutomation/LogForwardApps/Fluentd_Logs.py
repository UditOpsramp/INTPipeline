#!/usr/lib/python3

import requests
import yaml
import time
import subprocess as sp


def FluentDLogs(config_and_report_directory, parsedreportfile, AuthToken, portal, tenantid, starttimenanosec, endtimenanosec):

    cmd = "sudo systemctl restart td-agent"
    sp.getoutput(cmd)

    time.sleep(30)

    cmd = "sudo systemctl restart opsramp-agent"
    sp.getoutput(cmd)

    time.sleep(60)

    payload = {}

    headers = {
        'Authorization': AuthToken,
        'Content-Type': 'application/json'
    }

    logsurl = "https://"\
        + portal +\
        "/logsrql/api/v7/tenants/"\
        + tenantid +\
        '/logs?query={source="fluentd"}&limit=51&start='\
        + str(starttimenanosec) +\
        "&end="\
        + str(endtimenanosec)

    log_response = requests.request(
        "GET", logsurl, headers=headers, data=payload)

    if log_response.status_code == 200:
        logsresponsejson = log_response.json()
        logsdata = logsresponsejson['data']
        logsresultdata = logsdata['result']
        if not logsresultdata:
            status = "Source Name : FluentD : Validation Fail - Logs are not coming on portal"
            parsedreportfile['FluentD_Logs'] = status
        else:
            status = "Source Name : FluentD : Validation Pass - Logs are coming on portal"
            parsedreportfile['FluentD_Logs'] = status

    else:
        status = log_response.reason
        parsedreportfile['FluentD_Logs'] = status

    cmd = "sudo systemctl stop td-agent"
    sp.getoutput(cmd)

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
