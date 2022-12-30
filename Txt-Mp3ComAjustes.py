import tkinter as tk
import tkinter.filedialog as filedialog
import pyttsx3

# Inicialize o motor de fala
engine = pyttsx3.init()

# Crie a janela principal
root = tk.Tk()
root.title("Leitor de Texto")

# Crie a barra de rolagem para ajustar a velocidade da voz
barra_velocidade = tk.Scale(root, from_=0.5, to=2.0, orient=tk.HORIZONTAL, resolution=0.1,
                             label="Velocidade da voz")
barra_velocidade.pack()

# Crie a barra de rolagem para ajustar o volume da voz
barra_volume = tk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, resolution=0.1,
                        label="Volume da voz")
barra_volume.pack()

# Crie o botão "Escolher arquivo"
def escolher_arquivo():
    global arquivo
    arquivo = filedialog.askopenfilename(title="Escolher arquivo de texto")

botao_escolher = tk.Button(root, text="Escolher arquivo", command=escolher_arquivo)
botao_escolher.pack()

# Crie o botão "Ouvir o texto"
def ouvir_texto():
    # Obtenha a velocidade e o volume escolhidos nas barras de rolagem
    velocidade = barra_velocidade.get()
    volume = barra_volume.get()

    # Defina a velocidade e o volume no motor de fala
    engine.setProperty('rate', velocidade)
    engine.setProperty('volume', volume)

    # Abra o arquivo .txt para leitura
    with open(arquivo, 'r') as f:
        # Leia o conteúdo do arquivo
        text = f.read()

    # Faça o motor de fala ler o texto
    engine.say(text)
    engine.runAndWait()

botao_ouvir = tk.Button(root, text="Ouvir o texto", command=ouvir_texto)
botao_ouvir.pack()

# Crie o campo de texto para inserir o nome do arquivo
campo_nome = tk.Entry(root)
campo_nome.pack()

# Crie o botão "Salvar em MP3"
def salvar_mp3():
    # Obtenha o nome do arquivo informado no campo de texto
    nome = campo_nome.get()
# Obtenha a velocidade e o volume escolhidos nas barras de rolagem
    velocidade = barra_velocidade.get()
    volume = barra_volume.get()

    # Abra o arquivo .txt para leitura
    with open(arquivo, 'r') as f:
        # Leia o conteúdo do arquivo
        text = f.read()

    # Crie um objeto gTTS com o texto e outras opções (opcional)
    tts = gTTS(text, lang='pt', slow=False, 
               speaker=None, pitch=0, 
               extras=None, cache=None,
               ssl=True, ttl=None, 
               proxy=None, loop=0,
               max_svc_attempts=None)
    tts.set_speed(velocidade)
    tts.set_volume(volume)

    # Salve o arquivo de áudio com o nome informado
    tts.save(nome + '.mp3')

botao_salvar = tk.Button(root, text="Salvar em MP3", command=salvar_mp3)
botao_salvar.pack()

# Inicie a janela principal
root.mainloop()