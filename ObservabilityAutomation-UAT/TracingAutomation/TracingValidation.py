#!/usr/lib/python3

import os
import yaml
import calendar
import datetime
import GetAuthToken
import TestCases.TraceComingValidation
import TracingAutomation.TestCases.TracesLabelvalues
import TestCases.ServiceLabelValueValidation
import TestCases.OperationLabelValueValidation
import TestCases.ServiceValidation
import TestCases.ServiceTracesValidation
import TestCases.OperationValidation
import TestCases.OperationTracesValidation
import TestCases.TracingQueryFiltersValidation
import SendReporttoGoogleChat

config_and_report_directory = os.getcwd()
workdirectory = os.getcwd() + "TracingAutomation"

configfile = open(workdirectory + "/INTAutomationconfig.yml")
parsedconfigfile = yaml.load(configfile, Loader=yaml.FullLoader)
reportfile = open(config_and_report_directory + "/Report.yml")
parsedreportfile = yaml.load(reportfile, Loader=yaml.FullLoader)
portal = parsedconfigfile["portal_url"]
tenantid = parsedconfigfile["client_id"]
clientkey = parsedconfigfile["client_key"]
clientsecret = parsedconfigfile["client_secret"]
tracingoperation = parsedconfigfile["TracingOperation"]
tracingservice = parsedconfigfile["TracingService"]
traces_googlechat_webhook_url = parsedconfigfile["TRACES_GOOGLECHAT_WEBHOOK_URL"]
portal_name = parsedconfigfile['Portal_Name']

currentdate = datetime.date.today().strftime("%d %b %Y")
currenttime = datetime.datetime.utcnow()
starttimeUNIX = calendar.timegm(currenttime.timetuple())
starttimemilisec = starttimeUNIX * 1000
starttimenanosec = starttimeUNIX * 1000000000
endtime = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
endtimeUNIX = calendar.timegm(endtime.timetuple())
endtimemilisec = endtimeUNIX * 1000
endtimenanosec = endtimeUNIX * 1000000000

GetAuthToken.GetAuthToken(clientkey, clientsecret, portal)
AuthToken = GetAuthToken.token

TESTCASE1 = "\nTEST CASE-1 : VALIDATION OF TRACES COMING OR NOT \n\n"
TestCases.TraceComingValidation.TracingData(
    config_and_report_directory, AuthToken, tenantid, portal, starttimenanosec, endtimenanosec, parsedreportfile)

TESTCASE2 = "\n\nTESTCASE-2 : CHECK ALL LABELS-VALUES COMING OR NOT\n"
TracingAutomation.TestCases.TracesLabelvalues(config_and_report_directory, AuthToken, tenantid, portal,
                                  starttimemilisec, endtimemilisec, parsedreportfile)

TESTCASE3 = "\n\nTEST CASE-3 : VALIDATION OF SERVICE LABEL ATTRIBUTE VALUE COMING OR NOT \n\n"
TestCases.ServiceLabelValueValidation.ServiceLabelValue(
    config_and_report_directory, AuthToken, tenantid, portal, starttimemilisec, endtimemilisec, parsedreportfile)

TESTCASE4 = "\n\nTEST CASE-4 : VALIDATION OF OPERATION LABEL ATTRIBUTE VALUE COMING OR NOT \n\n"
TestCases.OperationLabelValueValidation.OperationLabelValue(
    config_and_report_directory, AuthToken, tenantid, portal, starttimemilisec, endtimemilisec, parsedreportfile)

TESTCASE5 = "\n\nTEST CASE-5 : VALIDATION OF TRACING SERVICE COMING OR NOT \n\n"
TestCases.ServiceValidation.TracingService(
    config_and_report_directory, AuthToken, tenantid, portal, tracingservice, starttimemilisec, endtimemilisec, parsedreportfile)

TESTCASE6 = "\n\nTEST CASE-6 : VALIDATION OF SERVICE TRACES COMING OR NOT\n\n"
if "Pass" in parsedreportfile['TracingServiceNameStatus']:
    TestCases.ServiceTracesValidation.ServiceTracingData(config_and_report_directory, AuthToken, tenantid, portal,
                                                         tracingservice, starttimenanosec, endtimenanosec, parsedreportfile)
else:
    parsedreportfile['TracingServiceDataStatus'] = "Value is not Coming for Tracing Service Label Attribute Hence Skipping the Validation of Service Traces Test Case"
    with open(config_and_report_directory + "/Report.yml", "w") as file:
        yaml.dump(parsedreportfile, file)

TESTCASE7 = "\n\nTEST CASE-7 : VALIDATION OF TRACING OPERATION COMING OR NOT\n\n"
TestCases.OperationValidation.TracingOperation(config_and_report_directory, AuthToken, tenantid, portal, tracingoperation,
                                               starttimemilisec, endtimemilisec, parsedreportfile)

TESTCASE8 = "\n\nTEST CASE-8 : VALIDATION OF OPERATION TRACES COMING OR NOT\n\n"
TestCases.OperationTracesValidation.OperationTracingData(config_and_report_directory, AuthToken, tenantid, portal, tracingoperation,
                                                         starttimenanosec, endtimenanosec, parsedreportfile)

TESTCASE9 = "\n\nTEST CASE-9 : VALIDATION OF QUERY FILTERS FUNCTIONALITY FOR EACH ATTRIBUTE\n\n"
TestCases.TracingQueryFiltersValidation.TracingQueryFilters(config_and_report_directory, AuthToken, tenantid, portal,
                                                            starttimemilisec, endtimemilisec, starttimenanosec, endtimenanosec, parsedreportfile)

tracescomingstatus = parsedreportfile['TracesComingStatus']
labelvaluesnotcoming = parsedreportfile['LabelValuesNotComing']
servicelabelvaluestatus = parsedreportfile['ServiceLabelValueStatus']
opearationlabelvaluestatus = parsedreportfile['OpearationLabelValueStatus']
tracingservicenamestatus = parsedreportfile['TracingServiceNameStatus']
tracingservicedatastatus = parsedreportfile['TracingServiceDataStatus']
tracingoperationstatus = parsedreportfile['TracingOperationStatus']
tracingoperationdatastatus = parsedreportfile['TracingOperationDataStatus']
queryfilter_functionalitylist = parsedreportfile['QueryFilter_FunctionalityList']

GOOGLECHAT_WEBHOOK_URL = traces_googlechat_webhook_url

SendReporttoGoogleChat.send_googlechat_message(GOOGLECHAT_WEBHOOK_URL, portal_name, currentdate, TESTCASE1, TESTCASE2, TESTCASE3,
                                               TESTCASE4, TESTCASE5, TESTCASE6, TESTCASE7, TESTCASE8, TESTCASE9, tracescomingstatus, labelvaluesnotcoming , servicelabelvaluestatus, opearationlabelvaluestatus, tracingservicenamestatus, tracingservicedatastatus, tracingoperationstatus, tracingoperationdatastatus, queryfilter_functionalitylist)

parsedreportfile['LabelValuesNotComing'] = []
parsedreportfile['QueryFilter_FunctionalityList'] = []

with open(config_and_report_directory + "/Report.yml", "w") as file:
    yaml.dump(parsedreportfile, file)
