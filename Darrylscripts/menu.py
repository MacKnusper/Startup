import Start_Panel_RD


menubar = nuke.menu("Nuke")
m = menubar.addMenu("&Script_Startup")
m.addCommand("Start your Script", lambda: Start_Panel_RD.Script_StartPanel().showModal(), 'ctrl+shift+n')

