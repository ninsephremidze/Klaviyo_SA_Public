import klaviyo  # friendly interface to Track & Identify API
import requests  # standard http library, used to provide interface to Templates API
import urllib.parse  # used for URL encoding

pub_key = 'HtseXi'
pri_key = 'INSERT_PRIVATE_KEY_HERE'  # this should never be exposed to public

'''
The Track API is intended to capture unique customer events (metrics).
In order to demonstrate interfacing with the Track API, we will use it here to create metrics to serve as a log for
whenever the Business Owner pulls media from Instagram and pushes it to Klaviyo.
'''
business_owner = klaviyo.Klaviyo(public_token=pub_key, private_token=pri_key)

template_url = "https://a.klaviyo.com/api/v1/email-templates"  # Template API endpoint

template_name = "Imported From Instagram"
template_name_URL_enc = urllib.parse.quote(template_name)  # URL encode template name

insta_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png"

insta_img = "https://miro.medium.com/max/1200/1*ab8xSbKUPQgDQaJvdmJxLA.jpeg"
html_template = "<html><body><img src=" + insta_img + "></body></html>"
html_template_URL_enc = urllib.parse.quote(html_template)  # URL encode template content

payload = "api_key=" + pri_key + "&name=" + template_name_URL_enc + "&html=" + html_template_URL_enc

headers = {
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.request("POST", template_url, data=payload, headers=headers)  # push image to Klaviyo, create new template
# print(response.text)

def logInstagramImportAsMetric():
    business_owner.Public.track(
        'Imported Instagram Image',
        email='ninaephremidze@gmail.com',  # represents business owner, although Track API is intended to track customers
        customer_properties={
            "$first_name":"Business",
            "$last_name":"Owner",
            "$city":"Tblisi",
            "$phone_number":"4797904555",
            "image": insta_logo,
        },
    )


logInstagramImportAsMetric()

print("Imported Image from Instagram to Klaviyo!")