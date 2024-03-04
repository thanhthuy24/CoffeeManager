import json
import uuid
import requests
import hmac
import hashlib

# parameters send to MoMo get get payUrl
endpoint = "https://test-payment.momo.vn/v2/gateway/api/create"
accessKey = "F8BBA842ECF85"
secretKey = "K951B6PE1waDMi640xX08PD3vg6EkVlz"
orderInfo = "pay with MoMo"
partnerCode = "MOMO"
redirectUrl = "http://localhost:5000/payment"
ipnUrl = "http://localhost:5000/payment"
amount = "50000"
orderId = str(uuid.uuid4())
requestId = str(uuid.uuid4())
extraData = ""  # pass empty value or Encode base64 JsonString
partnerName = "MoMo Payment"
requestType = "payWithATM"
storeId = "Test Store"
paymentCode = "L/U2a6KeeeBBU/pQAa+g8LilOVzWfvLf/P4XOnAQFmnkrKHICj51qrOTUQ+YrX8/Xs1YD4IOdyiGSkCfV6Je9PeRzl3sO+mDzXNG4enhigU3VGPFh67a37dSwItMJXRDuK64DCqv35YPQtiAOVVZV35/1XBw1rWopmRP03YMNgQWedGLHwmPSkRGoT6XtDSeypJtgbLZ5KIOJsdcynBdFEnHAuIjvo4stADmRL8GqdgsZ0jJCx/oq5JGr8wY+a4g9KolEOSTLBTih48RrGZq3LDBbT4QGBjtW+0W+/95n8W0Aot6kzdG4rWg1NB7EltY6/A8RWAHJav4kWQoFcxgfA=="
orderGroupId = ""
autoCapture = True
lang = "vi"
orderGroupId = ""
signature = "ca3c203f0c16873e688fada17…ee116b636ff407d6fe39"

# before sign HMAC SHA256 with format: accessKey=$accessKey&amount=$amount&extraData=$extraData&ipnUrl=$ipnUrl
# &orderId=$orderId&orderInfo=$orderInfo&partnerCode=$partnerCode&redirectUrl=$redirectUrl&requestId=$requestId
# &requestType=$requestType
rawSignature = "accessKey=" + accessKey + "&amount=" + amount + "&extraData=" + extraData + "&ipnUrl=" + ipnUrl + "&orderId=" + orderId \
               + "&orderInfo=" + orderInfo + "&partnerCode=" + partnerCode + "&redirectUrl=" + redirectUrl\
               + "&requestId=" + requestId + "&requestType=" + requestType

# puts raw signature
print("--------------------RAW SIGNATURE----------------")
print(rawSignature)
# signature
h = hmac.new(bytes(secretKey, 'ascii'), bytes(rawSignature, 'ascii'), hashlib.sha256)
signature = h.hexdigest()
print("--------------------SIGNATURE----------------")
print(signature)

# json object send to MoMo endpoint

data = {
    'partnerCode': partnerCode,
    'orderId': orderId,
    'partnerName': partnerName,
    'storeId': storeId,
    'ipnUrl': ipnUrl,
    'amount': amount,
    'paymentCode': paymentCode,
    'lang': lang,
    'autoCapture': autoCapture,
    'orderInfo': orderInfo,
    'requestId': requestId,
    'extraData': extraData,
    'signature': signature,
    'orderGroupId': orderGroupId
}
print("--------------------JSON REQUEST----------------\n")
data = json.dumps(data)
print(data)

clen = len(data)
response = requests.post(endpoint, data=data, headers={'Content-Type': 'application/json', 'Content-Length': str(clen)})

# f.close()
print("--------------------JSON response----------------\n")
print(response.json())
