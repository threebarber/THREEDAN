import sys
import optparse
import shodan
import time

print '''
######## ##     ## ########  ######## ######## ########     ###    ##    ##
   ##    ##     ## ##     ## ##       ##       ##     ##   ## ##   ###   ##
   ##    ##     ## ##     ## ##       ##       ##     ##  ##   ##  ####  ##
   ##    ######### ########  ######   ######   ##     ## ##     ## ## ## ##
   ##    ##     ## ##   ##   ##       ##       ##     ## ######### ##  ####
   ##    ##     ## ##    ##  ##       ##       ##     ## ##     ## ##   ###
   ##    ##     ## ##     ## ######## ######## ########  ##     ## ##    ##
                                            
'''

print ' by threebones \n https://github.com/threebarber\n'


parser = optparse.OptionParser()

parser.usage = "[+] Usage:   threedan.py -q <query> -f <filename.txt>" \
               "\n[+] Example: threedan.py -q ftp  -f ftplist.txt      "

parser.add_option(
        '-q','--query',dest='query',type='string',help='specify search query IE \'ftp\'')

parser.add_option(
        '-f','--file',dest='filename',default='list.txt',type='string',help='specify filename (add .txt to end)')

(options, args) = parser.parse_args(sys.argv)

SHODAN_API_KEY = "INSERT SHODAN API KEY HERE"
api = shodan.Shodan(SHODAN_API_KEY)

if (options.query) == None != (options.filename == None):
    print parser.usage
    exit(0)
try:
    results = api.search(options.query)
except shodan.APIError, se:
    print "[-] Shodan APIError, " +str(se)

print '[+] Saving to: '        +options.filename
time.sleep(5)
print '[+] Searching for: '    +options.query
time.sleep(5)
print '[+] Total Results: '    +str(results['total']) + "\n"
time.sleep(5)

for result in results['matches']:
    print str(result['ip_str'])
    list = open (options.filename,'a')
    list.write(str(result['ip_str'] + '\n'))

