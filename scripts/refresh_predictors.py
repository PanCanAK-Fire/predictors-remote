import sys
from pathlib import Path
import urllib.request

PROJPATH = Path(__file__).absolute().parent.parent
print(PROJPATH)
sys.path.append((PROJPATH / 'src').as_posix())
from predictors_remote import d_urls

datadir = PROJPATH / 'data'
OUTPATH = datadir / 'working'

if __name__ == '__main__':
    for item in d_urls.ICEURLS:
        url = item['URL']
        fn = f"{item['name']}.txt"
        if item['skipentry']:
            print(f"skipping {fn} at {url}")
            continue
        print(f"retrieving {fn} from {url}")
        urllib.request.urlretrieve(url, OUTPATH / fn)

    for item in d_urls.TELECONNECTIONURLS:
        url = item['URL']
        fn = f"{item['name']}.txt"
        if item['skipentry']:
            print(f"skipping {fn} at {url}")
            continue
        print(f"retrieving {fn} from {url}")
        opener = urllib.request.URLopener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        try:
            filename, headers = opener.retrieve(url, OUTPATH / fn)
        except Exception as e:
            print(f"Could not retrieve {fn} from {url}")
            print(e)
            continue