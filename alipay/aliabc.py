# -*- coding: utf-8 -*-

from alipay import AliPay

alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAjVqRKgIcITCBJEKXCp2GmQyjg9pO6GCAGBGFePZ5En0VWyl/4XNy5ApVKwkpKKo3N3p6tBrRCI4MSWL4oW3IwG3wf0zUR7uEOFvR/i2QFYXlx0aq1xoGjPltOsHkyUb7UUcG12Eb2t9ZGqFV59rdpUbpE40eY/gb16keY9Ht8Wfx02jWhIW/GW38bpYvIUxTq1jfIaB9sbZhtWLkQ5QnsMauIqnsytqaAEH1MyhgMMUqZdtMSt8Bdop9c+FjrJtEOeHpLzI0yWcKe6J36kla8qhzmYUGe2gUdEJoV30DF/Tyiszmn486k0KfxS2wYbZhF2fsIetlmJ0vQvmNV8KeBQIDAQAB
-----END PUBLIC KEY-----"""

app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAjVqRKgIcITCBJEKXCp2GmQyjg9pO6GCAGBGFePZ5En0VWyl/4XNy5ApVKwkpKKo3N3p6tBrRCI4MSWL4oW3IwG3wf0zUR7uEOFvR/i2QFYXlx0aq1xoGjPltOsHkyUb7UUcG12Eb2t9ZGqFV59rdpUbpE40eY/gb16keY9Ht8Wfx02jWhIW/GW38bpYvIUxTq1jfIaB9sbZhtWLkQ5QnsMauIqnsytqaAEH1MyhgMMUqZdtMSt8Bdop9c+FjrJtEOeHpLzI0yWcKe6J36kla8qhzmYUGe2gUdEJoV30DF/Tyiszmn486k0KfxS2wYbZhF2fsIetlmJ0vQvmNV8KeBQIDAQABAoIBAQCGFCYlxqKQCMY2csN6WjlV61sesnCukvpt2hDU0FW/Z85eDlsyqqOMExD+JU5ZODvv78l8FQO6LaMR6UMVPGFzxdSdq26gLAoau13Qz78f60YtY6ahKhqUlfM6DLjLAv1X9xtSKNaXIcwPKoGlz0D2iPCEjxMImEswoUYmQPaGSD0ICNl1eguOcaBU/pz1Rd14Rr+2/MrzYV7Yr1ghIoAQu+DzZHG83A3GK8MjbcMBf2u8mee1fCsKSs8pxjS8K9yJfTPNOZaJFMJqZ9ccX9GpS+bIgt7FW4gN5FRYNCeOfXklbxeckYmKsgtfSwoi+5oBw/JYFWGyJA7ayfkHf6pxAoGBAMhd0JoAfeLAi+VZoSF1UYPb5+RCQPpMvra6Y4K4WWSTC4ZJnfded4YGJz8p7yfDGGugXIrqucrbxpL18StfEu3Na0JXevy697taIZtUF80T9NaeV7Kz10LwLNUcN52ErZ/GKSi6mW60eLSvWaLtEjP7GnXIf9OWTrQl9BSumFZDAoGBALSaFxGlAsQ2gASBqfrcUKfKJxnAXqHZ+H+y1rkxPuAYMk+qPhBErkfn4R4c68XdZeyyZY0T5PfZtz4ar4Fhve+2NDZsheav++vBYG/7dGyj413n8l/8Goompn3QpGUeoddtFkVqXdx9eHgvBXsWsPA47IEfSigb4Zfc23vI1soXAoGAaNpvZ6gKOLd6fjNBVzkFx3M1DwZ86n9u7kDsAmRmo3Mv/L5ZpDITaleeAjf3p185UFlDFI9xWu9YI2ABLSk7xqZREw6klc1iBvFL1PVU30UqQ4XpbuMeKzF0xLFXiV79XTdeIqpD0OMwp5170v8tH3awiiK6ggeOeEfES25y2fECgYEAhlHMMn1NT21RTQi6yS6udfxtlEN0nl+k6CS0ekvb/YNBd+qf+i16iVQ2I9VSrXh6Y85SpNhVBNlR5cinG0z8nJogvxF7jRT6Al9yQBb+ggZqBd+KbkTr4C/ax9wzSFm9+KDTXZE8ec5/mLMwGlnIAwHzNB13Y9lIsU+7lZbL2MUCgYBCkcQv6XUtT/jLzGFGTTOwQ8bsYfwVhgIrnzZahvC91eW1cYUyjHt/uKR4nfpsU6JiofwMrE2aCfhj+7HX3GCSZyDwa9IIdko+NkNT4B8nGhgyk6TFVDAae8OX97NSaFuuoB6HAqkz1VMihfEkufsbTUXet2KxUvV7tXiosHYD4g==
-----END RSA PRIVATE KEY-----"""

# 实例化支付应用
alipay = AliPay(
    appid = "2021000120606030",# 你创建的沙箱环境的appid
    app_notify_url = None,
    app_private_key_string = app_private_key_string,
    alipay_public_key_string = alipay_public_key_string,
    sign_type= "RSA2"
)

#发起支付请求
order_string = alipay.api_alipay_trade_page_pay(
    out_trade_no="33451",   #订单号，多次请求不能一样
    total_amount=str(10000),  #支付金额
    subject="生鲜交易",   #交易主题
    return_url=None,
    notify_url=None
)

print("https://openapi.alipaydev.com/gateway.do?"+order_string)