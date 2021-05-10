def sanitize(searchString):
    if len(searchString) > 0 and searchString[-1] == ';':
        searchString = searchString[:-1]
    searchParameter = searchString.split(';')
    # print(searchParameter)
    sepratedString = []
    for parameter in searchParameter:
        parameter = parameter.split(':')
        print(parameter)
        if len(parameter) > 1:
            sepratedString.append([parameter[0],parameter[1].split(',')])
        else :
            sepratedString.append(parameter)
        print(sepratedString)
    return sepratedString