def greet(name, owner):
    # Usamos um operador ternário para decidir qual saudação retornar.
    # Se o nome fornecido for igual ao nome do proprietário (owner), retorna "Hello boss".
    # Caso contrário (else), retorna "Hello guest".

    # We use a ternary operator to decide which greeting to return.
    # If the provided name is equal to the owner's name, it returns "Hello boss".
    # Otherwise (else), it returns "Hello guest".

    return "Hello boss" if name == owner else "Hello guest"