#!/usr/lib/python3

import requests


def send_googlechat_message(GOOGLECHAT_WEBHOOK_URL, portal_name, currentdate, TESTCASE1, TESTCASE2, TESTCASE3,
                            TESTCASE4, TESTCASE5, TESTCASE6, TESTCASE7, TESTCASE8,TESTCASE9, tracescomingstatus,traces_labelvaluesnotcoming, servicelabelvaluestatus, opearationlabelvaluestatus, tracingservicenamestatus, tracingservicedatastatus, tracingoperationstatus, tracingoperationdatastatus, traces_queryfilter_functionalitylist):

    if "Pass" in tracescomingstatus:
        test1status = '<b><font color=\"#5AAF00\">' + \
            tracescomingstatus + '</font></b>'
    else:
        test1status = '<b><font color=\"#D70000\">' + \
            tracescomingstatus + '</font></b>'

    test2status = ''
    for j in traces_labelvaluesnotcoming : 
        if "Not" in j:
            labelvaluestatus = '<b><font color=\"#D70000\">' + \
            j + '</font></b>'
            test2status = test2status + "\n" + labelvaluestatus
        else:
            labelvaluestatus = '<b><font color=\"#5AAF00\">' + \
            j + '</font></b>'
            test2status = test2status + "\n" + labelvaluestatus

    if "Pass" in servicelabelvaluestatus:
        test3status = '<b><font color=\"#5AAF00\">' + \
            servicelabelvaluestatus + '</font></b>'
    else:
        test3status = '<b><font color=\"#D70000\">' + \
            servicelabelvaluestatus + '</font></b>'

    if "Pass" in opearationlabelvaluestatus:
        test4status = '<b><font color=\"#5AAF00\">' + \
            opearationlabelvaluestatus + '</font></b>'
    else:
        test4status = '<b><font color=\"#D70000\">' + \
            opearationlabelvaluestatus + '</font></b>'

    if "Pass" in tracingservicenamestatus:
        test5status = '<b><font color=\"#5AAF00\">' + \
            tracingservicenamestatus + '</font></b>'
    else:
        test5status = '<b><font color=\"#D70000\">' + \
            tracingservicenamestatus + '</font></b>'

    if "Pass" in tracingservicedatastatus:
        test6status = '<b><font color=\"#5AAF00\">' + \
            tracingservicedatastatus + '</font></b>'
    else:
        if "Fail" in tracingservicedatastatus:
            test6status = '<b><font color=\"#D70000\">' + \
                tracingservicedatastatus + '</font></b>'
        else:
            test6status = '<b><font color=\"#FFCC00\">' + \
                tracingservicedatastatus + '</font></b>'            
            
    if "Pass" in tracingoperationstatus:
        test7status = '<b><font color=\"#5AAF00\">' + \
            tracingoperationstatus + '</font></b>'
    else:
        test7status = '<b><font color=\"#D70000\">' + \
            tracingoperationstatus + '</font></b>'

    if "Pass" in tracingoperationdatastatus:
        test8status = '<b><font color=\"#5AAF00\">' + \
            tracingoperationdatastatus + '</font></b>'
    else:
        test8status = '<b><font color=\"#D70000\">' + \
            tracingoperationdatastatus + '</font></b>'

    test9status = ''
    for k in traces_queryfilter_functionalitylist:
        if "Pass" in k:
            queryfilterstatus = '<b><font color=\"#5AAF00\">' + k + '</font></b>'
            test9status = test9status + "\n" + queryfilterstatus
        else:
            queryfilterstatus = '<b><font color=\"#D70000\">' + k + '</font></b>'
            test9status = test9status + "\n" + queryfilterstatus

    WEBHOOK_URL = GOOGLECHAT_WEBHOOK_URL
    title = portal_name + " TRACING AUTOMATION REPORT"
    subtitle = currentdate

    paragraph = '<b>' + TESTCASE1 + '</b>' + test1status + '<b>' + TESTCASE2 + test2status + '<b>' + TESTCASE3 + test3status + '<b>' + TESTCASE4 + \
        test4status + '<b>' + TESTCASE5 + test5status + '<b>' + TESTCASE6 + \
        test6status + '<b>' + TESTCASE7 + test7status + '<b>' + TESTCASE8 + test8status + '<b>' + TESTCASE9 + test9status
    widget = {'textParagraph': {'text': paragraph}}
    res = requests.post(
        WEBHOOK_URL,
        json={
            'cards': [
                {
                    'header': {
                        'title': title,
                        'subtitle': subtitle,
                    },
                    'sections': [{'widgets': [widget]}],
                }
            ]
        },
    )
