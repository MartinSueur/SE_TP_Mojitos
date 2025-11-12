import sys
import os

min_freq = open("/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_min_freq", "r").readline()
max_freq = open("/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq", "r").readline()
print("freq between : ",min_freq,max_freq)
