def correo(asunto, mensaje,servidor,usuario,clave,destino):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    COMMASPACE = ', '
    mail_user = usuario
    mail_password = clave
    destinatarios = destino
    msg = MIMEMultipart()
    msg['From'] = mail_user
    msg['To'] = ", ".join(destinatarios)
    msg['Subject'] =  asunto
    message = mensaje
    msg.attach(MIMEText(message))
    sent_from = mail_user
    server = smtplib.SMTP_SSL(servidor, 465)
    server.ehlo()
    server.login(mail_user, mail_password)
    server.sendmail(mail_user,destinatarios,msg.as_string())
    server.close()
    return 0
