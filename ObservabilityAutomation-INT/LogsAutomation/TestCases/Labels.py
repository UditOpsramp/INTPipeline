#!/usr/lib/python3

import requests
import yaml
import ruamel.yaml
import time
import subprocess as sp
import os

def LabelsTest(config_and_report_directory,workdirectory, parsedreportfile, AuthToken, tenantid, portal, starttimeUNIX, endtimeUNIX):
    
    print('Absolute directoryname: ',
      os.path.dirname(os.path.abspath(__file__)))

    Logs_AllLabelStatus = parsedreportfile['Logs_AllLabelStatus']

    PostingLabels = ["source", "clusterName", "containerName", "eventCategory", "file_name", "file_path", "host", "level", "location", "logGroup", "logName", "logStream",
                     "messageType", "namespaceName", "operationName", "owner", "podName", "projectId", "resourceId", "resourceType", "subscriptionFilters", "tenantId", "type"]

    with open(workdirectory + "/TestCasesConfig/label-logconfig.yaml", "r") as file:
        labelconfigfile = yaml.load_all(file, Loader=yaml.FullLoader)
        labelconfigfilelist = list(labelconfigfile)

    for i in labelconfigfilelist:
        for k, j in i['inputs'].items():
            (j['include'][0]) = workdirectory + "/*.log"

    logconfigfile = yaml.safe_dump_all(
        labelconfigfilelist, sort_keys=False, explicit_start=True)

    yaml_new = ruamel.yaml.YAML(typ='safe')
    data = yaml_new.load(logconfigfile)

    with open(workdirectory + "/TestCasesConfig/label-logconfig.yaml", "w") as file:
        yaml.dump(data, file, explicit_start=True, sort_keys=False)

    cmd = "sudo cp " + workdirectory + \
        "/TestCasesConfig/label-logconfig.yaml /opt/opsramp/agent/conf/log.d/log-config.yaml"
    sp.getoutput(cmd)

    cmd = "sudo systemctl restart opsramp-agent"
    sp.getoutput(cmd)

    time.sleep(30)

    cmd = "sudo go build " + workdirectory + "/loggeneratorscript.go"
    sp.getoutput(cmd)

    cmd = "sudo chmod +x " + workdirectory + "/loggeneratorscript"
    sp.getoutput(cmd)

    cmd = "sudo " + workdirectory + "/./loggeneratorscript 1 1 100 600 0"
    sp.getoutput(cmd)

    time.sleep(60)

    payload = {}
    headers = {
        'Authorization': AuthToken,
        'Content-Type': 'application/json'
    }

    labelsurl = "https://"\
        + portal +\
        "/logsrql/api/v7/tenants/"\
        + tenantid +\
        "/logs/labels?start"\
        + str(starttimeUNIX) +\
        "&end="\
        + str(endtimeUNIX)

    labels_response = requests.request(
        "GET", labelsurl, headers=headers, data=payload)
    if labels_response.status_code == 200:
        labelsresponsejson = labels_response.json()
        labelsdata = labelsresponsejson['data']

        for l in PostingLabels:
            if l not in labelsdata:
                status = "Label " + l + " Not Coming"
                Logs_AllLabelStatus.append(status)
            else:
                status = "Label " + l + " is Coming"
                Logs_AllLabelStatus.append(status)
    else:
        status = labels_response.reason
        Logs_AllLabelStatus.append(status)

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)

    ReomveLogsGenerator()


def ReomveLogsGenerator():
    cmd = "rm -rf loggeneratorscript"
    sp.getoutput(cmd)

    cmd = "rm -rf *.log"
    sp.getoutput(cmd)
