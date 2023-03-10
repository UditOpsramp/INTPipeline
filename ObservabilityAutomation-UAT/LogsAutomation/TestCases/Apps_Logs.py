#!/usr/lib/python3
import requests
import yaml
import time
import subprocess as sp


def AppLogs(config_and_report_directory,workdirectory, parsedreportfile, AuthToken, portal, tenantid, starttimenanosec, endtimenanosec):

    time.sleep(30)

    cmd = "sudo cp " + workdirectory + \
        "/TestCasesConfig/app-logconfig.yaml /opt/opsramp/agent/conf/log.d/log-config.yaml"
    sp.getoutput(cmd)

    cmd = "sudo systemctl restart opsramp-agent"
    sp.getoutput(cmd)

    time.sleep(60)

    with open(workdirectory + "/TestCasesConfig/app-logconfig.yaml", "r") as file:
        logconfigfile = yaml.load_all(file, Loader=yaml.FullLoader)
        logconfigfilelist = list(logconfigfile)

    for i in logconfigfilelist:
        for k, j in i['inputs'].items():
            app = (k)

            payload = {}
            headers = {
                'Authorization': AuthToken,
                'Content-Type': 'application/json'
            }

            logsurl = "https://"\
                + portal +\
                "/logsrql/api/v7/tenants/"\
                + tenantid +\
                "/logs?query={source="\
                '"'\
                + app +\
                '"'\
                "}&limit=51&start="\
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
                    status = "Source Name : " + app + \
                        " : Validation Fail - Logs are not coming on portal"
                    parsedreportfile['Source_Logs'] = status
                else:
                    status = "Source Name : " + app + " : Validation Pass - Logs are coming on portal"
                    parsedreportfile['Source_Logs'] = status

            else:
                status = log_response.text
                parsedreportfile['Apps_Logs'] = status

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
