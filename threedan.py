import sys
import optparse
import shodan
import time

def search(query,filename):

    SHODAN_API_KEY = "SHODAN API KEY HERE" #api key to utilize shodan API
    api = shodan.Shodan(SHODAN_API_KEY) #create api shodan object

    try:
        results = api.search(query) #try to search using api object, error handling for messy shodan.APIERROR errors
    except shodan.APIError, se:
        print "[-] Shodan APIError, " +str(se)
        exit(0)

    print '[+] Saving to: '        +str(filename) #display progress and user-selected options back to user
    time.sleep(5)
    print '[+] Searching for: '    +(query)
    time.sleep(5)
    print '[+] Total Results: '    +str(results['total']) + "\n-----------------------------------"
    time.sleep(5)

    for result in results['matches']: #print list of returned IP's
        print str(result['ip_str'])
        list = open (filename,'a') #write retrieved ip's to text document defined by user
        list.write(str(result['ip_str'] + '\n'))

def main():
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


    parser = optparse.OptionParser() #create parser object called "parser"

    parser.usage = "[+] Usage:   threedan.py -q <query> -f <filename.txt>" \
                   "\n[+] Example: threedan.py -q ftp  -f ftplist.txt      " #add usage for "parser" object as well as example

    parser.add_option(
            '-q','--query',dest='query',type='string',help='specify search query IE \'ftp\'') #add search query option as -q

    parser.add_option(
            '-f','--file',dest='filename',default='list.txt',type='string',help='specify filename (add .txt to end)') #add filename option as -f

    (options, args) = parser.parse_args(sys.argv) #finalize parsing portion

    query = options.query
    filename = options.filename

    if (query) == None != (filename == None):
        print parser.usage
        exit(0) #check to make sure required params were assigned a value - if not, exit
    search(query,filename)

if __name__ == '__main__':
    main()
