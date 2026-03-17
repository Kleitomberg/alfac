# 🏢 alfac - Validador de CNPJ Alfanumérico

[![PyPI version](https://img.shields.io/pypi/v/alfac.svg)](https://pypi.org/project/alfac/)
[![Tests](https://github.com/seu-usuario/alfac/actions/workflows/tests.yml/badge.svg)](https://github.com/seu-usuario/alfac/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A **alfac** é uma biblioteca Python leve e robusta desenvolvida para validar CNPJs seguindo a nova norma técnica do Governo Brasileiro (2024/2025). Ela é compatível tanto com o formato numérico tradicional quanto com o novo formato **alfanumérico**.

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