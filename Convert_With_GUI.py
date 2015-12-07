
#Syntax to pass to the mid2cnc script: params = '-outfile ./mytest.gcode'
# Prints are here just to show the user what's happeneing. They might as be removed.

import os
import lib.easygui as eg
params = '' #initializing variable. This is the argument string that we will pass to Mid2CNC

machinelist = ('ultimaker', 'cupcake', 'thingomatic', 'shapercube', 'custom') #Creates a list of entries
machine = eg.choicebox(msg='Machine type', title='Pick machine', choices=machinelist) #Creates a GUI Window for a choice in the machine list
print 'Chosen machine :' + machine #What the user chose

params = params + ' --machine ' + machine #add that choice to the parameter string
#Same pattern for the other options

#Ask what MIDI input file to open
infile = eg.fileopenbox(msg='Choose the midi file ', title=' Grab the file you want to convert', default=os.path.expanduser("~")+ "//My Documents//", filetypes = "*.mid") # the "default=os.path.expanduser("~")" gets your home forlder so you don't have top start browsing from some obscure python install folder
print 'Opening file: ' + infile
params = params + ' --infile ' + infile

#asks where to save the output gcode file
#for some reason this window sometimes appears behind all others
outfile = eg.filesavebox(msg='Choose the output file ', title=' Pick where you want the gcode to arrive', default=os.path.expanduser("~")+"//My Documents//Output.gcode", filetypes = "*.gcode")
print 'Saving to: ' +  outfile
params = params + " --outfile " +  outfile

#ask if the verbose should be activated
verbose = eg.boolbox(msg='Do you want the verbose to be activated (for debug)', title=' Verbose Y/N ', choices=('No', 'Yes'), image=None) # returns true if the first is chosen
if verbose == 0:
	 params = params + " --verbose"

#prints the whole argument line
print 'The whole command: ' + params

#launches mid2cnc with the argument string
os.system ('python -i mid2cnc.py ' + params)




#TODO:
# Enforce .gcode at the end of outfile
# handle cases where nothing is entered and add error handlng in general
# Also why is filesavebox appearing in the background ?
