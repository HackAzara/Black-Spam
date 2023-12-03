import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from pyfiglet import Figlet
from termcolor import colored
import argparse

def send_email(smtp_server, smtp_port, sender_email, password, recipient_email, sender_name, subject, body, attachments, html_body):
    # Créez un objet MIMEMultipart
    msg = MIMEMultipart()

    # Ajoutez l'expéditeur et le destinataire à l'e-mail avec le nom personnalisé
    msg['From'] = f'{sender_name} <{sender_email}>'
    msg['To'] = recipient_email

    # Sujet de l'e-mail
    msg['Subject'] = subject

    # Corps de l'e-mail (texte ou HTML)
    if html_body:
        msg.attach(MIMEText(body, 'html'))
    else:
        msg.attach(MIMEText(body, 'plain'))

    # Ajoutez des pièces jointes
    for attachment in attachments:
        with open(attachment, "rb") as file:
            part = MIMEApplication(file.read(), Name=attachment)
            part['Content-Disposition'] = f'attachment; filename="{attachment}"'
            msg.attach(part)

    # Établissez une connexion avec le serveur SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Connectez-vous à votre compte
    server.login(sender_email, password)

    # Envoyez l'e-mail
    server.sendmail(sender_email, recipient_email, msg.as_string())

    # Fermez la connexion avec le serveur SMTP
    server.quit()

    print('E-mail envoyé avec succès')

def main():
    parser = argparse.ArgumentParser(description='Envoi d\'e-mails via SMTP')
    parser.add_argument('-s', '--smtp_server', required=True, help='Serveur SMTP')
    parser.add_argument('-p', '--smtp_port', required=True, type=int, help='Port SMTP')
    parser.add_argument('-e', '--sender_email', required=True, help='Adresse e-mail de l\'expéditeur')
    parser.add_argument('-pw', '--password', required=True, help='Mot de passe de l\'expéditeur')
    parser.add_argument('-r', '--recipient_email', required=True, help='Adresse e-mail du destinataire')
    parser.add_argument('-n', '--sender_name', required=True, help='Nom personnalisé de l\'expéditeur')
    parser.add_argument('-sb', '--subject', default='Test', help='Sujet de l\'e-mail')
    parser.add_argument('-b', '--body', default='Ceci est un test.', help='Corps de l\'e-mail')
    parser.add_argument('-a', '--attachments', nargs='+', default=[], help='Liste des chemins des pièces jointes')
    parser.add_argument('--html', action='store_true', help='Envoyer le corps de l\'e-mail au format HTML')
    
    args = parser.parse_args()

    send_email(args.smtp_server, args.smtp_port, args.sender_email, args.password, args.recipient_email, args.sender_name, args.subject, args.body, args.attachments, args.html)

if __name__ == "__main__":
    big_figlet = Figlet(width=80, justify='center')
    big_text = big_figlet.renderText("Black  spam")
    print(colored(big_text, 'blue'))
    print(colored("                                            Information : ", 'red'))
    print(colored("                                            ToolName: BlackSpam", 'red'))
    print(colored("                                            Author: HackAzara", 'red'))
    print(colored("                                            Copyright: HackAzara (2023)", 'red'))
    print(colored("                                            Github : https://github.com/HackAzara", 'red'))
    print(colored("                                            Telegram : @h4ckAzara", 'red'))
    print(colored("                                            Description: BlackSpam is an email sending tool\n", 'red'))
    main()
