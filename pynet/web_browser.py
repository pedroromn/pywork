#! -*- coding: utf-8 -*-
# This program displays the contents of a file on a web browser


from Tkinter import *
import Pmw
import urllib
import urlparse


class WebBrowser( Frame ):
    "A simple web browser"

    def __init__(self):
        "Create the web browser GUI"
        Frame.__init__(self)
        Pmw.initialise()
        self.pack( expand=YES, fill=BOTH )
        self.master.title("Simple Web BRowser")
        self.master.geometry( "400x300" )

        self.address = Entry( self )
        self.address.pack( fill = X, padx = 5, pady = 5)
        self.address.bind( "<Return>", self.get_page )

        self.contents = Pmw.ScrolledText( self,
            text_state = DISABLED)
        self.contents.pack( expand = YES, fill = BOTH, padx = 5,
            pady = 5)
    
    def get_page(self, event):
        "Parse the URL, add addressing scheme and retrieve file"

        # Parse the URL 
        my_url = event.widget.get()
        components = urlparse.urlparse(my_url)
        self.contents.text_state = NORMAL

        # If addressing scheme not specified, use http
        if components[0] == "":
            my_url = "http://" + my_url
        
        # Connect and retrieve the file
        try:
             temp_file = urllib.urlopen(my_url)
             self.contents.settext(temp_file.read()) # show results
        except IOError:
            self.contents.settext("Error finding file")

        self.contents.text_state = DISABLED

def main():
    wbrowser = WebBrowser()
    wbrowser.mainloop()

if __name__ == "__main__":
    main()

