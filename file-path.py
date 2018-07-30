import subprocess

class Curpath (gdb.Command):
    """print absolute path"""
    def __init__(self):
        super(Curpath, self).__init__("clippath", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        symtabline = gdb.selected_frame().find_sal()
        cmd = subprocess.Popen(["xclip","-sel", "clip"], stdin=subprocess.PIPE)
        cmd.communicate(symtabline.symtab.fullname() + ":" + str(symtabline.line))

Curpath()
