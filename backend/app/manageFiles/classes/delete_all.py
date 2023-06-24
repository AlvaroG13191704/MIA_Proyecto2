import os
import shutil
# class to create files in local or bucket s3
from ..setCredentials import setCredentials

class Delete_all():
  # constructor
  def __init__(self, type) -> None:
    self.type = type
    # set credentials
    self.s3 = setCredentials()
  

  # delete all files in local
  def local(self):
    # Get the absolute path of the project directory
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    path = os.path.join(root_dir, "Archivos")
    if os.path.exists(path):
      # delete files and directories
      shutil.rmtree(path)
      return {
        "status": "success",
        "message": f"Archivos eliminados exitosamente"
      }
    else:
      return {
        "status": "error",
        "message": f"No existen la carpeta 'Archivos' en el servidor"
      }

  # delete all files and directories in bucket s3
  def bucket(self):
    bucket_name = "mia-proyecto2"
    try:
      # evaluate if the file exists
      list_objects = self.s3.list_objects(Bucket=bucket_name)
      if 'Contents' in list_objects:
        for item in list_objects['Contents']:
          self.s3.delete_object(Bucket=bucket_name, Key=item['Key'])
        return {
          "status": "success",
          "message": f"Archivos eliminados exitosamente"
        }
      else:
        return {
          "status": "error",
          "message": f"No existen archivos en el bucket"
        }
    except Exception as e:
      return {
        "status": "error",
        "message": f"Error al eliminar los archivos en el bucket: {e}"
      }