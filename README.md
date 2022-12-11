## Note

Note é um assistente por voz experimental, ele só executa 3 funções: tocar, horas e silêncio.
Não planejo melhorá-lo, mas você pode utilizar o código dele para fazer modificações.

### Comandos

- tocar/toca/toque: toca uma música;
- silêncio/para/parar: para a música;
- horas/hora: diz que horas são.

### Bugs

- O comando "tocar" acumula na caixa de pesquisa o nome das músicas, fazendo com que bugue depois de alguns usos;
- Finaliza em erro caso o resultado for uma playlist/filme.

Além de que não existe o comando "pular" para pular a música; sim, eu sei como corrigir estes problemas, mas estou ocupado e sou preguiçoso.

### Dependências

É necessário instalar estas dependências: ```pyttsx3, speech_recognition, shutil e selenium```;
Utilize `pip install [dependência]` para baixá-las.

### Uso

Baixe os arquivos `note.py`, `chromedriver.exe`, e `cmedhionkhpnakcndndgjdbohmhepckk.zip`.

É necessário baixar, também, o `Google Chrome 89.0.4389.90` e colocá-lo na mesma pasta do script.

Execute `py note.py`.

### Créditos

- [<a href="https://www.geeksforgeeks.org/voice-assistant-using-python]">GeeksforGeeks</a>]
