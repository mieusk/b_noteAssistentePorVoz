## Note

Note é um assistente por voz experimental, ele só executa 3 funções: tocar, horas e silêncio.
Não planejo melhorá-lo, mas você pode utilizar o código dele para fazer modificações.

### Comandos

- tocar/toca/toque: toca uma música;
- silêncio/para/parar: para a música;
- horas/hora: diz que horas são.

### Bugs

- Finaliza em erro caso o resultado for uma playlist/filme;
- Falta o comando "pular" para pular a música.


Eu sei como corrigir estes problemas, mas estou ocupado e sou preguiçoso.

### Dependências

É necessário instalar estas dependências: ```pyttsx3, speech_recognition, shutil e selenium```;
Utilize `pip install [dependência]` para baixá-las.

### Uso

Baixe os arquivos `note.py`, `chromedriver.exe`, e `cmedhionkhpnakcndndgjdbohmhepckk.zip`.

É necessário baixar o `Google Chrome 89.0.4389.90` e **colocá-lo na mesma pasta do script**.

Vai ficar mais ou menos assim:
<p align="center">
<img src="https://user-images.githubusercontent.com/75510861/206913609-1726bdd9-6aa1-4fc1-b069-770994523d74.png" />
</p>


Execute `py note.py`.

Você deve falar o nome do assistente + o comando, exemplo: `note tocar justin bieber love me`.

### Créditos

- [<a href="https://www.geeksforgeeks.org/voice-assistant-using-python" target="_blank">GeeksforGeeks</a>]
