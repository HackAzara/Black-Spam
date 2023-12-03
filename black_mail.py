import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import keyring

class EmailSender:
    # Définir les couleurs comme attributs de classe
    bg_color = "#f0f0f0"  # Light gray background
    label_color = "#333333"  # Dark gray text

    def __init__(self, root):
        self.root = root
        self.root.title("Email Sender App")

        # Configuration des couleurs pour la racine
        self.root.configure(background=self.bg_color)

        self.smtp_server_label = ttk.Label(root, text="SMTP Server:", background=self.bg_color, foreground=self.label_color)
        self.smtp_server_entry = ttk.Entry(root)

        self.smtp_port_label = ttk.Label(root, text="SMTP Port:", background=self.bg_color, foreground=self.label_color)
        self.smtp_port_entry = ttk.Entry(root)

        self.sender_email_label = ttk.Label(root, text="Sender Email:", background=self.bg_color, foreground=self.label_color)
        self.sender_email_entry = ttk.Entry(root)

        self.password_label = ttk.Label(root, text="Password:", background=self.bg_color, foreground=self.label_color)
        self.password_entry = ttk.Entry(root, show='*')

        self.recipient_emails_label = ttk.Label(root, text="Recipient Emails:", background=self.bg_color, foreground=self.label_color)
        self.recipient_emails_entry = ttk.Entry(root)

        self.sender_name_label = ttk.Label(root, text="Sender Name:", background=self.bg_color, foreground=self.label_color)
        self.sender_name_entry = ttk.Entry(root)

        self.subject_label = ttk.Label(root, text="Subject:", background=self.bg_color, foreground=self.label_color)
        self.subject_entry = ttk.Entry(root)

        self.body_label = ttk.Label(root, text="Body:", background=self.bg_color, foreground=self.label_color)
        self.body_entry = tk.Text(root, height=5, width=30)

        self.html_body_var = tk.BooleanVar()
        self.html_body_checkbox = ttk.Checkbutton(root, text="HTML Body", variable=self.html_body_var, style="TCheckbutton")

        self.send_button = ttk.Button(root, text="Send Email", command=self.send_email, style="TButton")

        self.setup_layout()

    def setup_layout(self):
        padx = 10
        pady = 5

        # Header
        header_label = ttk.Label(self.root, text="Email Sender", font=('Helvetica', 16, 'bold'), background=self.bg_color, foreground=self.label_color)
        header_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        # Form
        self.smtp_server_label.grid(row=1, column=0, padx=padx, pady=pady, sticky="w")
        self.smtp_server_entry.grid(row=1, column=1, padx=padx, pady=pady, sticky="w")

        self.smtp_port_label.grid(row=2, column=0, padx=padx, pady=pady, sticky="w")
        self.smtp_port_entry.grid(row=2, column=1, padx=padx, pady=pady, sticky="w")

        self.sender_email_label.grid(row=3, column=0, padx=padx, pady=pady, sticky="w")
        self.sender_email_entry.grid(row=3, column=1, padx=padx, pady=pady, sticky="w")

        self.password_label.grid(row=4, column=0, padx=padx, pady=pady, sticky="w")
        self.password_entry.grid(row=4, column=1, padx=padx, pady=pady, sticky="w")

        self.recipient_emails_label.grid(row=5, column=0, padx=padx, pady=pady, sticky="w")
        self.recipient_emails_entry.grid(row=5, column=1, padx=padx, pady=pady, sticky="w")

        self.sender_name_label.grid(row=6, column=0, padx=padx, pady=pady, sticky="w")
        self.sender_name_entry.grid(row=6, column=1, padx=padx, pady=pady, sticky="w")

        self.subject_label.grid(row=7, column=0, padx=padx, pady=pady, sticky="w")
        self.subject_entry.grid(row=7, column=1, padx=padx, pady=pady, sticky="w")

        self.body_label.grid(row=8, column=0, padx=padx, pady=pady, sticky="w")
        self.body_entry.grid(row=8, column=1, padx=padx, pady=pady, sticky="w")

        self.html_body_checkbox.grid(row=9, column=1, padx=padx, pady=pady, sticky="w")

        self.send_button.grid(row=10, column=0, columnspan=2, pady=20)

    def send_email(self):
        smtp_server = self.smtp_server_entry.get()
        smtp_port = self.smtp_port_entry.get()
        sender_email = self.sender_email_entry.get()
        password = self.password_entry.get()
        recipient_emails = [email.strip() for email in self.recipient_emails_entry.get().split(',')]
        sender_name = self.sender_name_entry.get()
        subject = self.subject_entry.get()
        body = self.body_entry.get("1.0", tk.END)
        html_body = self.html_body_var.get()

        try:
            self._send_email(smtp_server, smtp_port, sender_email, password, recipient_emails, sender_name, subject, body, html_body)
            self.clear_fields()
            self.show_success_message()
        except ValueError as ve:
            messagebox.showerror("Error", f"Validation Error: {str(ve)}")
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror("Error", "Authentication failed. Please check your email and password.")
        except Exception as e:
            messagebox.showerror("Error", f"Error sending email: {str(e)}")

    def _send_email(self, smtp_server, smtp_port, sender_email, password, recipient_emails, sender_name, subject, body, html_body):
        if not all([smtp_server, smtp_port, sender_email, password, recipient_emails, sender_name, subject, body]):
            raise ValueError("All fields are required.")

        msg = MIMEMultipart()
        msg['From'] = f'{sender_name} <{sender_email}>'
        msg['To'] = ', '.join(recipient_emails)
        msg['Subject'] = subject

        if html_body:
            msg.attach(MIMEText(body, 'html'))
        else:
            msg.attach(MIMEText(body, 'plain'))

        # Stockage sécurisé du mot de passe
        keyring.set_password('email_sender_app', sender_email, password)

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_emails, msg.as_string())
        server.quit()

    def clear_fields(self):
        # Efface tous les champs après l'envoi
        for entry in [self.smtp_server_entry, self.smtp_port_entry, self.sender_email_entry, self.password_entry,
                      self.recipient_emails_entry, self.sender_name_entry, self.subject_entry, self.body_entry]:
            entry.delete(0, tk.END)

        self.html_body_var.set(False)

    def show_success_message(self):
        messagebox.showinfo("Success", "Email sent successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailSender(root)
    root.mainloop()
