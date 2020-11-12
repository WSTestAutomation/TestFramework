# coding=utf-8

import re
import datetime
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror, error


class Email:
    def __init__(self, receiver, path=None):
        """初始化Email
        :param title: 邮件标题，必填。
        :param message: 邮件正文，非必填。
        :param path: 附件路径，可传入list（多附件）或str（单个附件），非必填。
        :param server: smtp服务器，必填。
        :param sender: 发件人，必填。
        :param password: 发件人密码，必填。
        :param receiver: 收件人，多收件人用“；”隔开，必填。
        """

        self.title = "{} Automation Report".format(datetime.datetime.now().strftime('%Y-%m-%d-%H'))
        self.message = "This is an automation run result report email.Please do not reply."
        self.files = path

        self.msg = MIMEMultipart('related')

        self.server = '10.22.18.27'
        self.sender = 'autotest@juntianbroker.com'
        self.receiver = receiver
        self.password = 'Jt123456'

    def _attach_file(self, att_file):
        att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]
        self.msg.attach(att)

    def send(self):

        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

    # 邮件正文
        if self.message:
            self.msg.attach(MIMEText(self.message, 'plain'))

        # 添加附件，支持多个附件（传入list），或者单个附件（传入str）
        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files, str):
                self._attach_file(self.files)

        # 连接服务器并发送
        try:
            smtp_server = smtplib.SMTP(self.server)  # 连接sever
            smtp_server.connect(self.server, 25)
        except (gaierror and error) as e:
            logging.exception('发送邮件失败,无法连接到SMTP服务器，检查网络以及SMTP服务器. %s', e)            
        else:
            try:
                smtp_server.starttls()
                smtp_server.login('autotest', self.password)  # 登录
            except smtplib.SMTPAuthenticationError as e:
                logging.exception('用户名密码验证失败！%s', e)
            else:
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())  # 发送邮件
            finally:
                smtp_server.quit()  # 断开连接
                logging.info('发送邮件"{0}"成功! 收件人：{1}。如果没有收到邮件，请检查垃圾箱,同时检查收件人地址是否正确'.format(self.title, self.receiver))


if __name__ == '__main__':
    """
    report = os.path.join(REPORT_PATH, 'autotest_report_20191115001116.html')
    Email(receiver='shiquanzh@wicresoft.com', path=report).send()
    """
