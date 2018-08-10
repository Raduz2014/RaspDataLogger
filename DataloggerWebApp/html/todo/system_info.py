#!/usr/bin/python

import  psutil

def main():
    aa = psutil.cpu_times()
    print aa.user

if __name__ == '__main__':
    main()