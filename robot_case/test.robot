*** Setting ***
Library     RequestsLibrary
Library     Collections

*** Test Case ***
test_get_event_list
    ${payload}=   Create Dictionary  eid=1
    Create Session  event http://127.0.0.1:8000/api
    ${r}=   Get Request     event   /get_event_list/    params=${payload}
    Should Be Equal     ${r.status_code}   200
    log  ${r.json()}
    ${dict}     set variable  ${r.json}
    #断言结果
    ${msg}  Get from Dictionary     ${dict}     set test message
    Should Be Equal     ${msg}  success
    ${sta}  Get from Dictionary     ${dict}     status
    ${status}   Evaluate   int(200)
    Should Be Equal     ${sta}  ${status}