import smtplib, ssl


class LomaEmailSmtp():
	'''Takes email and password to initiate
	Manages sending email. 
	'''
	def __init__(self, email, password):
		self.port = 465
		self.smtp_server = "smtp.gmail.com"
		self.sender_email = email
		self.password = password
		self.context = ssl.create_default_context()

	def send_txt_email(self, recipients, message):
		with smtplib.SMTP_SSL(self.smtp_server, self.port, context = self.context) as server:
			server.login(self.sender_email, self.password)
			for recipient in recipients:
				server.sendmail(self.sender_email, recipient, message)
				print(f"Email sent to {recipient}")





