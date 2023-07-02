# from flask import Flask, render_template_string
# import os

# app = Flask(__name__)

# @app.route('/')
# @app.route('/<color>')
# def hello_world(color=None):
#     try:
#         if color is None:
#             color = os.getenv('COLOR', 'red')
#         return render_template_string('<body style="background-color:{}">Welcome to DevopClinics World!</body>'.format(color))
#     except Exception as e:
#         print(e)
#         return str(e), 500

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)


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
#                 .bounce {
#                     animation: bounce-animation 1.5s infinite;
#                     font-size: 24px;
#                     text-align: center;
#                 }

#                 @keyframes bounce-animation {
#                     0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
#                     40% {transform: translateY(-30px);}
#                     60% {transform: translateY(-15px);}
#                 }
#             </style>
#         </head>
#         <body style="background-color:{{color}}">
#             <div class="bounce">Dancing DevOps!</div>
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
def hello_world(color=None):
    try:
        if color is None:
            color = os.getenv('COLOR', 'red')

        return render_template_string('''
        <html>
        <head>
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
        </head>
        <body style="background-color:{{color}}">
            <div class="moving-text">Happy Learning With DevopClinics!!!</div>
        </body>
        </html>
        ''', color=color)

    except Exception as e:
        print(e)
        return str(e), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

    