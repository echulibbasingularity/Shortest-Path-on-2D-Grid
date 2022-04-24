# Queue operations

def enqueue(lst, data):
  lst.append(data)

def dequeue(lst):
  return lst.pop(0)

def top(lst):
  return lst[0]

def is_empty(lst):
  if len(lst)==0:
    return True   
  return False




# legal move function

def is_legal_position(x, y):
    if x<0 or y<0 or x>(n-1) or y>(n-1):
        return False
    return True
    


def play(p, d):
    dx=[-2,-2,-1,-1,1,1,2,2]  # x-coordinate change in UL, UR, UL_stretch, UR_stretch, DL_stretch, DR_stretch, DL, DR
    dy=[-1,1,-2,2,-2,2,-1,1]  # y-coordinate change in UL, UR, UL_stretch, UR_stretch, DL_stretch, DR_stretch, DL, DR
    visited=[[False]*n for i in range(m)]
    dist = [[0]*n for i in range(m)]
    queue=[]
    enqueue(queue, p)
    visited[p[0]][p[1]] = True
    #print(visited)
    dist[p[0]][p[1]] = 0
    while not is_empty(queue):
        v= dequeue(queue)
        for i in range(4):
            new_X = v[0] + dx[i]
            new_Y = v[1] + dy[i]
            if is_legal_position(new_X, new_Y) and not visited[new_X][new_Y]:
                valid_pos = (new_X, new_Y)
                visited[new_X][new_Y] = True
                dist[new_X][new_Y] = dist[v[0]][v[1]] + 1
                if new_X==d[0] and new_Y==d[1]:
                    return f' minimum number of moves to reach from {p} to {d} is {dist[new_X][new_Y]}'
                enqueue(queue, valid_pos)

                
# input command

n = int(input('number of rows = ' ))
m = int(input('number of columns = ' ))
if n!=m:
    print('WE DOING SQUARE MATRIX SON, CARBON COPY THOSE NUMBERS')
else:
    p = tuple(int(x) for x in input('Enter starting position = ' ).split(','))     # give x,y as input. for eg: 1,2
    d = tuple(int(x) for x in input('Enter destination = ' ).split(','))           # give x,y as input. for eg: 1,2
    if not is_legal_position(p[0], p[1]) and not is_legal_position(d[0], d[1]):
        print('WE\'RE OUT OF GRID SON, TRY AGAIN!')
    print(play(p,d))

    
            

    





