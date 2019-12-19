from django.http import HttpResponse
from django.shortcuts import render#导入render模块
from django.views.decorators.csrf import csrf_exempt
import kociemba
import sys
sys.path.append('./capsule-5723040/code/environments/')
sys.path.append('./capsule-5723040/code/solvers/cube3/')
import solver_algs
import cube_interactive_simple 
import json
import numpy

state =[]
legalmove = []
def index(request):
    print("OK")
    return render(request, 'index.html')

def about(request):
    print("good")
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def map(request):
    return render(request, 'map.html')
def news_show1(request):
    return render(request, 'news_show1.html')
def news_show2(request):
    return render(request, 'news_show2.html')
def news_show3(request):
    return render(request, 'news_show3.html')
def news_show4(request):
    return render(request, 'news_show4.html')
def news_show5(request):
    return render(request, 'news_show5.html')
def news_show6(request):
    return render(request, 'news_show6.html')
def news(request):
    return render(request, 'news.html')
def news1(request):
    return render(request, 'news1.html')
def product(request):
    return render(request, 'product.html')
def water(request):
    return render(request, 'water.html')
def indek(request):
    print("Oops!")
    return render(request, 'index1.html')

@csrf_exempt
def solve(request):
    post_data = request.POST.get('state')
    tempc = ''
    for i in range(len(post_data)):
        if post_data[i] != '[' and post_data[i] != ']': 
            tempc = tempc + post_data[i]
    #print(tempc)
    temp = tempc.split(',')
    color = numpy.array([],dtype=int)
    for i in temp:
        color=numpy.append(color,int(i))
    print(color)
    moveraw = solver_algs.Kociemba.solve(color)
    moves = []
    moves_rev = []
    move_txt = []
    for i in moveraw:
        moves.append("_".join([i[0],str(i[1])]))
        moves_rev.append("_".join([i[0],str(-i[1])]))
        if i[1] == -1:
            move_txt.append(i[0]+'`')
        else:
            move_txt.append(i[0])
    ## print(post_data)
    result = {'moves': moves,'moves_rev':moves_rev,'solve_text':move_txt}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json;charset=utf-8;')

@csrf_exempt
def initState(request):
    #post_data = request.POST.get()
    cube = cube_interactive_simple.Cube()
    stateToFE=[0 for i in range(54)]
    FETostate=[6,3,0,7,4,1,8,5,2,15,12,9,16,13,10,17,14,11,24,21,18,25,22,19,26,23,20,33,30,27,34,31,28,35,32,29,38,41,44,37,40,43,36,39,42,51,48,45,52,49,46,53,50,47]
    for i in range(54):
        stateToFE[FETostate[i]]=i
    for i in range(6):
        #state.append(i*9)
        for j in range(9):
            #state.append(((i+j)%6)*9)
            state.append(i*9)
    for f,n in cube.legalPlays_qtm:
        move = "_".join([f,str(n)])
        legalmove.append(move)
    for m in cube.rotateIdxs_old:
        cube.rotateIdxs_old[m] = cube.rotateIdxs_old[m].tolist()
        #print(type(cube.rotateIdxs_old[m]))
    for m in cube.rotateIdxs_new:
        cube.rotateIdxs_new[m] = cube.rotateIdxs_new[m].tolist()
    #for m in cube.rotateIdxs_old:
        #print(m)
        #print(cube.rotateIdxs_old[m])
        #print(cube.rotateIdxs_new[m])
    ##result = {'state':state, 'rotateIdxs_old':cube.rotateIdxs_old,'rotateIdxs_new':[], 'stateToFE':stateToFE, 'FEToState':stateToFE, 'legalMoves':legalmove}    
    result = {'state':state, 'rotateIdxs_old':cube.rotateIdxs_old,'rotateIdxs_new':cube.rotateIdxs_new, 'stateToFE':stateToFE, 'FEToState':FETostate, 'legalMoves':legalmove}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json;charset=utf-8;')
