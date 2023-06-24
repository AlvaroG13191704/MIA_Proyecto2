# local imports
from ..scanner.createC import scan_command_line_create
from ..scanner.deleteC import scan_command_line_delete
from ..scanner.copyC import scan_command_line_copy
from ..scanner.transferC import scan_command_line_transfer
from ..scanner.renameC import scan_command_line_rename
from ..scanner.modifyC import scan_command_line_modify
from ..scanner.backupC import scan_command_line_backup
from ..scanner.recoveryC import scan_command_line_recovery
from ..scanner.delete_allC import scan_command_line_delete_all
from ..scanner.openC import scan_command_line_open
# classes
from ...manageFiles.classes.create import Create
from ...manageFiles.classes.delete import Delete
from ...manageFiles.classes.copy import Copy
from ...manageFiles.classes.transfer import Transfer
from ...manageFiles.classes.rename import Rename
from ...manageFiles.classes.modify import Modify
from ...manageFiles.classes.backup import Backup
from ...manageFiles.classes.recovery import Recovery
from ...manageFiles.classes.delete_all import Delete_all
from ...manageFiles.classes.open import Open
# recieve an array of commands and execute them

# 1. extract values from the command string
# 2. valdiate the values
# 3. execute the command


def execute_commands(commands):
  for command in commands:
    if command.get("create"):
      create, name, path, body, type = scan_command_line_create(command.get("create"))
      if create and name and path and body and type:
        print("create")
        # create instance of create class
        create_object = Create(name, body, path, type)
        # evaluate if the type is local or bucket
        if type == "server":
          return create_object.local()
        elif type == "bucket":
         return  create_object.bucket()
      else:
        return {"status": "error", "message": "Comando invalido en create"}


    elif command.get("delete"):
      delete, path, name, type = scan_command_line_delete(command.get("delete"))
      if delete and path and type:
        print("delete")
        # create instance of delete class
        delete_object = Delete(path, name, type)
        # evaluate if the type is local or bucket
        if type == "server":
          return delete_object.local()
        elif type == "bucket":
          return delete_object.bucket()
        
      else:
        return {"status": "error", "message": "Comando invalido en delete"}

    elif command.get("copy"):
      copy, from_, to_, type_to, type_from = scan_command_line_copy(command.get("copy"))
      if copy and from_ and to_ and type_to and type_from:
        print("copy")
        # create instance of copy class
        copy_object = Copy(from_, to_, type_to, type_from)
        # evaluate if the type is local or bucket
        if type_from == "server":
          return copy_object.local()
        elif type_from == "bucket":
          return copy_object.bucket()
        
      else:
        return {"status": "error", "message": "Comando invalido en copy"}

    elif command.get("transfer"):
      transfer, from_, to_, type_to, type_from = scan_command_line_transfer(command.get("transfer"))
      if transfer and from_ and to_ and type_to and type_from:
        # create instance of transfer class
        transfer_object = Transfer(from_, to_, type_to, type_from)
        print("transfer")
        # evaluate if the type is local or bucket
        if type_from == "server":
          return transfer_object.local()
        elif type_from == "bucket":
          return transfer_object.bucket()
        
      else:
        return {"status": "error", "message": "Comando invalido en transfer"}
      
    elif command.get("rename"):
      rename, path, name, type = scan_command_line_rename(command.get("rename"))
      if rename and path and name and type:
        print("rename")
        # create instance of rename class
        rename_object = Rename(path, name, type)
        # evaluate if the type is local or bucket
        if type == "server":
          return rename_object.local()
        elif type == "bucket":
          return rename_object.bucket()
      else:
        return {"status": "error", "message": "Comando invalido en rename"}

    elif command.get("modify"):
      modify, path, body, type = scan_command_line_modify(command.get("modify"))
      if modify and path and body and type:
        print("modify")
        # create instance of modify class
        modify_object = Modify(path, body, type)
        # evaluate if the type is local or bucket
        if type == "server":
          return modify_object.local()
        elif type == "bucket":
          return modify_object.bucket()
        
      else:
        return {"status": "error", "message": "Comando invalido en modify"}

    elif command.get("backup"):
      backup, type_to, type_from, ip , port, name  = scan_command_line_backup(command.get("backup"))
      if backup and type_to and type_from and name:
        print("backup")
        # create instance of backup class
        backup_object = Backup(type_to, type_from, ip , port, name)
        # evaluate if the backup is only in our environment
        if ip == None and port == None:
          # evaluate if the type is local or bucket
          if type_from == "server":
            return backup_object.bucket()
          elif type_from == "bucket":
            return backup_object.local()
        # evaluate if the backup is in another environment (port and ip)
        elif ip != None and port != None:
          # evaluate if the type is local or bucket
          if type_from == "server":
            return backup_object.local_api()
          elif type_from == "bucket":
            return backup_object.bucket_api()
        else:
          return {"status": "error", "message": "Comando invalido en backup"}
      else:
        return {"status": "error", "message": "Comando invalido en backup"}

    elif command.get("recovery"):
      recovery, type_to, type_from, ip , port, name  = scan_command_line_recovery(command.get("recovery"))
      if recovery and type_to and type_from and name:
        print("recovery")
        # create instance of backup class
        recovery_object = Recovery(type_to, type_from, ip , port, name)
        # evaluate if the backup is only in our environment
        if ip == None and port == None:
          # evaluate if the type is local or bucket
          if type_from == "server":
            return recovery_object.local()
          elif type_from == "bucket":
            return recovery_object.bucket()
        # evaluate if the backup is in another environment (port and ip)
        elif ip != None and port != None:
          # evaluate if the type is local or bucket
          if type_from == "server":
            return recovery_object.local_api()
          elif type_from == "bucket":
            return recovery_object.bucket_api()
        else:
          return {"status": "error", "message": "Comando invalido en backup"}
      else:
        return {"status": "error", "message": "Comando invalido en recovery"}

    elif command.get("delete_all"):
      delete_all, type = scan_command_line_delete_all(command.get("delete_all"))
      if delete_all and type:
        print("delete_all")
        # create instance of delete_all class
        delete_all_object = Delete_all(type)
        # evaluate if the type is local or bucket
        if type == "server":
          return delete_all_object.local()
        elif type == "bucket":
          return delete_all_object.bucket()
      else:
        return {"status": "error", "message": "Comando invalido en delete_all"}

    elif command.get("open"):
      open, type, ip, port, name = scan_command_line_open(command.get("open"))
      if open and type and name:
        print("open")
        # create instance of open class
        open_object = Open(type, ip, port, name)
        # evaluate if the backup is only in our environment
        if ip == None and port == None:
          # evaluate if the type is local or bucket
          if type == "server":
            return open_object.local()
          elif type == "bucket":
            return open_object.bucket()
        # evaluate if the backup is in another environment (port and ip)
        elif ip != None and port != None:
          # evaluate if the type is local or bucket
          return open_object.api_ip()
        else:
          return {"status": "error", "message": "Comando invalido en backup"}
      else:
        return {"status": "error", "message": "Comando invalido en open"}
