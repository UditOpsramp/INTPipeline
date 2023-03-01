#!/usr/lib/python3

import requests
import yaml


def LabelValues(config_and_report_directory, parsedreportfile, AuthToken, tenantid, portal, starttimeUNIX, endtimeUNIX):

    Logs_LabelValuesNotComing = parsedreportfile['Logs_LabelValuesNotComing']

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

        for i in labelsdata:

            valueurl = "https://"\
                + portal +\
                "/logsrql/api/v7/tenants/"\
                + tenantid +\
                "/logs/label/"\
                + i +\
                "/values?start"\
                + str(starttimeUNIX) +\
                "&end="\
                + str(endtimeUNIX)

            value_response = requests.request(
                "GET", valueurl, headers=headers, data=payload)
            if value_response.status_code == 200:
                valuesresponsejson = value_response.json()
                valuesdata = valuesresponsejson['data']
                if valuesdata == "":
                    status = "Value Not Coming for " + i + " Label Attribute"
                    Logs_LabelValuesNotComing.append(status)
                else:
                    status = "Value is Coming for " + i + " Label Attribute"
                    Logs_LabelValuesNotComing.append(status)
            else:
                status = value_response.reason
                Logs_LabelValuesNotComing.append(status)
                
    else:
        status = labels_response.reason
        Logs_LabelValuesNotComing.append(status)                

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
