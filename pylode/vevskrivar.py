from pylode import OntDoc
import shutil, os

def lag():
    mappe = os.getcwd()
    os.mkdir("html")
    for fil in os.listdir(os.getcwd()):
        if fil.endswith(".ttl"):
            filsti = f"{mappe}\{fil}"
            od = OntDoc(ontology=filsti)
            
            html_filnamn = f"html/{fil.replace('.ttl', '.html')}"
            od.make_html(html_filnamn)

if __name__ == "__main__":
    lag()