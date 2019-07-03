# Posting to a Slack channel
def send_message_to_slack(text):
    from urllib import request, parse
    import json

    post = {"text": "{0}".format(text)}

    try:
        json_data = json.dumps(post)
        req = request.Request("https://hooks.slack.com/services/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",
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))

#send_message_to_slack('Dude, this Slack message is coming from my Python program!')

msg = input('write somethin:')
send_message_to_slack(msg)
