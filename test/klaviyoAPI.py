import klaviyo

client = klaviyo.Klaviyo(public_token='HtseXi', private_token='INSERT_PRIVATE_KEY_HERE')

def sendToKlaviyo():
    client.Public.track(
        'Bought Wet Food',
        email='ninaephremidze@gmail.com',
        customer_properties={
            "$first_name":"Nina",
            "$last_name":"Ephremidze",
            "$city":"San Diego",
            "$phone_number":"4797904555",
            "image": "https://cdn.mos.cms.futurecdn.net/cQXSWLZTT48Xt4yw7rpsj6-1200-80.jpg",
        },
        properties={
            "Items":{
                "item1_name":"wet food",
                "item1_image_link":"https://cdn.mos.cms.futurecdn.net/cQXSWLZTT48Xt4yw7rpsj6-1200-80.jpg",
                "item1_link":"www.google.com",
            },
            "categories":['wet food', 'dry food', 'catnip'],
            "cat_owner":'yes',
            "cat_quantity":'2'
        }
    )

sendToKlaviyo()

print("Sent to Klaviyo! (Hopefully!)")