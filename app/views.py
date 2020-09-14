from flask import Flask
from flask import render_template
from app.main import PhotoBooth

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/TakePhoto',methods=['GET','POST'])
def takePhoto():
    photoBooth = PhotoBooth()
    photoBooth.run_photo_booth()
    return photoBooth.collage_filename



@app.route('/PrintPhoto',methods=['GET'])
def printPhoto():
    print("Printing photo {0}".format("TODO: Some collage photo"))
    # TODO: Print existing photo

    return "Printing photo..."




if __name__=='__main__':
    app.run(debug=True)
