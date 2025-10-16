import parseIssueLine

def parseIssueLines(argsDict):
    issueDict={'parsedIssueLines':[]}
    for issueLine in argsDict['issueLines']:
        issueLineDict=parseIssueLine.parseIssueLine(issueLine)
        issueDict['parsedIssueLines'].append(issueLineDict)
    return issueDict
