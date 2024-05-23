import os
from os.path import exists
import tkinter as tk
from tkinter import filedialog
import PIL
from PIL import Image

def create_file(path:str):
    if exists(path):
        print("Error: File already exists")
    else:
        file = open(path, 'w')
        file.close()
        print("file created")



def create_header(path:str):
    if( exists(path)):
        file = open(path, 'w')
        file.write("""
            <!DOCTYPE html>
            <html lang="de">
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <title>Galerie</title>
                    <link rel="stylesheet" href="../../style/main.css">
                    <link rel="stylesheet" href="../../style/gallery_page.css">
                    <link rel="icon" type="image/x-icon" href="../../img/logoMBC.png">

                </head>
                <body id="body">

                    <div class="topnav" id="myTopnav">
                        <img src="../../img/logoMBC.png" alt="logoMBC" class="logo">
                        <a href="../index.html" class="hover-underline-animation">Home</a>
                        <a href="../anmeldung.html" class="hover-underline-animation">Anmeldung</a>
                        <div class="dropdown">
                            <button class="dropbtn hover-underline-animation" onclick="window.location.href='../about.html'">Über uns 
                            </button>
                            <div class="dropdown-content">
                                <a href="../flugzeiten.html">Flugzeiten</a>
                                <a href="../webcam.html">Webcam</a>
                                <a href="../flugplatzordnung.html">Flugplatzordnung</a>
                                <a href="../betrieb.html">Betrieb</a>
                                <a href="../laermessung.html">Lärmmessung</a>
                            </div>
                        </div> 
                        <a href="../neuigkeiten.html" class="hover-underline-animation">Neuigkeiten</a>
                        <a href="../gallerie.html" class="hover-underline-animation">Galerie</a>
                        <a href="../kontakt.html" class="hover-underline-animation">Kontakt</a>

                        <a href="javascript:void(0);" class="icon" onclick="responsiveTopnav()">&#9776;</a>
                    </div>
            \n""")
        file.close()
        print("header created")
    else:
        print("Error: file does not exist")

def create_desc(path:str):
    if( exists(path)):
        file = open(path, 'a')
        file.write("""
            <div class="content1">
            <!-- Titel der Gallerie -->
            <h1>Title</h1>
            <!-- kurze Beschreibung -->
            <p>descline 1</p>
            <p>descline 2</p>
        </div>
            \n""")
        file.close()
        print("desc created")
    else:
        print("Error: file does not exist")


def create_footer(path:str):
    if( exists(path)):
        file = open(path, 'a')
        file.write("""
            <div id="overlay" onclick="closeImageViewer()"></div>
            <div id="imageViewer">
                <img id="imageViewedImg" />
            </div>

            <footer>
                <p class="footerHeader">Infos</p>
                <address>Addresse : Modellbauclub Erlauftal, Moos 4, 3250 Wieselburg. </address>
                <p class="footerContact">Obmann Telefon: +43 664 3359101 <br> Email: office@mbc-erlauftal.at <br> ZVR: 382620803</p>

                <p class="footerBottom">Der MBC ist auch Betreiber der Website www.mbc-erlauftal.at</p>  

            </footer>


            <script src="../../script/main.js">

            </script>
        </body>

        <script src="../../script/gallery_page.js">    </script>
</html>
            """)
        file.close()
        print("footer created")

    else:
        print("Error: file does not exist")

def create_gallery(img_path:str, path:str):
    if(exists(img_path) & exists(path)):
        img_paths = []
        for filename in os.listdir(img_path):
            #filepath = os.path.join(img_path, filename).replace("\\", "/")
            #filepath = os.path.relpath(os.path.join(img_path, filename).replace("\\", "/"), path)
            filepath = "../../../" + os.path.basename(os.path.dirname(img_path)) + "/" + os.path.basename(img_path) + "/" + filename
            img_paths.append(filepath)
        
        content = """
        <div class="content2">
"""

        i = 0
        j = 0
        length = len(img_paths)
        length -= 1
        while (i < length):
            content += """            <div class="imgRow">\n"""
            while(j < 4 and i < length):
                content += """                <div class="imgDiv box"><img src=""" + '"'   + img_paths[i] + '"' + """ class="gallery-image" /></div>\n"""
                j+=1
                i+=1

            content += """            </div>\n"""
            j = 0
        content += """        </div>"""
        file = open(path, 'a')
        file.write(content)
        print("gallery created")
    else:
        print("files not existing")

def optimize_images(path, quality):
    image_names = []
    for filename in os.listdir(path):
    #Check if file is iamge (.jpg, .png , ...)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            #Add to array
            image_names.append(path + "/" + filename)
    for image in image_names:
        img = Image.open(image)
        #Resize and compress image
        img = img.resize(img.size, PIL.Image.Resampling.LANCZOS)
        #Replace old image with optimization and lower quality
        img.save(image, optimize=True, quality=quality)


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    #path = filedialog.askdirectory()
    path = "D:\Webentwicklung\mbc-website\html\gallery_pages"
    print('Dateiname: ')
    filename = input()
    filepath = path + '/' + filename + '.html'
    create_file(filepath)
    create_header(filepath)
    create_desc(filepath)
    root = tk.Tk()
    root.withdraw()
    imgs_path = filedialog.askdirectory()
    print("Want to optimize images (Y/n)?")
    result = input()
    if result == "Y" or result == "y":
        optimize_images(imgs_path, 85)
    create_gallery(imgs_path, filepath)
    create_footer(filepath)

    

