# WhatsApp Extractor

## Descrição Breve
Este projeto foi desenvolvido sob demanda de uma empresa local.

Ele automatiza a extração de nomes e números de telefone de contatos do WhatsApp Web, facilitando a criação de uma lista de contatos em formato digital. Ele resolve o problema de copiar manualmente informações de contatos, tornando o processo mais rápido e menos sujeito a erros.

## Tecnologias Utilizadas
- **Linguagem:** Python
- **Bibliotecas:**
  - pyautogui (automação de mouse e teclado)
  - pytesseract (OCR para reconhecimento de texto)
  - Pillow (manipulação de imagens)
  - json (armazenamento dos contatos)
- **Ferramentas:**
  - Tesseract-OCR (engine de OCR)
  - Git (controle de versão)

## Como Executar
1. **Clone o repositório:**
   ```powershell
   git clone <url-do-repositorio>
   cd Whataspp_extractor
   ```
2. **Instale as dependências:**
   ```powershell
   pip install pyautogui pytesseract pillow
   ```
3. **Instale o Tesseract-OCR:**
   - Baixe e instale em: https://github.com/tesseract-ocr/tesseract
   - Altere o caminho em `main.py` se necessário:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
     ```
4. **Execute o script:**
   ```powershell
   python main.py
   ```

## Funcionalidades
- Extração automática de nomes e telefones dos contatos visíveis no WhatsApp Web
- Armazenamento dos contatos extraídos em um arquivo JSON
- Detecção automática de falhas de extração e salvamento de screenshots para análise
- Limite configurável de contatos a serem extraídos
- Contagem e controle de tentativas para evitar repetições

## Exemplo de Uso
Ao rodar o script, posicione o WhatsApp Web conforme instruído no terminal. O programa irá capturar os contatos visíveis, extrair nome e telefone, e salvar no arquivo `contatos.json`.

![Exemplo de execução](screenshot_exemplo.png)

## Status do Projeto
Em desenvolvimento.

## Próximos Passos
- Adicionar interface gráfica para facilitar o uso
- Permitir configuração dinâmica das coordenadas de captura
- Exportação para outros formatos (CSV, Excel)

## Observação Importante
As coordenadas de captura de tela estão pré-definidas com base na minha tela. Caso utilize em outro computador ou resolução, será necessário ajustar as posições no código para garantir o funcionamento correto.
