#!/usr/lib/python3

import requests
import yaml
import json


def LabelValues(workdirectory, AuthToken, tenantid, portal,
                starttimemilisec, endtimemilisec, parsedreportfile):

    Traces_LabelValuesNotComing = parsedreportfile['Traces_LabelValuesNotComing']

    headers = {
        'Authorization': AuthToken,
        'Content-Type': 'application/json'
    }

    labelsurl = "https://"\
        + portal +\
        "/tracing-query/api/v1/tenants/"\
        + tenantid +\
        "/labels?start"\
        + str(starttimemilisec) +\
        "&end="\
        + str(endtimemilisec)

    labels_response = requests.request(
        "GET", labelsurl, headers=headers)
    if labels_response.status_code == 200:
        labelsresponsejson = labels_response.json()
        labelsdata = labelsresponsejson['labels']

        for i in labelsdata:

            valueurl = "https://"\
                + portal +\
                "/tracing-query/api/v1/tenants/"\
                + tenantid +\
                "/label/"\
                + i +\
                "/values?start"\
                + str(starttimemilisec) +\
                "&end="\
                + str(endtimemilisec)

            value_response = requests.request(
                "GET", valueurl, headers=headers)
            if value_response.status_code == 200:
                valuesresponsejson = value_response.json()
                valuesdata = valuesresponsejson['values']
                if valuesdata == "":
                    status = "Value Not Coming for " + i + " Label Attribute"
                    Traces_LabelValuesNotComing.append(status)
                else:
                    status = "Value is Coming for " + i + " Label Attribute"
                    Traces_LabelValuesNotComing.append(status)
            else:
                status = value_response.reason
                Traces_LabelValuesNotComing.append(status)

    with open(workdirectory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
