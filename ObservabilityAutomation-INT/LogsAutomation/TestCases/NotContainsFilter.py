#!/usr/lib/python3
import requests
import yaml
import time
import subprocess as sp


def QueryNotContainsLogs(config_and_report_directory,workdirectory, parsedreportfile,parsedconfigfile, AuthToken, portal, tenantid, starttimenanosec, endtimenanosec):

    cmd = "sudo cp " + workdirectory + \
        "/TestCasesConfig/count-logconfig.yaml /opt/opsramp/agent/conf/log.d/log-config.yaml"
    sp.getoutput(cmd)

    cmd = "sudo systemctl restart opsramp-agent"
    sp.getoutput(cmd)

    time.sleep(30)

    cmd = "sudo go build -o " + workdirectory + "/loggeneratorscript " + workdirectory + "/loggeneratorscript.go"
    sp.getoutput(cmd)

    cmd = "sudo chmod +x " + workdirectory + "/loggeneratorscript"
    sp.getoutput(cmd)

    cmd = "sudo " + workdirectory + "/./loggeneratorscript 40 1 100 600 0"
    sp.getoutput(cmd)

    time.sleep(60)

    with open(workdirectory + "/TestCasesConfig/count-logconfig.yaml", "r") as file:
        logconfigfile = yaml.load_all(file, Loader=yaml.FullLoader)
        logconfigfilelist = list(logconfigfile)

    for i in logconfigfilelist:
        for k, j in i['inputs'].items():
            app = (k)

            url = "https://"\
                + portal +\
                "/logsrql/api/v7/tenants/"\
                + tenantid +\
                "/logs?query={source!="\
                '"'\
                + app +\
                '"'\
                "}&step=30&start="\
                + str(starttimenanosec) +\
                "&end="\
                + str(endtimenanosec)

            payload = {}
            headers = {
                'Authorization': AuthToken,
                'Content-Type': 'application/json'
            }
            response = requests.request(
                "GET", url, headers=headers, data=payload)
            if response.status_code == 200:
                responsejson = response.json()
                data = responsejson['data']
                resultdata = data['result']
                logsresultStatus = False
                for p in resultdata:
                    streamvalue = (p['stream'])
                if app not in str(streamvalue):
                    logsresultStatus = True
                if not logsresultStatus:
                    status = "Validation Fail - Not Contains Query Filter Functionality is not Working Properly"
                    parsedreportfile['Logs_NotContains_Functionality'] = status
                else:
                    status = "Validation Pass - Not Contains Query Filter Functionality is Working Properly"
                    parsedreportfile['Logs_NotContains_Functionality'] = status

            else:
                status = response.reason
                parsedreportfile['Logs_NotContains_Functionality'] = status

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)

    ReomveLogsGenerator(workdirectory)


def ReomveLogsGenerator(workdirectory):
    cmd = "rm -rf " + workdirectory + "/loggeneratorscript"
    sp.getoutput(cmd)

    cmd = "rm -rf " + workdirectory + "/*.log"
    sp.getoutput(cmd)