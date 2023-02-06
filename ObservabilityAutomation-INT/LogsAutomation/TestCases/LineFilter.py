#!/usr/lib/python3
import requests
import json
import yaml


def LineFilter(config_and_report_directory, parsedreportfile, AuthToken, tenantid, portal, starttimenanosec, endtimenanosec):

    payload = {}
    headers = {
        'Authorization': AuthToken,
        'Content-Type': 'application/json'
    }

    logsurl = "https://"\
        + portal +\
        "/logsrql/api/v7/tenants/"\
        + tenantid +\
        '/logs?query={source="agent"}|="connectivity"&limit=51&start='\
        + str(starttimenanosec) +\
        "&end="\
        + str(endtimenanosec)

    message = ''
    log_response = requests.request(
        "GET", logsurl, headers=headers, data=payload)
    if log_response.status_code == 200:
        logsresponsejson = log_response.json()
        logsdata = logsresponsejson['data']
        logsresultdata = logsdata['result']
        for p in logsresultdata:
            val = (p['values'])
            for k in val:
                jsondata = json.loads(k[1])
            message = jsondata['message']

        if "connectivity" not in message:
            status = "Validation Fail - Line Filter Functionality is not Working Properly"
            parsedreportfile['Logs_LineFilter_Functionality'] = status
        else:
            status = "Validation Pass - Line Filter Functionality is Working Properly"
            parsedreportfile['Logs_LineFilter_Functionality'] = status
    else:
        status = log_response.reason
        parsedreportfile['Logs_LineFilter_Functionality'] = status

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
