# -*- coding: utf-8 -*-
import sys
import string
import threading
from time import sleep
import requests
import ctypes
import datetime

request_interval=100
mail_notify=0

def is_stream(room):
    url="http://www.douyutv.com/"+room
    r = requests.get(url,timeout=20,verify=False)
    if "feedback_report_button" in r.text:
        return 1

def monitor(room):
    print "start monitoring streaming status of " + room
    while 1:
        try:
                if is_stream(room):
                    current_time = datetime.datetime.now().time()
                    print room + ' started live streaming at ' + str(current_time)
                    ctypes.windll.user32.MessageBoxA(0,  room, str(current_time), 1)
                    if mail_notify:
                        send_email(room)
                    sleep(3600)
                    while (is_stream(room)):
                        sleep(3600)
                sleep(request_interval)
        except Exception, e:
            print str(e)
            sleep(10)


def send_email(SUBJECT):
            import smtplib
            mail_user = "188888888@wo.cn"
            mail_pwd = "88888"
            FROM = '188888888@wo.cn'
            TO = ['188888888@wo.cn'] #must be a list
            TEXT = SUBJECT
 
            message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
           """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
            try:
                server = smtplib.SMTP("smtp.wo.cn", 25)
                #server.ehlo()
                #server.starttls()
                server.login(mail_user, mail_pwd)
                server.sendmail(FROM, TO, message)
                #server.quit()
                server.close()
                print SUBJECT + ' mail sent successfully'
            except Exception, e:
                print str(e)

if __name__ == "__main__":
    threads = []
#   usage: python douyu.py chenyifaer erke 71771
#   for room in sys.argv[1:]: # uncomment this line to get room ids from command line arguments
    for room in ["chenyifaer","erke"]:
        t = threading.Thread(target=monitor, args=(room,))
        threads.append(t)
        t.daemon = True
        t.start()
    while len(threads) > 0:
            # Join all threads using a timeout so it doesn't block
            # Filter out threads which have been joined or are None
            threads = [t.join(1000) for t in threads if t is not None and t.isAlive()]
    print "done"
