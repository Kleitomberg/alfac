import re
from math import ceil

class DigitoVerificador:
    """Classe responsável pelo cálculo matemático do Módulo 11 alfanumérico."""
    def __init__(self, conteudo: str):
        self.conteudo = conteudo.upper()
        self.pesos = []

    def _calcula_ascii(self, char: str) -> int:
        # Regra oficial: Valor ASCII - 48
        return ord(char) - 48

    def _gerar_pesos(self):
        tamanho = len(self.conteudo)
        # Repetições de 2 a 9
        num_repeticoes = ceil(tamanho / 8)
        for _ in range(num_repeticoes):
            self.pesos.extend(range(2, 10))
        self.pesos = self.pesos[:tamanho]
        self.pesos.reverse()

    def calcula(self) -> int:
        self._gerar_pesos()
        # Soma ponderada dos valores convertidos pelos pesos
        soma = sum(a * b for a, b in zip(map(self._calcula_ascii, self.conteudo), self.pesos))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

class CNPJ:
    """Classe de negócio para tratar a estrutura do CNPJ."""
    def __init__(self, cnpj_input: str):
        # Remove caracteres de pontuação comuns
        self.limpo = "".join(filter(str.isalnum, str(cnpj_input))).upper()

    def e_valido(self) -> bool:
        # 1. Validação de tamanho e formato (Regex oficial do Serpro)
        if not re.match(r'^([A-Z]|\d){12}\d{2}$', self.limpo):
            return False
        
        # 2. Bloqueio de letras proibidas pela norma (I, O, Q)
        if any(c in self.limpo for c in "IOQ"):
            return False

        # 3. Bloqueio de valores zerados (comum em testes de fumaça)
        if self.limpo == "0" * 14:
            return False

        base = self.limpo[:12]
        dv_informado = self.limpo[12:]
        
        # Cálculo do DV1
        dv1 = DigitoVerificador(base).calcula()
        # Cálculo do DV2 (base + dv1)
        dv2 = DigitoVerificador(base + str(dv1)).calcula()
        
        return f"{dv1}{dv2}" == dv_informado

def validar_cnpj(cnpj: str) -> bool:
    """Interface simplificada para uso externo."""
    return CNPJ(cnpj).e_valido()