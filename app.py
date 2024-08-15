from flask import Flask, render_template,request
import mysql.connector as mc
import joblib


model = joblib.load("./models/linear_model.lb")
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')
 


@app.route("/predict", methods=['GET','POST']) 
def predict():
    if request.method=="POST":
        brand_name=int(request.form['brand_name'])
        Kms_Driven=int(request.form['Kms_Driven'])
        owner=int(request.form['owner'])
        age=int(request.form['age'])
        power=int(request.form['power'])
        brand_dict={'TVS': 1,
        'Royal Enfield': 2,'Triumph': 3,'Yamaha': 4,'Honda': 5,'Hero': 6,'Bajaj': 7,'Suzuki': 8,'Benelli': 9,'KTM': 10,'Mahindra': 11,'Kawasaki': 12,'Ducati': 13,'Hyosung': 14,'Harley-Davidson': 15,'Jawa': 16,'BMW': 17}
                
        brand_dict2 = {value: key for key, value in brand_dict.items()}
        
        UNSEEN_DATA = [[brand_name,Kms_Driven, owner, age, power ]]
        
        PREDICTION = model.predict(UNSEEN_DATA)[0][0]
        
        # MySQL INSERT statement using %s placeholders
        query_to_insert= """
        INSERT INTO bikeData (brand, kms_driven, owner, power, age, predicted_price) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        # Connect to MySQL database
        conn = mc.connect(
            host='localhost',
            user='root',
            password='somya2657',
            database='Bike',
            charset='utf8' 
        )
        cur = conn.cursor()
        
        data = (brand_dict2[brand_name], Kms_Driven,owner, power, age, int(round(PREDICTION, 2)))
        cur.execute(query_to_insert, data)
        conn.commit()
        
        print("Your record has been stored in the database")
        
        cur.close()
        conn.close()
        
        return render_template('home.html', prediction_text=str(round(PREDICTION, 2)))

if __name__ == "__main__":
    app.run(debug=True)