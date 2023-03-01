#!/usr/lib/python3
import requests
import yaml
import json
import gzip
import base64
import datetime
import calendar
import time


def AWSLambda_Logs(config_and_report_directory, parsedreportfile, AuthToken, awstoken, portal, tenantid, starttimenanosec, endtimenanosec):

    currenttime = datetime.datetime.utcnow()
    starttimeUNIX = calendar.timegm(currenttime.timetuple())
    starttime = starttimeUNIX * 1000

    awslambdapayload_json = {"owner": "320444959714", "logEvents": [{"type": "platform.end", "timestamp": starttime, "message": "{\"requestId\":\"891d5360-1126-48aa-86cb-65beacf21444\"}"}, {
        "type": "platform.report", "timestamp": starttime, "message": "{\"metrics\":{\"billedDurationMs\":1006,\"durationMs\":1005.146,\"initDurationMs\":491.12,\"maxMemoryUsedMB\":99,\"memorySizeMB\":512},\"requestId\":\"891d5360-1126-48aa-86cb-65beacf21444\"}"}]}
    json_str = json.dumps(awslambdapayload_json).encode()
    gzipcompress = gzip.compress(json_str)
    convertobase64 = base64.encodebytes(gzipcompress)
    decode_awslambdapayload = convertobase64.decode()

    awslambdalogsgenerating_url = "https://"\
        + portal +\
        "/logs/api/v1/tenants/"\
        + tenantid +\
        "/aws/"\
        + awstoken

    payload = json.dumps({
        "timestamp": starttime,
        "extResourceId": "arn:aws:lambda:us-east-1:320444959714:function:extension-validate-func",
        "resourceType": "LAMBDA",
        "records": [
            {
                "data": decode_awslambdapayload
            }
        ]
    })

    headers = {
        'Authorization': AuthToken,
        'Content-Type': 'application/json'
    }

    awslambdagenerating_response = requests.request(
        "POST", awslambdalogsgenerating_url, headers=headers, data=payload)
    print(awslambdagenerating_response.text)

    getresourcetypevalue = json.loads(payload)
    resourceTypevalue = getresourcetypevalue['resourceType']

    time.sleep(60)

    logsurl = "https://"\
        + portal +\
        "/logsrql/api/v7/tenants/"\
        + tenantid +\
        "/logs?query={resourceType="\
        '"'\
        + resourceTypevalue +\
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
            status = "Source Name: " + 'AWS LAMBDA' + \
                " : Validation Fail - Logs are not coming on portal"
            parsedreportfile['AWSLambda_Logs'] = status
        else:
            status = "Source Name : " + "AWS LAMBDA" + \
                " : Validation Pass - Logs are coming on portal"
            parsedreportfile['AWSLambda_Logs'] = status

    else:
        status = log_response.reason
        parsedreportfile['AWSLambda_Logs'] = status

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
