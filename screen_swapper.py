#!/usr/bin/python
# Must use system python
import sys                  # make decisions based on system configuration
import warnings                 # control warning settings for
import abc              # allows use of abstract classes
import objc             # access Objective-C functions and variables
import CoreFoundation   # work with Objective-C data types
import Quartz           # work with system graphics

(error, config_ref) = Quartz.CGBeginDisplayConfiguration(None)

(error, display_ids, count) = Quartz.CGGetOnlineDisplayList(32, None, None)
for display_id in display_ids:
    print(display_id)
    print(str(Quartz.CGDisplayCopyColorSpace(display_id))).split("; ")[2].replace(")","")
    print(Quartz.CGDisplayPixelsWide(display_id))
    print(Quartz.CGDisplayBounds(display_id))
    print("")

for display_id in display_ids:
    if Quartz.CGDisplayIsBuiltin(display_id):
        print("Built-in Display")
        print(display_id)
        Quartz.CGConfigureDisplayOrigin(config_ref, display_id, -1440, 900)
    else:
        if Quartz.CGDisplayIsMain(display_id):
            print("Main Display< Move it")
            print(display_id)
            Quartz.CGConfigureDisplayOrigin(config_ref, display_id, 3200, 0)
        else:
            print("Not Main Display")
            print(display_id)
            Quartz.CGConfigureDisplayOrigin(config_ref, display_id, 0, 0)

Quartz.CGCompleteDisplayConfiguration(config_ref, Quartz.kCGConfigurePermanently)
"""
for display_id in display_ids:
    if Quartz.CGDisplayIsBuiltin(display_id):
        print("Built-in Display")
        (error, config_ref) = Quartz.CGBeginDisplayConfiguration(None)
        Quartz.CGConfigureDisplayOrigin(config_ref, display_id, -1440, 900)
        Quartz.CGCompleteDisplayConfiguration(config_ref, Quartz.kCGConfigurePermanently)
    else:
        if Quartz.CGDisplayIsMain(display_id):
            print("Main Display")
            (error, config_ref) = Quartz.CGBeginDisplayConfiguration(None)
            Quartz.CGConfigureDisplayOrigin(config_ref, display_id, 3201, 0)
            Quartz.CGCompleteDisplayConfiguration(config_ref, Quartz.kCGConfigurePermanently)
        else:
            (error, config_ref) = Quartz.CGBeginDisplayConfiguration(None)
            Quartz.CGConfigureDisplayOrigin(config_ref, display_id, 0, 0)
            Quartz.CGCompleteDisplayConfiguration(config_ref, Quartz.kCGConfigurePermanently)
"""

#Z27s
#59592001
#59592002
"""
(error, config_ref) = Quartz.CGBeginDisplayConfiguration(None)
Quartz.CGConfigureDisplayOrigin(config_ref, 59592001, 30840, 0)
Quartz.CGCompleteDisplayConfiguration(config_ref, Quartz.kCGConfigurePermanently)
"""
