import parseIssueLine

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
    parseResult = parseIssueLine.parseIssueLine(sample)
    print(parseResult)
