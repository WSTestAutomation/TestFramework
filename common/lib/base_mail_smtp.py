# coding=utf-8
import os
import re
import smtplib
import logging
import datetime
from socket import gaierror, error
from email.mime.text import MIMEText
from common.lib.base_yaml import Yaml
from email.mime.multipart import MIMEMultipart
from common.lib.base_config import COMMON_CONFIG_DIR


class Email:
    def __init__(self, path=None):
        self.files = path
        self.msg = MIMEMultipart('related')
        self.mail_config_path = os.path.join(
            COMMON_CONFIG_DIR, 'mail_config.yaml')

    def _attach_file(self, att_file):
        att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]
        self.msg.attach(att)

    def send(self, yaml_setting_name='smtp_default'):
        """mail_config.yaml 中需要填入的参数：
        :param yaml_setting_name: yaml块中首行的key值，默认为smtp_default。
        :param subject: 邮件标题，必填。
        :param message: 邮件正文, 必填。
        :param sender: 发件人，必填。
        :param to: 收件人，必填。多收件人用“ ; ”隔开。
        :param cc: 抄送，非必填。多收件人用“ , ”隔开。
        :param server: smtp服务器，默认为：mail.wicresoft.com。
        :param user: 登录邮箱服务器用户名，发送给外部邮箱时必填。
        :param password: 登录邮箱服务器密码，发送给外部邮箱时必填。
        """
        mail_settings = Yaml(self.mail_config_path).read_get(yaml_setting_name)

        server = mail_settings['server']
        user = mail_settings['user']
        password = mail_settings['password']
        subject = "{} {}".format(
            mail_settings['subject'], datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        sender = mail_settings['sender']
        to = mail_settings['to']
        cc = mail_settings['cc']
        message = mail_settings['message']

        self.msg['Subject'] = subject
        self.msg['From'] = sender
        self.msg['To'] = to
        self.msg['Cc'] = cc

    # 邮件正文
        if message:
            self.msg.attach(MIMEText(message, 'plain'))

        # 添加附件，支持多个附件（传入list），或者单个附件（传入str）
        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files, str):
                self._attach_file(self.files)

        # 连接服务器并发送
        try:
            smtp_server = smtplib.SMTP(server)  # 连接sever
            smtp_server.connect(server, 25)
        except (gaierror and error) as e:
            logging.exception('发送邮件失败,无法连接到SMTP服务器，检查网络以及SMTP服务器. %s', e)
        else:
            try:
                if password:
                    smtp_server.starttls()
                    smtp_server.login(user, password)
                else:
                    logging.info(' 登录邮箱服务器的密码为空，跳过登录。')
            except smtplib.SMTPAuthenticationError as e:
                logging.exception('用户名密码验证失败！%s', e)
            else:
                to_addrs = to.split(";") + cc.split(",")
                smtp_server.sendmail(sender, to_addrs, self.msg.as_string())  # 发送邮件
                logging.info(
                    '发送邮件"{0}"成功! 收件人：{1}。如果没有收到邮件，请检查垃圾箱,同时检查收件人地址是否正确'.format(subject, to))
            finally:
                smtp_server.quit()


if __name__ == '__main__':
    """
    report = os.path.join(REPORT_PATH, 'autotest_report_20201112174407.html')
    Email(path=report).send()
    """
