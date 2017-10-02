# coding=utf-8
import os
import sqlite3
import sys
from copy import deepcopy
reload(sys)
sys.setdefaultencoding( "utf-8" )


from flask import Flask, request, render_template,  g,flash,redirect,url_for
import random
parpath = os.path.dirname(__file__)
app = Flask(__name__)
app.config.from_object("appConfig.DevelopmentConfig")

# 初始函数
def connect_db():
    return sqlite3.connect(os.path.join(parpath,'mock.db'))
app = Flask(__name__)
@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()
@app.before_request
def before_request():
    print request.full_path
    g.db = connect_db()

def get_connection():
    db = getattr(g, '_db', None)
    if db is None:
        db = g._db = connect_db()
    return db


def init_db():
    with app.app_context():
        db = get_connection()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def exe(sql):
    with app.app_context():
        db = get_connection()
        db.cursor().execute(sql)
        db.commit()



@app.route('/')
def lianliankan():
    return redirect(url_for('lianliankanWithPostId',post_id=15))

@app.route('/<post_id>')
def lianliankanWithPostId(post_id):
    cur = g.db.execute("select aid,pic,name,price,basicPro,skill from store ORDER BY random() LIMIT {post_id};".format(post_id=post_id))
    desDics = [dict(aid="aid_{aid}".format(aid=row[0]), pic=row[1],des=u"名称:{name};价格:{price};{basicPro};{skill}".format(name=row[2],price=row[3],basicPro=row[4],skill=row[5])) for row in cur.fetchall()]
    shuffleDeses = deepcopy(desDics)
    random.shuffle(shuffleDeses)
    # print shuffleDeses
    # print desDics
    return render_template('demo.html', deses=desDics,shuffleDeses=shuffleDeses,count=post_id)

if __name__ == '__main__':
    app.run(debug=True)
