import phsnodes

def doGET(get = {}, addargs = {}):
  try: nodeObj = phsnodes.nodes[get['nodeid']]
  except: return 'Provide a VALID node ID with HTTP GET value "nodeid"'

  return f"""NODE INFORMATION:
id={nodeObj.nodeID}
travelable={nodeObj.connectedTo}
nearby={nodeObj.classroom}
x={nodeObj.render_coords[0]}
y={nodeObj.render_coords[1]}
  """