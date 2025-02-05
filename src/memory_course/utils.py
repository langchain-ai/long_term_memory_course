def parse_email(email_input: dict) -> dict:
    """Parse an email input dictionary.

    Args:
        email_input (dict): Dictionary containing email fields:
            - author: Sender's name and email
            - to: Recipient's name and email
            - subject: Email subject line
            - email_thread: Full email content

    Returns:
        tuple[str, str, str, str]: Tuple containing:
            - author: Sender's name and email
            - to: Recipient's name and email
            - subject: Email subject line
            - email_thread: Full email content
    """
    return (
        email_input["author"],
        email_input["to"],
        email_input["subject"],
        email_input["email_thread"],
    )
