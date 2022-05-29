#imports
import phsnodes
import find_node

def doGET(get = {}, addargs = {}):
#show top X solutions
  if 'top' not in get.keys():
    get['top'] = 3

# first, translate the inputs: see if we can resolve it automatically and then fall back
  try:
    print('Attempting automatic resolution of starting point.')
    start = find_node.doGET(
      {
        'room_number': get['start']
      }
    )
    if start == '-1': blank = 0/0
  except:
    try:
      print('Using manually inputted start node ID.')
      start = get['start_nodeid']
    except:
      return 'unable to obtain starting point'


  #do the same for the endpoint
  try:
    print('Attempting automatic resolution of stopping point.')
    end = find_node.doGET(
      {
        'room_number': get['end']
      }
    )
    if end == '-1': blank = 0/0
  except:
    try:
      print('Using manually inputted start node ID.')
      end = get['end_nodeid']
    except:
      return 'unable to obtain ending point'

  print('Beginning trace.')
  routes = []
  #here is the routes object
  #that we will be using to store the output 

  
  #pass a reference of routes (not a copy) to phsnodes.Recursive
  phsnodes.Recursive(routes, [str(start)], str(end))
  
  
  for i in routes:
    if len(i.routeArray) != len(set(i.routeArray)):
      routes.remove(i)
      #remove any routes that had duplicates
  
  # add each of the acceptable routeArrays into a secondary array
  filteredRoutes = []
  for i in routes:
    for j in i.routeArray:
      i.routeString = i.routeString + str(j) + f'=[{phsnodes.nodes[j].render_coords[0]},{phsnodes.nodes[j].render_coords[1]}' + ']:'
    i.routeString = i.routeString[:-1]
    #print(i.routeString)
    filteredRoutes.append(i.routeString)
  
  # which will then be ranked by length
  filteredRoutes = sorted(filteredRoutes, key=len)

  #return str(filteredRoutes[0:int(get['top'])])
  #input('Any key to terminate program.')
  reply = ''
  for i in filteredRoutes[0:int(get['top'])]:
    for j in i:
      reply = reply + str(j)

    reply = reply
    reply = reply + '\n'
  return reply