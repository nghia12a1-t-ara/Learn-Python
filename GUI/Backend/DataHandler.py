import os
from pathlib import Path

"""
 @ List all Configuration Files to Gen Sources
"""
def getConfigFile(Folder):
    ListFiles = []
    dir_list = os.listdir(Folder)
    for subdir in dir_list:
        ListConfigFile = os.listdir(Folder + '\\' + subdir)
        for Files in ListConfigFile:
            ListFiles.append(Folder + '\\' + subdir + '\\' + Files)
    return ListFiles

"""
 @ Generate Source File from File Config
"""
def getSourceFile(ConfigFile):
    parentProj = getParent(ConfigFile, 2)
    Filename = getFileName(ConfigFile, 1)
    
    GenerateDir = parentProj + "\\Generate"
    GenerateFile = GenerateDir + "\\" + Filename
    return GenerateFile

"""
 @ Generate Source File from File Config
"""
def GenerateFile(Folder, ConfigList, ConfigListName):
    ConfigListFile = getConfigFile(Folder)
    for i in range(len(ConfigList)):
        cfgFile = ConfigListFile[i]
        mysrcfile = Path(cfgFile)
        mysrcfile.touch(exist_ok=True)
            
        GenFile = getSourceFile(cfgFile)
        mydestfile = Path(GenFile)
        mydestfile.touch(exist_ok=True)
            
        fsrc = open(mysrcfile, 'r')
        srcText = fsrc.read()

        Index_1 = srcText.find('/* Generate Code */') + 19
        Index_2 = srcText.find('/* !Generate Code */')
        # @TODO
        GenString = ReplaceCfg(srcText, ConfigList, ConfigListName)
        srcText = srcText.replace(srcText[Index_1:Index_2], GenString)

        ### Write Data to Generate Files ###
        fdest = open(mydestfile, 'w')
        destText = fdest.write(srcText)        

"""
 @ Replace Configuration
"""    
def ReplaceCfg(srctext, ConfigList, ConfigListName):
    GenString = ""
    Index_1 = srctext.find('/* Generate Code */') + 19
    Index_2 = srctext.find('/* !Generate Code */')
    cfgStr = srctext[Index_1:Index_2]
    print(ConfigList)
    for i in range(len(ConfigList)):
        tempStr = cfgStr
        for j in range(len(ConfigListName)):
            srcstr = '$(' + ConfigListName[j] + ')$'
            tempStr = tempStr.replace(srcstr, ConfigList[i][j])
        GenString = GenString + tempStr + '\n'

    return GenString
    
"""
 @ function to get parent directory
"""
def getParent(path, levels = 1):
    common = path
 
    # Using for loop for getting
    # starting point required for
    # os.path.relpath()
    for i in range(levels + 1):
 
        # Starting point
        common = os.path.dirname(common)
 
    # Parent directory upto specified
    # level
    return common

"""
 @ function to get Folder + File Name
"""
def getFileName(path, levels = 1):
    common = path
 
    # Using for loop for getting
    # starting point required for
    # os.path.relpath()
    for i in range(levels + 1):
 
        # Starting point
        common = os.path.dirname(common)
 
    # Parent directory upto specified
    # level
    return os.path.relpath(path, common)

#print(GenerateFile("D:\Python\Python_Repo\Learn-Python\GUI\Example\Bai1\Config_Files"))
#print(getSourceFile('D:\\Python\\Python_Repo\\Learn-Python\\GUI\\Example\\Bai1\\Config_Files\\Inc\\GPIO_Config.h'))

