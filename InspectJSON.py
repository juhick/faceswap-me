import json
import sys

def inspect(path):

    with open(path, 'r') as fp:

        faces = json.load(fp)

        for keys in faces:
            if len(faces[keys]) == 1:
                pass
            elif len(faces[keys]) > 1:
                maxsize = 0
                face = faces[keys]
                faceneed = {}
                for i in range(len(face)):
                    size = face[i]['w'] * face[i]['h']
                    if (size > maxsize):
                        maxsize = size
                        faceneed = face[i]
                faces[keys].clear()
                faces[keys].append(faceneed)
                print(len(faces[keys]))

    with open(path, 'w') as fp:
        json.dump(faces, fp, sort_keys=True, indent=4, separators=(',', ':'))

if __name__ == '__main__':
    path = str(sys.argv[1])
    inspect(path)