from io import BytesIO
import base64
import fitz  # PyMuPDF
from fastapi import FastAPI, Form

app = FastAPI()


@app.get("/")
def read_root():
    return { "Hello": "run World" }

@app.post("/convert_pdf_toImage_by_pages")
async def convert_pdf_and_upload(pdf_base64: str = Form(...)):
    try:
        # Convertir base64 a bytes
        pdf_bytes = base64.b64decode(pdf_base64)

        # Abrir el archivo PDF usando PyMuPDF
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")

        images_base64 = []

        # Configurar la escala para mejorar la calidad (aumenta la resolución)
        zoom_x = 2.0  # Escala horizontal (2.0 = 200%)
        zoom_y = 2.0  # Escala vertical (2.0 = 200%)
        matrix = fitz.Matrix(zoom_x, zoom_y)

        # Convertir cada página a imagen PNG
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap(matrix=matrix)

            # Convertir a PNG en base64
            buffered = BytesIO()
            buffered.write(pix.tobytes(output="png"))
            img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
            images_base64.append(img_base64)

        return {
            "images_base64": images_base64
        }

    except Exception as e:
        return {"error": str(e)}
