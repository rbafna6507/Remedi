import requests

calc_url = 'https://docs.google.com/forms/d/1FAIpQLScVeL1SkeB9Q80CN1tlzdfbCoIfslCb6fS2xqdepZYJg5eIKg/formResponse'
compsci_url = 'https://docs.google.com/forms/d/1FAIpQLSeLbRcBtMidmKYN01g_D6LeK4RyX1bftJSABGmViJe9yzdxOg/formResponse'
psych_url = 'https://docs.google.com/forms/d/1FAIpQLSdpIiX1PE_EQxv_ThJ0TBXBoTXlB_faom4g5nQfPSpHVdp49Q/formResponse'
lang_url = 'https://docs.google.com/forms/d/1FAIpQLSfj88HOwxsQaGu7wimc776_3c6B4FfMfO78lOCL5uj6lYlBfA/formResponse'
urls = [calc_url, compsci_url, psych_url, lang_url]

calc_subs = {"entry.1931030274": "Bafna", "entry.597690435": "Rohan", "entry.2146828073": "None", "entry.903501512": "Yes"}
compsci_subs = {"entry.1931030274": "Bafna", "entry.597690435": "Rohan", "entry.2146828073": "None", "entry.903501512": "Yes"}
psych_subs = {"entry.340679026": "Bafna, Rohan"}
lang_subs = {"entry.1931030274": "Bafna", "entry.597690435": "Rohan", "entry.620403578": "4th Period", "entry.903501512": "Yes"}
subs = [calc_subs, compsci_subs, psych_subs, lang_subs]

for url, sub in zip(urls, subs):
    requests.post(url, sub)
    print(url + " goes to " + sub)