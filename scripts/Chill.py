from import_all import *
from utilities import *
from pathlib import Path

class keithleys():
    def __init__(self):
        station = Station(config_file="electrochemistry.station.yaml")
        keithley1 = station.load_keithley1()
        keithley2 = station.load_keithley2()

        keithleys = [keithley1, keithley2]

    def ramp(self, chan, target, speed):
        chan = [chan
        target = [target]

        for ch, target in zip(chan, target):
            trigger.set_v(chan,)
            speed



class trigger(keithleys):
    chan = 
    def abort(chan):
        chan.write(f"{chan.channel}.abort()")

    def meas_trig_params(chan):
        #setup buffer
        chan.write(f"{chan.channel}.trigger.measure.i({chan.channel}.nvbuffer1)")
        chan.write(f"{chan.channel}.nvbuffer1.appendmode = 1")

        #clear any residual values
        chan.write(f"{chan.channel}.nvbuffer1.clear()")
        chan.write(f"{chan.channel}.nvbuffer1.collectsourcevalues = 1")

        #set measure trig to automatic (after source)
        chan.write(f"{chan.channel}.measure.count = 1")
        chan.write(f"{chan.channel}.trigger.measure.stimulus = 0")

        #enable
        chan.write(f"{chan.channel}.trigger.measure.action = {chan.channel}.ENABLE")


    def source_trig_params(chan):
        #tie source to bus trigger
        chan.write(f"{chan.channel}.trigger.source.stimulus = trigger.EVENT_ID")

        #end of sweep phase action
        chan.write(f"{chan.channel}.trigger.endsweep.action = smua.SOURCE_HOLD")

        #enable
        chan.write(f"{chan.channel}.trigger.source.action = {chan.channel}.ENABLE")


    def trigger(keithleys, channels):
        for ch in channels:
            ch.write(f"{ch.channel}.nvbuffer1.clear()")
            ch.write(f"{ch.channel}.trigger.initiate()")

        for k in keithleys:
            k.write("*TRG")


    def recall_buffer(ch):
        j = ch.ask(f"{ch.channel}.nvbuffer1.readings[1]") 
        v = ch.ask(f"{ch.channel}.nvbuffer1.sourcevalues[1]")
        return v, j


    def set_v(ch,volt):
        ch.write(f"{ch.channel}.trigger.source.linearv({volt}, {volt}, 1)")





class parameters(keithleys):

    time_independent = False  #plot time as indepent variable? 
    ramp_up = True # ramp to initial values?
    ramp_down = True #ramp back to 0?
    round_ramp =False #ramp to new configuration each time vt+vb changes? Useful for sparse map, unecessary for full map
    temp_measure = True
    ktime_control = True
    #----Set gate and drain source parameters
    e_lims = [-0.6,-0.6] # max and min E
    e_start = -0.6
    dV_e = 0.0 # number of E values
    e_return =True

    n_lims = [-0.5, 4.0] #max and min of n
    n_start = -0.5
    dV_n = 0.02 #voltage step for n
    n_return = True

    fixed_voltage = 5e-4 # drain source voltage
    temp_voltage = 5e-3 # voltage applied across thermistor
    ########----Scanning parameters----######
    dt = 1
    delayNPLC_ratio = 0.9 #ratio of wait/integrate

    start_delay = 1 #time between setting initial voltages and beginning scan
    round_delay=0 #round delay is the delay built in between succesive loops through intercepts (each back-forward trace)
    repeat = 1 #how many times to repeat entire map
    forward_write_period = 2

    sweepers = [top_gate, bottom_gate, drain_source, tempDict]
    sweepers_save_order = [top_gate, bottom_gate, drain_source,tempDict] #Order for saving in database, for easy parsing of data in plottr-inspectr
    channels_save_order = [top_gate["channel"], bottom_gate["channel"], drain_source["channel"],
                            tempDict["channel"]] #Order for saving in database, for easy parsing of data in plottr-inspectr



    def __init__(self):
        pass



class Measurements(trigger, parameters):



    def __init__(self):
        super().__init__()



    def trigger(keithleys, channels):
    for ch in channels:
        ch.write(f"{ch.channel}.nvbuffer1.clear()")
        ch.write(f"{ch.channel}.trigger.initiate()")

    for k in keithleys:
        k.write("*TRG")


class database(Measurements):
