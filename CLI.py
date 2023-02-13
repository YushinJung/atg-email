import click
import send

@click.group()
def CLI():
    """
    How to use sending emails
    """
    pass

@CLI.command()
@click.argument('sender_email')
@click.argument('password')
@click.argument('receiver_email')
@click.argument('subject')
@click.argument('text_message')
def send_simple(sender_email, password, receiver_email, subject, text_message):
    print(sender_email, password, receiver_email, subject, text_message)
    send.send_simpleNotice(sender_email, password, receiver_email, subject, text_message)
    
if __name__=='__main__':
    CLI()