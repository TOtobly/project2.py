import requests,json
from discord import Webhook,Embed,RequestsWebhookAdapter

def webhook_url():
    return 'https://discordapp.com/api/webhooks/698151737491587122/lWM73-6dEjZWPDq2ufv6ulDV_YcPBll9xtTR3HutPmaOTI5eD9KVNHnJt5f8YQ93OK4k'

def avatar_url():
    return 'https://cdn.shopify.com/s/files/1/0219/2362/files/NiceKicks_Logo_downsized_black_140x.png?v=1565118222'

def get_variants():
    url = 'https://shopnicekicks.com/collections/mens-kicks/products/adidas-superstar-mens-running-white-black.json'
    resp = requests.get(url)
    j = json.loads(resp.text)
    product_title = j['product']['title']
    img_url = j['product']['image']['src']
    variants = j['product']['variants']
    result = []
    for v in variants:
        title = v['title']
        v_id = v['id']
        inventory_quantity = v['inventory_quantity']
        act_link = 'https://shopnicekicks.com/cart/{}:1'.format(v_id)
        v_result = '[{}]({})'.format(title,act_link)
        if inventory_quantity >0:
            result.append(v_result)
    return product_title, img_url, result


def send_webhook():
    url = webhook_url()
    product_title,img_url,result=get_variants()
    webhook = Webhook.from_url(url=url,adapter=RequestsWebhookAdapter())
    embed = Embed(title=product_title, url=url)
    embed.add_field(name='可用尺码', value='\n'.join(result))
    embed.set_thumbnail(url=img_url)
    webhook.send(embed=embed,avatar_url=avatar_url(),username='shopnicekicks')


send_webhook()
