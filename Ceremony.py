
import sys
import time

from naoqi import ALBroker
from naoqi import ALProxy
from naoqi import ALModule

from optparse import OptionParser



BriApp = []
bList = []
naos = []

Nao_IP = "localhost"

nao_address = ""

def main():
    print "-----------------------------------------"
    print "Welcome to Mediatec Robotics Manager"
    print "-----------------------------------------"
    print "Enter the internet directions of the NAOs pressing enter between them. At the end put 'end' to finish the addresses\n"
    while True:
        nao_address = raw_input("")
        if nao_address == "end":
            break
        elif nao_address == "":
            print "Error no valid address...\n"
        else:
            naos.append(nao_address)
            
        pass
    
    for i in naos:
        try:
            BriApp.append(ALProxy("ALBehaviorManager",str(i),9559))
            print "--------------------------------------"
            print str(i) + " Connection Success"
            print "--------------------------------------"
        except:
            print "--------------------------------------"
            print "Failed connection with " + str(i) + ". Connection Refused."
            print "--------------------------------------"
            

    if len(BriApp) > 0:
        raw_input("Press any key to continue...")
    else:
        raw_input("No connections found")
        sys.exit()
    
    for i in BriApp:
        try:
            print "--------------------------------------"
            print "Behaviors installed in " + str(i)
            print "--------------------------------------"
            bList = i.getInstalledBehaviors()
            for j in bList:
                print j
            print 
            print "--------------------------------------"
            raw_input("press any key to continue...")
        except:
            None

        
    while True:
        showTime = True
        showName = raw_input("Write which behavior you want to run, for aditional commands use ?\n")
        if showName == "?":
            print ">>exit\n>>?\n"            
                
        elif showName == "exit":
            sys.exit(0)
            
            for i in BriApp:
                i.stopAllBehaviors()
                
                
        else:
            
            for i in BriApp:
                if i.isBehaviorInstalled(showName) == False:
                    print "--------------------------------------"
                    print "Behaviors not installed in Nao " + str(i)
                    print "--------------------------------------"
                    showTime = False
                    
            if showTime == True:
                for i in BriApp:
                    i.preloadBehavior(showName)
                    print "--------------------------------------"
                    print "Nao " + str(i) + " ready..."
                    print "--------------------------------------"
                raw_input("press any key to run...")
                for i in BriApp:
                    i.post.runBehavior(showName)
                print "--------------------------------------"
                print "running..."
                print "--------------------------------------"
            else:
                raw_input("press any key to continue...")
                
if __name__ == "__main__":
    main()        
