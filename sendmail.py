#First way Program of Sending mail using python



#import smtplib
#content="Hi, Bro how are you?"
#mail=smtplib.SMTP('smtp,gmail.com',587)
#mail.ehlo()
#mail.starttls()
#mail.login('singh@gmail.com','Password')
#mail.sendmail('singh1@gmail.com','singh2@gmail.com',content)
#mail.close()



#Second way Program of Sending mail using python



import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('singh1@gmail.com','Password')
 
msg = "YOUR MESSAGE!"
server.sendmail('singh1@gmail.com','singh2@gmail.com',msg)
server.quit()
