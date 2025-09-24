def validar_comprobante_numero(numero):
    """Valida que el número de comprobante sea un entero positivo de doce dígitos."""
    if not isinstance(numero, int) or numero <= 0:
        return False
    return len(str(numero)) == 12