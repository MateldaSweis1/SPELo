from flask import Flask, request, render_template
import finalspell
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
    if request.method=="GET":
        return render_template('index.html',text = '')
    else:
        user_input = request.form["ogtext"]
        trans_input = finalspell.main(user_input)
        punc = ".,:;!?"
        final_string=""
        for word in trans_input:
            if word in punc:
                final_string+=word
            else:
                final_string+=(" "+word)
        return render_template('index.html',text = final_string)


if __name__ == "__main__":
    app.run(debug=True)
