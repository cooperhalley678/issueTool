import re

lineTypeCheckingOrder=["heading", "checkbox", "bullet", "property"]

lineTypeDict={
    "heading": {
        "re": r'^(?P<hashes>#+)\s*(?P<heading>.*?)\s*$',
        "extractData": lambda m: {
            "heading": m.group("heading"),
            "level": len(m.group("hashes")),
        },
    },
    "checkbox": {
        "re": r'^\s*\*\s*\[(?P<mark>[\sx0])\]\s*(?P<label>.*?)\s*$',
        "extractData": lambda m: {
            "mark": m.group("mark"),
            "marked": m.group("mark") != " ",
            "didntDo": m.group("mark") == "0",
            "executed": m.group("mark") == "x",
            "label": m.group("label"),
        },
    },
    "bullet": {
        "re": r'^(\s*\*\s*(?P<label>.*?)\s*)$',
        "extractData": lambda m: {"label": m.group("label")},
    },
    "property": {
        "re": r'^\s*(?P<name>.*?)\s*:\s*(?P<value>.*?)\s*$',
        "extractData": lambda m: {
            "name": m.group("name"),
            "value": m.group("value"),
        },
    },
}

indentRegex = r'^(\s*).*?$'
def parseIssueLine(issueLine):
    foundIssueLineDict = None
    for type in lineTypeCheckingOrder:
        lineTypeDef=lineTypeDict[type]
        lineTypeRE=lineTypeDef["re"]
        extractData = lineTypeDef["extractData"]
        lineMatches=re.fullmatch(lineTypeRE,issueLine)
        if lineMatches:
            detailsDict = extractData(lineMatches)
            issueLineDict={
                "lineType":type,
                "issueLine":issueLine,
                **detailsDict
            }
            print(lineMatches.groupdict())
            foundIssueLineDict = issueLineDict
            break # found it! first past the post
    
    # get indent
    indentMatch = re.fullmatch(indentRegex, issueLine);
    indentStr = indentMatch.group(1) if indentMatch else ""
    indentVal = len(indentStr)
    if not foundIssueLineDict:
        foundIssueLineDict = {
            "lineType":"other",
            "issueLine":issueLine,
        }
    foundIssueLineDict["indent"] = indentVal
    return foundIssueLineDict
if __name__ == "main":
    parseIssueLine("# Title")
