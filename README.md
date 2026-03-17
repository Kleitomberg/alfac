# 🏢 alfac - Validador de CNPJ Alfanumérico

[![PyPI version](https://img.shields.io/pypi/v/alfac.svg)](https://pypi.org/project/alfac/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A **alfac** é uma biblioteca Python leve e robusta desenvolvida para validar CNPJs seguindo a nova norma técnica do Governo Brasileiro). Ela é compatível tanto com o formato numérico tradicional quanto com o novo formato **alfanumérico**.

## 📖 Contexto
Devido ao esgotamento das combinações numéricas, o Governo Brasileiro passou a adotar letras nas 12 primeiras posições do CNPJ. Esta biblioteca implementa o cálculo oficial de **Módulo 11** com conversão ASCII, conforme os manuais técnicos do Serpro.

## ✨ Funcionalidades
- ✅ **Validação Universal:** Aceita CNPJs antigos (numéricos) e novos (alfanuméricos).
- 🛠️ **Limpeza Automática:** Ignora pontos, barras e traços automaticamente.
- 🚫 **Regras de Negócio:** Bloqueia caracteres proibidos (I, O, Q) e sequências inválidas.
- 🏗️ **Arquitetura Sólida:** Baseada em classes para fácil manutenção e extensibilidade.

## 📦 Instalação

```bash
pip install alfac

```

## 🚀 Como Usar

### Validação Rápida
A forma mais simples de usar a biblioteca é através da função `validar_cnpj`:

```python
from alfac import validar_cnpj

# ✅ Suporta o novo formato alfanumérico (Nota Técnica 2024)
is_valid_alfa: bool = validar_cnpj("SASB0MA7000124")
print(IS_VALID)  # True

# ✅ Suporta o formato numérico tradicional com ou sem máscara
is_valid_num: bool = validar_cnpj("11.222.333/0001-81")
print(is_valid_num)  # True

# ❌ Caracteres proibidos (I, O, Q não são permitidos no CNPJ alfanumérico)
err_letra: bool = validar_cnpj("12I45678000199")
print(err_letra)  # False

# ❌ Formato inválido ou tamanho incorreto
err_formato: bool = validar_cnpj("ABC-123")
print(err_formato)  # False

# ❌ Dígitos Verificadores (DVs) que não batem com a base
err_calculo: bool = validar_cnpj("SASB0MA7000100")
print(err_calculo)  # False