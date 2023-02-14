import click
import email_utils.send as send

@click.group()
def CLI():
    """
    CLI to send emails
    """
    pass

@CLI.command()
@click.argument('sender_email')
@click.argument('password')
@click.argument('receiver_email')
@click.argument('subject')
@click.argument('text_message')
@click.option('-f', '--d_file', default='', show_default=True, help='file path to attach')

def send_simple(sender_email, password, receiver_email, subject, text_message, d_file):
    print(sender_email, password, receiver_email, subject, text_message, d_file)
    send.send_simpleEmail(sender_email, password, receiver_email, subject, text_message, d_file=d_file)
    
if __name__=='__main__':
    CLI()