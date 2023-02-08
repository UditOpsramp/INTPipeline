#!/usr/lib/python3
import yaml
import datetime
import calendar
import os
import GetAuthToken
import TestCases.Apps_Logs
import TestCases.Count_Logs
import TestCases.Hosts_Logs
import TestCases.QueryFilters
import TestCases.Labels
import TestCases.Label_Values
import TestCases.FilteringLogs
import TestCases.MultiFilters
import TestCases.NotContainsFilter
import TestCases.LineFilter
import TestCases.MaskingLogs
import AlertDefintionValidation.Createalertdef
import AlertDefintionValidation.GetAlertDetails
import AlertDefintionValidation.DeleteAlertDefinition
import CloudAppsValidation.AWS_Logs
import CloudAppsValidation.AWSLambda_Logs
import CloudAppsValidation.Azure_Logs
import CloudAppsValidation.GCP_Logs
import LogForwardApps.Fluentd_Logs
import LogForwardApps.Fluentbit_Logs
import SendReport_to_GooleChat
import SendReport_to_Slack

config_and_report_directory = os.getcwd() + "/ObservabilityAutomation-INT"
workdirectory = os.path.dirname(os.path.abspath(__file__))

configfile = open(config_and_report_directory + "/INTAutomationconfig.yml")
parsedconfigfile = yaml.load(configfile, Loader=yaml.FullLoader)
reportfile = open(config_and_report_directory + "/Report.yml")
parsedreportfile = yaml.load(reportfile, Loader=yaml.FullLoader)
portal = parsedconfigfile["portal_url"]
tenantid = parsedconfigfile["client_id"]
clientkey = parsedconfigfile["partner_key"]
clientsecret = parsedconfigfile["partner_secret"]
awstoken = parsedconfigfile["AWS_TOKEN"]
azuretoken = parsedconfigfile["AZURE_TOKEN"]
gcptoken = parsedconfigfile["GCP_TOKEN"]
logs_googlechat_webhook_url = parsedconfigfile["LOGS_GOOGLECHAT_WEBHOOK_URL"]
slack_webhook_url = parsedconfigfile["SLACK_WEBHOOK_URL"]
portal_name = parsedconfigfile['Portal_Name']

currentdate = datetime.date.today().strftime("%d %b %Y")
currenttime = datetime.datetime.utcnow()
starttimeUNIX = calendar.timegm(currenttime.timetuple())
starttimenanosec = starttimeUNIX * 1000000000
endtime = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
endtimeUNIX = calendar.timegm(endtime.timetuple())
endtimenanosec = endtimeUNIX * 1000000000

# Put Hash before the Test Case to Skip (Example #TestCases.Apps_Logs.AppLogs)

GetAuthToken.GetAuthToken(clientkey, clientsecret, portal)
AuthToken = GetAuthToken.token

TESTCASE1 = "\nTEST CASE-1 : VALIDATION OF AWS LOGS\n\n"
CloudAppsValidation.AWS_Logs.AWSLogs(
    config_and_report_directory, parsedreportfile, AuthToken, awstoken, portal, tenantid, starttimenanosec, endtimenanosec)

TESTCASE2 = "\n\nTEST CASE-2 : VALIDATION OF AWS LAMBDA LOGS\n\n"
CloudAppsValidation.AWSLambda_Logs.AWSLambda_Logs(
    config_and_report_directory, parsedreportfile, AuthToken, awstoken, portal, tenantid, starttimenanosec, endtimenanosec)

TESTCASE3 = "\n\nTEST CASE-3 : VALIDATION OF AZURE LOGS\n\n"
CloudAppsValidation.Azure_Logs.AZURELogs(
    config_and_report_directory, parsedreportfile, AuthToken, azuretoken, portal, tenantid, starttimenanosec, endtimenanosec)

TESTCASE4 = "\n\nTEST CASE-4 : VALIDATION OF GCP LOGS\n\n"
CloudAppsValidation.GCP_Logs.GCPLogs(
    config_and_report_directory, parsedreportfile, AuthToken, gcptoken, portal, tenantid, starttimenanosec, endtimenanosec)

TESTCASE5 = "\n\nTESTCASE-5 : CHECK ALL LABELS COMING OR NOT\n"
TestCases.Labels.LabelsTest(config_and_report_directory, workdirectory, parsedreportfile,
                            AuthToken, tenantid, portal, starttimeUNIX, endtimeUNIX)

TESTCASE6 = "\n\nTESTCASE-6 : CHECK ALL LABELS-VALUES COMING OR NOT\n"
TestCases.Label_Values.LabelValues(
    config_and_report_directory, parsedreportfile, AuthToken, tenantid, portal, starttimeUNIX, endtimeUNIX)

TESTCASE7 = "\n\nTEST CASE-7 : VALIDATION OF APP'S LOGS\n\n"
TestCases.Apps_Logs.AppLogs(
    config_and_report_directory, workdirectory, parsedreportfile, AuthToken, portal, tenantid, starttimenanosec, endtimenanosec)

TESTCASE8 = "\n\nTEST CASE-8 : VALIDATION OF COUNT OF LOGS\n\n"
TestCases.Count_Logs.CountLogs(
    config_and_report_directory, workdirectory, parsedreportfile, parsedconfigfile, AuthToken, portal, tenantid, starttimeUNIX, endtimeUNIX)

TESTCASE9 = "\n\nTEST CASE-9 : VALIDATION OF LOGS FOR EACH HOST\n\n"
TestCases.Hosts_Logs.HostLogs(config_and_report_directory, parsedreportfile, AuthToken, tenantid, portal,
                              starttimeUNIX, endtimeUNIX, starttimenanosec, endtimenanosec)

TESTCASE10 = "\n\nTEST CASE-10 : VALIDATION OF NOT CONTAINS FILTER FUNCTIONALITY\n\n"
TestCases.NotContainsFilter.QueryNotContainsLogs(
    config_and_report_directory, workdirectory, parsedreportfile, parsedconfigfile, AuthToken, portal, tenantid, starttimenanosec, endtimenanosec)

TESTCASE11 = "\n\nTEST CASE-11 : VALIDATION OF MULTI-FILTERING FUNCTIONALITY\n\n"
TestCases.MultiFilters.MultiFilter(
    config_and_report_directory, parsedreportfile, AuthToken, tenantid, portal, starttimenanosec, endtimenanosec)

TESTCASE12 = "\n\nTEST CASE-12 : VALIDATION OF LINE-FILTERING FUNCTIONALITY\n\n"
TestCases.LineFilter.LineFilter(
    config_and_report_directory, parsedreportfile, AuthToken, tenantid, portal, starttimenanosec, endtimenanosec)

TESTCASE13 = "\n\nTEST CASE-13 : VALIDATION OF FILTERING LOGS FUNCTIONALITY\n\n"
TestCases.FilteringLogs.FilteringLogs(
    config_and_report_directory, workdirectory, parsedreportfile, parsedconfigfile, AuthToken, tenantid, portal, starttimenanosec, endtimenanosec)

TESTCASE14 = "\n\nTEST CASE-14 : VALIDATION OF MASKING LOGS FUNCTIONALITY\n\n"
TestCases.MaskingLogs.MaskingLogs(
    config_and_report_directory, workdirectory, parsedreportfile, parsedconfigfile, AuthToken, tenantid, portal, starttimenanosec, endtimenanosec)

TESTCASE15 = "\n\nTEST CASE-15 : VALIDATION OF FLUENTD LOGS\n\n"
LogForwardApps.Fluentd_Logs.FluentDLogs(
    config_and_report_directory, parsedreportfile, AuthToken, portal, tenantid, starttimenanosec, endtimenanosec)

TESTCASE16 = "\n\nTEST CASE-16 : VALIDATION OF FLUENT-BIT LOGS\n\n"
LogForwardApps.Fluentbit_Logs.FluentBitLogs(
    config_and_report_directory, parsedreportfile, AuthToken, portal, tenantid, starttimenanosec, endtimenanosec)

TESTCASE17 = "\n\nTEST CASE-17 : VALIDATION OF QUERY FILTERS FUNCTIONALITY FOR EACH ATTRIBUTE"
TestCases.QueryFilters.QueryFilter(
    config_and_report_directory, parsedreportfile, AuthToken, tenantid, portal, starttimeUNIX, endtimeUNIX, starttimenanosec, endtimenanosec)

TESTCASE18 = "\n\nTEST CASE-18 : VALIDATION OF CREATION OF LOG-ALERT DEFINITION\n\n"
AlertDefintionValidation.Createalertdef.CreateLogAlertDefinition(
    config_and_report_directory, workdirectory, parsedreportfile, AuthToken, portal, tenantid)

TESTCASE19 = "\n\nTEST CASE-19 : VALIDATION OF ALERT GENERATION\n\n"
AlertDefintionValidation.GetAlertDetails.GetAlertDetails(
    config_and_report_directory, workdirectory, parsedreportfile, AuthToken, portal, tenantid)

TESTCASE20 = "\n\nTEST CASE-20 : VALIDATION OF DELETION OF LOG-ALERT DEFINITION\n\n"
AlertDefintionValidation.DeleteAlertDefinition.DeleteLogAlertDefinition(
    config_and_report_directory, workdirectory, parsedreportfile, AuthToken, portal, tenantid)

GeneratedLogsCount = TestCases.Count_Logs.generatedlogscountvalue
Logscomingonportal = TestCases.Count_Logs.logscomingonportal

logs_alllabelstatus = parsedreportfile['Logs_AllLabelStatus']
logs_labelvaluesnotcoming = parsedreportfile['Logs_LabelValuesNotComing']
appslogsstaus = parsedreportfile['Source_Logs']
countlogsstaus = parsedreportfile['Count_Logs']
hostlogsstatus = parsedreportfile['Host_Logs']
logs_queryfilterstatuslist = parsedreportfile['Logs_QueryFilter_Functionality']
logs_notcontainsfunctionalitystatus = parsedreportfile['Logs_NotContains_Functionality']
logs_multifilter_functionaltystatus = parsedreportfile['Logs_MultiFilter_Functionalty']
logs_linefilter_functionalitystatus = parsedreportfile['Logs_LineFilter_Functionality']
filteringlogsfunctionalitystatus = parsedreportfile['FilteringLogs_Functionality']
maskinglogsfunctionalitystatus = parsedreportfile['MaskingLogs_Functionality']
logalertcreationfunctionalitystatus = parsedreportfile['LogAlertCreation']
logalertgenerationfunctionalitystatus = parsedreportfile['LogAlertGeneration']
logalertdeletionfunctionalitystatus = parsedreportfile['LogAlertDeletion']
awslogsstatus = parsedreportfile['AWS_Logs']
awslambdalogsstatus = parsedreportfile['AWSLambda_Logs']
azurelogsstatus = parsedreportfile['AZURE_Logs']
gcplogsstatus = parsedreportfile['GCP_Logs']
fluentdlogsstatus = parsedreportfile['FluentD_Logs']
fluentbitlogsstatus = parsedreportfile['FluentBit_Logs']

GOOGLECHAT_WEBHOOK_URL = logs_googlechat_webhook_url

SLACK_WEBHOOK_URL = slack_webhook_url

SendReport_to_GooleChat.send_googlechat_message(GOOGLECHAT_WEBHOOK_URL, portal_name, currentdate, TESTCASE1, TESTCASE2, TESTCASE3, TESTCASE4, TESTCASE5, TESTCASE6, TESTCASE7, TESTCASE8, TESTCASE9, TESTCASE10, TESTCASE11, TESTCASE12, TESTCASE13, TESTCASE14, TESTCASE15, TESTCASE16, TESTCASE17, TESTCASE18, TESTCASE19,TESTCASE20, logs_alllabelstatus, logs_labelvaluesnotcoming, appslogsstaus, countlogsstaus, GeneratedLogsCount, Logscomingonportal, hostlogsstatus, logs_queryfilterstatuslist,
                                                logs_notcontainsfunctionalitystatus, logs_multifilter_functionaltystatus, logs_linefilter_functionalitystatus, filteringlogsfunctionalitystatus, maskinglogsfunctionalitystatus, logalertcreationfunctionalitystatus, logalertgenerationfunctionalitystatus, logalertdeletionfunctionalitystatus, awslogsstatus,awslambdalogsstatus, azurelogsstatus, gcplogsstatus, fluentdlogsstatus, fluentbitlogsstatus)

SendReport_to_Slack.send_slack_message(SLACK_WEBHOOK_URL, portal_name, currentdate, logs_alllabelstatus, logs_labelvaluesnotcoming, appslogsstaus, countlogsstaus, hostlogsstatus, logs_queryfilterstatuslist,
                                       logs_notcontainsfunctionalitystatus, logs_multifilter_functionaltystatus, logs_linefilter_functionalitystatus, filteringlogsfunctionalitystatus, maskinglogsfunctionalitystatus, logalertcreationfunctionalitystatus, logalertgenerationfunctionalitystatus, logalertdeletionfunctionalitystatus, awslogsstatus,awslambdalogsstatus, azurelogsstatus, gcplogsstatus, fluentdlogsstatus, fluentbitlogsstatus)

parsedreportfile['QueryFilter_Functionality'] = []
parsedreportfile['AllLabelStatus'] = []
parsedreportfile['LabelValuesNotComing'] = []
with open(config_and_report_directory + "/Report.yml", "w") as file:
    yaml.dump(parsedreportfile, file)

