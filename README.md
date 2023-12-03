# BlackSpam

![BlackSpam](black_spam_image.jpg)

## Information

Tool Name: BlackSpam
Author: HackAzara
Copyright: HackAzara (2023)
Github: https://github.com/HackAzara/BlackSpam
Telegram: https://t.me/h4ckAzara
Description: BlackSpam is an email sending tool.

## Usage

python3 black_spam.py -s [SMTP_SERVER] -p [SMTP_PORT] -e [SENDER_EMAIL] -pw [PASSWORD] -r [RECIPIENT_EMAIL] -n [SENDER_NAME] -sb [SUBJECT] -b [BODY] -a [ATTACHMENTS] --html
```

- `-s, --smtp_server`: SMTP server.
- `-p, --smtp_port`: SMTP port.
- `-e, --sender_email`: Sender's email address.
- `-pw, --password`: Sender's password.
- `-r, --recipient_email`: Recipient's email address.
- `-n, --sender_name`: Custom sender name.
- `-sb, --subject`: Email subject.
- `-b, --body`: Email body.
- `-a, --attachments`: List of attachment file paths.
- `--html`: Send email body in HTML format.

## Installation

1. Clonez le dépôt :

git clone https://github.com/HackAzara/BlackSpam.git

2. Installez les dépendances :

pip install -r requirements.txt


3. Exécutez le script :

python3 black_spam.py -s [SMTP_SERVER] -p [SMTP_PORT] -e [SENDER_EMAIL] -pw [PASSWORD] -r [RECIPIENT_EMAIL] -n [SENDER_NAME] -sb [SUBJECT] -b [BODY] -a [ATTACHMENTS] --html
