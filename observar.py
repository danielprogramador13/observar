# "Controle de observações de arquivos e diretórios na pasta downloads"


#Importações
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

#Classe para criar um Sistema de Observação
class Sistema_De_Observacao(FileSystemEventHandler):

    def on_created(self, event):
        #------------------------------Created----------------------------------------#
        if event.is_directory:
            print(f"Novo diretório criado: -- {event.src_path} --\n")
        else: 
            print(f"Novo arquivo criado: -- {event.src_path} --")
            print(f"Extensão do arquivo: {os.path.splitext(event.src_path)}\n")

        time.sleep(1)
        #-----------------------------------------------------------------------------#
    def on_deleted(self, event):
        #------------------------------Deleted----------------------------------------#
        # É diretório ou não? (Mostrando o que aconteceu)
        if event.is_directory:
            print(f"Um diretório foi excluído!")
            print(f"Diretório excluído: -- {event.src_path} --\n")
        else:
            print(f"Um arquivo foi excluído!\n")
            print(f"Arquivo excluído: -- {event.src_path} --")
            print(f"Extensão do arquivo: {os.path.splitext(event.src_path)}\n")
        time.sleep(1)
        #-----------------------------------------------------------------------------#

    def on_moved(self, event):
        #------------------------------Moved------------------------------------------#
        if event.is_directory:
            print("Um diretório foi movido!")
            print(f"Arquivo movido -- para -- {os.path.dirname(event.dest_path)} --\n")
        else: 
            print("Um arquivo foi movido!")
            print(f"Arquivo movido de -- {event.src_path} -- para -- {event.dest_path} --")
            print(f"Extensão do arquivo: {os.path.splitext(event.src_path)}\n")
        time.sleep(1)
        #-----------------------------------------------------------------------------#

    def on_modified(self, event):
        #------------------------------Modified---------------------------------------#
        print(f"Arquivo modificado: -- {event.src_path} --\n")
        time.sleep(1)
        #-----------------------------------------------------------------------------#
        
print("Bem vindo ao observar.py! Aqui você pode ver o que está acontecendo na sua pasta de preferência!")
print("Para parar o observador, é só digitar ctrl/cmd + c. Isso vai encerrar o observador e o programa.")

while True:
    pathWay = input("Olá, back_end dev! Coloque o seu caminho de arquivo aqui, utilizando barras invertidas: \n")

    if os.path.exists(pathWay):
        if os.path.isdir(pathWay):
            break
        else:
            print("O caminho existe, mas é um arquivo. Certifique-se de colocar um diretório em vez disso.")
            continue
    else:
        print("Parece que o diretório não existe. Dica: tente encontrar na pasta de arquivos o endereço do diretório...")


print("O observador está funcionando! As informações sobre as ações no seu diretório aparecerão abaixo |")
print("_______________________________________________________________________________________________ V")
event_handler = Sistema_De_Observacao()
observer = Observer()
observer.schedule(event_handler, path=pathWay, recursive=False)
observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()
    print("O programa foi encerrado. Para rodar novamente, rode <python observar.py>.")
    print("--------------------------------------------------------------------------")
observer.join()