#coded by N17RO (noob hackers) 
  
 #modules required 
 import argparse 
 import requests, json 
 import sys 
 from sys import argv 
 import os 
  
 #arguments and parser 
  
 parser = argparse.ArgumentParser() 
  
 parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target', required=True ) 
  
 args = parser.parse_args() 
  
 #colours used 
 red = '\033[31m' 
 yellow = '\033[93m' 
 lgreen = '\033[92m' 
 clear = '\033[0m' 
 bold = '\033[01m' 
 cyan = '\033[96m' 
  
 #banner of script 
 print (red+""" 
  
 
  _____                               _               
 |_   _|                             | |              
   | |  _ __  ___  ___  __ _ _ __ ___| |__   ___ _ __ 
   | | | '_ \/ __|/ _ \/ _` | '__/ __| '_ \ / _ \ '__|
  _| |_| |_) \__ \  __/ (_| | | | (__| | | |  __/ |   
 |_____| .__/|___/\___|\__,_|_|  \___|_| |_|\___|_|   
       | |                                            
       |_|                                            

                                                       v 1.0 beta 
 """+red) 
 print (lgreen+bold+"         <===[[ Developed by Sajadtlpr ]]===> \n"+clear) 
 print (yellow+bold+"   <---(( Greets to all HITLOS SQUAD MEMBERS ))--> \n"+clear) 
  
  
 ip = args.target 
  
 api = "http://ip-api.com/json/" 
  
 try: 
         data = requests.get(api+ip).json() 
         sys.stdout.flush() 
         a = lgreen+bold+"[$]" 
         b = cyan+bold+"[$]" 
         print (a, "[Victim]:", data['query']) 
         print(red+"<--------------->"+red) 
         print (b, "[ISP]:", data['isp']) 
         print(red+"<--------------->"+red) 
         print (a, "[Organisation]:", data['org']) 
         print(red+"<--------------->"+red) 
         print (b, "[City]:", data['city']) 
         print(red+"<--------------->"+red) 
         print (a, "[Region]:", data['region']) 
         print(red+"<--------------->"+red) 
         print (b, "[Longitude]:", data['lon']) 
         print(red+"<--------------->"+red) 
         print (a, "[Latitude]:", data['lat']) 
         print(red+"<--------------->"+red) 
         print (b, "[Time zone]:", data['timezone']) 
         print(red+"<--------------->"+red) 
         print (a, "[Zip code]:", data['zip']) 
         print (" "+yellow) 
  
 except KeyboardInterrupt: 
         print ('Terminating, Bye'+lgreen) 
         sys.exit(0) 
 except requests.exceptions.ConnectionError as e: 
         print (red+"[~]"+" check your internet connection!"+clear) 
 sys.exit(1)
