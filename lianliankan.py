# coding=utf-8
import os
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


from flask import Flask, request, render_template,  g,flash
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
    # sql = 'select * from Store limit 15;'
    # exe(sql)
    cur = g.db.execute("select aid,pic,name,price,basicPro,skill from store limit 15")
    desDics = [dict(aid="aid_{aid}".format(aid=row[0]), pic=row[1],des=u"名称:{name};价格:{price};{basicPro};{skill}".format(name=row[2],price=row[3],basicPro=row[4],skill=row[5])) for row in cur.fetchall()]
    print desDics
    # desDics = [
    #     {"aid": "aid_infoId01","pic":"haha" ,"des":  u"\u540d\u79f0:\u7834\u519b;\u4ef7\u683c:2950;\u7269\u7406\u653b\u51fb\uff1a200\u70b9;\u552f\u4e00\u88ab\u52a8 \u7834\u519b\uff1a\u76ee\u6807\u751f\u547d\u4f4e\u4e8e50%\u65f6\u4f24\u5bb3\u63d0\u9ad830%"},
    #     {"aid": "aid_infoId02","pic":"http://img.bugu.18183.com/db_18183/static/wzry/static/images/equips/28.png", "des": u"这把宝剑效果超群了多久啊是发链接啊;螺丝钉解放邻居阿叔到了;飞机;垃圾收到了;放假啊老师;都放假啦就是;了都放假啦;就是的;来房间看;啊就是对方了解啊螺丝钉解放;啊就是的;"},
    #     {"aid": "aid_infoId03","pic":"pic2", "des": u"这把宝剑效果超群了多久啊是发链接啊;螺丝钉解放邻居阿叔到了;飞机;垃圾收到了;放假啊老师;都放假啦就是;了都放假啦;就是的;来房间看;啊就是对方了解啊螺丝钉解放;啊就是的;"},
    #     {"aid": "aid_infoId04","pic":"pic2", "des": u"这把宝剑效果超群了多久啊是发链接啊;螺丝钉解放邻居阿叔到了;飞机;垃圾收到了;放假啊老师;都放假啦就是;了都放假啦;就是的;来房间看;啊就是对方了解啊螺丝钉解放;啊就是的;"},
    #     {"aid": "aid_infoId05","pic":"pic2", "des": u"这把宝剑效果超群了多久啊是发链接啊;螺丝钉解放邻居阿叔到了;飞机;垃圾收到了;放假啊老师;都放假啦就是;了都放假啦;就是的;来房间看;啊就是对方了解啊螺丝钉解放;啊就是的;"},
    #           {'aid': 'aid_infoId120', 'des': u'\u540d\u79f0:\u7834\u519b;\u4ef7\u683c:2950;\u7269\u7406\u653b\u51fb\uff1a200\u70b9;\u552f\u4e00\u88ab\u52a8 \u7834\u519b\uff1a\u76ee\u6807\u751f\u547d\u4f4e\u4e8e50%\u65f6\u4f24\u5bb3\u63d0\u9ad830%', 'pic': u'http://img.bugu.18183.com/db_18183/static/wzry/static/images/equips/30.png'},
    #
    #
    #
    # ]


    return render_template('demo.html', deses=desDics)


if __name__ == '__main__':
    app.run(debug=True)
