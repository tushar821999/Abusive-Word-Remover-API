from flask import *
import urllib.request as req


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/Documentation')
def documen():
    return render_template("documentation.html")

@app.route('/Aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route("/filtered",methods=["GET"])
def filtered():
        paragraph = request.args.get('inputpara')
        paragraph = paragraph.replace(" ","%20")
        print(paragraph)
        words = paragraph.split("%20")
        result = []
        awlist = ["idiot","Idiot","IDIOT","whore","Whore","WHORE","fuck","Fuck","FUCK","suck","Suck","SUCK","hoe","Hoe","HOE","piss","Piss","PISS","penis","Penis","PENIS","dick","Dick","DICK","cock","Cock","COCK","pussy","Pussy","PUSSY","sex","Sex","SEX","sexy","Sexy","SEXY","bastard","Bastard","BASTARD","bitch","Bitch","BITCH","gay","Gay","GAY","transsexual","Transsexual","TRANSSEXUAL","ass","Ass","ASS","milf","Milf","MILF","vaginal","Vaginal","VAGINAL","vagina","Vagina","VAGINA","boobs","Boobs","BOOBS","tits","Tits","TITS","fucker","Fucker","FUCKER","sucker","Sucker","SUCKER","pervert","Pervert","PERVERT"]
        for i in words:
            conn = req.urlopen("https://wdylike.appspot.com/?q="+i)
            if conn.read().decode("utf-8") == "false" and i not in awlist:
                result.append(i)
            else:
                str = ""
                for i in range(len(i)):
                    str = str + "*"
                result.append(str)
        filtered_text = ' '.join(result)
        json_result = {"message":filtered_text}
        resp = jsonify(json_result)
        return resp
    #    return render_template("Output.html",paragraph=filtered_text)

if __name__ =='__main__':
    app.run(host = "0.0.0.0",port=8080,debug=False)
