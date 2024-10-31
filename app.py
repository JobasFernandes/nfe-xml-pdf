import os
from pdf_docs import Danfe
from tqdm import tqdm
import warnings

def printpdf(fullpath, filename, destfolder):

    with open(fullpath, "r", encoding="utf8") as f:
        xml_content = f.read()

    try:
        pdf = Danfe(xmls=[xml_content], image=None, cfg_layout="ICMS_IPI", receipt_pos="top")
    except Exception as e:
        print(f"Error processing file {fullpath}: {e}")
        return

    pdf_filename = os.path.splitext(filename)[0] + '.pdf'
    pdf_fullpath = os.path.join(destfolder, pdf_filename)

    dest_dir = os.path.dirname(pdf_fullpath)
    os.makedirs(dest_dir, exist_ok=True)

    pdf.output(pdf_fullpath)

def ler_paths_xml(pasta):
    arquivos_xml = []
    for dirpath, dirnames, filenames in os.walk(pasta):
        for filename in filenames:
            if filename.endswith(".xml"):
                filepath = os.path.join(dirpath, filename)
                relpath = os.path.relpath(filepath, pasta)
                arquivos_xml.append(relpath)
    return arquivos_xml

if __name__ == "__main__":
    warnings.simplefilter("ignore")
    pastaXML = "XML/"
    paths_xml = ler_paths_xml(pastaXML)
    PastaPDF = "PDF/"

    for path_xml in tqdm(paths_xml, desc="Imprimindo XML to PDF", unit="file"):
        fullpath = os.path.join(pastaXML, path_xml)
        printpdf(fullpath, path_xml, PastaPDF)