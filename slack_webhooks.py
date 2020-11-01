#!/usr/bin/env python

import json
import requests

#Read alertblock.json file for alert data
with open("alertblock.json", "r") as alerts:
    alertdata = json.load(alerts)

resp = {}
resp['status'] = "Success"


# Function to receive alert data into Slack using Webhook url
def data_to_slack(message,slack_webhook_url):
    
    slack_data = json.dumps({'blocks': message})
    response = requests.post(slack_webhook_url, data=slack_data,
        headers={'Content-Type': 'application/json'}
    )
         
    if ("error" in response):
        resp['status'] = "Failure"
        resp['reason'] = response.text
        resp['statusCode'] = response.status_code
    else:
        resp['status'] = "Alerts routed successfully to Slack channel"
        resp['reason'] = response.text
        resp['statusCode'] = response.status_code
    
    return (resp)
    


if __name__ == '__main__':
    slack_webhook = 'https://hooks.slack.com/services/************************************************'                                                 
    data_to_slack(alertdata,slack_webhook)
   

