#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on November 23, 2017, at 14:51
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\Temp\\Desktop\\REBOOT_II\\EpMem\\EpMem.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1280, 720), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "fixPre"
fixPreClock = core.Clock()
polygon_2 = visual.Polygon(
    win=win, name='polygon_2',
    edges=90, size=(0.02, 0.02),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,1.000,-0.498], lineColorSpace='rgb',
    fillColor=[-1.000,1.000,-0.498], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
index = visual.TextStim(win=win, name='index',
    text='>',
    font='Arial',
    pos=(-0.95, -0.9), height=0.05, wrapWidth=None, ori=0, 
    color=[0.506,0.506,0.506], colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "intro"
introClock = core.Clock()
intro_pic = visual.ImageStim(
    win=win, name='intro_pic',
    image='stim/intro.png', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
instructions = visual.TextStim(win=win, name='instructions',
    text=u'Om du *k\xe4nner* igen bilden fr\xe5n tr\xe4ningsperioden trycker du p\xe5 knappen till v\xe4nster.\nOm du *inte k\xe4nner* igen bilden fr\xe5n tr\xe4ningsperioden trycker du p\xe5 knappen till h\xf6ger.\nDu har 3 sekunder p\xe5 dig att svara, sedan f\xf6rsvinner bilden s\xe5 det \xe4r viktigt att du trycka p\xe5 en av knapparna innan dess.',
    font=u'Arial',
    pos=[0, 0.5], height=0.075, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Trigger"
TriggerClock = core.Clock()
varRedo = visual.TextStim(win=win, name='varRedo',
    text='Var redo...',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "P"
PClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0.1], size=[1.35, 1.35],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
instr = visual.TextStim(win=win, name='instr',
    text=u'svara!',
    font=u'Arial',
    pos=[0, 0.92], height=0.3, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);
seen = visual.TextStim(win=win, name='seen',
    text=u'Ja',
    font=u'Arial',
    pos=(-0.4, -0.75), height=0.1, wrapWidth=None, ori=0, 
    color=[-0.420,-0.420,1.000], colorSpace='rgb', opacity=1,
    depth=-3.0);
new = visual.TextStim(win=win, name='new',
    text='Nej',
    font='Arial',
    pos=(0.4, -0.75), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "fix"
fixClock = core.Clock()
polygon = visual.Polygon(
    win=win, name='polygon',
    edges=90, size=[1.0, 1.0],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "end"
endClock = core.Clock()
thanks = visual.TextStim(win=win, name='thanks',
    text='Tack!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "fixPost"
fixPostClock = core.Clock()
polygon_3 = visual.Polygon(
    win=win, name='polygon_3',
    edges=90, size=(0.02, 0.02),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,1.000,-0.498], lineColorSpace='rgb',
    fillColor=[-1.000,1.000,-0.498], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
index_2 = visual.TextStim(win=win, name='index_2',
    text='<',
    font='Arial',
    pos=(-0.95, -0.9), height=0.05, wrapWidth=None, ori=0, 
    color=[0.506,0.506,0.506], colorSpace='rgb', opacity=1,
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "fixPre"-------
t = 0
fixPreClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
skipFIX = event.BuilderKeyResponse()
# keep track of which components have finished
fixPreComponents = [polygon_2, index, skipFIX]
for thisComponent in fixPreComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "fixPre"-------
while continueRoutine:
    # get current time
    t = fixPreClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_2* updates
    if t >= 0.0 and polygon_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_2.tStart = t
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.setAutoDraw(True)
    
    # *index* updates
    if t >= 0.0 and index.status == NOT_STARTED:
        # keep track of start time/frame for later
        index.tStart = t
        index.frameNStart = frameN  # exact frame index
        index.setAutoDraw(True)
    
    # *skipFIX* updates
    if t >= 0.0 and skipFIX.status == NOT_STARTED:
        # keep track of start time/frame for later
        skipFIX.tStart = t
        skipFIX.frameNStart = frameN  # exact frame index
        skipFIX.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(skipFIX.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if skipFIX.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            skipFIX.keys = theseKeys[-1]  # just the last key pressed
            skipFIX.rt = skipFIX.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixPreComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixPre"-------
for thisComponent in fixPreComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if skipFIX.keys in ['', [], None]:  # No response was made
    skipFIX.keys=None
thisExp.addData('skipFIX.keys',skipFIX.keys)
if skipFIX.keys != None:  # we had a response
    thisExp.addData('skipFIX.rt', skipFIX.rt)
thisExp.nextEntry()
# the Routine "fixPre" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "intro"-------
t = 0
introClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
skip = event.BuilderKeyResponse()
# keep track of which components have finished
introComponents = [intro_pic, instructions, skip]
for thisComponent in introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_pic* updates
    if t >= 0.0 and intro_pic.status == NOT_STARTED:
        # keep track of start time/frame for later
        intro_pic.tStart = t
        intro_pic.frameNStart = frameN  # exact frame index
        intro_pic.setAutoDraw(True)
    
    # *instructions* updates
    if t >= 0.0 and instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions.tStart = t
        instructions.frameNStart = frameN  # exact frame index
        instructions.setAutoDraw(True)
    
    # *skip* updates
    if t >= 0.0 and skip.status == NOT_STARTED:
        # keep track of start time/frame for later
        skip.tStart = t
        skip.frameNStart = frameN  # exact frame index
        skip.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(skip.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if skip.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            skip.keys = theseKeys[-1]  # just the last key pressed
            skip.rt = skip.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if skip.keys in ['', [], None]:  # No response was made
    skip.keys=None
thisExp.addData('skip.keys',skip.keys)
if skip.keys != None:  # we had a response
    thisExp.addData('skip.rt', skip.rt)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Trigger"-------
t = 0
TriggerClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
trigger = event.BuilderKeyResponse()
# keep track of which components have finished
TriggerComponents = [varRedo, trigger]
for thisComponent in TriggerComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Trigger"-------
while continueRoutine:
    # get current time
    t = TriggerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *varRedo* updates
    if t >= 0.0 and varRedo.status == NOT_STARTED:
        # keep track of start time/frame for later
        varRedo.tStart = t
        varRedo.frameNStart = frameN  # exact frame index
        varRedo.setAutoDraw(True)
    
    # *trigger* updates
    if t >= 0.0 and trigger.status == NOT_STARTED:
        # keep track of start time/frame for later
        trigger.tStart = t
        trigger.frameNStart = frameN  # exact frame index
        trigger.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(trigger.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if trigger.status == STARTED:
        theseKeys = event.getKeys(keyList=['5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            trigger.keys = theseKeys[-1]  # just the last key pressed
            trigger.rt = trigger.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TriggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Trigger"-------
for thisComponent in TriggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if trigger.keys in ['', [], None]:  # No response was made
    trigger.keys=None
thisExp.addData('trigger.keys',trigger.keys)
if trigger.keys != None:  # we had a response
    thisExp.addData('trigger.rt', trigger.rt)
thisExp.nextEntry()
# the Routine "Trigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('IOstim-2017-03-10.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "P"-------
    t = 0
    PClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(img)
    resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    PComponents = [image, instr, resp, seen, new]
    for thisComponent in PComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "P"-------
    while continueRoutine:
        # get current time
        t = PClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 0.0 + dur- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        
        # *instr* updates
        if t >= 0.0 and instr.status == NOT_STARTED:
            # keep track of start time/frame for later
            instr.tStart = t
            instr.frameNStart = frameN  # exact frame index
            instr.setAutoDraw(True)
        frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if instr.status == STARTED and t >= frameRemains:
            instr.setAutoDraw(False)
        
        # *resp* updates
        if t >= 0.0 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + dur- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resp.status == STARTED and t >= frameRemains:
            resp.status = STOPPED
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp.keys = theseKeys[-1]  # just the last key pressed
                resp.rt = resp.clock.getTime()
                # was this 'correct'?
                if (resp.keys == str(cr)) or (resp.keys == cr):
                    resp.corr = 1
                else:
                    resp.corr = 0
        
        # *seen* updates
        if t >= 0.0 and seen.status == NOT_STARTED:
            # keep track of start time/frame for later
            seen.tStart = t
            seen.frameNStart = frameN  # exact frame index
            seen.setAutoDraw(True)
        frameRemains = 0.0 + dur- win.monitorFramePeriod * 0.75  # most of one frame period left
        if seen.status == STARTED and t >= frameRemains:
            seen.setAutoDraw(False)
        
        # *new* updates
        if t >= 0.0 and new.status == NOT_STARTED:
            # keep track of start time/frame for later
            new.tStart = t
            new.frameNStart = frameN  # exact frame index
            new.setAutoDraw(True)
        frameRemains = 0.0 + dur- win.monitorFramePeriod * 0.75  # most of one frame period left
        if new.status == STARTED and t >= frameRemains:
            new.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "P"-------
    for thisComponent in PComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys=None
        # was no response the correct answer?!
        if str(cr).lower() == 'none':
           resp.corr = 1  # correct non-response
        else:
           resp.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('resp.keys',resp.keys)
    trials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials.addData('resp.rt', resp.rt)
    # the Routine "P" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "fix"-------
    t = 0
    fixClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    polygon.setSize([0.02, 0.02])
    # keep track of which components have finished
    fixComponents = [polygon]
    for thisComponent in fixComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fix"-------
    while continueRoutine:
        # get current time
        t = fixClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if t >= 0.0 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        frameRemains = 0.0 + fix- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon.status == STARTED and t >= frameRemains:
            polygon.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix"-------
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "fix" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
end_task = event.BuilderKeyResponse()
# keep track of which components have finished
endComponents = [end_task, thanks]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_task* updates
    if t >= 0.0 and end_task.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_task.tStart = t
        end_task.frameNStart = frameN  # exact frame index
        end_task.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(end_task.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if end_task.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            end_task.keys = theseKeys[-1]  # just the last key pressed
            end_task.rt = end_task.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *thanks* updates
    if t >= 0.0 and thanks.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanks.tStart = t
        thanks.frameNStart = frameN  # exact frame index
        thanks.setAutoDraw(True)
    
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

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_task.keys in ['', [], None]:  # No response was made
    end_task.keys=None
thisExp.addData('end_task.keys',end_task.keys)
if end_task.keys != None:  # we had a response
    thisExp.addData('end_task.rt', end_task.rt)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixPost"-------
t = 0
fixPostClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
skipFIX_2 = event.BuilderKeyResponse()
# keep track of which components have finished
fixPostComponents = [polygon_3, index_2, skipFIX_2]
for thisComponent in fixPostComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "fixPost"-------
while continueRoutine:
    # get current time
    t = fixPostClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_3* updates
    if t >= 0.0 and polygon_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_3.tStart = t
        polygon_3.frameNStart = frameN  # exact frame index
        polygon_3.setAutoDraw(True)
    
    # *index_2* updates
    if t >= 0.0 and index_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        index_2.tStart = t
        index_2.frameNStart = frameN  # exact frame index
        index_2.setAutoDraw(True)
    
    # *skipFIX_2* updates
    if t >= 0.0 and skipFIX_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        skipFIX_2.tStart = t
        skipFIX_2.frameNStart = frameN  # exact frame index
        skipFIX_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(skipFIX_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if skipFIX_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            skipFIX_2.keys = theseKeys[-1]  # just the last key pressed
            skipFIX_2.rt = skipFIX_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixPostComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixPost"-------
for thisComponent in fixPostComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if skipFIX_2.keys in ['', [], None]:  # No response was made
    skipFIX_2.keys=None
thisExp.addData('skipFIX_2.keys',skipFIX_2.keys)
if skipFIX_2.keys != None:  # we had a response
    thisExp.addData('skipFIX_2.rt', skipFIX_2.rt)
thisExp.nextEntry()
# the Routine "fixPost" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
