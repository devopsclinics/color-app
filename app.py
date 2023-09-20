


# from flask import Flask, render_template_string
# import os

# app = Flask(__name__)

# @app.route('/')
# @app.route('/<color>')
# def hello_world(color=None):
#     try:
#         if color is None:
#             color = os.getenv('COLOR', 'red')

#         return render_template_string('''
#         <html>
#         <head>
#             <style>
#                 .moving-text {
#                     font-size: 48px;
#                     text-align: center;
#                     position: absolute;
#                     animation: move-animation 5s linear infinite;
#                 }

#                 @keyframes move-animation {
#                     0%   { top: 0; left: 0; }
#                     25%  { top: 0; right: 0; }
#                     50%  { bottom: 0; right: 0; }
#                     75%  { bottom: 0; left: 0; }
#                     100% { top: 0; left: 0; }
#                 }
#             </style>
#         </head>
#         <body style="background-color:{{color}}">
#             <div class="moving-text">Happy Learning With DevopClinics!!!</div>
#         </body>
#         </html>
#         ''', color=color)

#     except Exception as e:
#         print(e)
#         return str(e), 500

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)


from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
@app.route('/<color>')
def display_pattern(color=None):
    try:
        # Set default color if none provided.
        if color is None:
            color = os.getenv('COLOR', 'red')

        # CSS for the pattern display.
        pattern_style = """
        <style>
            .moving-text {
                font-size: 48px;
                text-align: center;
                position: absolute;
                animation: move-animation 5s linear infinite;
            }

            @keyframes move-animation {
                0%   { top: 0; left: 0; }
                25%  { top: 0; right: 0; }
                50%  { bottom: 0; right: 0; }
                75%  { bottom: 0; left: 0; }
                100% { top: 0; left: 0; }
            }
        </style>
        """

        # HTML to render.
        html_content = f"""
        <html>
            <head>
                {pattern_style}
            </head>
            <body style="background-color:{color}">
                <div class="moving-text">Happy Learning With DevopClinics!!!</div>
            </body>
        </html>
        """

        return render_template_string(html_content)

    # Catch and display errors.
    except Exception as e:
        print(e)
        return str(e), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
