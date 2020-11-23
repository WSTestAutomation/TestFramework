# coding=utf-8

import os
import datetime
from exchangelib import Credentials, Account, Message, Mailbox, HTMLBody, FileAttachment
from common.lib.base_yaml import Yaml
from common.lib.base_config import COMMON_CONFIG_DIR

def email(report_path, attachment, setting_name='default'):

    def get_receiver(mailbox_list):
        list_receiver = []
        for mailbox in mailbox_list.split(','):
            list_receiver.append(Mailbox(email_address=mailbox.strip(' ')))
        return list_receiver

    config_file_path = os.path.join(COMMON_CONFIG_DIR, 'mail_config.yaml')
    settings = Yaml(config_file_path).read_get(setting_name)

    sender = settings['sender']
    pwd = settings['password']
    subject = settings['subject']
    list_to = get_receiver(settings['to'])
    list_cc = get_receiver(settings['cc'])

    html_report_path = os.path.join(report_path, attachment)
    content = open(html_report_path, 'rb').read()
    credentials = Credentials(sender, pwd)
    account = Account(sender, credentials=credentials, autodiscover=True)

    item = Message(
        account=account,
        subject="{} {}".format(datetime.datetime.now().strftime('%Y-%m-%d-%H'), subject),
        #body=HTMLBody(content.decode('utf-8')),
        body=HTMLBody('This is an automation run result report email. Please do not reply.*'),
        to_recipients=list_to,
        cc_recipients=list_cc,
    )

    my_file = FileAttachment(name=attachment, content=content)
    item.attach(my_file)
    item.send()


if __name__ == '__main__':
    report_file_path= ''
    email(report_file_path, 'smart_main_scenario_report_20190814130019.html')
