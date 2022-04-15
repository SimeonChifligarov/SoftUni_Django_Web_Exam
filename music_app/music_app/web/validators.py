from django.core.exceptions import ValidationError

VALIDATE_ONLY_LETTERS_OR_NUMBERS_EXCEPTION_MESSAGE = 'Ensure this value contains only letters, numbers, and underscore.'


def validate_only_letters_or_numbers(value):
    for c in value:
        if not (c.isalnum() or c == '_'):
            raise ValidationError(VALIDATE_ONLY_LETTERS_OR_NUMBERS_EXCEPTION_MESSAGE)
