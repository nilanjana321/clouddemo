from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def nilanjana():  
    return "<h1>We are learning cloud deployment</h1>";  
  
if __name__ =='__main__':  
    app.run()  



