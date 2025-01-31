from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# CSV fájl beolvasása
def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df

# Globális változó a CSV adatok tárolására
data = []

@app.route("/")
def index():
    global data  # Itt globálisan hivatkozunk a data változóra
    file_path = "onkonyes_mervado_podcast_with_summaries.csv"  # A fájl neve itt
    data = read_csv(file_path)
    
    # Az adatok listába konvertálása
    data_list = data.to_dict(orient="records")
    
    return render_template("index.html", data=data_list)


@app.route('/full-summary/<int:index>')
def full_summary(index):
    global data  # Globálisan hivatkozunk a data változóra
    podcast = data.iloc[index - 1]  # A pandas DataFrame megfelelő sorát választjuk
    return render_template('full-summary.html', title=podcast['Cím'], full_summary=podcast['Összefoglaló'])


if __name__ == "__main__":
    app.run(debug=True)
