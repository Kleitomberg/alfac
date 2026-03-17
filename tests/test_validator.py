import pytest

from alfac.validator import validar_cnpj


@pytest.mark.parametrize("cnpj", [
    "588B78BM000145", 
    "X4MEXGBD000177", 
    "SASB0MA7000124",  # Exemplo que você validou
    "11.222.333/0001-81", # Tradicional com máscara
    "92645463000129"      # Tradicional sem máscara
])
def test_cnpjs_validos(cnpj):
    assert validar_cnpj(cnpj) is True

@pytest.mark.parametrize("cnpj", [
    "12I45678000199",     # Letra I proibida
    "12O45678000199",     # Letra O proibida
    "11222333000180",     # DV errado
    "00000000000000",     # Zerado
    "ABC",                # Tamanho curto
  
])
def test_cnpjs_invalidos(cnpj):
    if cnpj is None:
        with pytest.raises(Exception):
            validar_cnpj(cnpj)
    else:
        assert validar_cnpj(cnpj) is False