#!/usr/lib/python3

import requests


def send_googlechat_message(GOOGLECHAT_WEBHOOK_URL, portal_name, currentdate, TESTCASE1, TESTCASE2, TESTCASE3, TESTCASE4, TESTCASE5, TESTCASE6, TESTCASE7, TESTCASE8, TESTCASE9, TESTCASE10, TESTCASE11, TESTCASE12, TESTCASE13, TESTCASE14, TESTCASE15, TESTCASE16, TESTCASE17, TESTCASE18, TESTCASE19, TESTCASE20, TESTCASE21, TESTCASE22, TESTCASE23, logs_alllabelstatus, logs_labelvaluesnotcoming, appslogsstaus, countlogsstaus, GeneratedLogsCount, Logscomingonportal, hostlogsstatus, logs_queryfilterstatuslist,
                            logs_notcontainsfunctionalitystatus, logs_multifilter_functionaltystatus, logs_linefilter_functionalitystatus, filteringlogsfunctionalitystatus, maskinglogsfunctionalitystatus, logalertcreationfunctionalitystatus, logalertgenerationfunctionalitystatus, logalertdeletionfunctionalitystatus, logalertcreationgroupbyfunctionalitystatus, logalertgenerationgroupbyfunctionalitystatus, logalertdeletiongroupbyfunctionalitystatus, awslogsstatus, awslambdalogsstatus, azurelogsstatus, gcplogsstatus, fluentdlogsstatus, fluentbitlogsstatus):

    if "Pass" in awslogsstatus:
        test1status = '<b><font color=\"#5AAF00\">' + awslogsstatus + '</font></b>'
    else:
        test1status = '<b><font color=\"#D70000\">' + awslogsstatus + '</font></b>'

    if "Pass" in awslambdalogsstatus:
        test2status = '<b><font color=\"#5AAF00\">' + awslambdalogsstatus + '</font></b>'
    else:
        test2status = '<b><font color=\"#D70000\">' + awslambdalogsstatus + '</font></b>'

    if "Pass" in azurelogsstatus:
        test3status = '<b><font color=\"#5AAF00\">' + azurelogsstatus + '</font></b>'
    else:
        test3status = '<b><font color=\"#D70000\">' + azurelogsstatus + '</font></b>'

    if "Pass" in gcplogsstatus:
        test4status = '<b><font color=\"#5AAF00\">' + gcplogsstatus + '</font></b>'
    else:
        test4status = '<b><font color=\"#D70000\">' + gcplogsstatus + '</font></b>'

    test5status = ''
    for i in logs_alllabelstatus:
        if "Not" in i:
            labelstatus = '<b><font color=\"#D70000\">' + \
                i + '</font></b>'
            test5status = test5status + "\n" + labelstatus
        else:
            labelstatus = '<b><font color=\"#5AAF00\">' + \
                i + '</font></b>'
            test5status = test5status + "\n" + labelstatus

    test6status = ''
    for j in logs_labelvaluesnotcoming:
        if "Not" in j:
            labelvaluestatus = '<b><font color=\"#D70000\">' + \
                j + '</font></b>'
            test6status = test6status + "\n" + labelvaluestatus
        else:
            labelvaluestatus = '<b><font color=\"#5AAF00\">' + \
                j + '</font></b>'
            test6status = test6status + "\n" + labelvaluestatus

    if "Pass" in appslogsstaus:
        test7status = '<b><font color=\"#5AAF00\">' + appslogsstaus + '</font></b>'
    else:
        test7status = '<b><font color=\"#D70000\">' + appslogsstaus + '</font></b>'

    if "Pass" in countlogsstaus:
        test8status = '<b><font color=\"#5AAF00\">' + countlogsstaus + '</font></b>'
    else:
        test8status = '<b><font color=\"#D70000\">' + countlogsstaus + '</font></b>'

    if "Pass" in hostlogsstatus:
        test9status = '<b><font color=\"#5AAF00\">' + hostlogsstatus + '</font></b>'
    else:
        test9status = '<b><font color=\"#D70000\">' + hostlogsstatus + '</font></b>'

    if "Pass" in logs_notcontainsfunctionalitystatus:
        test10status = '<b><font color=\"#5AAF00\">' + \
            logs_notcontainsfunctionalitystatus + '</font></b>'
    else:
        test10status = '<b><font color=\"#D70000\">' + \
            logs_notcontainsfunctionalitystatus + '</font></b>'

    if "Pass" in logs_multifilter_functionaltystatus:
        test11status = '<b><font color=\"#5AAF00\">' + \
            logs_multifilter_functionaltystatus + '</font></b>'
    else:
        test11status = '<b><font color=\"#D70000\">' + \
            logs_multifilter_functionaltystatus + '</font></b>'

    if "Pass" in logs_linefilter_functionalitystatus:
        test12status = '<b><font color=\"#5AAF00\">' + \
            logs_linefilter_functionalitystatus + '</font></b>'
    else:
        test12status = '<b><font color=\"#D70000\">' + \
            logs_linefilter_functionalitystatus + '</font></b>'

    if "Pass" in filteringlogsfunctionalitystatus:
        test13status = '<b><font color=\"#5AAF00\">' + \
            filteringlogsfunctionalitystatus + '</font></b>'
    else:
        test13status = '<b><font color=\"#D70000\">' + \
            filteringlogsfunctionalitystatus + '</font></b>'

    if "Pass" in maskinglogsfunctionalitystatus:
        test14status = '<b><font color=\"#5AAF00\">' + \
            maskinglogsfunctionalitystatus + '</font></b>'
    else:
        test14status = '<b><font color=\"#D70000\">' + \
            maskinglogsfunctionalitystatus + '</font></b>'

    if "Pass" in fluentdlogsstatus:
        test15status = '<b><font color=\"#5AAF00\">' + fluentdlogsstatus + '</font></b>'
    else:
        test15status = '<b><font color=\"#D70000\">' + fluentdlogsstatus + '</font></b>'

    if "Pass" in fluentbitlogsstatus:
        test16status = '<b><font color=\"#5AAF00\">' + \
            fluentbitlogsstatus + '</font></b>'
    else:
        test16status = '<b><font color=\"#D70000\">' + \
            fluentbitlogsstatus + '</font></b>'

    test17status = ''
    for k in logs_queryfilterstatuslist:
        if "Pass" in k:
            queryfilterstatus = '<b><font color=\"#5AAF00\">' + k + '</font></b>'
            test17status = test17status + "\n" + queryfilterstatus
        else:
            queryfilterstatus = '<b><font color=\"#D70000\">' + k + '</font></b>'
            test17status = test17status + "\n" + queryfilterstatus

    if "Pass" in logalertcreationfunctionalitystatus:
        test18status = '<b><font color=\"#5AAF00\">' + \
            logalertcreationfunctionalitystatus + '</font></b>'
    else:
        test18status = '<b><font color=\"#D70000\">' + \
            logalertcreationfunctionalitystatus + '</font></b>'

    if "Pass" in logalertgenerationfunctionalitystatus:
        test19status = '<b><font color=\"#5AAF00\">' + \
            logalertgenerationfunctionalitystatus + '</font></b>'
    else:
        test19status = '<b><font color=\"#D70000\">' + \
            logalertgenerationfunctionalitystatus + '</font></b>'

    if "Pass" in logalertdeletionfunctionalitystatus:
        test20status = '<b><font color=\"#5AAF00\">' + \
            logalertdeletionfunctionalitystatus + '</font></b>'
    else:
        test20status = '<b><font color=\"#D70000\">' + \
            logalertdeletionfunctionalitystatus + '</font></b>'

    if "Pass" in logalertcreationgroupbyfunctionalitystatus:
        test21status = '<b><font color=\"#5AAF00\">' + \
            logalertcreationgroupbyfunctionalitystatus + '</font></b>'
    else:
        test21status = '<b><font color=\"#D70000\">' + \
            logalertcreationgroupbyfunctionalitystatus + '</font></b>'

    if "Pass" in logalertgenerationgroupbyfunctionalitystatus:
        test22status = '<b><font color=\"#5AAF00\">' + \
            logalertgenerationgroupbyfunctionalitystatus + '</font></b>'
    else:
        test22status = '<b><font color=\"#D70000\">' + \
            logalertgenerationgroupbyfunctionalitystatus + '</font></b>'

    if "Pass" in logalertdeletiongroupbyfunctionalitystatus:
        test23status = '<b><font color=\"#5AAF00\">' + \
            logalertdeletiongroupbyfunctionalitystatus + '</font></b>'
    else:
        test23status = '<b><font color=\"#D70000\">' + \
            logalertdeletiongroupbyfunctionalitystatus + '</font></b>'

    WEBHOOK_URL = GOOGLECHAT_WEBHOOK_URL
    title = portal_name + " LOGS OBSERVABILITY AUTOMATION REPORT"
    subtitle = currentdate

    paragraph = '<b>' + TESTCASE1 + '</b>' + test1status + '<b>' + TESTCASE2 + test2status + '<b>' + TESTCASE3 + test3status + '<b>' + TESTCASE4 + test4status + '<b>' + TESTCASE5 + test5status + '<b>' + TESTCASE6 + test6status + '<b>' + TESTCASE7 + test7status + '<b>' + TESTCASE8 + "INGESTED-LOGS-COUNT : " + str(GeneratedLogsCount) + "\n\n" + "UI-LOGS-COUNT: " + str(Logscomingonportal) + "\n\n" + test8status + '<b>' + TESTCASE9 + test9status + '<b>' + TESTCASE10 + \
        test10status + '<b>' + TESTCASE11 + test11status + '<b>' + TESTCASE12 + test12status + '<b>' + TESTCASE13 + test13status + '<b>' + TESTCASE14 + test14status + \
        '<b>' + TESTCASE15 + test15status + '<b>' + TESTCASE16 + \
        test16status + '<b>' + TESTCASE17 + \
        test17status + '<b>' + TESTCASE18 + test18status + '<b>' + TESTCASE19 + test19status + '<b>' + TESTCASE20 + \
        test20status + '<b>' + TESTCASE21 + test21status + '<b>' + \
        TESTCASE22 + test22status + '<b>' + TESTCASE23 + test23status
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
