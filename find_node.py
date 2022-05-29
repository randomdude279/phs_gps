import phsnodes


def doGET(get={}, addargs={}):
    try:
        toSearch = get['room_number']
    except:
        return 'Add a value on HTTP GET value "room_number"'

    try:
        potentialResults = []
        results = ''

        for i in phsnodes.nodes:
            if str(toSearch) in phsnodes.nodes[i].classroom:
                potentialResults.append(phsnodes.nodes[i].nodeID)

        if len(potentialResults) == 0:
            return '-1'

        if len(potentialResults) == 1:
            return potentialResults[0]
        else:
            for i in potentialResults:
                results = results + i + ','

            results = results[:-1]
            return results
    except Exception:
        return '-1'
