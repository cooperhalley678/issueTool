import parseIssueLine

def parseIssueLines(argsDict):
    issueDict = {'parsedIssueLines' : []}
    for issueLine in argsDict.values():
        issueLineDict = parseIssueLine(issueLine)
        issueDict['parsedIssueLines'].append(issueLineDict)
    return issueDict
