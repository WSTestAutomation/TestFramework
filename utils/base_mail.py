# coding=utf-8

import os
import datetime
from exchangelib import Credentials, Account, Message, Mailbox, HTMLBody, FileAttachment


def email(report_path, attachment):
    html_report_path = os.path.join(report_path, attachment)

    content = open(html_report_path, 'rb').read()
    credentials = Credentials('autotest@juntianbroker.com', 'Jt123456')
    account = Account('autotest@juntianbroker.com', credentials=credentials, autodiscover=True)

    item = Message(
        account=account,
        subject="{} Automation Report".format(datetime.datetime.now().strftime('%Y-%m-%d-%H')),
        body=HTMLBody('This is an automation run result report email. Please do not reply.*'),
        to_recipients=[
            Mailbox(email_address='aval@wicresoft.com'),
            Mailbox(email_address='allent@wicresoft.com'),
            Mailbox(email_address='shiquanzh@wicresoft.com'),
        ],
    )

    my_file = FileAttachment(name=attachment, content=content)
    item.attach(my_file)
    item.send()


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(__file__))
    report1_path = os.path.join(base_dir, 'reports', 'smart_report')
    email(report1_path, 'smart_main_scenario_report_20190814130019.html')
