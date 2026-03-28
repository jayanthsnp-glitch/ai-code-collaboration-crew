from typing import Optional

class InvalidUserInputError(Exception):
    """ Raised when the user input is invalid or empty """
    pass


def create_greeting_message(
    user_name: Optional[str] = None, 
    user_greeting: Optional[str] = "Hello"
) -> str:
    """
    Creates a greeting message for the user.

    Args:
    - user_name (str): The name of the user. Defaults to None.
    - user_greeting (str): The greeting message. Defaults to "Hello".

    Returns:
    - A greeting message for the user.

    Raises:
    - ValueError: If either user_name or user_greeting is None or empty.
    """

    # Validate the user input
    if not user_name:
        raise InvalidUserInputError("User name is required")
    if not user_greeting.strip():
        raise InvalidUserInputError("Greeting message is required")

    # Create the greeting message
    greeting_message = f"{user_greeting}, {user_name}!"

    return greeting_message


# Usage example
try:
    greeting = create_greeting_message("John Doe", "Hi")
    print(greeting)  # Output: Hi, John Doe!
except InvalidUserInputError as e:
    print(f"Error: {e}")