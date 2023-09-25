import os
import subprocess
import urllib3
from urllib3.util import Retry
from urllib3.exceptions import MaxRetryError

def cli():
    def getDownloadURL():
        version = '0.0.1'
        downloadOS = 'linux'
        arch = 'x84'
        extension = ''

        return f'https://github.com/evilmartians/lefthook/releases/download/v${version}/lefthook_${version}_${downloadOS}_${arch}${extension}'

    def downloadBinary():
        http = urllib3.PoolManager()
        retry = Retry(3, raise_on_status=True, status_forcelist=range(500, 600))

        try:
            url = getDownloadURL()
            r = http.request('GET', url, retries=retry)
        except MaxRetryError as m_err:
            logger.error('Failed to fetch lefthook binary due to {}'.format(m_err.reason))

        
    print('cwd:', os.getcwd())
    execPath = downloadBinary()
    print('execPath:', execPath)
    subprocess.run(
        execPath,
        stdin=None,
        stdout=None,
        stderr=None,
        cwd=os.getcwd()
    )
    
    
