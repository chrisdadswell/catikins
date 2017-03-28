#CATIKINS Flask based app
#V1.0 - 16/03/2017

import io,os,time
from flask import Flask, send_file, jsonify
from PIL import Image, ImageFont, ImageDraw
###############################################
#We would never hard code values in a real app!

CAT_FILE="happy.gif"

###############################################

app = Flask(__name__)
app.config["CAT_NAME"]="No-Name"
app.config["CAT_COLOUR"]=(0,0,255,128)
app.config.from_pyfile('settings.cfg')

port=int(os.getenv("PORT",5002))

@app.after_request
def add_header(response):
  response.headers['Cache-Control'] = 'no-store'
  return response



@app.route("/")
def hello():
  return "Hello World!"



@app.route("/cat")
def cat():
  return send_file(CAT_FILE, mimetype='image/gif')



@app.route("/catinfo")
def catinfo():
  im=Image.open(CAT_FILE)
  (fmode,fino,fdev,fnlink,fuid,fgid,fsize,fatime,fmtime,fctime)=os.stat(CAT_FILE)
  mode=im.mode
  width=im.width
  height=im.height
  catname=app.config["CAT_NAME"]
  now=time.strftime("%c")
  infoset={"width":width,"height":height,"mode":mode,"bytes":fsize,"name":catname,"timedate":now}
  return jsonify(infoset)


@app.route("/colourcat")
def colourcat():
  im=Image.open(CAT_FILE).convert('RGBA')
  cat_colour=app.config["CAT_COLOUR"]
  catname=app.config["CAT_NAME"]
  width=im.width
  height=im.height

  #overlay=Image.new('RGBA',im.size,(255,0,0,128))
  overlay=Image.new('RGBA',im.size,cat_colour)
  out=Image.alpha_composite(im,overlay)
  font=ImageFont.truetype('./fonts/spleen_machine.ttf', 32)
  draw = ImageDraw.Draw(out)
  w, h = draw.textsize(catname,font=font)
  draw.text(((width-w)/2,(height-h)/2),catname,(0,0,0),font=font) 
  bytes=io.BytesIO()
  out.rotate(10).save(bytes,format='PNG')
  bytes.seek(0)
  return send_file(bytes,mimetype='image/png')



if __name__ == "__main__":
  app.run(host='0.0.0.0',port=port)

