#! /usr/bin/env python

import codecs
import sys
import requests
from bs4 import BeautifulSoup
import re

sys.stdout = codecs.getwriter('utf_8')(sys.stdout.detach())
print('Content-type: text/html; charset=UTF-8')

# Webページを取得して解析する
theme = "自然"
load_url = "https://colorpea.com/photo-nature"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# classで検索し、その中のすべてのaタグを検索して表示する
# ファイルを書き込みモードで開く
background = []
comment = []

for element in soup.find_all(class_="image-list__picture lazyload"):
    image = element.get("data-bgset")
    text = element.text
    #f.write(url+"\n")
    #print(url)
    background.append(image)
    comment.append(text)



# ヤフーニュースのトップページ情報を取得する
URL = "https://www.yahoo.co.jp/"
rest = requests.get(URL)
news = []

# BeautifulSoupにヤフーニュースのページ内容を読み込ませる
soup = BeautifulSoup(rest.text, "html.parser")

# ヤフーニュースの見出しとURLの情報を取得して出力する
data_list = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
for data in data_list:
    print(data.span.string)
    print(data.attrs["href"])
    string = {}
    string["str"] = data.span.string
    string["url"] = data.attrs["href"]
    news.append(string)


print('''
<!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="utf-8">
        <title>Book Search</title>

        <head>
            <title>Book Search</title>

            <style type="text/css">
vegas-overlay,.vegas-slide,.vegas-slide-inner,.vegas-timer,.vegas-wrapper{
    position:absolute;
    top:0;
    left:0;
    bottom:0;
    right:0;
    overflow:hidden;
    border:none;
    padding:0;
    margin:0
}
    
.vegas-overlay{
    opacity:.5;
    background:url(overlays/02.png) center center
}

.vegas-timer{
    top:auto;
    bottom:0;
    height:2px
}

.vegas-timer-progress{
    width:0;
    height:100%;
    background:#fff;
    transition:width ease-out
}

.vegas-timer-running .vegas-timer-progress{
    width:100%
}

.vegas-slide,.vegas-slide-inner{
    margin:0;
    padding:0;
    background:center center no-repeat;
    -webkit-transform:translateZ(0);
    transform:translateZ(0);
    will-change:transform,opacity
}

body .vegas-container{
    overflow:hidden!important;
    position:relative
}

.vegas-video{
    min-width:100%;
    min-height:100%;
    width:auto;
    height:auto
}

body.vegas-container{
    overflow:auto;
    position:static;
    z-index:-2;
    margin: 0;
}

body.vegas-container>.vegas-overlay,body.vegas-container>.vegas-slide,body.vegas-container>.vegas-timer{
    position:fixed;
    z-index:-1
}

.vegas-transition-blur,.vegas-transition-blur2{
    opacity:0;
    -webkit-filter:blur(32px) brightness(1.01);
    filter:blur(32px) brightness(1.01)
}

.vegas-transition-blur-in,.vegas-transition-blur2-in{
    opacity:1;
    -webkit-filter:blur(0) brightness(1.01);
    filter:blur(0) brightness(1.01)
}

.vegas-transition-blur2-out{
    opacity:0
}

.vegas-transition-burn,.vegas-transition-burn2{
    opacity:0;
    -webkit-filter:contrast(1000%) saturate(1000%);
    filter:contrast(1000%) saturate(1000%)
}

.vegas-transition-burn-in,.vegas-transition-burn2-in{
    opacity:1;
    -webkit-filter:contrast(100%) saturate(100%);
    filter:contrast(100%) saturate(100%)
}

.vegas-transition-burn2-out{
    opacity:0;
    -webkit-filter:contrast(1000%) saturate(1000%);
    filter:contrast(1000%) saturate(1000%)
}

.vegas-transition-fade,.vegas-transition-fade2{
    opacity:0
}

.vegas-transition-fade-in,.vegas-transition-fade2-in{
    opacity:1
}

.vegas-transition-fade2-out{
    opacity:0
}

.vegas-transition-flash,.vegas-transition-flash2{
    opacity:0;
    -webkit-filter:brightness(25);
    filter:brightness(25)
}

.vegas-transition-flash-in,.vegas-transition-flash2-in{
    opacity:1;
    -webkit-filter:brightness(1);
    filter:brightness(1)
}

.vegas-transition-flash2-out{
    opacity:0;
    -webkit-filter:brightness(25);
    filter:brightness(25)
}

.vegas-transition-negative,.vegas-transition-negative2{
    opacity:0;
    -webkit-filter:invert(100%);
    filter:invert(100%)
}

.vegas-transition-negative-in,.vegas-transition-negative2-in{
    opacity:1;
    -webkit-filter:invert(0);
    filter:invert(0)
}

.vegas-transition-negative2-out{
    opacity:0;-webkit-filter:invert(100%);filter:invert(100%)
}

.vegas-transition-slideDown,.vegas-transition-slideDown2{
    -webkit-transform:translateY(-100%);transform:translateY(-100%)
}

.vegas-transition-slideDown-in,.vegas-transition-slideDown2-in{
    -webkit-transform:translateY(0);transform:translateY(0)
}

.vegas-transition-slideDown2-out{
    -webkit-transform:translateY(100%);transform:translateY(100%)
}

.vegas-transition-slideLeft,.vegas-transition-slideLeft2{
    -webkit-transform:translateX(100%);transform:translateX(100%)
}

.vegas-transition-slideLeft-in,.vegas-transition-slideLeft2-in{
    -webkit-transform:translateX(0);transform:translateX(0)
}

.vegas-transition-slideLeft2-out,.vegas-transition-slideRight,.vegas-transition-slideRight2{
    -webkit-transform:translateX(-100%);transform:translateX(-100%)
}

.vegas-transition-slideRight-in,.vegas-transition-slideRight2-in{
    -webkit-transform:translateX(0);transform:translateX(0)
}

.vegas-transition-slideRight2-out{
    -webkit-transform:translateX(100%);transform:translateX(100%)
}

.vegas-transition-slideUp,.vegas-transition-slideUp2{
    -webkit-transform:translateY(100%);transform:translateY(100%)
}

.vegas-transition-slideUp-in,.vegas-transition-slideUp2-in{
    -webkit-transform:translateY(0);transform:translateY(0)
}

.vegas-transition-slideUp2-out{
    -webkit-transform:translateY(-100%);transform:translateY(-100%)
}

.vegas-transition-swirlLeft,.vegas-transition-swirlLeft2{
    -webkit-transform:scale(2) rotate(35deg);transform:scale(2) rotate(35deg);opacity:0
}

.vegas-transition-swirlLeft-in,.vegas-transition-swirlLeft2-in{
    -webkit-transform:scale(1) rotate(0);transform:scale(1) rotate(0);opacity:1
}

.vegas-transition-swirlLeft2-out,.vegas-transition-swirlRight,.vegas-transition-swirlRight2{
    -webkit-transform:scale(2) rotate(-35deg);transform:scale(2) rotate(-35deg);opacity:0
}

.vegas-transition-swirlRight-in,.vegas-transition-swirlRight2-in{
    -webkit-transform:scale(1) rotate(0);transform:scale(1) rotate(0);opacity:1
}

.vegas-transition-swirlRight2-out{
    -webkit-transform:scale(2) rotate(35deg);transform:scale(2) rotate(35deg);opacity:0
}

.vegas-transition-zoomIn,.vegas-transition-zoomIn2{
    -webkit-transform:scale(0);transform:scale(0);opacity:0
}

.vegas-transition-zoomIn-in,.vegas-transition-zoomIn2-in{
    -webkit-transform:scale(1);transform:scale(1);opacity:1
}

.vegas-transition-zoomIn2-out,.vegas-transition-zoomOut,.vegas-transition-zoomOut2{
    -webkit-transform:scale(2);transform:scale(2);opacity:0
}

.vegas-transition-zoomOut-in,.vegas-transition-zoomOut2-in{
    -webkit-transform:scale(1);transform:scale(1);opacity:1
}

.vegas-transition-zoomOut2-out{
    -webkit-transform:scale(0);transform:scale(0);opacity:0
}

.vegas-animation-kenburns{
    -webkit-animation:kenburns ease-out;animation:kenburns ease-out
}

@-webkit-keyframes kenburns{
    0%{
        -webkit-transform:scale(1.5);transform:scale(1.5)
    }
    100%{
        -webkit-transform:scale(1);transform:scale(1)
    }
}

@keyframes kenburns{
    0%{
        -webkit-transform:scale(1.5);transform:scale(1.5)
    }
    100%{
        -webkit-transform:scale(1);transform:scale(1)
    }
}

.vegas-animation-kenburnsDownLeft{
    -webkit-animation:kenburnsDownLeft ease-out;animation:kenburnsDownLeft ease-out
}

@-webkit-keyframes kenburnsDownLeft{
    0%{
        -webkit-transform:scale(1.5) translate(10%,-10%);transform:scale(1.5) translate(10%,-10%)
    }
    100%{
        -webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)
    }
}

@keyframes kenburnsDownLeft{
    0%{
        -webkit-transform:scale(1.5) translate(10%,-10%);transform:scale(1.5) translate(10%,-10%)
    }
    100%{
        -webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)
    }
}

.vegas-animation-kenburnsDownRight{
    -webkit-animation:kenburnsDownRight ease-out;animation:kenburnsDownRight ease-out
}

@-webkit-keyframes kenburnsDownRight{
    0%{
        -webkit-transform:scale(1.5) translate(-10%,-10%);transform:scale(1.5) translate(-10%,-10%)
    }
    100%{
        -webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)
    }
}

@keyframes kenburnsDownRight{
    0%{
        -webkit-transform:scale(1.5) translate(-10%,-10%);transform:scale(1.5) translate(-10%,-10%)
    }
    100%{
        -webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)
    }
}

.vegas-animation-kenburnsDown{
    -webkit-animation:kenburnsDown ease-out;animation:kenburnsDown ease-out
}

@-webkit-keyframes kenburnsDown{
    0%{
        -webkit-transform:scale(1.5) translate(0,-10%);transform:scale(1.5) translate(0,-10%)
    }
    100%{
        -webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)
    }
}

@keyframes kenburnsDown{
    0%{
        -webkit-transform:scale(1.5) translate(0,-10%);transform:scale(1.5) translate(0,-10%)
    }
    100%{
        -webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)
    }
}

.vegas-animation-kenburnsLeft{
    -webkit-animation:kenburnsLeft ease-out;animation:kenburnsLeft ease-out
}

@-webkit-keyframes kenburnsLeft{
    0%{
        -webkit-transform:scale(1.5) translate(10%,0);transform:scale(1.5) translate(10%,0)
    }
    100%{
        -webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)
    }
}

@keyframes kenburnsLeft{
    0%{
        -webkit-transform:scale(1.5) translate(10%,0);transform:scale(1.5) translate(10%,0)
    }
    100%{
        -webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)
    }
}

.vegas-animation-kenburnsRight{
    -webkit-animation:kenburnsRight ease-out;animation:kenburnsRight ease-out
}

@-webkit-keyframes kenburnsRight{
    0%{
        -webkit-transform:scale(1.5) translate(-10%,0);transform:scale(1.5) translate(-10%,0)
    }
    100%{
        -webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)
    }
}

@keyframes kenburnsRight{
    0%{
        -webkit-transform:scale(1.5) translate(-10%,0);transform:scale(1.5) translate(-10%,0)
    }
    100%{
        -webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)
    }
}

.vegas-animation-kenburnsUpLeft{
    -webkit-animation:kenburnsUpLeft ease-out;animation:kenburnsUpLeft ease-out
}

@-webkit-keyframes kenburnsUpLeft{
    0%{
        -webkit-transform:scale(1.5) translate(10%,10%);transform:scale(1.5) translate(10%,10%)
    }
    100%{
        -webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)
    }
}

@keyframes kenburnsUpLeft{
    0%{
        -webkit-transform:scale(1.5) translate(10%,10%);transform:scale(1.5) translate(10%,10%)
    }
    100%{
        -webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)
    }
}

.vegas-animation-kenburnsUpRight{
    -webkit-animation:kenburnsUpRight ease-out;animation:kenburnsUpRight ease-out
}

@-webkit-keyframes kenburnsUpRight{
    0%{
        -webkit-transform:scale(1.5) translate(-10%,10%);transform:scale(1.5) translate(-10%,10%)
    }
    100%{
        -webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)
    }
}

@keyframes kenburnsUpRight{
    0%{
        -webkit-transform:scale(1.5) translate(-10%,10%);transform:scale(1.5) translate(-10%,10%)
    }
    100%{
        -webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)
    }
}

.vegas-animation-kenburnsUp{
    -webkit-animation:kenburnsUp ease-out;animation:kenburnsUp ease-out
}
    
@-webkit-keyframes kenburnsUp{
    0%{
        -webkit-transform:scale(1.5) translate(0,10%);transform:scale(1.5) translate(0,10%)
    }
    100%{-webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)
    }
}
        
@keyframes kenburnsUp{
    0%{
        -webkit-transform:scale(1.5) translate(0,10%);transform:scale(1.5) translate(0,10%)
    }
    100%{
        -webkit-transform:scale(1) translate(0,0);transform:scale(1) translate(0,0)
    }
}


  * {
    padding: 0;
    margin: 0;
  }

                .headline {
                    z-index: 11;
                    font-weight: bold;
                    font-size: 30px;
                    text-align: center;
                    position: absolute;
                    top: 100px;
                    left: 50%;
                    transform: translate(-50%,-50%);
                    color: white;
                    text-decoration: none;
                }

                .input{
                    z-index: 13;
                    text-align: center;
                    position: absolute;
                    top: 300px;
                    left: 50%;
                    transform: translate(-50%,-50%);
                    color: black;
                }

                .image-url{
                    z-index: 13;
                    position: absolute; /*自由に配置する指定*/
                    top: 650px;
                    right: 0%;
                    transform: translate(-50%,-50%);
                    color: red;
                }

                #slider {
                    width: 100%;
                    height: 100vh;/*スライダー全体の縦幅を画面の高さいっぱい（100vh）にする*/
                }

                   .wrapper{
                       position: relative;
                   }

            </style>
        </head>

        <body>
            <div class="wrapper">
                <div id="slider">
                    <a href="bookSearch3.py"><p class="headline">Book Management System</p></a>

                    <form name="form1" action="bookList.py" method="post" class="input">
                        <input type="text" name="param1" class="search" placeholder="Search the books." style="color:black; width:500px; height: 30px;"><br>

                        <select name = "option" style="text-align:center;">
                            <option value="TITLE">Title</option>
                            <option value="AUTHOR">Author</option>
                            <option value="PUBLISHER">Publisher</option>
                            <option value="ISBN">Isbn</option>
                        </select><br>

                        <button type="submit" name="submit" onclick="return check();">Search</button>
                    </form>
''')

print('<p class="image-url" >画像引用元：<a href="{0}" style="color:red;">Bingの日替わり画像　テーマ：{1}</a></p>'.format(load_url, theme))

print('<p>Yahooニュース</p>')
for i in news:
    print('<a href="{0}" style="color : white;"><p>{1}</p></a>'.format(i["url"], i["str"]))

print('''
                </div>
            </div>


            <script src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/vegas/2.4.4/vegas.min.js"></script>

            <script>
                //画像の設定
                var windowwidth = window.innerWidth || document.documentElement.clientWidth || 0;
                var responsiveImage = [];
''')

for i in background:
    image_str = "'{0}'".format(i)
    print('responsiveImage.push({0});'.format("{src : " +  image_str + "}"))


print('''
               //Vegas全体の設定
               $('#slider').vegas({
                   overlay: true,    //画像の上に網線やドットのオーバーレイパターン画像を指定。
                   transition: 'blur',    //切り替わりのアニメーション。http://vegas.jaysalvat.com/documentation/transitions/参照。
                   transitionDuration: 2000,    //切り替わりのアニメーション時間をミリ秒単位で設定
                   delay: 10000,    //スライド間の遅延をミリ秒単位で。
                   animationDuration: 20000,    //スライドアニメーション時間をミリ秒単位で設定
                   animation: 'kenburns',    //スライドアニメーションの種類。http://vegas.jaysalvat.com/documentation/transitions/参照。
                   slides: responsiveImage,    //画像設定を読む
               });

            </script>

        </body>
    </html>
''')
