import nuke
import nukescripts
import os

#
##
### Startup Panel for an easier Script Start - by Robin Schneider
##
#
class Script_StartPanel(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__( self, "Start a Script")
        self.first_tab = nuke.Tab_Knob("START", "Start")
        self.second_tab = nuke.Tab_Knob("OPEN", "Open")
        #Create Knobs
        self.Text = nuke.Text_Knob('Start', 'Start a new Script')

        #self.Text()['label'].setValue("<center> <h1>Heading 1</h1><h2>Start a new Script</h2> </center>>")
        self.gap = nuke.Text_Knob("divName","","")

        #Change name input
        self.name = nuke.String_Knob('Skript-Name', 'Name')
        
        if nuke.root()['name'].value() == '':
             self.name.setValue('Shot0000_V01_TTMMJJ.nk')
        else:
             self.name.setValue(nuke.root()['name'].value())
             
        self.proj = nuke.File_Knob('directory', 'Speicherort')

        ########################Please insert your standard File Location Folder (Watch out for "/" at the end)#############
        if nuke.root()['project_directory'].value() == '':
             self.proj.setValue('J:/Working_Volume/WIP/002_LuN_Comp/20191118_VFX_Paket_Robin/02.2_Dorf/LuN_VFX_02.2_Dorf/')
        else:
             self.proj.setValue(nuke.root()['project_directory'].value())
        ########################
        
        
        self.set = nuke.PyScript_Knob('SET', 'Set')
        self.set.setFlag(nuke.STARTLINE)

        self.save = nuke.Script_Knob('SAVE', 'Save')
        self.save.setFlag(nuke.STARTLINE)

        self.cancel = nuke.PyScript_Knob('CANCEL', 'CANCEL')

        self.Ordner = nuke.Script_Knob('Ordner', 'Ordner anlegen')

        self.format = nuke.Format_Knob('Resolutions')

        self.realFPS = nuke.Int_Knob('Frames', 'fps')
        self.realFPS.setValue(25)

        self.label = nuke.Multiline_Eval_String_Knob('Notes', 'Notizen', '' )
        self.label.setValue('Changes/ToDo-Liste')
        
        self.bdropt = nuke.Text_Knob('BDROPT', 'Choose your Backdrops')

        self.bdrop1 = nuke.Boolean_Knob('BDROP1','Input+Output')
        self.bdrop1.setFlag(nuke.STARTLINE)
        self.bdrop2 = nuke.Boolean_Knob('BDROP2','CG_Passes')
        self.bdrop2.setFlag(nuke.STARTLINE)
        self.bdrop3 = nuke.Boolean_Knob('BDROP3','Blacklevels')
        self.bdrop3.setFlag(nuke.STARTLINE)
        self.bdrop4 = nuke.Boolean_Knob('BDROP4','POST')
        self.bdrop4.setFlag(nuke.STARTLINE)
        self.bdrop5 = nuke.Boolean_Knob('BDROP5','ColourCorrection')
        self.bdrop5.setFlag(nuke.STARTLINE)
        self.bdrop6 = nuke.Boolean_Knob('BDROP6','Keying')
        self.bdrop6.setFlag(nuke.STARTLINE)
        self.bdrop7 = nuke.Boolean_Knob('BDROP7','Despill')
        self.bdrop7.setFlag(nuke.STARTLINE)
        self.bdrop8 = nuke.Boolean_Knob('BDROP8','Camera Projection')
        self.bdrop8.setFlag(nuke.STARTLINE)
        self.gap2 = nuke.Text_Knob("divName","","")
        self.gap3 = nuke.Text_Knob("divName","","")

        self.Delete = nuke.PyScript_Knob("DELETE", "Delete all Backdrops")
   
        #######################################################################
        #######################################################################Second Tab: Open a old script

        self.opentxt = nuke.Text_Knob('OPENTXT', 'Open a Script')
        self.opentxtgap = nuke.Text_Knob("divName3","","")
        self.Proj_Folder = nuke.File_Knob("PROJECT", "Project folder with all Shots")
        ############################### Set overall Projects Folder here: 
        self.Proj_Folder.setValue('J:/Working_Volume/WIP/002_LuN_Comp/20191118_VFX_Paket_Robin/02.2_Dorf/LuN_VFX_02.2_Dorf/')
        ###############################
        

        path = self.Proj_Folder.value()
        self.CheckforFiles = nuke.PyScript_Knob("CheckFiles", "Find all Scripts")
        self.Load = nuke.PyScript_Knob("OPEN", "   Open Script  ")
        self.Load.setFlag(nuke.STARTLINE)
        
        files = []
        
        self.ChooseScript = nuke.Enumeration_Knob("AllScripts", "All Found Scripts",files)
        self.ChooseScript.setFlag(nuke.STARTLINE)

        self.listcount = nuke.Text_Knob ('List-Text', 'Total count of Nuke-Files')
        self.listcount.setFlag(nuke.STARTLINE)
        
        self.cancel2 = nuke.PyScript_Knob('CANCEL2', 'CANCEL')
    	   
        self.bgap = nuke.Text_Knob("DIV_2",'', '')
        self.filter = nuke.String_Knob('FILTER', 'Filter for this String')
        
        
        #Window_Settings
        self.setMinimumSize(700, 750)
        #add Knobs
        for k in (self.first_tab, self.Text, self.gap, self.name, self.proj, self.realFPS, self.format, self.label, self.set, self.Ordner,self.bdropt, self.bdrop1,self.bdrop2,self.bdrop3,self.bdrop4,self.bdrop5,self.bdrop6,self.bdrop7,self.bdrop8,self.gap2,self.Delete, self.gap3, self.save, self.cancel, self.second_tab, self.opentxt, self.opentxtgap, self.Proj_Folder,self.filter, self. CheckforFiles, self.ChooseScript,self.bgap, self.listcount, self.Load, self.cancel2):
            self.addKnob( k )
    
    def knobChanged(self, knob):
        print knob.name()
        if knob.name() == "SET":
            #    print "OK pressed"
            sticky = nuke.createNode("StickyNote")
            sticky.knob("label").setValue( self.label.value() )
            sticky.knob("note_font_size").setValue(25)
            sticky.setXpos(233)
            sticky.setYpos(-1326)
            if  self.label.setValue == "":
                sticky = nuke.createNode("StickyNote")
                sticky.knob("label").setValue( 'Changes/ToDo-Liste' )
            nuke.root()['project_directory'].setValue(self.proj.value())
            nuke.root()['name'].setValue(self.proj.value()+ self.name.value())
            nuke.root()['fps'].setValue(self.realFPS.value()*1.0)
            nuke.root()['format'].setValue(self.format.value())
            
            #ALL Backdrops_Settings
        if knob.name() == 'BDROP1':
           bdrop = nuke.createNode('BackdropNode', inpanel = False)
           bdrop.knob("name").setValue("INPUT")
           bdrop.knob("label").setValue('INPUT')
           bdrop.knob("xpos").setValue(-101)
           bdrop.knob("ypos").setValue(-1324)
           bdrop.knob("bdwidth").setValue(300)
           bdrop.knob("bdheight").setValue(220)
           bdrop.knob("note_font_size").setValue(50)
           bdrop.knob("tile_color").setValue(0x515151ff)
           bdrop.knob("note_font").setValue("Verdana Bold")
           bdropex = nuke.createNode('BackdropNode', inpanel = False)
           bdropex.knob("name").setValue("OUTPUT")
           bdropex.knob("label").setValue('OUTPUT')
           bdropex.knob("xpos").setValue(-101)
           bdropex.knob("ypos").setValue(2822)
           bdropex.knob("bdwidth").setValue(300)
           bdropex.knob("bdheight").setValue(220)
           bdropex.knob("note_font_size").setValue(50)
           bdropex.knob("tile_color").setValue(0xe5c634ff)
           bdropex.knob("note_font").setValue("Verdana Bold")
           bdropp = nuke.createNode("Dot", inpanel = False)
           bdropp.knob("xpos").setValue(35)
           bdropp.knob("ypos").setValue(-1165)
           bdropp2 = nuke.createNode("Dot", inpanel = False)
           bdropp2.knob("xpos").setValue(35)
           bdropp2.knob("ypos").setValue(2919)

        if knob.name() == 'BDROP2' :
           bdrop2 = nuke.createNode('BackdropNode', inpanel = False)
           bdrop2.knob("name").setValue("CG_Passes")
           bdrop2.knob("label").setValue('CG_Passes')
           bdrop2.knob("xpos").setValue(-1135)
           bdrop2.knob("ypos").setValue(-1310)
           bdrop2.knob("bdwidth").setValue(380)
           bdrop2.knob("bdheight").setValue(210)
           bdrop2.knob("note_font_size").setValue(35)
           bdrop2.knob("tile_color").setValue(0x880200ff)
    
        if knob.name() == 'BDROP3' :
           bdrop3 = nuke.createNode('BackdropNode', inpanel = False)
           bdrop3.knob("name").setValue("Blacklevels")
           bdrop3.knob("label").setValue('Blacklevels')
           bdrop3.knob("xpos").setValue(-107)
           bdrop3.knob("ypos").setValue(1783)
           bdrop3.knob("bdwidth").setValue(270)
           bdrop3.knob("bdheight").setValue(210)
           bdrop3.knob("note_font_size").setValue(35)
           bdrop3.knob("tile_color").setValue(0xff)
         
        if knob.name() == 'BDROP4' :
           bdrop4 = nuke.createNode('BackdropNode', inpanel = False)
           bdrop4.knob("name").setValue("_POST")
           bdrop4.knob("label").setValue('_POST')
           bdrop4.knob("xpos").setValue(-100)
           bdrop4.knob("ypos").setValue(2103)
           bdrop4.knob("bdwidth").setValue(272)
           bdrop4.knob("bdheight").setValue(402)
           bdrop4.knob("note_font_size").setValue(35)
           bdrop4.knob("tile_color").setValue(0x537cff)
         
        if knob.name() == 'BDROP5' :
           bdrop5 = nuke.createNode('BackdropNode', inpanel = False)
           bdrop5.knob("name").setValue("Colour_Correction")
           bdrop5.knob("label").setValue('Colour_Correction')
           bdrop5.knob("xpos").setValue(585)
           bdrop5.knob("ypos").setValue(464)
           bdrop5.knob("bdwidth").setValue(490)
           bdrop5.knob("bdheight").setValue(256)
           bdrop5.knob("note_font_size").setValue(35)
           bdrop5.knob("tile_color").setValue(0xffffffff)
        
        if knob.name() == 'BDROP6' :
           bdrop6 = nuke.createNode('BackdropNode', inpanel = False)
           bdrop6.knob("name").setValue("Despill")
           bdrop6.knob("label").setValue('Despill')
           bdrop6.knob("xpos").setValue(580)
           bdrop6.knob("ypos").setValue(-162)
           bdrop6.knob("bdwidth").setValue(777)
           bdrop6.knob("bdheight").setValue(488)
           bdrop6.knob("note_font_size").setValue(35)
           bdrop6.knob("tile_color").setValue(0x264f2aff)
   
        if knob.name() == 'BDROP7' :
           bdrop7 = nuke.createNode('BackdropNode', inpanel = False)
           bdrop7.knob("name").setValue("Keying")
           bdrop7.knob("label").setValue('Keying')
           bdrop7.knob("xpos").setValue(579)
           bdrop7.knob("ypos").setValue(-1038)
           bdrop7.knob("bdwidth").setValue(1400)
           bdrop7.knob("bdheight").setValue(800)
           bdrop7.knob("note_font_size").setValue(35)
           bdrop7.knob("tile_color").setValue(0xa045ff)
        
        if knob.name() == 'BDROP8' :
           bdrop8 = nuke.createNode('BackdropNode', inpanel = False)
           bdrop8.knob("name").setValue("3D_Camera-Projection")
           bdrop8.knob("label").setValue('3D_Camera-Projection')
           bdrop8.knob("xpos").setValue(-1487)
           bdrop8.knob("ypos").setValue(-163)
           bdrop8.knob("bdwidth").setValue(1060)
           bdrop8.knob("bdheight").setValue(740)
           bdrop8.knob("note_font_size").setValue(35)
           bdrop8.knob("tile_color").setValue(0xa03c3cff)
        if knob.name() == "DELETE":
            for w in nuke.allNodes():
                w.setSelected(True)
            nukescripts.node_delete()
            for k in (self.bdrop1, self.bdrop2, self.bdrop3, self.bdrop4, self.bdrop5, self.bdrop6, self.bdrop7, self.bdrop8 ):
                k.setValue(False) 
           
        if knob.name() == "Ordner":
            ## Define which folders you need
            RD = nuke.Root()['project_directory'].value()
            R = 'RENDER'
            S = 'SCRIPTS'
            TWDR = 'ASSETS/2D_RENDERS'
            THDR = 'ASSETS/3D_RENDERS'
            ST = 'ASSETS/STILLS'
            F = 'FOOTAGE'
    
            ## Combines Folders with Project Directory
            F1 = RD+R
            F2 = RD+S
            F3 = RD+TWDR
            F4 = RD+THDR
            F5 = RD+ST
            F6 = RD+F
            
            ## Prints for Debugging
            print F1
            print F2
            print F3
            print F4
            print F5
            print F6
            
            ## Generates Folders
            if not os.path.exists(F1):
                os.makedirs(F1)
            if not os.path.exists(F2):
                os.makedirs(F2)
            if not os.path.exists(F3):
                os.makedirs(F3)
            if not os.path.exists(F4):
                os.makedirs(F4)
            if not os.path.exists(F5):
                os.makedirs(F5)
            if not os.path.exists(F6):
                os.makedirs(F6)
                
            nuke.message('Folders Generated')
        if knob.name() == "SAVE":
            nuke.scriptSave()
        if knob.name() == "CANCEL":
            self.finishModalDialog(True)

        ########second tab: Open new script
        if knob.name() == "OPEN": 
             nuke.scriptOpen(self.ChooseScript.value())  
        if knob.name() == "CheckFiles":
            path = self.Proj_Folder.value()
            files = []
            for r, d, f in os.walk(path):
                for item in f: 
                    if self.filter.value() in item: 
                        files.append(os.path.join(r, item))
                    if '~' in item:
                        files.remove(os.path.join(r,item))
            #print files 
            self.ChooseScript.setValues(files)
            #print len(files)
            self.listcount.setValue(str(len(files)))
        if knob.name() == "CANCEL2":
            self.finishModalDialog(True)


