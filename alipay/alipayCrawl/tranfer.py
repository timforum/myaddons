from datetime import datetime
from alipay import AliPay


class Payment():
    def __init__(self, appid, url):
        '''
        ???????
        :param appid: ??appid
        :param url: ?????url
        '''
        self.app_private_key_string = open("app_private_key.txt").read()  # ??????????TXT??????
        self.alipay_public_key_string = open("alipay_public_key.txt").read()  # ?????
        self.alipay = AliPay(
            appid=appid,
            app_notify_url=url,
            app_private_key_string=self.app_private_key_string,
            alipay_public_key_string=self.alipay_public_key_string,
            sign_type="RSA2",
            debug=True
        )


def pay(self, payee_account, amount, payee_real_name=None, remark=None, payer_show_name=None,
        payee_type="ALIPAY_LOGONID"):
    '''
    ????
    :param payee_account: ?????
    :param amount: ????
    :param payee_real_name:
    :param remark: ?????
    :param payer_show_name: ????
    :param payee_type: ?????
    :return:
    '''
    result = self.alipay.api_alipay_fund_trans_toaccount_transfer(
        datetime.now().strftime("%Y%m%d%H%M%S"),
        payee_type=payee_type,  # ???????
        payee_account=payee_account,  # ?????
        amount=amount,  # ????
        payee_real_name=payee_real_name,  # ???????????????????
        remark=remark,  # ????
        payer_show_name=payer_show_name  # ?????

    )
    # result={'code':'10000','msg':'Success','order_id': '','out_biz_no': '', 'pay_date': '2017-06-26 14:36:25'}
    # ?????https://docs.open.alipay.com/api_28/alipay.fund.trans.toaccount.transfer

    if result['code'] == '10000':
        if result['msg'] == "Success":
            print("????" + " ?????" + result["order_id"])

    else:
        print(result)
        print(result['sub_msg'])