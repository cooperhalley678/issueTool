import parseIssueLines

def parseIssueFile(filepath):
    issueLines = {'issueLines':[]}
    fileObject = open(filepath)
    for line in fileObject:
        issueLines['issueLines'].append(line.strip())
    parseIssueLinesResult = parseIssueLines.parseIssueLines(issueLines)
    return parseIssueLinesResult
