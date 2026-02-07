def any_arrows(arrows):
    for arrow in arrows:
        # Se 'damaged' não estiver no dicionário ou for False, a flecha é boa
        # If 'damaged' is not in the dictionary or is False, the arrow is good
        if not arrow.get('damaged', False):
            return True 
            
    # Se percorrer tudo e não achar nenhuma boa, retorna False
    # If it goes through everything and finds no good ones, return False
    return False


def any_arrows(arrows):
    # any() verifica se existe QUALQUER item que satisfaça a condição
    # 'not i.get('damaged', False)' significa: "Não está danificada"

    # any() checks if there is ANY item that satisfies the condition
    # 'not i.get('damaged', False)' means: "It is not damaged"

    return any(not arrow.get('damaged', False) for arrow in arrows)