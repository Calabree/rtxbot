import smtplib, ssl

class SendAlert():
    def sendAlert(self, email, password, notifyContact, port, cardName, purchaseURL):
        
        message=f"Subject:Card In Stock \nCard- {cardName}\nURL- {purchaseURL}"
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(email, password)
            server.sendmail(email, notifyContact, message)