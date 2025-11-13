# 📘 README — Aplicação Web de Inscrições Corta‑Mato Escolar

## 🏃‍♂️ Funcionalidades
Esta aplicação web permite gerir todo o processo de inscrições e classificações de uma **prova de Corta‑Mato Escolar**, com geração automática de dorsais com QR Code e cálculo de classificações automáticas por escalão e género.

### 🔧 Funcionalidades principais
- Carregamento de ficheiro Excel com dados dos alunos (número, nome, turma, data de nascimento, género)
- Registo de inscrições na prova (seleção manual ou total)
- Geração de dorsais individuais ou em massa (ZIP) com QR Code
- Cálculo automático de escalão com base na data de nascimento
- Registo de tempos (hh:mm:ss, mm:ss ou segundos)
- Classificação automática geral e por **escalão/género**
- Exportação de inscrições e classificações em CSV

---

## 🧮 Escalões
| Escalão | Data de Nascimento |
|----------|-------------------|
| Infantil A | 01/01/2015 – 31/12/2017 |
| Infantil B | 01/01/2013 – 31/12/2014 |
| Iniciado | 01/01/2011 – 31/12/2012 |
| Juvenil | 01/01/2008 – 31/12/2010 |
| Júnior | 01/01/2004 – 31/12/2007 |

---

## ⚙️ Instalação local

### 1️⃣ Pré‑requisitos
Instalar **Python 3.9+**.

### 2️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 3️⃣ Executar a aplicação
```bash
streamlit run streamlit_cross_country_app.py
```

### 4️⃣ Aceder no navegador
A aplicação ficará disponível em:
```
http://localhost:8501
```

---

## ☁️ Publicar online (Streamlit Cloud)

### Passos:
1. Criar conta gratuita em [https://share.streamlit.io](https://share.streamlit.io)
2. Criar um **repositório GitHub** (ex.: `corta-mato-app`)
3. Adicionar estes ficheiros:
   - `streamlit_cross_country_app.py`
   - `requirements.txt`
   - (opcional) `ListagemAlunos_25_26.xls`
4. No Streamlit Cloud, clicar em **“Deploy an app”** → selecionar o repositório.

O Streamlit irá gerar um link público, ex.:
```
https://teu-utilizador-corta-mato.streamlit.app
```

---

## 📦 requirements.txt
```
streamlit
pandas
qrcode
pillow
python-multipart
```

---

## 🏫 Sugestão de utilização
- Ideal para professores de Educação Física.
- Pode ser usada em computadores da escola ou publicada na cloud.
- Cada inscrição gera automaticamente o **dorsal com QR Code** que inclui nome, número, turma, género e escalão.
- As classificações podem ser geradas automaticamente ou ajustadas manualmente.

---

© 2025 — Escola Secundária de Monserrate — Aplicação desenvolvida para gestão de provas desportivas escolares.
