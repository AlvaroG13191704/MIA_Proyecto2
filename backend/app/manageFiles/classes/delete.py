import os
import shutil
from ..setCredentials import setCredentials
# if the path does not exist, return error
# if the name comes but the name file does not exist, return error
# if the name does not come, delete the folder

class Delete():
  def __init__(self, path, name, type) -> None:
    self.path = path
    self.name = name
    self.type = type
    self.s3 = setCredentials()

  def local(self):
    path = self.path.replace('"', '').lstrip('/').rstrip('/')
    name = None
    # evaluate if the name is not false
    if self.name:
      name = ""
    # Get the absolute path of the project directory
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    file_ = os.path.join(root_dir, "Archivos", path, name)

    if os.path.exists(file_):
      if os.path.isfile(file_):
        os.remove(file_)
        return {
          "status": "success",
          "message": f"Archivo {name} eliminado exitosamente"
        }
      elif os.path.isdir(file_):
        shutil.rmtree(file_)
        return {
          "status": "success",
          "message": f"Carpeta {name} eliminada exitosamente"
        }
    else:
      return {
        "status": "error",
        "message": f"El archivo o carpeta {name} no existe"
      }

  def bucket(self):
    bucket_name = "mia-proyecto2"
    name = self.name

    if self.name == False:
      object_key = 'Archivos' + self.path + ""
      objects = self.s3.list_objects(Bucket=bucket_name, Prefix=object_key)
      if "Contents" in objects:
        key = [obj["Key"] for obj in objects["Contents"]]
        self.s3.delete_objects(Bucket=bucket_name, Delete={"Objects": [{"Key": k} for k in key]})
        return {
          "status": "success",
          "message": f"Archivos de {object_key} eliminados exitosamente"
        }
      else:
        return {
          "status": "error",
          "message": f"La carpeta {object_key} no existe"
        }
    else:
      object_key = 'Archivos' + self.path + name
      try:
        self.s3.delete_object(Bucket=bucket_name, Key=object_key)
        return {
          "status": "success",
          "message": f"Archivo {name} eliminado exitosamente"
        }
      except Exception as e:
        return {
          "status": "error",
          "message": f"Error al eliminar archivo {name}"
        }