import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
  port = 2525
  smtp_server = 'smtp.mailtrap.io'
  login = '71b3dcee303626'
  password = '7cdc597589bc3a'
  message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"
  sender_email = 'info@means-business.com'
  receiver_email = 'admin@means-business.com'
  msg = MIMEText(message, 'html')
  msg['Subject'] = 'Lexus Feedback'
  msg['From'] = sender_email
  msg['To'] = receiver_email

  # Send email
  with smtplib.SMTP(smtp_server, port) as server:
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())