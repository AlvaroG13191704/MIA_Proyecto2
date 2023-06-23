import os
import shutil
from ..setCredentials import setCredentials
# if the path does not exist, return error
# if the name comes but the name file does not exist, return error
# if the name does not come, delete the folder

class Rename():
  def __init__(self, path, name, type) -> None:
    self.path = path
    self.name = name
    self.type = type
    self.s3 = setCredentials()

  
  def local(self):
    path = self.path.replace("'","").lstrip('/').rstrip('/')
    # Get the absolute path of the project directory
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

    file_ = os.path.join(root_dir, "Archivos", path)

    if os.path.exists(file_):
      if os.path.isfile(file_):
        new_path = os.path.join(os.path.dirname(file_), self.name)

        if os.path.exists(new_path):
          return {
            "status": "error",
            "message": f"El archivo {self.name} ya existe"
          }
        else:
          os.rename(file_, new_path)
          return {
            "status": "success",
            "message": f"Archivo {self.name} renombrado exitosamente"
          }
      elif os.path.isdir(file_):
        parent_dir = os.path.dirname(file_)
        new_path = os.path.join(parent_dir, self.name)

        if not os.path.exists(new_path):
          shutil.move(file_, new_path)
          return {
            "status": "success",
            "message": f"Archivo {self.name} renombrado exitosamente"
          }
        else:
          return {
            "status": "error",
            "message": f"El archivo {self.name} ya existe"
          }
    else:
      return {
        "status": "error",
        "message": f"El archivo {self.name} no existe"
      }

  def bucket(self):
    name_bucket = "mia-proyecto2"
    origin_path_bucket = "Archivos" + self.path
    destini_path_bucket = "Archivos" + self.path.replace(self.path.split("/")[-1], self.name)
    print(origin_path_bucket, destini_path_bucket)
    # evaluate if the file exists
    object_list_origin = self.s3.list_objects(Bucket=name_bucket, Prefix=origin_path_bucket)
    if "Contents" in object_list_origin:
      # evaluate if the file exists
      object_list_destini = self.s3.list_objects(Bucket=name_bucket, Prefix=destini_path_bucket)
      if "Contents" in object_list_destini:
        return {
          "status": "error",
          "message": f"El archivo {self.name} ya existe"
        }
      else:
        # copy the file
        self.s3.copy_object(
          Bucket=name_bucket,
          CopySource={
            "Bucket": name_bucket,
            "Key": origin_path_bucket
          },
          Key=destini_path_bucket
        )
        # delete the file
        self.s3.delete_object(
          Bucket=name_bucket,
          Key=origin_path_bucket
        )
        return {
          "status": "success",
          "message": f"Archivo {self.name} renombrado exitosamente"
        }