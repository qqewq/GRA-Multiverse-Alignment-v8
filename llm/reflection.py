def reflect(old_text, alignment_signal):
    return f"""
Previous statement:
{old_text}

Alignment signal:
{alignment_signal}

Improve your statement to reduce conflict with others.
"""
