import re

lineTypeDict = {
    "heading": {
        "re": r'^#+\s*(.*?)\s*$'
    },
    "checkbox": {
        "re": r'^\s*\*\s*\[[\sx]\]\s*(.*?)\s*$'
    },
    "bullet": {
        "re": r'^(\s*\*\s*(.*?)\s*)$'
    },
    "property": {
        "re": r'^\s*(.*?)\s*:\s*(.*?)\s*$'
    },
}

lineTypeCheckingOrder = ["heading", "checkbox", "bullet", "property"]

def parseIssueLine(issueLine):
    for type in lineTypeCheckingOrder:
        lineTypeDef = lineTypeDict[type]
        lineTypeRE = lineTypeDef["re"]
        lineMatches = re.fullmatch(lineTypeRE, issueLine)
        if lineMatches:
            issueLineDict = {"lineType": type, "issueLine": issueLine}
            return issueLineDict
    return {"lineType": "other", "issueLine": issueLine}

# testResult = parseIssueLine("other")
# print(testResult)