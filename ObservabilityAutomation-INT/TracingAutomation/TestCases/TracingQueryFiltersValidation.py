#!/usr/lib/python3

import requests
import yaml
import json


def TracingQueryFilters(config_and_report_directory, AuthToken, tenantid, portal,
                        starttimemilisec, endtimemilisec, starttimenanosec, endtimenanosec, parsedreportfile):

    Traces_QueryFilter_FunctionalityList = parsedreportfile['Traces_QueryFilter_FunctionalityList']

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

                tracesresultStatus = False

                for k in valuesdata:

                    tracedataurl = "https://"\
                        + portal +\
                        "/tracing-query/api/v1/tenants/"\
                        + tenantid +\
                        '/search/traces'

                    payload = json.dumps({
                        "end": str(endtimenanosec),
                        "limit": 51,
                        "query": i + " IN (\"" + k + "\")",
                        "start": str(starttimenanosec)
                    })
                    tracedata_response = requests.request(
                        "POST", tracedataurl, headers=headers, data=payload)
                    if tracedata_response.status_code == 200:
                        tracedata_responsejson = tracedata_response.json()
                        tracesdatalist = tracedata_responsejson['traces']

                        for j in tracesdatalist:
                            if j['attributes'][i] == k:
                                tracesresultStatus = True
                if not tracesresultStatus:
                    status = "QueryFilter : " + i + \
                        " : Validation Fail - Traces are coming for that Queryfilter\n"
                    Traces_QueryFilter_FunctionalityList.append(status)
                else:
                    status = "QueryFilter : " + i + \
                        " : Validation Pass - Traces are coming for that Queryfilter\n"
                    Traces_QueryFilter_FunctionalityList.append(status)

            else:
                status = value_response.reason
                Traces_QueryFilter_FunctionalityList.append(status)

    else:
        status = labels_response.reason
        Traces_QueryFilter_FunctionalityList.append(status)

    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)
