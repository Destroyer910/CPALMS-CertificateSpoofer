import subprocess
import datetime
from subprocess import Popen, PIPE, STDOUT

def execute(cmd):
    p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    output = p.stdout.read()
    return output
print("NOTE: All values should be accurate or the page will return an Error (e.g. typing 13 for the month number")
year = input("Which Year do You Want the Certificate to Start In? ")
month = input("Start Month? (1-12) ")
day = input("Start Day? (1-31) ")
endyear = input("Which Year do You Want the Certificate to End In? ")
endmonth = input("End Month? (1-12) ")
endday = input("End Day? (1-31) ")
sessionid = input("Session ID? ")
command = 'curl -s -d "input=%7B%22StartDateTime%22%3A%22'+str(year)+'-'+str(month)+'-'+str(day)+'T10%3A10%3A20.439Z%22%2C%22EndDateTime%22%3A%22'+str(endyear)+'-'+str(endmonth)+'-'+str(endday)+'T10%3A28%3A34.587Z%22%2C%22ResourceId%22%3A%22'+str(sessionid)+'%22%2C%22isFromCpalms%22%3A1%2C%22Path%22%3A%22%22%7D" -X POST https://www.cpalms.org/Public/PreviewResource/Encrypt'
print(command)
dataOut = execute(command)
dataOut = dataOut.decode("utf-8")
print(dataOut)
finalData, junkData = dataOut[11:].split('"')
command2 = "start /MIN "" https://www.cpalms.org/Public/PreviewCertification/Certificate?Data=" + str(finalData)
execute(command2)
