import sys
import optparse
import shodan
from colorama import Fore, Back, Style

print (Fore.RED + '''
######## ##     ## ########  ######## ######## ########     ###    ##    ##
   ##    ##     ## ##     ## ##       ##       ##     ##   ## ##   ###   ##
   ##    ##     ## ##     ## ##       ##       ##     ##  ##   ##  ####  ##
   ##    ######### ########  ######   ######   ##     ## ##     ## ## ## ##
   ##    ##     ## ##   ##   ##       ##       ##     ## ######### ##  ####
   ##    ##     ## ##    ##  ##       ##       ##     ## ##     ## ##   ###
   ##    ##     ## ##     ## ######## ######## ########  ##     ## ##    ##

'''

       ) + (Fore.GREEN + ' by threebones \n https://github.com/threebarber')




parser = optparse.OptionParser()

parser.add_option(
        '-q','--query',dest='query',type='string',help='specify search query IE \'ftp\'')

parser.add_option(
        '-f','--file',dest='filename',default='list.txt',type='string',help='specify filename (add .txt to end)')

(options, args) = parser.parse_args(sys.argv)

SHODAN_API_KEY = "INSERT SHODAN API KEY HERE"
api = shodan.Shodan(SHODAN_API_KEY)

results = api.search(options.query)
print (Style.BRIGHT + '[+] Saving to: ') +options.filename
print (Style.BRIGHT +'[+] Searching for: ') +options.query
print (Style.BRIGHT + '[+] Total Results: ') +str(results['total']) + "\n"

for result in results['matches']:
    print str(result['ip_str'])
    list = open (options.filename,'a')
    list.write(str(result['ip_str'] + '\n'))


