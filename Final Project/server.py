import http.server
import socketserver
import termcolor
import colorama
from urllib.parse import urlparse, parse_qs
import server_utils as su

# Define the Server's port
PORT = 8080

LIST_SPECIES = ['Human', 'Cat', 'Mouse','Clown Anemonefish','Blue Whale','Gorilla','Great Tit','Channel Catfish','Eurasian Red Squirrel', 'Zebrafish']
DICT_GENES = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "SMIM36": "ENSG00000261873",
    "DACH1": "ENSGGOG00000004058",
    "GLS": "ENSBMSG00010000717",
    "SURF6": "ENSPMJG00000006670",
    "oafa": "ENSIPUG00000011673",
    "ANKAR": "ENSSVLG00005000904"
}
#SMIM36 chr 17 human; 13 gorilla, blue whale, great tit, channel catfish, eu red squirrel
socketserver.TCPServer.allow_reuse_address = True


#def read_html_file(filename):
#    return Path(filename).read_text()




# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        global contents
        colorama.init(strip="False")
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print('Resource request: ', path_name)
        print('Parameters: ', arguments)

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok
        # Message to send back to the client
        context = {}
        if path_name == "/":
            context['n_species'] = len(LIST_SPECIES)
            context['list_species'] = LIST_SPECIES
            contents = su.read_template_html_file('HTML/index.html').render(context=context)
        elif path_name == '/ping':
            contents = su.read_template_html_file('HTML/ping.HTML').render()
        elif path_name == '/list':
            list_number = arguments['list'][0]
            contents = su.list(list_number, LIST_SPECIES)
        elif path_name == '/karyotype':
            specie = arguments['karyotype'][0]
            contents = su.karyotype(specie, LIST_SPECIES)
        elif path_name == '/length':
            election = arguments['election'][0]
            info = arguments['msg'][0]
            contents = su.length(election, info, LIST_SPECIES)

        else:
            contents = su.read_template_html_file('./HTML/ERROR.html').render()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!
        #length = len(contents.encode())
        # Define the content-type header:
        self.send_header('Content-Type', 'text/HTML')
        self.send_header('Content-Length', str(len(contents.encode())))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
