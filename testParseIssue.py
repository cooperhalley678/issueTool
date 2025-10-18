import parseIssueLine
import parseIssueLines

import json

sampleLines=[
    "# Title",
    "## Section Title",
    "status: inProgress",
    "* [ ]",
    "* [x]",
    "* ",
    "other",
]

for sample in sampleLines:
    parseLineResult=parseIssueLine.parseIssueLine(sample)
    print(parseLineResult)

print()

sampleIssue="""
# dilithium-crytal-converter-v2

This task is to build the v 2.0 converter for changing dilithium into batteries.

## Actions

* [ ] setup up assembly lab
* [ ] purchase timespacers
  * [ ] identify number needed
  * [ ] create estimate 
  * [x] give to purchasing
* [ ] construct inner mechanism
  * [ ] finalize model
  * [ ] print in matter printer
* [ ] construct out box with controls
  * [x] assemble inner mechanism into box
* [ ] isolated lab test completely
* [x] attach automated inputs
* [ ] supervise automated test runs
* [ ] get final checkoff

## Questions

* [ ] Is it possible to create new dilithium transfer sub-network
* [ ] Does spock need to review timespacers?


## Notes

* dilithium supplier is connected to the d5 substations
* warp drive adapters come with liquid state dilithium coupler, need replacement with jigawhat outputs.

## Status

status: done
priority: 1-50q4
precedence: 8
created: 2050-04-21
"""

sampleIssueLines=sampleIssue.split('\n')
argsDictTest={'issueLines':sampleIssueLines}
parseLinesResult=parseIssueLines.parseIssueLines(argsDictTest)
print(json.dumps(parseLinesResult, indent=2))
