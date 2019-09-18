import sys                               # sysモジュールのimport
from OpenGL.GL import *                  # GLモジュールのimport
from OpenGL.GLU import *                 # GLUモジュールのimport
from OpenGL.GLUT import *                # GLUTモジュールのimport
import cubePosition as cp


def display():                           # 描画要求に伴うコールバック関数
  '''
  描画要求に伴う処理を行う (放射状の線を描画する)
  '''
  vertices = ((-1, -1, -1),(1, -1, -1),(1, 1, -1),(-1, 1, -1),
            (-1, -1, 1),(1, -1, 1),(1, 1, 1),(-1, 1, 1))
  
  faces = ((1,2,6,5),(2,3,7,6),(4,5,6,7),
            (0,4,7,3),(0,1,5,4),(0,3,2,1))

  colors = ((0,1,1),(1,0,1),(1,1,0),
            (0,0.5,0.5),(0.5,0,0.5),(0.5,0.5,0))
 
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)           # 背景の消去
                       # 線分描画の開始
  for i in range(len(faces)):  
    glBegin(GL_POLYGON)          # 線分描画の反復 (終点の個数分)
    glColor3dv(colors[i])
    for j in range(len(faces[i])):  
        glVertex3dv(vertices[faces[i][j]])                  # 線分の始点
    glEnd()                                # 線分描画の終了
  glFlush()                              # 描画命令の送信

def loop():                              # コールバック関数の設定とループ起動
  '''
  reshape と displayコールバック関数を設定し，ループを起動する
  '''
  glutReshapeFunc(cp.reshape)               # reshapeコールバック関数の登録
  glutDisplayFunc(display)               # displayコールバック関数の登録
  glutMainLoop()                         # GLUTのメインループ起動

def main():                              # main関数
  W, H = (500, 500)
  cp.window(W, H)                           # ウィンドウの作成
  cp.init()                                 # OpenGLの初期化
  cp.argsInit()
  loop()                                 # コールバック関数の設定とループ起動

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出
