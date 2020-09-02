import camelot
import sys, random, time
from colorama import init, Fore

init()

def ClownLogo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

       ____  ____  ______   __        __    __                  __                  __            
      / __ \/ __ \/ ____/  / /_____ _/ /_  / /__     ___  _  __/ /__________ ______/ /_____  _____
     / /_/ / / / / /_     / __/ __ `/ __ \/ / _ \   / _ \| |/_/ __/ ___/ __ `/ ___/ __/ __ \/ ___/
    / ____/ /_/ / __/    / /_/ /_/ / /_/ / /  __/  /  __/>  </ /_/ /  / /_/ / /__/ /_/ /_/ / /    
   /_/   /_____/_/       \__/\__,_/_.___/_/\___/   \___/_/|_|\__/_/   \__,_/\___/\__/\____/_/     
                                                                                               
        Nota! : Scanning Port es un escaner 100% funcional, verifique con nmap.       
    """
    for N, line in enumerate(x.split("\n")):
         sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
         time.sleep(0.05)
ClownLogo()
try:
	pdf_file = sys.argv[1]
except:
	print('[x] Error')

try:
    # PDF file to extract tables from
    file = pdf_file

    # extract all the tables in the PDF file
    tables = camelot.read_pdf(file)

    # number of tables extracted
    print("Total tables extracted:", tables.n)

    # print the first table as Pandas DataFrame
    print(tables[0].df)

    # export individually
    tables[0].to_csv("foo.csv")

    # or export all in a zip
    tables.export("foo.csv", f="csv", compress=True)

    # export to HTML
    tables.export("foo.html", f="html")
except:
	print('[-] PDF no encontrado')
