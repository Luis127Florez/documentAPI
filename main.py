from typing import Union
from io import BytesIO
import base64
from html2image import Html2Image
from pdf2image import convert_from_bytes
from fastapi import FastAPI, Form

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World xasx"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/pdfToPng")
def changeFile(fileBase64: str = Form(...)):
    try:
        # Decodificar el PDF base64 recibido
        pdf_bytes = base64.b64decode(fileBase64)
        print(pdf_bytes, '┗( (๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧')
        print('┗( (๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧')
        print('┗( (๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧')
        print('┗( (๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧')
        print('┗( (๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧')
        print('┗( (๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧')
        
        
        # Convertir PDF a imágenes (puede haber varias páginas)
        images = convert_from_bytes(open('./documentp.pdf',"rb").read())
        
        print(images, '┗( T﹏T )┛┗( T﹏T )┛(￣﹏￣；)')
        print('┗( T﹏T )┛┗( T﹏T )┛(￣﹏￣；)')
        print('┗( T﹏T )┛┗( T﹏T )┛(￣﹏￣；)')
        print('┗( T﹏T )┛┗( T﹏T )┛(￣﹏￣；)')
        print('┗( T﹏T )┛┗( T﹏T )┛(￣﹏￣；)')
        print('┗( T﹏T )┛┗( T﹏T )┛(￣﹏￣；)')

        # Convertir la primera página a PNG y a base64
        img_buffer = BytesIO()
        images[0].save(img_buffer, format='PNG')
        img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        # Devolver la imagen en formato base64
        return {"file": img_base64}

    except Exception as e:
        return {"error": str(e)}
   
 
@app.post("/htmlToPng")  
def changeHTML(codeHTML: str):
    try:
        hti = Html2Image()
        # Decodificar el PDF base64 recibido
        
        html = codeHTML
        
        css = """
        body { background: white; margin: 0; padding: 20px; }
        p { font-size: 32px; line-height: 1.6; text-align: justify; }
        h1 { font-size: 44px; text-align: center; }
        """
        
        img = hti.screenshot(html_str=html, css_str=css, save_as='asd.png', size=(2480, 3508))
        
        print(img, '┗( (๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧')
        print('┗( (๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧')
        print('┗( (๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧')
        print('┗( (๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧')
        print('┗( (๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧')
        print('┗( (๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧(๑•̀ㅂ•́)و✧')
        
    
        # Devolver la imagen en formato base64
        return {"file": img}

    except Exception as e:
        return {"error": str(e)}