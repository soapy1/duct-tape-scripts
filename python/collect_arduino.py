#! /usr/bin/env/python2
import serial
import csv
import time
import argparse

def main(args):

    print "starting up"
    data_feed = serial.Serial()
    data_feed.port =  args.port[0]
    data_feed.baudrate = 9600
    data_feed.open()
  
    start_time = time.time()
    duration = args.duration[0]
    endtime = 0
    collecting = True

    with open('data.csv', 'wb') as csvfile:
        fieldnames = ['timestamp', 'point']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            
        writer.writeheader()
        while collecting: 
            dp = data_feed.readline() 
            writer.writerow({'timestamp': time.time(), 'point': dp.strip()})
        
            if time.time() > start_time + duration:
                endtime = time.time()
                collecting = False

    data_feed.close()
    print "start time: {}".format(start_time)
    print "end time: {}".format(endtime)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Collect data on serial port")
    parser.add_argument('--port', nargs=1, default=["/dev/ttyACM0"], type=str,  dest="port", help='selects the port') 
    parser.add_argument('--duration', nargs=1, default=[1], type=int, dest="duration", help="duration of data collection") 
    args = parser.parse_args()

    main(args)