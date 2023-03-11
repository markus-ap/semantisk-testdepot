from pylode import OntDoc
import os

def lag():
    mappe = os.getcwd()
    
    os.chdir("..")
    if not os.path.exists("doc"):
        os.mkdir("doc") 

    for fil in os.listdir(mappe):
        if fil.endswith(".ttl"):
            filsti = f"{mappe}/{fil}"
            od = OntDoc(ontology=filsti)
            
            html_filnamn = f"doc\{fil.replace('.ttl', '.html')}"
            od.make_html(html_filnamn)

if __name__ == "__main__":
    lag()