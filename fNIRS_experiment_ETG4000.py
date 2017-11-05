#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), November 05, 2017, at 15:14
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'fNIRS_experiment_block_design'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'E:\\Experiments\\Eryk\\Pilot\\PsychoPy\\fNIRS_experiment_Oct2017_with_baseline_fixed_pause.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(2048, 1152), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
import serial # to connect the serial port
from time import sleep

# set the serial port
port = serial.Serial('COM1', 9600, timeout=0)
port.write('ST\r') # harcoded end command
introduction = visual.TextStim(win=win, ori=0, name='introduction',
    text='Welcome to the experiment.\n\nYou will hear repeated /a/ sounds.\n\nThere will be four conditions in this experiment.\nEach condition will contain 10 blocks of 30 repetitions.\n\nPress SPACE to continue',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "instructions_baseline"
instructions_baselineClock = core.Clock()
text_baseline = visual.TextStim(win=win, ori=0, name='text_baseline',
    text=u'Sit back and relax while \nyour baseline brain activity is being measured.\n\nIt will take one minute.\n\nYou will be notified when the trial is over.\n\nPress SPACE to start.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block_J_baseline"
block_J_baselineClock = core.Clock()
baseline_fixation = visual.TextStim(win=win, ori=0, name='baseline_fixation',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "instructions_perception"
instructions_perceptionClock = core.Clock()
thank_you = visual.TextStim(win=win, ori=0, name='thank_you',
    text='Thank you.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_perception = visual.TextStim(win=win, ori=0, name='text_perception',
    text='The next condition that you will hear will involve passive listening.\n\nPlease sit back and try to remain steady.\n\nYou will be presented with 10 blocks of 30 repetitions of the /a/ stimulus.\n\nOnce a block finishes, please press SPACE to continue.\n\nPress SPACE to start.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "block_B"
block_BClock = core.Clock()


# Initialize components for Routine "sound_2"
sound_2Clock = core.Clock()

a_sound = sound.Sound('stim-AAA-fall_fem-166-255Hz-220med_with1sec_silence.wav', secs=-1)
a_sound.setVolume(1)
fix_A = visual.TextStim(win=win, ori=0, name='fix_A',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "block_B"
block_BClock = core.Clock()


# Initialize components for Routine "instructions_within_condition"
instructions_within_conditionClock = core.Clock()
text_within_condition = visual.TextStim(win=win, ori=0, name='text_within_condition',
    text=u'Press SPACE when you are ready to rest.\n\nIt will take around 15 seconds.\n\nThe testing condition will resume after the rest.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "pause_within_block_I"
pause_within_block_IClock = core.Clock()
pause_fixation = visual.TextStim(win=win, ori=0, name='pause_fixation',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "instructions_shadowing"
instructions_shadowingClock = core.Clock()
text_shadowing2 = visual.TextStim(win=win, ori=0, name='text_shadowing2',
    text=u'In this trial you will hear the same /a/ sound as in the previous condition.\n\nThis time your task is to REPEAT THE SOUND ALOUD as it is played.\n\nTry to keep your mouth steady and do not move during this condition.\n\nThere will be 10 blocks of 30 repetitions of the stimulus.\n\nPress SPACE when you are ready to continue.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block_D"
block_DClock = core.Clock()


# Initialize components for Routine "sound_c_shad"
sound_c_shadClock = core.Clock()

sound_C_shad = sound.Sound('stim-AAA-fall_fem-166-255Hz-220med_with1sec_silence.wav', secs=-1)
sound_C_shad.setVolume(1)
fix_C = visual.TextStim(win=win, ori=0, name='fix_C',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "block_D"
block_DClock = core.Clock()


# Initialize components for Routine "instructions_within_condition"
instructions_within_conditionClock = core.Clock()
text_within_condition = visual.TextStim(win=win, ori=0, name='text_within_condition',
    text=u'Press SPACE when you are ready to rest.\n\nIt will take around 15 seconds.\n\nThe testing condition will resume after the rest.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "pause_within_block_I"
pause_within_block_IClock = core.Clock()
pause_fixation = visual.TextStim(win=win, ori=0, name='pause_fixation',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "instructions_silent_mouthing"
instructions_silent_mouthingClock = core.Clock()
text_silent_mouthing = visual.TextStim(win=win, ori=0, name='text_silent_mouthing',
    text=u'In this trial you will hear the same /a/ sound as in the previous conditions.\n\nThis time your task is to imagine that you are producing the /a/ sound but\nwithout actually saying it.\n\nTry to keep your mouth steady and do not move during this condition.\n\nThere will be 10 blocks of 30 repetitions of the stimulus.\n\nPress SPACE when you are ready to continue.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block_F"
block_FClock = core.Clock()


# Initialize components for Routine "sound_E_sil"
sound_E_silClock = core.Clock()

sound_e_shad = sound.Sound('stim-AAA-fall_fem-166-255Hz-220med_with1sec_silence.wav', secs=-1)
sound_e_shad.setVolume(1)
fix_E = visual.TextStim(win=win, ori=0, name='fix_E',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "block_F"
block_FClock = core.Clock()


# Initialize components for Routine "instructions_within_condition"
instructions_within_conditionClock = core.Clock()
text_within_condition = visual.TextStim(win=win, ori=0, name='text_within_condition',
    text=u'Press SPACE when you are ready to rest.\n\nIt will take around 15 seconds.\n\nThe testing condition will resume after the rest.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "pause_within_block_I"
pause_within_block_IClock = core.Clock()
pause_fixation = visual.TextStim(win=win, ori=0, name='pause_fixation',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "instructions_self_production"
instructions_self_productionClock = core.Clock()
text_self_production = visual.TextStim(win=win, ori=0, name='text_self_production',
    text=u'In this trial you will NOT hear the sound.\nThis time your task is to produce the /a/ sound that you heard in the previous conditions.\n\nTry to keep your mouth steady and do not move during this condition.\n\nPlease continue to produce the /a/ sound\nuntil you see the information to relax.\nTry to keep the same pace as in the previous conditions.\n\nThere will be 10 blocks of 30 repetitions.\nPress SPACE to start.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "block_H"
block_HClock = core.Clock()


# Initialize components for Routine "sound_G_self"
sound_G_selfClock = core.Clock()

fix_G = visual.TextStim(win=win, ori=0, name='fix_G',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
fix_G_wait = visual.TextStim(win=win, ori=0, name='fix_G_wait',
    text=None,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "block_H"
block_HClock = core.Clock()


# Initialize components for Routine "instructions_within_condition"
instructions_within_conditionClock = core.Clock()
text_within_condition = visual.TextStim(win=win, ori=0, name='text_within_condition',
    text=u'Press SPACE when you are ready to rest.\n\nIt will take around 15 seconds.\n\nThe testing condition will resume after the rest.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "pause_within_block_I"
pause_within_block_IClock = core.Clock()
pause_fixation = visual.TextStim(win=win, ori=0, name='pause_fixation',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "instructions_restart_self_prod"
instructions_restart_self_prodClock = core.Clock()
self_restart_instruction = visual.TextStim(win=win, ori=0, name='self_restart_instruction',
    text=u'The rest is over.\n\nStart saying /a/ when the cross reappears.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "end"
endClock = core.Clock()

the_end = visual.TextStim(win=win, ori=0, name='the_end',
    text='THE END\n\nPress Space',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

forward_instructions = event.BuilderKeyResponse()  # create an object of type KeyResponse
forward_instructions.status = NOT_STARTED
# keep track of which components have finished
trialComponents = []
trialComponents.append(introduction)
trialComponents.append(forward_instructions)
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "trial"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *introduction* updates
    if t >= 0.0 and introduction.status == NOT_STARTED:
        # keep track of start time/frame for later
        introduction.tStart = t  # underestimates by a little under one frame
        introduction.frameNStart = frameN  # exact frame index
        introduction.setAutoDraw(True)
    
    # *forward_instructions* updates
    if t >= 1.0 and forward_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        forward_instructions.tStart = t  # underestimates by a little under one frame
        forward_instructions.frameNStart = frameN  # exact frame index
        forward_instructions.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(forward_instructions.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if forward_instructions.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            forward_instructions.keys = theseKeys[-1]  # just the last key pressed
            forward_instructions.rt = forward_instructions.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if forward_instructions.keys in ['', [], None]:  # No response was made
   forward_instructions.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('forward_instructions.keys',forward_instructions.keys)
if forward_instructions.keys != None:  # we had a response
    thisExp.addData('forward_instructions.rt', forward_instructions.rt)
thisExp.nextEntry()
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instructions_baseline"-------
t = 0
instructions_baselineClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_baseline = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_baseline.status = NOT_STARTED
# keep track of which components have finished
instructions_baselineComponents = []
instructions_baselineComponents.append(text_baseline)
instructions_baselineComponents.append(key_resp_baseline)
for thisComponent in instructions_baselineComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions_baseline"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions_baselineClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_baseline* updates
    if t >= 0.0 and text_baseline.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_baseline.tStart = t  # underestimates by a little under one frame
        text_baseline.frameNStart = frameN  # exact frame index
        text_baseline.setAutoDraw(True)
    
    # *key_resp_baseline* updates
    if t >= 1.0 and key_resp_baseline.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_baseline.tStart = t  # underestimates by a little under one frame
        key_resp_baseline.frameNStart = frameN  # exact frame index
        key_resp_baseline.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_baseline.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_baseline.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_baseline.keys = theseKeys[-1]  # just the last key pressed
            key_resp_baseline.rt = key_resp_baseline.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_baselineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instructions_baseline"-------
for thisComponent in instructions_baselineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_baseline.keys in ['', [], None]:  # No response was made
   key_resp_baseline.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_baseline.keys',key_resp_baseline.keys)
if key_resp_baseline.keys != None:  # we had a response
    thisExp.addData('key_resp_baseline.rt', key_resp_baseline.rt)
thisExp.nextEntry()
# the Routine "instructions_baseline" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "block_J_baseline"-------
t = 0
block_J_baselineClock.reset()  # clock 
frameN = -1
routineTimer.add(60.000000)
# update component parameters for each repeat
port.write('J \r')
# keep track of which components have finished
block_J_baselineComponents = []
block_J_baselineComponents.append(baseline_fixation)
for thisComponent in block_J_baselineComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "block_J_baseline"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = block_J_baselineClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *baseline_fixation* updates
    if t >= 0.0 and baseline_fixation.status == NOT_STARTED:
        # keep track of start time/frame for later
        baseline_fixation.tStart = t  # underestimates by a little under one frame
        baseline_fixation.frameNStart = frameN  # exact frame index
        baseline_fixation.setAutoDraw(True)
    if baseline_fixation.status == STARTED and t >= (0.0 + (60.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        baseline_fixation.setAutoDraw(False)
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block_J_baselineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "block_J_baseline"-------
for thisComponent in block_J_baselineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
port.write('J \r')

#------Prepare to start Routine "instructions_perception"-------
t = 0
instructions_perceptionClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
end_text_perc = event.BuilderKeyResponse()  # create an object of type KeyResponse
end_text_perc.status = NOT_STARTED
# keep track of which components have finished
instructions_perceptionComponents = []
instructions_perceptionComponents.append(thank_you)
instructions_perceptionComponents.append(text_perception)
instructions_perceptionComponents.append(end_text_perc)
for thisComponent in instructions_perceptionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions_perception"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions_perceptionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thank_you* updates
    if t >= 0.0 and thank_you.status == NOT_STARTED:
        # keep track of start time/frame for later
        thank_you.tStart = t  # underestimates by a little under one frame
        thank_you.frameNStart = frameN  # exact frame index
        thank_you.setAutoDraw(True)
    if thank_you.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        thank_you.setAutoDraw(False)
    
    # *text_perception* updates
    if t >= 1.0 and text_perception.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_perception.tStart = t  # underestimates by a little under one frame
        text_perception.frameNStart = frameN  # exact frame index
        text_perception.setAutoDraw(True)
    
    # *end_text_perc* updates
    if t >= 2.0 and end_text_perc.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_text_perc.tStart = t  # underestimates by a little under one frame
        end_text_perc.frameNStart = frameN  # exact frame index
        end_text_perc.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(end_text_perc.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if end_text_perc.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            end_text_perc.keys = theseKeys[-1]  # just the last key pressed
            end_text_perc.rt = end_text_perc.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_perceptionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instructions_perception"-------
for thisComponent in instructions_perceptionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_text_perc.keys in ['', [], None]:  # No response was made
   end_text_perc.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('end_text_perc.keys',end_text_perc.keys)
if end_text_perc.keys != None:  # we had a response
    thisExp.addData('end_text_perc.rt', end_text_perc.rt)
thisExp.nextEntry()
# the Routine "instructions_perception" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
perception_loop = data.TrialHandler(nReps=10, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='perception_loop')
thisExp.addLoop(perception_loop)  # add the loop to the experiment
thisPerception_loop = perception_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPerception_loop.rgb)
if thisPerception_loop != None:
    for paramName in thisPerception_loop.keys():
        exec(paramName + '= thisPerception_loop.' + paramName)

for thisPerception_loop in perception_loop:
    currentLoop = perception_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPerception_loop.rgb)
    if thisPerception_loop != None:
        for paramName in thisPerception_loop.keys():
            exec(paramName + '= thisPerception_loop.' + paramName)
    
    #------Prepare to start Routine "block_B"-------
    t = 0
    block_BClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    port.write('B \r')
    sleep(0.2)
    
    # keep track of which components have finished
    block_BComponents = []
    for thisComponent in block_BComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block_B"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = block_BClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_BComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block_B"-------
    for thisComponent in block_BComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    port.write('B \r')
    sleep(1.0)
    
    # the Routine "block_B" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_sound_perception = data.TrialHandler(nReps=30, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_sound_perception')
    thisExp.addLoop(trials_sound_perception)  # add the loop to the experiment
    thisTrials_sound_perception = trials_sound_perception.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrials_sound_perception.rgb)
    if thisTrials_sound_perception != None:
        for paramName in thisTrials_sound_perception.keys():
            exec(paramName + '= thisTrials_sound_perception.' + paramName)
    
    for thisTrials_sound_perception in trials_sound_perception:
        currentLoop = trials_sound_perception
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_sound_perception.rgb)
        if thisTrials_sound_perception != None:
            for paramName in thisTrials_sound_perception.keys():
                exec(paramName + '= thisTrials_sound_perception.' + paramName)
        
        #------Prepare to start Routine "sound_2"-------
        t = 0
        sound_2Clock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        port.write('A \r')
        # keep track of which components have finished
        sound_2Components = []
        sound_2Components.append(a_sound)
        sound_2Components.append(fix_A)
        for thisComponent in sound_2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "sound_2"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = sound_2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # start/stop a_sound
            if t >= 0.0 and a_sound.status == NOT_STARTED:
                # keep track of start time/frame for later
                a_sound.tStart = t  # underestimates by a little under one frame
                a_sound.frameNStart = frameN  # exact frame index
                a_sound.play()  # start the sound (it finishes automatically)
            
            # *fix_A* updates
            if t >= 0.0 and fix_A.status == NOT_STARTED:
                # keep track of start time/frame for later
                fix_A.tStart = t  # underestimates by a little under one frame
                fix_A.frameNStart = frameN  # exact frame index
                fix_A.setAutoDraw(True)
            if fix_A.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                fix_A.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sound_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "sound_2"-------
        for thisComponent in sound_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        a_sound.stop() #ensure sound has stopped at end of routine
        # the Routine "sound_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 30 repeats of 'trials_sound_perception'
    
    
    #------Prepare to start Routine "block_B"-------
    t = 0
    block_BClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    port.write('B \r')
    sleep(0.2)
    
    # keep track of which components have finished
    block_BComponents = []
    for thisComponent in block_BComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block_B"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = block_BClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_BComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block_B"-------
    for thisComponent in block_BComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    port.write('B \r')
    sleep(1.0)
    
    # the Routine "block_B" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "instructions_within_condition"-------
    t = 0
    instructions_within_conditionClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    within_cond_continue = event.BuilderKeyResponse()  # create an object of type KeyResponse
    within_cond_continue.status = NOT_STARTED
    # keep track of which components have finished
    instructions_within_conditionComponents = []
    instructions_within_conditionComponents.append(text_within_condition)
    instructions_within_conditionComponents.append(within_cond_continue)
    for thisComponent in instructions_within_conditionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions_within_condition"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions_within_conditionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_within_condition* updates
        if t >= 0.0 and text_within_condition.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_within_condition.tStart = t  # underestimates by a little under one frame
            text_within_condition.frameNStart = frameN  # exact frame index
            text_within_condition.setAutoDraw(True)
        
        # *within_cond_continue* updates
        if t >= 0.5 and within_cond_continue.status == NOT_STARTED:
            # keep track of start time/frame for later
            within_cond_continue.tStart = t  # underestimates by a little under one frame
            within_cond_continue.frameNStart = frameN  # exact frame index
            within_cond_continue.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(within_cond_continue.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if within_cond_continue.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                within_cond_continue.keys = theseKeys[-1]  # just the last key pressed
                within_cond_continue.rt = within_cond_continue.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_within_conditionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions_within_condition"-------
    for thisComponent in instructions_within_conditionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if within_cond_continue.keys in ['', [], None]:  # No response was made
       within_cond_continue.keys=None
    # store data for perception_loop (TrialHandler)
    perception_loop.addData('within_cond_continue.keys',within_cond_continue.keys)
    if within_cond_continue.keys != None:  # we had a response
        perception_loop.addData('within_cond_continue.rt', within_cond_continue.rt)
    # the Routine "instructions_within_condition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "pause_within_block_I"-------
    t = 0
    pause_within_block_IClock.reset()  # clock 
    frameN = -1
    routineTimer.add(15.000000)
    # update component parameters for each repeat
    port.write('I \r')
    # keep track of which components have finished
    pause_within_block_IComponents = []
    pause_within_block_IComponents.append(pause_fixation)
    for thisComponent in pause_within_block_IComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pause_within_block_I"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pause_within_block_IClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pause_fixation* updates
        if t >= 0.0 and pause_fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            pause_fixation.tStart = t  # underestimates by a little under one frame
            pause_fixation.frameNStart = frameN  # exact frame index
            pause_fixation.setAutoDraw(True)
        if pause_fixation.status == STARTED and t >= (0.0 + (15.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            pause_fixation.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pause_within_block_IComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pause_within_block_I"-------
    for thisComponent in pause_within_block_IComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    port.write('I \r')
    sleep(0.2)
    thisExp.nextEntry()
    
# completed 10 repeats of 'perception_loop'


#------Prepare to start Routine "instructions_shadowing"-------
t = 0
instructions_shadowingClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
text_shad_continue = event.BuilderKeyResponse()  # create an object of type KeyResponse
text_shad_continue.status = NOT_STARTED
# keep track of which components have finished
instructions_shadowingComponents = []
instructions_shadowingComponents.append(text_shadowing2)
instructions_shadowingComponents.append(text_shad_continue)
for thisComponent in instructions_shadowingComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions_shadowing"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions_shadowingClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_shadowing2* updates
    if t >= 0.0 and text_shadowing2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_shadowing2.tStart = t  # underestimates by a little under one frame
        text_shadowing2.frameNStart = frameN  # exact frame index
        text_shadowing2.setAutoDraw(True)
    
    # *text_shad_continue* updates
    if t >= 1.0 and text_shad_continue.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_shad_continue.tStart = t  # underestimates by a little under one frame
        text_shad_continue.frameNStart = frameN  # exact frame index
        text_shad_continue.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(text_shad_continue.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if text_shad_continue.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            text_shad_continue.keys = theseKeys[-1]  # just the last key pressed
            text_shad_continue.rt = text_shad_continue.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_shadowingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instructions_shadowing"-------
for thisComponent in instructions_shadowingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if text_shad_continue.keys in ['', [], None]:  # No response was made
   text_shad_continue.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('text_shad_continue.keys',text_shad_continue.keys)
if text_shad_continue.keys != None:  # we had a response
    thisExp.addData('text_shad_continue.rt', text_shad_continue.rt)
thisExp.nextEntry()
# the Routine "instructions_shadowing" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
shadowing_loop = data.TrialHandler(nReps=10, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='shadowing_loop')
thisExp.addLoop(shadowing_loop)  # add the loop to the experiment
thisShadowing_loop = shadowing_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisShadowing_loop.rgb)
if thisShadowing_loop != None:
    for paramName in thisShadowing_loop.keys():
        exec(paramName + '= thisShadowing_loop.' + paramName)

for thisShadowing_loop in shadowing_loop:
    currentLoop = shadowing_loop
    # abbreviate parameter names if possible (e.g. rgb = thisShadowing_loop.rgb)
    if thisShadowing_loop != None:
        for paramName in thisShadowing_loop.keys():
            exec(paramName + '= thisShadowing_loop.' + paramName)
    
    #------Prepare to start Routine "block_D"-------
    t = 0
    block_DClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    port.write('D \r')
    sleep(0.2)
    
    # keep track of which components have finished
    block_DComponents = []
    for thisComponent in block_DComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block_D"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = block_DClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_DComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block_D"-------
    for thisComponent in block_DComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    port.write('D \r')
    sleep(1.0)
    
    # the Routine "block_D" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_sound_shadowing = data.TrialHandler(nReps=30, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_sound_shadowing')
    thisExp.addLoop(trials_sound_shadowing)  # add the loop to the experiment
    thisTrials_sound_shadowing = trials_sound_shadowing.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrials_sound_shadowing.rgb)
    if thisTrials_sound_shadowing != None:
        for paramName in thisTrials_sound_shadowing.keys():
            exec(paramName + '= thisTrials_sound_shadowing.' + paramName)
    
    for thisTrials_sound_shadowing in trials_sound_shadowing:
        currentLoop = trials_sound_shadowing
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_sound_shadowing.rgb)
        if thisTrials_sound_shadowing != None:
            for paramName in thisTrials_sound_shadowing.keys():
                exec(paramName + '= thisTrials_sound_shadowing.' + paramName)
        
        #------Prepare to start Routine "sound_c_shad"-------
        t = 0
        sound_c_shadClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        port.write('C \r')
        # keep track of which components have finished
        sound_c_shadComponents = []
        sound_c_shadComponents.append(sound_C_shad)
        sound_c_shadComponents.append(fix_C)
        for thisComponent in sound_c_shadComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "sound_c_shad"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = sound_c_shadClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # start/stop sound_C_shad
            if t >= 0.0 and sound_C_shad.status == NOT_STARTED:
                # keep track of start time/frame for later
                sound_C_shad.tStart = t  # underestimates by a little under one frame
                sound_C_shad.frameNStart = frameN  # exact frame index
                sound_C_shad.play()  # start the sound (it finishes automatically)
            
            # *fix_C* updates
            if t >= 0.0 and fix_C.status == NOT_STARTED:
                # keep track of start time/frame for later
                fix_C.tStart = t  # underestimates by a little under one frame
                fix_C.frameNStart = frameN  # exact frame index
                fix_C.setAutoDraw(True)
            if fix_C.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                fix_C.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sound_c_shadComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "sound_c_shad"-------
        for thisComponent in sound_c_shadComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        sound_C_shad.stop() #ensure sound has stopped at end of routine
        # the Routine "sound_c_shad" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 30 repeats of 'trials_sound_shadowing'
    
    
    #------Prepare to start Routine "block_D"-------
    t = 0
    block_DClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    port.write('D \r')
    sleep(0.2)
    
    # keep track of which components have finished
    block_DComponents = []
    for thisComponent in block_DComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block_D"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = block_DClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_DComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block_D"-------
    for thisComponent in block_DComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    port.write('D \r')
    sleep(1.0)
    
    # the Routine "block_D" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "instructions_within_condition"-------
    t = 0
    instructions_within_conditionClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    within_cond_continue = event.BuilderKeyResponse()  # create an object of type KeyResponse
    within_cond_continue.status = NOT_STARTED
    # keep track of which components have finished
    instructions_within_conditionComponents = []
    instructions_within_conditionComponents.append(text_within_condition)
    instructions_within_conditionComponents.append(within_cond_continue)
    for thisComponent in instructions_within_conditionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions_within_condition"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions_within_conditionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_within_condition* updates
        if t >= 0.0 and text_within_condition.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_within_condition.tStart = t  # underestimates by a little under one frame
            text_within_condition.frameNStart = frameN  # exact frame index
            text_within_condition.setAutoDraw(True)
        
        # *within_cond_continue* updates
        if t >= 0.5 and within_cond_continue.status == NOT_STARTED:
            # keep track of start time/frame for later
            within_cond_continue.tStart = t  # underestimates by a little under one frame
            within_cond_continue.frameNStart = frameN  # exact frame index
            within_cond_continue.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(within_cond_continue.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if within_cond_continue.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                within_cond_continue.keys = theseKeys[-1]  # just the last key pressed
                within_cond_continue.rt = within_cond_continue.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_within_conditionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions_within_condition"-------
    for thisComponent in instructions_within_conditionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if within_cond_continue.keys in ['', [], None]:  # No response was made
       within_cond_continue.keys=None
    # store data for shadowing_loop (TrialHandler)
    shadowing_loop.addData('within_cond_continue.keys',within_cond_continue.keys)
    if within_cond_continue.keys != None:  # we had a response
        shadowing_loop.addData('within_cond_continue.rt', within_cond_continue.rt)
    # the Routine "instructions_within_condition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "pause_within_block_I"-------
    t = 0
    pause_within_block_IClock.reset()  # clock 
    frameN = -1
    routineTimer.add(15.000000)
    # update component parameters for each repeat
    port.write('I \r')
    # keep track of which components have finished
    pause_within_block_IComponents = []
    pause_within_block_IComponents.append(pause_fixation)
    for thisComponent in pause_within_block_IComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pause_within_block_I"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pause_within_block_IClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pause_fixation* updates
        if t >= 0.0 and pause_fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            pause_fixation.tStart = t  # underestimates by a little under one frame
            pause_fixation.frameNStart = frameN  # exact frame index
            pause_fixation.setAutoDraw(True)
        if pause_fixation.status == STARTED and t >= (0.0 + (15.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            pause_fixation.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pause_within_block_IComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pause_within_block_I"-------
    for thisComponent in pause_within_block_IComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    port.write('I \r')
    sleep(0.2)
    thisExp.nextEntry()
    
# completed 10 repeats of 'shadowing_loop'


#------Prepare to start Routine "instructions_silent_mouthing"-------
t = 0
instructions_silent_mouthingClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
instructions_silent_mouthingComponents = []
instructions_silent_mouthingComponents.append(text_silent_mouthing)
instructions_silent_mouthingComponents.append(key_resp_2)
for thisComponent in instructions_silent_mouthingComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions_silent_mouthing"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions_silent_mouthingClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_silent_mouthing* updates
    if t >= 0.0 and text_silent_mouthing.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_silent_mouthing.tStart = t  # underestimates by a little under one frame
        text_silent_mouthing.frameNStart = frameN  # exact frame index
        text_silent_mouthing.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 1.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_silent_mouthingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instructions_silent_mouthing"-------
for thisComponent in instructions_silent_mouthingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
   key_resp_2.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "instructions_silent_mouthing" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
silent_loop = data.TrialHandler(nReps=10, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='silent_loop')
thisExp.addLoop(silent_loop)  # add the loop to the experiment
thisSilent_loop = silent_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisSilent_loop.rgb)
if thisSilent_loop != None:
    for paramName in thisSilent_loop.keys():
        exec(paramName + '= thisSilent_loop.' + paramName)

for thisSilent_loop in silent_loop:
    currentLoop = silent_loop
    # abbreviate parameter names if possible (e.g. rgb = thisSilent_loop.rgb)
    if thisSilent_loop != None:
        for paramName in thisSilent_loop.keys():
            exec(paramName + '= thisSilent_loop.' + paramName)
    
    #------Prepare to start Routine "block_F"-------
    t = 0
    block_FClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    port.write('F \r')
    sleep(0.2)
    
    # keep track of which components have finished
    block_FComponents = []
    for thisComponent in block_FComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block_F"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = block_FClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_FComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block_F"-------
    for thisComponent in block_FComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    port.write('F \r')
    sleep(1.0)
    
    # the Routine "block_F" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_sound_silent = data.TrialHandler(nReps=30, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_sound_silent')
    thisExp.addLoop(trials_sound_silent)  # add the loop to the experiment
    thisTrials_sound_silent = trials_sound_silent.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrials_sound_silent.rgb)
    if thisTrials_sound_silent != None:
        for paramName in thisTrials_sound_silent.keys():
            exec(paramName + '= thisTrials_sound_silent.' + paramName)
    
    for thisTrials_sound_silent in trials_sound_silent:
        currentLoop = trials_sound_silent
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_sound_silent.rgb)
        if thisTrials_sound_silent != None:
            for paramName in thisTrials_sound_silent.keys():
                exec(paramName + '= thisTrials_sound_silent.' + paramName)
        
        #------Prepare to start Routine "sound_E_sil"-------
        t = 0
        sound_E_silClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        port.write('E \r')
        # keep track of which components have finished
        sound_E_silComponents = []
        sound_E_silComponents.append(sound_e_shad)
        sound_E_silComponents.append(fix_E)
        for thisComponent in sound_E_silComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "sound_E_sil"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = sound_E_silClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # start/stop sound_e_shad
            if t >= 0.0 and sound_e_shad.status == NOT_STARTED:
                # keep track of start time/frame for later
                sound_e_shad.tStart = t  # underestimates by a little under one frame
                sound_e_shad.frameNStart = frameN  # exact frame index
                sound_e_shad.play()  # start the sound (it finishes automatically)
            
            # *fix_E* updates
            if t >= 0.0 and fix_E.status == NOT_STARTED:
                # keep track of start time/frame for later
                fix_E.tStart = t  # underestimates by a little under one frame
                fix_E.frameNStart = frameN  # exact frame index
                fix_E.setAutoDraw(True)
            if fix_E.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                fix_E.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sound_E_silComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "sound_E_sil"-------
        for thisComponent in sound_E_silComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        sound_e_shad.stop() #ensure sound has stopped at end of routine
        # the Routine "sound_E_sil" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 30 repeats of 'trials_sound_silent'
    
    
    #------Prepare to start Routine "block_F"-------
    t = 0
    block_FClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    port.write('F \r')
    sleep(0.2)
    
    # keep track of which components have finished
    block_FComponents = []
    for thisComponent in block_FComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block_F"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = block_FClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_FComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block_F"-------
    for thisComponent in block_FComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    port.write('F \r')
    sleep(1.0)
    
    # the Routine "block_F" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "instructions_within_condition"-------
    t = 0
    instructions_within_conditionClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    within_cond_continue = event.BuilderKeyResponse()  # create an object of type KeyResponse
    within_cond_continue.status = NOT_STARTED
    # keep track of which components have finished
    instructions_within_conditionComponents = []
    instructions_within_conditionComponents.append(text_within_condition)
    instructions_within_conditionComponents.append(within_cond_continue)
    for thisComponent in instructions_within_conditionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions_within_condition"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions_within_conditionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_within_condition* updates
        if t >= 0.0 and text_within_condition.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_within_condition.tStart = t  # underestimates by a little under one frame
            text_within_condition.frameNStart = frameN  # exact frame index
            text_within_condition.setAutoDraw(True)
        
        # *within_cond_continue* updates
        if t >= 0.5 and within_cond_continue.status == NOT_STARTED:
            # keep track of start time/frame for later
            within_cond_continue.tStart = t  # underestimates by a little under one frame
            within_cond_continue.frameNStart = frameN  # exact frame index
            within_cond_continue.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(within_cond_continue.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if within_cond_continue.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                within_cond_continue.keys = theseKeys[-1]  # just the last key pressed
                within_cond_continue.rt = within_cond_continue.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_within_conditionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions_within_condition"-------
    for thisComponent in instructions_within_conditionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if within_cond_continue.keys in ['', [], None]:  # No response was made
       within_cond_continue.keys=None
    # store data for silent_loop (TrialHandler)
    silent_loop.addData('within_cond_continue.keys',within_cond_continue.keys)
    if within_cond_continue.keys != None:  # we had a response
        silent_loop.addData('within_cond_continue.rt', within_cond_continue.rt)
    # the Routine "instructions_within_condition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "pause_within_block_I"-------
    t = 0
    pause_within_block_IClock.reset()  # clock 
    frameN = -1
    routineTimer.add(15.000000)
    # update component parameters for each repeat
    port.write('I \r')
    # keep track of which components have finished
    pause_within_block_IComponents = []
    pause_within_block_IComponents.append(pause_fixation)
    for thisComponent in pause_within_block_IComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pause_within_block_I"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pause_within_block_IClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pause_fixation* updates
        if t >= 0.0 and pause_fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            pause_fixation.tStart = t  # underestimates by a little under one frame
            pause_fixation.frameNStart = frameN  # exact frame index
            pause_fixation.setAutoDraw(True)
        if pause_fixation.status == STARTED and t >= (0.0 + (15.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            pause_fixation.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pause_within_block_IComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pause_within_block_I"-------
    for thisComponent in pause_within_block_IComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    port.write('I \r')
    sleep(0.2)
    thisExp.nextEntry()
    
# completed 10 repeats of 'silent_loop'


#------Prepare to start Routine "instructions_self_production"-------
t = 0
instructions_self_productionClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
text_self_continue = event.BuilderKeyResponse()  # create an object of type KeyResponse
text_self_continue.status = NOT_STARTED
# keep track of which components have finished
instructions_self_productionComponents = []
instructions_self_productionComponents.append(text_self_production)
instructions_self_productionComponents.append(text_self_continue)
for thisComponent in instructions_self_productionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions_self_production"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions_self_productionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_self_production* updates
    if t >= 0.0 and text_self_production.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_self_production.tStart = t  # underestimates by a little under one frame
        text_self_production.frameNStart = frameN  # exact frame index
        text_self_production.setAutoDraw(True)
    
    # *text_self_continue* updates
    if t >= 1.0 and text_self_continue.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_self_continue.tStart = t  # underestimates by a little under one frame
        text_self_continue.frameNStart = frameN  # exact frame index
        text_self_continue.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(text_self_continue.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if text_self_continue.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            text_self_continue.keys = theseKeys[-1]  # just the last key pressed
            text_self_continue.rt = text_self_continue.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_self_productionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instructions_self_production"-------
for thisComponent in instructions_self_productionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if text_self_continue.keys in ['', [], None]:  # No response was made
   text_self_continue.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('text_self_continue.keys',text_self_continue.keys)
if text_self_continue.keys != None:  # we had a response
    thisExp.addData('text_self_continue.rt', text_self_continue.rt)
thisExp.nextEntry()
# the Routine "instructions_self_production" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
self_loop = data.TrialHandler(nReps=10, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='self_loop')
thisExp.addLoop(self_loop)  # add the loop to the experiment
thisSelf_loop = self_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisSelf_loop.rgb)
if thisSelf_loop != None:
    for paramName in thisSelf_loop.keys():
        exec(paramName + '= thisSelf_loop.' + paramName)

for thisSelf_loop in self_loop:
    currentLoop = self_loop
    # abbreviate parameter names if possible (e.g. rgb = thisSelf_loop.rgb)
    if thisSelf_loop != None:
        for paramName in thisSelf_loop.keys():
            exec(paramName + '= thisSelf_loop.' + paramName)
    
    #------Prepare to start Routine "block_H"-------
    t = 0
    block_HClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    port.write('H \r')
    sleep(0.2)
    
    # keep track of which components have finished
    block_HComponents = []
    for thisComponent in block_HComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block_H"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = block_HClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_HComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block_H"-------
    for thisComponent in block_HComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    port.write('H \r')
    sleep(1.0)
    
    # the Routine "block_H" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_sound_self = data.TrialHandler(nReps=30, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_sound_self')
    thisExp.addLoop(trials_sound_self)  # add the loop to the experiment
    thisTrials_sound_self = trials_sound_self.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrials_sound_self.rgb)
    if thisTrials_sound_self != None:
        for paramName in thisTrials_sound_self.keys():
            exec(paramName + '= thisTrials_sound_self.' + paramName)
    
    for thisTrials_sound_self in trials_sound_self:
        currentLoop = trials_sound_self
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_sound_self.rgb)
        if thisTrials_sound_self != None:
            for paramName in thisTrials_sound_self.keys():
                exec(paramName + '= thisTrials_sound_self.' + paramName)
        
        #------Prepare to start Routine "sound_G_self"-------
        t = 0
        sound_G_selfClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        port.write('G \r')
        # keep track of which components have finished
        sound_G_selfComponents = []
        sound_G_selfComponents.append(fix_G)
        sound_G_selfComponents.append(fix_G_wait)
        for thisComponent in sound_G_selfComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "sound_G_self"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = sound_G_selfClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *fix_G* updates
            if t >= 0.0 and fix_G.status == NOT_STARTED:
                # keep track of start time/frame for later
                fix_G.tStart = t  # underestimates by a little under one frame
                fix_G.frameNStart = frameN  # exact frame index
                fix_G.setAutoDraw(True)
            if fix_G.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                fix_G.setAutoDraw(False)
            
            # *fix_G_wait* updates
            if t >= 1.0 and fix_G_wait.status == NOT_STARTED:
                # keep track of start time/frame for later
                fix_G_wait.tStart = t  # underestimates by a little under one frame
                fix_G_wait.frameNStart = frameN  # exact frame index
                fix_G_wait.setAutoDraw(True)
            if fix_G_wait.status == STARTED and t >= (1.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                fix_G_wait.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sound_G_selfComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "sound_G_self"-------
        for thisComponent in sound_G_selfComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 30 repeats of 'trials_sound_self'
    
    
    #------Prepare to start Routine "block_H"-------
    t = 0
    block_HClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    port.write('H \r')
    sleep(0.2)
    
    # keep track of which components have finished
    block_HComponents = []
    for thisComponent in block_HComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "block_H"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = block_HClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_HComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "block_H"-------
    for thisComponent in block_HComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    port.write('H \r')
    sleep(1.0)
    
    # the Routine "block_H" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "instructions_within_condition"-------
    t = 0
    instructions_within_conditionClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    within_cond_continue = event.BuilderKeyResponse()  # create an object of type KeyResponse
    within_cond_continue.status = NOT_STARTED
    # keep track of which components have finished
    instructions_within_conditionComponents = []
    instructions_within_conditionComponents.append(text_within_condition)
    instructions_within_conditionComponents.append(within_cond_continue)
    for thisComponent in instructions_within_conditionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions_within_condition"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions_within_conditionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_within_condition* updates
        if t >= 0.0 and text_within_condition.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_within_condition.tStart = t  # underestimates by a little under one frame
            text_within_condition.frameNStart = frameN  # exact frame index
            text_within_condition.setAutoDraw(True)
        
        # *within_cond_continue* updates
        if t >= 0.5 and within_cond_continue.status == NOT_STARTED:
            # keep track of start time/frame for later
            within_cond_continue.tStart = t  # underestimates by a little under one frame
            within_cond_continue.frameNStart = frameN  # exact frame index
            within_cond_continue.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(within_cond_continue.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if within_cond_continue.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                within_cond_continue.keys = theseKeys[-1]  # just the last key pressed
                within_cond_continue.rt = within_cond_continue.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_within_conditionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions_within_condition"-------
    for thisComponent in instructions_within_conditionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if within_cond_continue.keys in ['', [], None]:  # No response was made
       within_cond_continue.keys=None
    # store data for self_loop (TrialHandler)
    self_loop.addData('within_cond_continue.keys',within_cond_continue.keys)
    if within_cond_continue.keys != None:  # we had a response
        self_loop.addData('within_cond_continue.rt', within_cond_continue.rt)
    # the Routine "instructions_within_condition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "pause_within_block_I"-------
    t = 0
    pause_within_block_IClock.reset()  # clock 
    frameN = -1
    routineTimer.add(15.000000)
    # update component parameters for each repeat
    port.write('I \r')
    # keep track of which components have finished
    pause_within_block_IComponents = []
    pause_within_block_IComponents.append(pause_fixation)
    for thisComponent in pause_within_block_IComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pause_within_block_I"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pause_within_block_IClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pause_fixation* updates
        if t >= 0.0 and pause_fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            pause_fixation.tStart = t  # underestimates by a little under one frame
            pause_fixation.frameNStart = frameN  # exact frame index
            pause_fixation.setAutoDraw(True)
        if pause_fixation.status == STARTED and t >= (0.0 + (15.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            pause_fixation.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pause_within_block_IComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pause_within_block_I"-------
    for thisComponent in pause_within_block_IComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    port.write('I \r')
    sleep(0.2)
    
    #------Prepare to start Routine "instructions_restart_self_prod"-------
    t = 0
    instructions_restart_self_prodClock.reset()  # clock 
    frameN = -1
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    instructions_restart_self_prodComponents = []
    instructions_restart_self_prodComponents.append(self_restart_instruction)
    for thisComponent in instructions_restart_self_prodComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions_restart_self_prod"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = instructions_restart_self_prodClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *self_restart_instruction* updates
        if t >= 0.0 and self_restart_instruction.status == NOT_STARTED:
            # keep track of start time/frame for later
            self_restart_instruction.tStart = t  # underestimates by a little under one frame
            self_restart_instruction.frameNStart = frameN  # exact frame index
            self_restart_instruction.setAutoDraw(True)
        if self_restart_instruction.status == STARTED and t >= (0.0 + (3.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            self_restart_instruction.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_restart_self_prodComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions_restart_self_prod"-------
    for thisComponent in instructions_restart_self_prodComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 10 repeats of 'self_loop'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

the_end_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
the_end_resp.status = NOT_STARTED
# keep track of which components have finished
endComponents = []
endComponents.append(the_end)
endComponents.append(the_end_resp)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *the_end* updates
    if t >= 0.0 and the_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        the_end.tStart = t  # underestimates by a little under one frame
        the_end.frameNStart = frameN  # exact frame index
        the_end.setAutoDraw(True)
    
    # *the_end_resp* updates
    if t >= 0.2 and the_end_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        the_end_resp.tStart = t  # underestimates by a little under one frame
        the_end_resp.frameNStart = frameN  # exact frame index
        the_end_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(the_end_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if the_end_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            the_end_resp.keys = theseKeys[-1]  # just the last key pressed
            the_end_resp.rt = the_end_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if the_end_resp.keys in ['', [], None]:  # No response was made
   the_end_resp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('the_end_resp.keys',the_end_resp.keys)
if the_end_resp.keys != None:  # we had a response
    thisExp.addData('the_end_resp.rt', the_end_resp.rt)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


















port.write('ED\r') # harcoded end command
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
