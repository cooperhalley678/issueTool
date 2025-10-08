import parseIssueLineFile

sampleLines = [
    "# Title",
    "## Section Title",
    "status: inProgress",
    "* [ ]",
    "* [x]",
    "* ",
    "other",
]

for sample in sampleLines:
    parseResult = parseIssueLineFile.parseIssueLine(sample)
    print(parseResult)
