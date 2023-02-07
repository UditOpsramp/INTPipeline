#!/usr/lib/python3
import requests
import yaml


def MultiFilter(config_and_report_directory, parsedreportfile, AuthToken, tenantid, portal, starttimenanosec, endtimenanosec):

    payload = {}
    headers = {
        'Authorization': AuthToken,
        'Content-Type': 'application/json'
    }

    logsurl = "https://"\
        + portal +\
        "/logsrql/api/v7/tenants/"\
        + tenantid +\
        '/logs?query={source="agent",type="log",file_path="/var/log/opsramp/agent.log",level="Info"}&limit=51&start='\
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
            status = "Validation Fail -  MultiFilter Functionality is not Working Properly"
            parsedreportfile['Logs_MultiFilter_Functionalty'] = status
        else:
            status = "Validation Pass - MultiFilter Functionality is  Working Properly"
            parsedreportfile['Logs_MultiFilter_Functionalty'] = status

    else:
        status = log_response.reason
        parsedreportfile['Logs_MultiFilter_Functionalty'] = status

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
