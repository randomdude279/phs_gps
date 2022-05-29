def doGET(get = {}, addargs = {}):
  return """available endpoints:
  /find_node.dpy: takes a room number or location code and finds a nearby node for it. Parameters: room_number
  /info_node.dpy: gives information about a node with a given ID. Parameters: nodeid.
  /link_nodes.dpy: gives a route between a start point and end point. Parameters: start and end (for automatic name resolution) OR start_nodeid, stop_nodeid (for manual node ID entry).
  """