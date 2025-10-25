import parseIssueFile

parseTest = parseIssueFile.parseIssueFile('C:/Users/coope/Python/issueTool/testData/ISSUES/sampleIssue.md')

for parse in parseTest['parsedIssueLines']:
    for key, value in parse.items():
        print(f"{key}: {value}")
    print()