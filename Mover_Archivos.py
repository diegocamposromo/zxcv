import os
import shutil
def mover_archivos(origen, destino):
    if not os.path.exists(destino):
        os.makedirs(destino)
    archivos = os.listdir(origen)
    for archivo in archivos:
        ext = os.path.splitext(archivo)[1].lower()
        path1 = os.path.join(origen, archivo)
        if ext == '':
            continue
        if ext in ['.txt', '.doc', '.docx', '.pdf']:
            path2 = os.path.join(destino, "Document_Files")
            path3 = os.path.join(path2, archivo) 
        else: 
            path2 = os.path.join(destino, "Image_Files")
            path3 = os.path.join(path2, archivo)
        if not os.path.exists(path2):
            os.makedirs(path2)
        shutil.move(path1, path3)
        print(f"Archivo {archivo} movido correctamente.")
origen = "C:/Users/campo/Downloads"
destino = "C:/Users/campo/OneDrive/Escritorio"
mover_archivos(origen, destino)