from git import Repo
import re, sys, signal



def extract(repo_dir):
    reposit = Repo(repo_dir)
    commits = list(reposit.iter_commits('develop'))
    return commits

def transform_and_load(com):
    claves = ['credentials', 'pin', 'password', 'key', 'pwd', 'code']
    lista_datos = []
    for c in com:
        for word in claves:
            if re.search(word, c.message, re.I):
                dic = {}
                dic['Commit'] = c.hexsha
                dic['Mensaje'] = c.message
                lista_datos.append(dic)

    return lista_datos

            
def control_c(signal, frame):
    print('\n Se ha finalizado el programa <3 \n')
    sys.exit()
signal.signal(signal.SIGINT, control_c)

if __name__ == '__main__':
    repositorio = './skale/skale-manager'
    
    com = extract(repositorio)
    print(transform_and_load(com))