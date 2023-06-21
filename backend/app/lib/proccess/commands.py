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
        print(name)
        print(path)
        print(body)
        print(type)
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
        print(path)
        print(name)
        print(type)
      else:
        return {"status": "error", "message": "Comando invalido en delete"}

    elif command.get("copy"):
      copy, from_, to_, type_to, type_from = scan_command_line_copy(command.get("copy"))
      if copy and from_ and to_ and type_to and type_from:
        print("copy")
        print(from_)
        print(to_)
        print(type_to)
        print(type_from)
      else:
        return {"status": "error", "message": "Comando invalido en copy"}

    elif command.get("transfer"):
      transfer, from_, to_, type_to, type_from = scan_command_line_transfer(command.get("transfer"))
      if transfer and from_ and to_ and type_to and type_from:
        print("transfer")
        print(from_)
        print(to_)
        print(type_to)
        print(type_from)
      else:
        return {"status": "error", "message": "Comando invalido en transfer"}
      

    elif command.get("rename"):
      rename, path, name, type = scan_command_line_rename(command.get("rename"))
      if rename and path and name and type:
        print("rename")
        print(path)
        print(name)
        print(type)
      else:
        return {"status": "error", "message": "Comando invalido en rename"}

    elif command.get("modify"):
      modify, path, body, type = scan_command_line_modify(command.get("modify"))
      if modify and path and body and type:
        print("modify")
        print(path)
        print(body)
        print(type)
      else:
        return {"status": "error", "message": "Comando invalido en modify"}

    elif command.get("backup"):
      backup, type_to, type_from, ip , port, name  = scan_command_line_backup(command.get("backup"))
      if backup and type_to and type_from and name:
        print("backup")
        print(type_to)
        print(type_from)
        print(name)
        print(ip)
        print(port)
      else:
        return {"status": "error", "message": "Comando invalido en backup"}

    elif command.get("recovery"):
      recovery, type_to, type_from, ip , port, name  = scan_command_line_recovery(command.get("recovery"))
      if recovery and type_to and type_from and name:
        print("recovery")
        print(type_to)
        print(type_from)
        print(name)
        print(ip)
        print(port)
      else:
        return {"status": "error", "message": "Comando invalido en recovery"}

    elif command.get("delete_all"):
      delete_all, type = scan_command_line_delete_all(command.get("delete_all"))
      if delete_all and type:
        print("delete_all")
        print(type)
      else:
        return {"status": "error", "message": "Comando invalido en delete_all"}

    elif command.get("open"):
      open, type, ip, port, name = scan_command_line_open(command.get("open"))
      if open and type and name:
        print("open")
        print(type)
        print(ip)
        print(port)
        print(name)
      else:
        return {"status": "error", "message": "Comando invalido en open"}
