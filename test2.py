import io,base64
from flask import Flask, send_file
from PIL import Image

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/cat")
def cat():
  return send_file('cat1.gif', mimetype='image/gif')

@app.route("/colourcat")
def colourcat():
  im=Image.open("cat1.gif").convert('RGBA')
  width=im.width
  height=im.height
  
  overlay=Image.new('RGBA',im.size,(255,0,0,128))
  out=Image.alpha_composite(im,overlay)

  out.rotate(45).save('cat2.gif')
  return send_file('cat2.gif', mimetype='image/gif')

@app.route("/colourcat2")
def colourcat2():
  im=Image.open("cat1.gif").convert('RGBA')
  
  overlay=Image.new('RGBA',im.size,(255,0,0,128))
  out=Image.alpha_composite(im,overlay)

  out.rotate(45)
   
  bytes=io.BytesIO()
  out.save(bytes,format='PNG')
  bytes.seek(0) 
  return send_file(bytes,mimetype='image/png')
#  return '<html><body><src="data:image/png;base64,'+base64.b64encode(outdata)+'" /></body></html>'

if __name__ == "__main__":
  app.run()

